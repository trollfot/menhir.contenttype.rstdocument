# -*- coding: utf-8 -*-

import doctest
import unittest
import menhir.contenttype.rstdocument.tests
from zope.component.testlayer import ZCMLFileLayer


def test_suite():
    readme = doctest.DocFileSuite(
        'README.txt',
        globs={'__name__': 'menhir.contenttype.rstdocument.tests'},
        optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS)
    readme.layer = ZCMLFileLayer(menhir.contenttype.rstdocument.tests)
    return unittest.TestSuite([readme])
