#
#  test_pyshogi_mochi_koma.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2013 Jun Kikuchi. All rights reserved.
#

import pyshogi
import unittest

class KikiTestCase(unittest.TestCase):
    def test_kiki(self):
        ban = pyshogi.Ban([
            (False, 'Gyoku', (4, 0), False),
            (True,  'Kin',   (4, 1), False),
            (True,  'Fu',    (4, 2), False),
        ])

        kiki = ban.kiki(True)
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

        kiki = ban.kiki(False)
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
