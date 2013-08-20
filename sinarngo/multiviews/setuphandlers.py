from collective.grok import gs
from sinarngo.multiviews import MessageFactory as _

@gs.importstep(
    name=u'sinarngo.multiviews', 
    title=_('sinarngo.multiviews import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sinarngo.multiviews.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
