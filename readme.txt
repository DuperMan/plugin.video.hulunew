::CREDIT::
All icons and fanart created by SamHill from XBMC forums

Version 3.9.5 is derived from Bluecop's original plugin and has no new functionality other than fixes for Frodo compatibility
Version 3.9.5 Changes made to support Frodo:

- fixed most if something: to if something is not None:
- fixed date format issues
- move the "cache" folder from pluginpath to user profile - using pluginpath on some linux systems will write fail
- added edgecast CDN recognition
- tried to fix fanart and art to carry through dir views properly - still some work to do
- fixed errors with search and subscriptions
- modified most prints to log - turn on debug flag to send data to xbmc.log
- added writing a tvshow.nfo for library export so that the XBMC library updates correctly
- various addon.xml changes

