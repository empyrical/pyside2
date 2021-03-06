import unittest

import PySide2
from PySide2.QtCore import QPoint, QPointF
from PySide2.QtCore import QLine, QLineF
from PySide2.QtCore import QSize, QSizeF

class testCases(unittest.TestCase):
    def testQPointToTuple(self):
        p = QPoint(1, 2)
        self.assertEqual((1, 2), p.toTuple())

    def testQPointFToTuple(self):
        p = QPointF(1, 2)
        self.assertEqual((1, 2), p.toTuple())

    def testQLineToTuple(self):
        l = QLine(1, 2, 3, 4)
        self.assertEqual((1, 2, 3, 4), l.toTuple())

    def testQLineFToTuple(self):
        l = QLineF(1, 2, 3, 4)
        self.assertEqual((1, 2, 3, 4), l.toTuple())

    def testQSizeToTuple(self):
        s = QSize(1, 2)
        self.assertEqual((1, 2), s.toTuple())

    def testQSizeFToTuple(self):
        s = QSizeF(1, 2)
        self.assertEqual((1, 2), s.toTuple())

if __name__ == '__main__':
    unittest.main()
