# -*- coding: utf-8 -*-

BOT_NAME = 'disney_spider'

SPIDER_MODULES = ['disney_spider.spiders']
NEWSPIDER_MODULE = 'disney_spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'disney_spider (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'disney_spider.pipelines.FeedToGraphitePipeline':500,
    #'disney_spider.pipelines.SaveToJsonPipeline':500
    }

# Disable telnet console
TELNETCONSOLE_ENABLED = False

# Disable webservice
WEBSERVICE_ENABLED = False

LOG_LEVEL = 'INFO'

STATS_DUMP = False

# ---- FeedToGraphitePipeline Settings ----
GRAPHITE_SERVER = "localhost"
GRAPHITE_PORT = 2003
GRAPHITE_DRYRUN_ENABLED = True

# Maps the attraction ID (taken from the attraction link href) to a Graphite
# metric name.
ATTRACTION_METRIC_MAP = {
    # Disneyland
    'al_carib':    'disney.land.adventure_land.pirates_of_the_caribbean',
    'al_jungle':   'disney.land.adventure_land.jungle_cruise',
    'cc_splash':   'disney.land.critter_country.splash_mountain',
    'fl_haunted':  'disney.land.fantasy_land.haunted_mansion',
    'fl_pooh':     'disney.land.fantasy_land.winnie_the_pooh',
    'tl_buzz':     'disney.land.tomorrow_land.buzz_lightyear',
    'tl_monster':  'disney.land.tomorrow_land.monsters_inc',
    'tl_mountain': 'disney.land.tomorrow_land.space_mountain',
    'tl_tours':    'disney.land.tomorrow_land.star_tours',
    'wl_mountain': 'disney.land.western_land.big_thunder_mountain',
    # Disneysea
    'aw_tot':      'disney.sea.american_waterfront.tower_of_terror',
    'aw_toy':      'disney.sea.american_waterfront.toy_story_mania',
    'mi_center':   'disney.sea.mysterious_island.center_of_the_earth',
    'pd_storm':    'disney.sea.port_discovery.storm_riders',
    'pd_aqua':     'disney.sea.port_discovery.aquatopia',
    'ld_indiana':  'disney.sea.lost_river_delta.indiana_jones',
    'ld_raging':   'disney.sea.lost_river_delta.raging_spirits',
}
