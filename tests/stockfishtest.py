#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unittests"""

import unittest
from stockfishpy.stockfishpy import *


class test_stockfish(unittest.TestCase):

    def test_initiate(self):
        self.assertRaises(Exception, Engine(param={'Ponder': 'false'}))

    def test_ponder_NoneType(self):
        self.Engine = Engine(param={'Ponder': 'false'})
        self.Engine.ucinewgame()
        self.assertIsNone(self.Engine.bestmove()['ponder'])

    def test_setdepth(self):
        self.Engine = Engine(depth='2')
        self.Engine.ucinewgame()
        self.assertIs(self.Engine.depth, '2')

    def test_check_rightposition(self):
        self.Engine = Engine(depth='5')
        allmove = ['e2e4']
        for x in xrange(0, 11):
            self.Engine.ucinewgame()
            self.Engine.setposition(allmove)
            allmove.append(self.Engine.bestmove()['bestmove'])

            # if Engine get unrecognized position in loop, it duplicate last bestmove
            self.assertFalse(allmove[x] == allmove[x+1])


if __name__ == '__main__':
    unittest.main()
