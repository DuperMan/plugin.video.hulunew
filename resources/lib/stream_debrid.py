import xbmc
import xbmcgui
import xbmcplugin

import common
import debridroutines
import subtitles

class Main:
    def __init__( self ):
        hulu_url = 'http://www.hulu.com/watch/'+common.args.videoid
        debriduser = common.settings['realdebrid-username']
        debridpass = common.settings['realdebrid-password']
        qualties = ['HD','HQ','SD']
        quality = qualties[int(common.settings['realdebrid-quality'])]
        cookie_jar = common.COOKIEFILE
        rd = debridroutines.RealDebrid(cookie_jar, debriduser, debridpass)
        if rd.Login():
            finalUrl = rd.Resolve(hulu_url, quality)
            item = xbmcgui.ListItem(path=finalUrl)
            xbmcplugin.setResolvedUrl(common.handle, True, item)
        if (common.settings['enable_captions'] == 'true'):
            subtitles.Main().PlayWaitSubtitles(common.args.url)



