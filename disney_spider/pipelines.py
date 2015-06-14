# -*- coding: utf-8 -*-
import json
import codecs
import time
import graphitesend
from scrapy import log


class FeedToGraphitePipeline(object):
    """
    Feeds the scraped data into Graphite (carbon_cache).
    """

    default_graphite_server = 'localhost'
    default_graphite_port = 2003
    attraction_metric_map = {}

    def process_item(self, item, spider):
        """
        Maps the attraction_id to a metric name, then feeds the wait time
        into Graphite (carbon_cache).

        If the attraction_id is not listed in the map, then the item will
        be ignored (but not removed from the pipeline).
        """

        attr_id = item['attraction_id'][0]
        wait = item['wait_time'][0].strip() if len(item['wait_time']) > 0 else 0
        if attr_id in self.attraction_metric_map:
            metric = self.attraction_metric_map[attr_id]
            if not self.g.dryrun:
                self.g.send(metric, wait, self.timestamp)
            else:
                log.msg("Graphite: "+self.g.send(metric, wait, self.timestamp).strip(), level=log.INFO, spider=spider)
        return item

    def open_spider(self, spider):
        self.timestamp = time.time()
        self.attraction_metric_map = spider.settings.get('ATTRACTION_METRIC_MAP')
        if self.attraction_metric_map is None or len(self.attraction_metric_map) == 0:
            raise KeyError('No ATTRACTION_METRIC_MAP defined in settings.py.')

        graphite_server = spider.settings.get('GRAPHITE_SERVER', self.default_graphite_server)
        graphite_port = spider.settings.get('GRAPHITE_PORT', self.default_graphite_port)
        log.msg("Using %s:%d as Graphite server" % (graphite_server, graphite_port), level=log.INFO, spider=spider)
        try:
            self.g = graphitesend.init(
                    graphite_server=graphite_server,
                    graphite_port=graphite_port,
                    prefix='',
                    system_name='')
        except graphitesend.GraphiteSendException, e:
            if spider.settings.get('GRAPHITE_DRYRUN_ENABLED', True):
                log.msg("Unable to connect to Graphite server %s:%d; will use dry run mode" % (graphite_server, graphite_port), level=log.WARNING, spider=spider)
                self.g = graphitesend.init(
                        prefix='',
                        system_name='',
                        dryrun=True)
            else:
                log.msg("Unable to connect to Graphite server %s:%d and dry run mode disabled" % (graphite_server, graphite_port), level=log.ERROR, spider=spider)
                raise e


class SaveToJsonPipeline(object):
    """
    Saves the scraped data to a file in JSON format.
    """

    def open_spider(self, spider):
        self.file = codecs.open(
                'scraped_data_utf8.json',
                'w',
                encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()
