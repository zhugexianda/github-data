__author__ = 'xianda'
# 世界地图
from pygal_maps_world.maps import World
from pygal_maps_world.i18n import COUNTRIES


def world_country_map():
    '''世界各国地图'''
    wm_c = World()
    wm_c.force_uri_protocol = 'http'
    wm_c.title = '世界地图'
    for code, name in COUNTRIES.items():
        # print(name, code)
        wm_c.add(name, code)
    wm_c.add('Yemen', {'ye': 'Yemen'})
    wm_c.render_to_file('world_map.svg')


def one_country_map():
    '''一国地图'''
    wm_o = World()
    wm_o.force_uri_protocol = 'http'
    wm_o.title = '世界地图(中国)'
    wm_o.add('China', {'中国': 'cn'})
    wm_o.render_to_file('country_map.svg')


world_country_map()
one_country_map()