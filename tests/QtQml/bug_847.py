#!/usr/bin/python
# -*- coding: utf-8 -*-
# Testcase for PySide bug 847
# Released under the same terms as PySide itself
# 2011-05-04 Thomas Perl <m@thp.io>

import unittest

from helper import adjust_filename, UsesQApplication

from PySide2.QtCore import Slot, Signal, QUrl
from PySide2.QtQuick import QQuickView

class View(QQuickView):
    def __init__(self):
        QQuickView.__init__(self)
        self.setSource(QUrl.fromLocalFile(adjust_filename('bug_847.qml', __file__)))
        self.rootObject().setProperty('pythonObject', self)

    @Slot(int, int)
    def blubb(self, x, y):
        self.called.emit(x, y)

    called = Signal(int, int)


class TestQML(UsesQApplication):
    def done(self, x, y):
        self._sucess = True
        self.app.quit()

    def testPythonSlot(self):
        self._sucess = False
        view = View()
        view.called.connect(self.done)
        view.show()
        self.app.exec_()
        self.assertTrue(self._sucess)

if __name__ == '__main__':
    unittest.main()

