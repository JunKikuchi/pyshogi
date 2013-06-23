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
                True,
                [
                    (False, Gyoku, (4, 0), False),
                    (True,  Kin,   (4, 1), False),
                    (True,  Fu,    (4, 2), False),
                    (True,  Gyoku, (4, 8), False),
                ]
            ]
        )

        ban.teban = True
        self.assertFalse(ban.tsumi())

        ban.teban = False
        self.assertTrue(ban.tsumi())

    def test_not_atamakin(self):
        ban = pyshogi.Shogiban(
            [
                True,
                [
                    (False, Gyoku, (4, 0), False),
                    (True,  Kin,   (4, 1), False),
                    (True,  Gyoku, (4, 8), False),
                ]
            ]
        )

        ban.teban = True
        self.assertFalse(ban.tsumi())

        ban.teban = False
        self.assertFalse(ban.tsumi())

if __name__ == '__main__': unittest.main()
