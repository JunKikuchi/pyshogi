#
#  test_pyshogi_uchifuzume.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2013 Jun Kikuchi. All rights reserved.
#

import pyshogi
from pyshogi import Gyoku, Hisya, Kaku, Kin, Gin, Keima, Kyosya, Fu
import unittest

class SenteTestCase(unittest.TestCase):
    def test_uchifuzume(self):
        '''
          7    8
        0 Fu   Gyoku
        1
        2 Kin
        '''
        ban = pyshogi.Shogiban(
            [
                0,
                [
                    (1, Fu,    (7, 0), 0),
                    (1, Gyoku, (8, 0), 0),
                    (0, Kin,   (7, 2), 0),
                    (0, Fu,    None,   0),
                ]
            ]
        )
        fu = ban.mochigoma(0)[0]

        masus = set(ban)
        for x in range(0, 9):
            masus.remove(ban.masu(x, 0))
        masus.remove(ban.masu(7, 2))
        masus.remove(ban.masu(8, 1))
        ugoki = dict([(masu, None) for masu in masus])

        self.assertEqual(
            dict([(masu, fu.narikomi(masu)) for masu in fu.ugoki()]),
            ugoki
        )

    def test_not_uchifuzume(self):
        '''
          7    8
        0 Fu   Gyoku
        1
        2 Kin  Fu
        '''
        ban = pyshogi.Shogiban(
            [
                0,
                [
                    (1, Fu,    (7, 0), 0),
                    (1, Gyoku, (8, 0), 0),
                    (0, Kin,   (7, 2), 0),
                    (0, Fu,    (8, 2), 0),
                ]
            ]
        )
        fu = ban.masu(8, 2).koma

        self.assertEqual(
            dict([(masu, fu.narikomi(masu)) for masu in fu.ugoki()]),
            dict([(ban.masu(8, 1), [0, 1])])
        )
