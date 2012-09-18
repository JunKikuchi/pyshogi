#
#  pyshogi.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2012 Jun Kikuchi. All rights reserved.
#

class Error(Exception):
    pass

class KomaCanNotMoveError(Error):
    def __init__(self, koma, masu):
        self.koma = koma
        self.masu = masu

class Koma:
    UGOKI = [None, None]
    narikoma = False

    def __init__(self, ban, masu, sente):
        self.ban   = ban
        self.masu  = masu
        self.sente = sente

        if self.masu: masu.koma = self

    def __str__(self):
        return "%s:%s" % (self.__class__.__name__, self.sente)

    def naru(self):
        if self.UGOKI[1]: self.narikoma = True

    def is_movable(self, x, y):
        masu = self.ban.masu(self.masu.x + x, self.masu.y + y)
        if masu and (masu.koma is None or masu.koma.sente <> self.sente):
            return masu
        return None;

    def movables(self):
        masus = []

        if not self.sente: self.masu.ban.round()

        if self.narikoma:
            ugokis = self.UGOKI[1]
        else:
            ugokis = self.UGOKI[0]

        for hashiru, ugoki in ugokis:
            for mx, my in ugoki:
                x, y = mx, my
                masu = self.is_movable(x, y)
                if hashiru:
                    while(masu):
                        masus.append(masu)
                        if masu.koma and masu.koma.sente <> self.sente: break
                        x += mx
                        y += my
                        masu = self.is_movable(x, y)
                else:
                    masus.append(masu)

        if not self.sente: self.masu.ban.round()

        return frozenset(masus)

    def move(self, masu):
        if masu not in self.movables():
            raise KomaCanNotMoveError, self, masu

        koma = masu.koma
        if koma:
            koma.masu     = None
            koma.sente    = self.sente
            koma.narikoma = False

        masu.koma = self

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
    UGOKI = [
        [
            (False, frozenset([
                (1, -2),          (-1, -2)


            ]))
        ],
        Kin.UGOKI[0]
    ]

class Kyosya(Koma):
    UGOKI = [
        [
            (True, frozenset([
                         (0, -1),
            ]))
        ],
        Kin.UGOKI[0]
    ]

class Fu(Koma):
    UGOKI = [
        [
            (False, frozenset([
                         (0, -1),
            ]))
        ],
        Kin.UGOKI[0]
    ]

class Masu:
    koma = None

    def __init__(self, ban, x, y):
        self.ban = ban
        self.x = x
        self.y = y

    def __str__(self):
        return "%d,%d,%s" % (self.x, self.y, self.koma)

    def round(self):
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
        self.masus = [
            [
                Masu(self, x, y) for y in range(0, 9)
            ] for x in range(0, 9)
        ]

        self.mochigomas = {True: [], False: []}

        self.komas = []
        for sente, koma_class, masu in data:
            if masu:
                x, y = masu
                masu = self.masus[x][y]
                koma = eval(koma_class)(self, masu, sente)
            else:
                koma = eval(koma_class)(self, masu, sente)
                self.mochigomas[sente].append(koma)
            self.komas.append(koma)

    def __iter__(self):
        for x in range(0, 9):
            for y in range(0, 9):
                yield self.masus[x][y]

    def __str__(self):
        return "\n".join(
            [
                " ".join(
                    [
                        str(self.masus[x][y]) for x in range(8, -1, -1)
                    ]
                ) for y in range(0, 9)
            ]
        )

    def masu(self, x, y):
        if 0 <= x <= 8 and 0 <= y <= 8:
            return self.masus[x][y]
        else:
            return None

    def round(self):
        for xs in self.masus:
            xs.reverse()
            for masu in xs:
                masu.round()
        self.masus.reverse()

