#
#  pyshogi.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2012 Jun Kikuchi. All rights reserved.
#

class Error(Exception):
    pass

class CanNotPlaceKomaError(Error):
    def __init__(self, koma, masu):
        self.koma = koma
        self.masu = masu

class Koma:
    KACHI = None
    UGOKI = [None, None]

    def __init__(self, ban, sente, masu=None, narikoma=False):
        self.ban   = ban
        self.sente = sente

        if masu:
            if narikoma:
                masus = [masu for masu in self.ban if masu.koma is None]
            else:
                if not self.sente: self.ban.kaiten()
                ugoki = self._tegoma_ugoki()
                if not self.sente: self.ban.kaiten()
            if masu not in ugoki: raise CanNotPlaceKomaError(self, masu)
            masu.koma = self

        self.masu     = masu
        self.narikoma = narikoma

    def __str__(self):
        return "%s:%s" % (self.__class__.__name__, self.sente)

    def __cmp__(self, other):
        return cmp(self.KACHI, other.KACHI)

    def ugoki(self):
        if not self.sente: self.ban.kaiten()

        if self.masu:
            ugoki = self._banjyo_ugoki()
        else:
            ugoki = self._tegoma_ugoki()

        ugoki = dict([(masu, self._nareru(masu)) for masu in ugoki])

        if not self.sente: self.ban.kaiten()

        return ugoki

    def move(self, masu, naru=False):
        if masu not in self.ugoki():
            raise CanNotPlaceKomaError(self, masu)

        if self.masu and self.masu.koma:
            self.masu.koma = None

        koma = masu.koma
        if koma:
            koma.masu     = None
            koma.sente    = self.sente
            koma.narikoma = False

        masu.koma = self
        self.masu = masu

        if naru and self.UGOKI[1]:
            self.narikoma = True

    def _banjyo_ugoki(self):
        masus = []

        if self.narikoma:
            ugokis = self.UGOKI[1]
        else:
            ugokis = self.UGOKI[0]

        for hashiru, ugoki in ugokis:
            for mx, my in ugoki:
                x, y = mx, my
                masu = self._banjyo_ugoki_check(x, y)
                if hashiru:
                    while(masu):
                        masus.append(masu)
                        if masu.koma and masu.koma.sente <> self.sente: break
                        x += mx
                        y += my
                        masu = self._banjyo_ugoki_check(x, y)
                else:
                    if masu:
                        masus.append(masu)

        return frozenset(masus)

    def _tegoma_ugoki(self):
        return frozenset([masu for masu in self.ban if masu.koma is None])

    def _banjyo_ugoki_check(self, x, y):
        if self.masu:
            masu = self.ban.masu(self.masu.x + x, self.masu.y + y)
            if masu and (masu.koma is None or masu.koma.sente <> self.sente):
                return masu
        return None;

    def _nareru(self, masu):
        if self.narikoma or self.masu is None or self.UGOKI[1] is None:
            return None
        return self._nareru_check(masu)

    def _nareru_check(self, masu):
        if self.masu.y < 3 or masu.y < 3:
            return [False, True]
        return None

# 8 7 6 5 4 3 2 1 0
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
                (1, -1), (0, -1), (-1, -1),
                (1,  0),          (-1,  0),
                (1,  1), (0,  1), (-1,  1),
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
                (1,  0),          (-1,  0),
                         (0,  1)
            ]))
        ],
        [
            (True, frozenset([
                         (0, -1),
                (1,  0),          (-1,  0),
                         (0,  1)
            ])),
            (False, frozenset([
                (1, -1),          (-1, -1),

                (1,  1),          (-1,  1),
            ]))
        ]
    ]

class Kaku(Koma):
    KACHI = 3
    UGOKI = [
        [
            (True, frozenset([
                (1, -1),          (-1, -1),

                (1,  1),          (-1,  1)
            ]))
        ],
        [
            (True, frozenset([
                (1, -1),          (-1, -1),

                (1,  1),          (-1,  1)
            ])),
            (False, frozenset([
                         (0, -1),
                (1,  0),          (-1,  0),
                         (0,  1)
            ])),
        ]
    ]

class Kin(Koma):
    KACHI = 4
    UGOKI = [
        [
            (False, frozenset([
                (1, -1), (0, -1), (-1, -1),
                (1,  0),          (-1,  0),
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
                (1, -1), (0, -1), (-1, -1),

                (1,  1),          (-1,  1),
            ]))
        ],
        Kin.UGOKI[0]
    ]

class Keima(Koma):
    KACHI = 6
    UGOKI = [
        [
            (False, frozenset([
                (1, -2),          (-1, -2)


            ]))
        ],
        Kin.UGOKI[0]
    ]

    def _tegoma_ugoki(self):
        return frozenset([
            masu for masu in self.ban if masu.koma is None and masu.y > 1])

    def _nareru_check(self, masu):
        if masu.y < 2:
            return [True]
        if self.masu.y < 3 or masu.y < 3:
            return [False, True]
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

    def _nareru_check(self, masu):
        if masu.y == 0:
            return [True]
        if self.masu.y < 3 or masu.y < 3:
            return [False, True]
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
                   masu.koma.sente == self.sente and
                   isinstance(masu.koma, self.__class__)])
        return frozenset([
            masu for masu in self.ban
                if masu.koma is None and
                   masu.y > 0 and
                   masu.x not in fu_x])

    def _nareru_check(self, masu):
        if masu.y == 0:
            return [True]
        if self.masu.y < 3 or masu.y < 3:
            return [False, True]
        return None

class Masu:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.koma = None

    def __str__(self):
        return "%d,%d,%s" % (self.x, self.y, self.koma)

    def kaiten(self):
        self.x = 8 - self.x
        self.y = 8 - self.y

HIRATE = [
    (False, 'Kyosya', (8, 0)),
    (False, 'Keima',  (7, 0)),
    (False, 'Gin',    (6, 0)),
    (False, 'Kin',    (5, 0)),
    (False, 'Gyoku',  (4, 0)),
    (False, 'Kin',    (3, 0)),
    (False, 'Gin',    (2, 0)),
    (False, 'Keima',  (1, 0)),
    (False, 'Kyosya', (0, 0)),
    (False, 'Hisya',  (7, 1)),
    (False, 'Kaku',   (1, 1)),
    (False, 'Fu',     (8, 2)),
    (False, 'Fu',     (7, 2)),
    (False, 'Fu',     (6, 2)),
    (False, 'Fu',     (5, 2)),
    (False, 'Fu',     (4, 2)),
    (False, 'Fu',     (3, 2)),
    (False, 'Fu',     (2, 2)),
    (False, 'Fu',     (1, 2)),
    (False, 'Fu',     (0, 2)),
    (True,  'Fu',     (8, 6)),
    (True,  'Fu',     (7, 6)),
    (True,  'Fu',     (6, 6)),
    (True,  'Fu',     (5, 6)),
    (True,  'Fu',     (4, 6)),
    (True,  'Fu',     (3, 6)),
    (True,  'Fu',     (2, 6)),
    (True,  'Fu',     (1, 6)),
    (True,  'Fu',     (0, 6)),
    (True,  'Kaku',   (7, 7)),
    (True,  'Hisya',  (1, 7)),
    (True,  'Kyosya', (8, 8)),
    (True,  'Keima',  (7, 8)),
    (True,  'Gin',    (6, 8)),
    (True,  'Kin',    (5, 8)),
    (True,  'Gyoku',  (4, 8)),
    (True,  'Kin',    (3, 8)),
    (True,  'Gin',    (2, 8)),
    (True,  'Keima',  (1, 8)),
    (True,  'Kyosya', (0, 8)),
]

class Ban:
    def __init__(self, data=HIRATE):
        self.masus = [[Masu(x, y) for y in range(9)] for x in range(9)]

        self.komas = []
        for sente, koma_class, masu in data:
            if masu:
                x, y = masu
                masu = self.masus[x][y]
            koma = eval(koma_class)(self, sente, masu)
            self.komas.append(koma)

    def __iter__(self):
        for x in range(9):
            for y in range(9):
                yield self.masus[x][y]

    def __str__(self):
        return "\n".join(
            [
                " ".join(
                    [
                        str(self.masus[x][y]) for x in range(8, -1, -1)
                    ]
                ) for y in range(9)
            ]
        )

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

    def mochigoma(self, sente):
        xs = [a for a in self.komas if a.sente == sente and a.masu is None]
        xs.sort()
        return xs
