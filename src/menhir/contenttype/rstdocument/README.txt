******************************
menhir.contenttype.rstdocument
******************************

``menhir.contenttype.rstdocument`` provides a way to render RST text
in your application.

  >>> from menhir.contenttype.rstdocument import RsTDocument
  >>> doc = RsTDocument(title=u"My RsT document")


Schema
======

  >>> from dolmen.content import IBaseContent
  >>> from menhir.contenttype.rstdocument import IRsTDocument
  >>> from zope.interface.verify import verifyClass, verifyObject

  >>> IRsTDocument.providedBy(doc)
  True
  >>> verifyClass(IRsTDocument, RsTDocument)
  True
  >>> verifyObject(IRsTDocument, doc)
  True
  >>> IRsTDocument.isOrExtends(IBaseContent)
  True

  >>> print doc.raw_text
  None
  >>> print doc.processed_text
  None


Factory
=======

The factory is protected by a common ``dolmen.app.security`` right::

  >>> from dolmen.content import require
  >>> print require.bind().get(doc)
  dolmen.content.Add


Transformation
==============

  >>> from zope.event import notify
  >>> from zope.lifecycleevent import Attributes, ObjectModifiedEvent

  >>> rst = u"""Creating your own Dolmen site
  ... ------------------------------
  ...
  ... In *src/mydolmen/app.py* module, implement a Dolmen
  ... site by inheriting from the ``Dolmen`` class::
  ...
  ...    from dolmen.app.site import Dolmen
  ...    class MySite(Dolmen):
  ...        title = u"My project site"
  ... """

  >>> doc.raw_text = rst
  >>> print doc.processed_text
  None

  >>> notify(ObjectModifiedEvent(doc))
  >>> print doc.processed_text
  None

  >>> notify(ObjectModifiedEvent(doc, Attributes(IRsTDocument, 'raw_text')))
  >>> print doc.processed_text
  <p>In <em>src/mydolmen/app.py</em> module, implement a Dolmen
  site by inheriting from the <tt class="docutils literal">Dolmen</tt>
  class:</p>
  <pre class="literal-block">
    from dolmen.app.site import Dolmen
    class MySite(Dolmen):
        title = u&quot;My project site&quot;
  </pre>
