# -*- coding: utf-8 -*-
#
#  pyshogi.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2012-2013 Jun Kikuchi. All rights reserved.
#

import itertools
import types

class Error(Exception):
    pass

class CanNotPlaceKomaError(Error):
    def __init__(self, koma, masu):
        self.koma = koma
        self.masu = masu

    def __str__(self):
        return "%s %s %s" % (self.__class__.__name__, self.koma, self.masu)

class TebanError(Error):
    def __init__(self, koma, masu):
        self.koma = koma
        self.masu = masu

    def __str__(self):
        return "%s %s %s" % (self.__class__.__name__, self.koma, self.masu)

class Koma:
    KACHI = None
    UGOKI = [None, None]

    def __init__(self, ban, sengo, masu, nari):
        self.ban   = ban
        self.sengo = sengo

        if masu:
            if nari == 1:
                ugoki = frozenset([m for m in self.ban if masu.koma is None])
            else:
                if self.sengo == 1: self.ban.kaiten()
                ugoki = self._tegoma_ugoki()
                if self.sengo == 1: self.ban.kaiten()
            if masu not in ugoki:
                raise CanNotPlaceKomaError(self, masu)
            masu.koma = self

        self.masu  = masu
        self.nari  = nari
        self.index = None

    def __cmp__(self, other):
        return cmp(self.KACHI, other.KACHI)

    def dump(self, string_class_name=False):
        if self.masu:
            masu = self.masu.dump()
        else:
            masu = None

        class_name = self.__class__
        if string_class_name:
            class_name = class_name.__name__

        return (self.sengo, class_name, masu, self.nari)

    def kiki(self):
        if self.sengo == 1: self.ban.kaiten()
        kiki = self._banjyo_ugoki(True)
        if self.sengo == 1: self.ban.kaiten()

        return kiki

    def ugoki(self, teban=None):
        if (teban != None) and ((self.ban.teban != teban) or (self.sengo != teban)):
            return frozenset([])

        if self.sengo == 1: self.ban.kaiten()
        if self.masu:
            ugoki = self._banjyo_ugoki()
        else:
            ugoki = self._tegoma_ugoki()
        if self.sengo == 1: self.ban.kaiten()

        oute = set()
        for masu in ugoki:
            ban = self.ban.clone()
            koma = ban.komas[self.index]
            koma.idou(masu.x, masu.y, check_ugoki=False)
            ban.teban = self.ban.teban
            if ban.oute():
                oute.add(masu)

        return ugoki.difference(oute)

    def idou(self, x, y, naru=0, check_ugoki=True):
        masu = self.ban.masu(x, y)

        if self.sengo <> self.ban.teban:
            raise TebanError(self, masu)

        if check_ugoki and (masu not in self.ugoki()):
            raise CanNotPlaceKomaError(self, masu)

        if self.masu and self.masu.koma:
            self.masu.koma = None

        koma = masu.koma
        if koma:
            koma.masu  = None
            koma.sengo = self.sengo
            koma.nari  = 0

        masu.koma = self
        self.masu = masu

        if naru == 1 and self.UGOKI[1]:
            self.nari = 1

        if self.ban.teban == 0:
            self.ban.teban = 1
        else:
            self.ban.teban = 0

    def _banjyo_ugoki(self, kiki=False):
        masus  = []
        ugokis = self.UGOKI[self.nari]

        for hashiru, ugoki in ugokis:
            for mx, my in ugoki:
                x, y = mx, my
                masu = self._banjyo_ugoki_check(x, y, kiki)
                if hashiru:
                    while(masu):
                        masus.append(masu)
                        if masu.koma and masu.koma.sengo <> self.sengo: break
                        x += mx
                        y += my
                        masu = self._banjyo_ugoki_check(x, y, kiki)
                else:
                    if masu:
                        masus.append(masu)

        return frozenset(masus)

    def _tegoma_ugoki(self):
        return frozenset([masu for masu in self.ban if masu.koma is None])

    def _banjyo_ugoki_check(self, x, y, kiki=False):
        if self.masu:
            masu = self.ban.masu(self.masu.x + x, self.masu.y + y)
            if masu:
                if kiki:
                    return masu
                if (masu.koma is None or masu.koma.sengo <> self.sengo):
                    return masu
        return None;

    def narikomi(self, masu):
        if self.sengo == 1: self.ban.kaiten()

        if self.nari == 1 or self.masu is None or self.UGOKI[1] is None:
            narikomi = None
        else:
            narikomi = self._narikomi_check(masu)

        if self.sengo == 1: self.ban.kaiten()

        return narikomi

    def _narikomi_check(self, masu):
        if self.masu.y < 3 or masu.y < 3:
            return [0, 1]
        return None

# 0 1 2 3 4 5 6 7 8
#                 1
#                 2
#                 3
#                 4
#                 5
#                 6
#                 7
#                 8

class Gyoku(Koma):
    KACHI = 1
    UGOKI = [
        [
            (False, frozenset([
                (-1, -1), (0, -1), (1, -1),
                (-1,  0),          (1,  0),
                (-1,  1), (0,  1), (1,  1),
            ]))
        ],
        None
    ]

class Hisya(Koma):
    KACHI = 2
    UGOKI = [
        [
            (True, frozenset([
                         (0, -1),
                (-1,  0),          (1,  0),
                         (0,  1)
            ]))
        ],
        [
            (True, frozenset([
                         (0, -1),
                (-1,  0),          (1,  0),
                         (0,  1)
            ])),
            (False, frozenset([
                (-1, -1),          (1, -1),

                (-1,  1),          (1,  1),
            ]))
        ]
    ]

class Kaku(Koma):
    KACHI = 3
    UGOKI = [
        [
            (True, frozenset([
                (-1, -1),          (1, -1),

                (-1,  1),          (1,  1)
            ]))
        ],
        [
            (True, frozenset([
                (-1, -1),          (1, -1),

                (-1,  1),          (1,  1)
            ])),
            (False, frozenset([
                         (0, -1),
                (-1,  0),          (1,  0),
                         (0,  1)
            ])),
        ]
    ]

class Kin(Koma):
    KACHI = 4
    UGOKI = [
        [
            (False, frozenset([
                (-1, -1), (0, -1), (1, -1),
                (-1,  0),          (1,  0),
                          (0,  1)
            ]))
        ],
        None
    ]

class Gin(Koma):
    KACHI = 5
    UGOKI = [
        [
            (False, frozenset([
                (-1, -1), (0, -1), (1, -1),

                (-1,  1),          (1,  1),
            ]))
        ],
        Kin.UGOKI[0]
    ]

class Keima(Koma):
    KACHI = 6
    UGOKI = [
        [
            (False, frozenset([
                (-1, -2),          (1, -2)


            ]))
        ],
        Kin.UGOKI[0]
    ]

    def _tegoma_ugoki(self):
        return frozenset([
            masu for masu in self.ban if masu.koma is None and masu.y > 1])

    def _narikomi_check(self, masu):
        if masu.y < 2:
            return [1]
        if self.masu.y < 3 or masu.y < 3:
            return [0, 1]
        return None

class Kyosya(Koma):
    KACHI = 7
    UGOKI = [
        [
            (True, frozenset([
                         (0, -1),
            ]))
        ],
        Kin.UGOKI[0]
    ]

    def _tegoma_ugoki(self):
        return frozenset([
            masu for masu in self.ban if masu.koma is None and masu.y > 0])

    def _narikomi_check(self, masu):
        if masu.y == 0:
            return [1]
        if self.masu.y < 3 or masu.y < 3:
            return [0, 1]
        return None

class Fu(Koma):
    KACHI = 8
    UGOKI = [
        [
            (False, frozenset([
                         (0, -1),
            ]))
        ],
        Kin.UGOKI[0]
    ]

    def _tegoma_ugoki(self):
        fu_x = set([
            masu.x for masu in self.ban
                if masu.koma and
                   masu.koma.sengo == self.sengo and
                   isinstance(masu.koma, self.__class__) and
                   (not masu.koma.nari)])
        return frozenset([
            masu for masu in self.ban
                if masu.koma is None and
                   masu.y > 0 and
                   masu.x not in fu_x])

    def _narikomi_check(self, masu):
        if masu.y == 0:
            return [1]
        if self.masu.y < 3 or masu.y < 3:
            return [0, 1]
        return None

class Masu:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.koma = None

    def __str__(self):
        return "(%d,%d):%s" % (self.x, self.y, self.koma)

    def dump(self):
        return (self.x, self.y)

    def kaiten(self):
        self.x = 8 - self.x
        self.y = 8 - self.y

HIRATE = [
    # 0:先手番, 1:後手番
    0,
    [
        # (
        #   0:先手, 1:後手,
        #   駒クラス名文字列,
        #   (列, 行):升目, None:手駒,
        #   0:不成, 1:成駒
        # )
        (1, Kyosya, (0, 0), 0),
        (1, Keima,  (1, 0), 0),
        (1, Gin,    (2, 0), 0),
        (1, Kin,    (3, 0), 0),
        (1, Gyoku,  (4, 0), 0),
        (1, Kin,    (5, 0), 0),
        (1, Gin,    (6, 0), 0),
        (1, Keima,  (7, 0), 0),
        (1, Kyosya, (8, 0), 0),
        (1, Hisya,  (1, 1), 0),
        (1, Kaku,   (7, 1), 0),
        (1, Fu,     (0, 2), 0),
        (1, Fu,     (1, 2), 0),
        (1, Fu,     (2, 2), 0),
        (1, Fu,     (3, 2), 0),
        (1, Fu,     (4, 2), 0),
        (1, Fu,     (5, 2), 0),
        (1, Fu,     (6, 2), 0),
        (1, Fu,     (7, 2), 0),
        (1, Fu,     (8, 2), 0),
        (0, Fu,     (0, 6), 0),
        (0, Fu,     (1, 6), 0),
        (0, Fu,     (2, 6), 0),
        (0, Fu,     (3, 6), 0),
        (0, Fu,     (4, 6), 0),
        (0, Fu,     (5, 6), 0),
        (0, Fu,     (6, 6), 0),
        (0, Fu,     (7, 6), 0),
        (0, Fu,     (8, 6), 0),
        (0, Kaku,   (1, 7), 0),
        (0, Hisya,  (7, 7), 0),
        (0, Kyosya, (0, 8), 0),
        (0, Keima,  (1, 8), 0),
        (0, Gin,    (2, 8), 0),
        (0, Kin,    (3, 8), 0),
        (0, Gyoku,  (4, 8), 0),
        (0, Kin,    (5, 8), 0),
        (0, Gin,    (6, 8), 0),
        (0, Keima,  (7, 8), 0),
        (0, Kyosya, (8, 8), 0),
    ]
]

class Shogiban:
    def __init__(self, data=HIRATE):
        self.teban    = data[0]
        self.masus    = [[Masu(x, y) for y in range(9)] for x in range(9)]
        self.komas    = []
        self.gyokus   = {}

        koma_data = zip(data[1], range(0, len(data[1])))
        for (sengo, koma_class, masu, nari), (i) in koma_data:
            if isinstance(koma_class, unicode):
                koma_class = eval(koma_class)
            if masu:
                x, y = masu
                masu = self.masus[x][y]
            koma = koma_class(self, sengo, masu, nari)
            koma.index = i
            self.komas.append(koma)
            if koma_class == Gyoku:
                self.gyokus[koma.sengo] = koma

    def __iter__(self):
        for x in range(9):
            for y in range(9):
                yield self.masus[x][y]

    def dump(self, string_class_name=False):
        return [self.teban, [koma.dump(string_class_name) for koma in self.komas]]

    def xdump(self, teban):
        shogiban  = []
        mochigoma = [[], []]

        for koma in self.komas:
            if koma.masu:
                shogiban.append(
                    koma.dump(True) + tuple([
                        [(masu.x, masu.y, koma.narikomi(masu)) for masu in koma.ugoki(teban)]
                    ])
                )
            else:
                mochigoma[koma.sengo].append(koma)

        mochigoma = [
            [
                koma.dump(True) + tuple([
                    [(masu.x, masu.y) for masu in koma.ugoki(teban)]
                ]) + tuple([
                    len(list(g))
                ]) for koma, g in itertools.groupby(sorted(komas))
            ] for komas in mochigoma
        ]

        return [self.teban, shogiban, mochigoma[0] + mochigoma[1]]

    def clone(self):
        return self.__class__(self.dump())

    def masu(self, x, y):
        if 0 <= x <= 8 and 0 <= y <= 8:
            return self.masus[x][y]
        else:
            return None

    def kaiten(self):
        for xs in self.masus:
            xs.reverse()
            for masu in xs:
                masu.kaiten()
        self.masus.reverse()

    def mochigoma(self, sengo):
        xs = [a for a in self.komas if a.sengo == sengo and a.masu is None]
        xs.sort()
        return xs

    def kiki(self, sengo):
        kiki = []
        for koma in [a for a in self.komas if a.sengo == sengo]:
            kiki += koma.kiki()
        return frozenset(kiki)

    def oute(self):
        if self.teban not in self.gyokus:
            return None

        gyoku = self.gyokus[self.teban]
        return gyoku.masu in self.kiki(not self.teban)

    def tsumi(self):
        if self.teban not in self.gyokus:
            return None

        gyoku = self.gyokus[self.teban]
        return self.oute() and gyoku.ugoki().issubset(self.kiki(not self.teban))
