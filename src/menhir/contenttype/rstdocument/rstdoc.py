# -*- coding: utf-8 -*-

import dolmen.content as content
import grokcore.view as grok

from cStringIO import StringIO
from docutils.core import publish_parts

from dolmen.menu import menuentry
from dolmen.app.layout import Index, ContextualMenu, Page
from dolmen.app.security import content as security

from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.schema import Text
from zope.event import notify
from zope.lifecycleevent import (
    Attributes, ObjectModifiedEvent, IObjectModifiedEvent)

_ = MessageFactory('menhir.contenttype.rstdocument')


class IDocumentTransformer(Interface):
    """A component dedicated to the document transformation.
    """
    def transform(source, target):
        """Transform a string from a source mimetype to another.
        """


class IRsTDocument(content.IBaseContent):
    """A simple file object.
    """
    raw_text = Text(
        title = _(u"Restructured Text input"),
        required = True)

    processed_text = Text(
        title = _(u"Restructured Text input"),
        required = True)
    

class RsTDocument(content.Content):
    """A file content type storing the data in blobs.
    """
    content.name(_(u"Restructured Text Document"))
    content.schema(IRsTDocument)
    content.require(security.CanAddContent)
        

class RstDocumentTransformer(grok.Adapter):
    grok.context(IRsTDocument)
    grok.provides(IDocumentTransformer)
    
    def transform(self, source="restructuredtext", target="html"):
        """Transforms a RsT document to another format.
        """
        settings = {'initial_header_level': 2,
                    'default_output_encoding': 'utf-8',}
        return publish_parts(
            self.context.raw_text,
            settings_overrides=settings,
            parser_name='restructuredtext',
            writer_name='html')['body']


@grok.subscribe(IRsTDocument, IObjectModifiedEvent)
def TransformRstDocument(doc, event):
    for desc in event.descriptions:
        if desc.interface.isOrExtends(IRsTDocument):
            if 'raw_text' in desc.attributes:
                processed = IDocumentTransformer(doc).transform()
                doc.processed_text = processed
                notify(ObjectModifiedEvent(
                    doc, Attributes(IRsTDocument, 'processed_text')))
                return True
    return False


class RsTDocView(Index):
    grok.name("index")

    def update(self):
        self.html = self.context.processed_text


@menuentry(ContextualMenu)
class RawDocSource(Page):
    grok.title(_("Raw source"))


class Download(grok.View):
    """Download view.
    """
    def render(self):
        html = self.context.raw_text.encode('utf-8')
        self.response.setHeader('Content-Type', "text/x-rst; charset=utf-8")
        self.response.setHeader('Content-Length', len(html))
        self.response.setHeader(
            'Content-Disposition',
            'attachment; filename="%s.rst"' % (
                self.context.title.encode('utf-8')))
        return html
