#
#  test_pyshogi_tsumi.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2013 Jun Kikuchi. All rights reserved.
#

import pyshogi
import unittest

class BanTestCase(unittest.TestCase):
    def test_dump(self):
        ban = pyshogi.Ban()
        self.assertEqual(ban.dump(), {'TEBAN': True, 'KOMA': pyshogi.HIRATE})

        ban1 = pyshogi.Ban(ban.dump())
        self.assertEqual(ban.dump(), ban1.dump())

    def test_clone(self):
        ban = pyshogi.Ban([
            (False, 'Gyoku', (4, 0), False),
            (True,  'Kin',   (4, 1), False),
            (True,  'Fu',    (4, 2), False),
            (True,  'Gyoku', (4, 8), False),
        ])
        ban1 = ban.clone()
        self.assertEqual(ban.dump(), ban1.dump())

if __name__ == '__main__': unittest.main()
