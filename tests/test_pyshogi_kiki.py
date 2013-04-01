#
#  test_pyshogi_mochi_koma.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2013 Jun Kikuchi. All rights reserved.
#

import pyshogi
from pyshogi import Gyoku, Hisya, Kaku, Kin, Gin, Keima, Kyosya, Fu
import unittest

class KikiTestCase(unittest.TestCase):
    def test_kiki(self):
        ban = pyshogi.ShogiBan(
            [
                0,
                [
                    (1, Gyoku, (4, 0), 0),
                    (0, Kin,   (4, 1), 0),
                    (0, Fu,    (4, 2), 0),
                ]
            ]
        )

        kiki = ban.kiki(0)
        self.assertEqual(
            kiki,
            frozenset([
                ban.masu(3, 0),
                ban.masu(3, 1),
                ban.masu(4, 0),
                ban.masu(4, 1),
                ban.masu(4, 2),
                ban.masu(5, 0),
                ban.masu(5, 1),
            ])
        )

        kiki = ban.kiki(1)
        self.assertEqual(
            kiki,
            frozenset([
                ban.masu(3, 0),
                ban.masu(3, 1),
                ban.masu(4, 1),
                ban.masu(5, 0),
                ban.masu(5, 1),
            ])
        )

if __name__ == '__main__': unittest.main()
