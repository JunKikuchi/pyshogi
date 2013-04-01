#
#  test_pyshogi_tsumi.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2013 Jun Kikuchi. All rights reserved.
#

import pyshogi
from pyshogi import Gyoku, Hisya, Kaku, Kin, Gin, Keima, Kyosya, Fu
import unittest

class TsumiTestCase(unittest.TestCase):
    def test_hirate(self):
        ban = pyshogi.Shogiban()
        self.assertFalse(ban.tsumi())

    def test_atamakin(self):
        ban = pyshogi.Shogiban(
            [
                0,
                [
                    (1, Gyoku, (4, 0), 0),
                    (0, Kin,   (4, 1), 0),
                    (0, Fu,    (4, 2), 0),
                    (0, Gyoku, (4, 8), 0),
                ]
            ]
        )

        ban.teban = 0
        self.assertFalse(ban.tsumi())

        ban.teban = 1
        self.assertTrue(ban.tsumi())

    def test_not_atamakin(self):
        ban = pyshogi.Shogiban(
            [
                0,
                [
                    (1, Gyoku, (4, 0), 0),
                    (0, Kin,   (4, 1), 0),
                    (0, Gyoku, (4, 8), 0),
                ]
            ]
        )

        ban.teban = 0
        self.assertFalse(ban.tsumi())

        ban.teban = 1
        self.assertFalse(ban.tsumi())

if __name__ == '__main__': unittest.main()
