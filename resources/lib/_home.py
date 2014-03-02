import xbmc
import xbmcplugin
from xbmcgui import Dialog
import urllib
import common
import os
import sys
import xbmcaddon
import xbmcgui

import xml.etree.ElementTree as ElementTree


class Main:
    def __init__( self ):
        self.addMainHomeItems()
        xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ) )
    
    def addMainHomeItems( self ):
        xml=common.getFEED(common.BASE_MENU_URL)
        tree = ElementTree.XML(xml)
        menuitems = tree.findall('item')
        fanart = common.hulu_fanart
        for item in menuitems:
            display= item.findtext('display')
            items_url='http://m.hulu.com'+item.findtext('items_url') 
            cmtype=item.find('app_data').findtext('cmtype')
            thumbnail = xbmc.translatePath(os.path.join(common.imagepath,"icon.png"))
            cm = []
            if cmtype == 'None' or display == 'Help' or display == 'Profiles' or display == 'Now Playing':
                continue
            elif display =='Popular':
                thumbnail = xbmc.translatePath(os.path.join(common.imagepath,"icon_popular.jpg"))
                cm.append( ('Export Popular Shows', "XBMC.RunPlugin(%s?mode='ForcePopularShowsLibrary')" % ( sys.argv[0] ) ) )
                cm.append( ('Export Popular Movies', "XBMC.RunPlugin(%s?mode='ForcePopularMoviesLibrary')" % ( sys.argv[0] ) ) )
                cm.append( ('Export Popular Episodes', "XBMC.RunPlugin(%s?mode='ForcePopularEpisodesLibrary')" % ( sys.argv[0] ) ) )
            elif display =='Recently Added':
                thumbnail = xbmc.translatePath(os.path.join(common.imagepath,"icon_recently_added.jpg"))        
            elif display == 'TV':
                cm.append( ('Export All Full Shows', "XBMC.RunPlugin(%s?mode='ForceFullShowsLibrary')" % ( sys.argv[0] ) ) )
                thumbnail = xbmc.translatePath(os.path.join(common.imagepath,"icon_tv.jpg"))
            elif display == 'Movies':
                cm.append( ('Export All Full Movies', "XBMC.RunPlugin(%s?mode='ForceFullMoviesLibrary')" % ( sys.argv[0] ) ) )
                thumbnail = xbmc.translatePath(os.path.join(common.imagepath,"icon_movies.jpg"))
            elif display == 'Search':
                thumbnail = xbmc.translatePath(os.path.join(common.imagepath,"icon_search.jpg"))
            common.addDirectory(display,items_url,cmtype,thumbnail,thumbnail,fanart=fanart,page='1',perpage='25',cm=cm)
        if common.settings['enable_login']=='true':
            if not os.path.isfile(common.QUEUETOKEN):
                common.login_queue()
            thumbnail = xbmc.translatePath(os.path.join(common.imagepath,"icon_queue.jpg"))
            cm = [ ('Add Queue to Library', "XBMC.RunPlugin(%s?mode='ForceQueueLibrary')" % ( sys.argv[0] ) ) ]
            cm.append( ('Clear Library Directory', "XBMC.RunPlugin(%s?mode='ClearLibrary')" % ( sys.argv[0] ) ) )
            common.addDirectory('Queue'         ,'http://m.hulu.com/menu/hd_user_queue'          , 'Queue'         ,thumbnail,thumbnail,fanart=fanart,page='1',perpage='2000',cm=cm)
            thumbnail = xbmc.translatePath(os.path.join(common.imagepath,"icon_subscriptions.jpg"))
            cm = [ ('Add Subscriptions to Library', "XBMC.RunPlugin(%s?mode='ForceSubscriptionsLibrary')" % ( sys.argv[0] ) ) ]
            cm.append( ('Clear Library Directory', "XBMC.RunPlugin(%s?mode='ClearLibrary')" % ( sys.argv[0] ) ) )
            common.addDirectory('Subscriptions' ,'http://m.hulu.com/menu/hd_user_subscriptions'  , 'Subscriptions' ,thumbnail,thumbnail,fanart=fanart,page='1',perpage='2000',cm=cm)
            thumbnail = xbmc.translatePath(os.path.join(common.imagepath,"icon_history.jpg"))
            common.addDirectory('History'       ,'http://m.hulu.com/menu/hd_user_history'        , 'History'       ,thumbnail,thumbnail,fanart=fanart,page='1',perpage='2000')
