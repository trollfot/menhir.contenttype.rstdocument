# -*- coding: utf-8 -*-

import grokcore.view as grok
import dolmen.content as content
from zope.schema import Text
from zope.interface import Interface
from docutils.core import publish_string
from dolmen.app.security import content as security
from dolmen.app.layout import Index, ContextualMenuEntry, Page
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('dolmen')


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
        required = True
        )
    

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
        return publish_string(self.context.raw_text,
                              parser_name=source,
                              writer_name=target)


class RsTDocView(Index):
    grok.name("index")

    def update(self):
        self.html = IDocumentTransformer(self.context).transform()


class RawDocSource(Page, ContextualMenuEntry):
    """
    """
    grok.title(_("Raw source"))


class Download(grok.View):

    def render(self):
        html = self.context.raw_text
        self.response.setHeader('Content-Type', "text/plain")
        self.response.setHeader('Content-Length', len(html))
        self.response.setHeader(
            'Content-Disposition',
            'attachment; filename="%s.rst"' % self.context.title
            )
        return html
