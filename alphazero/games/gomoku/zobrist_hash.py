from .player import GomokuPlayer
from .move import GomokuMove

HASH_CODE = {
    (GomokuMove(x=0, y=0), GomokuPlayer.BLACK): 1640916283469823784,
    (GomokuMove(x=0, y=0), GomokuPlayer.WHITE): 976422092777360760,
    (GomokuMove(x=0, y=1), GomokuPlayer.BLACK): 5174344035470024551,
    (GomokuMove(x=0, y=1), GomokuPlayer.WHITE): 7359103841376922855,
    (GomokuMove(x=0, y=2), GomokuPlayer.BLACK): 3683840070627260062,
    (GomokuMove(x=0, y=2), GomokuPlayer.WHITE): 8228072856136547783,
    (GomokuMove(x=0, y=3), GomokuPlayer.BLACK): 4781225997110054669,
    (GomokuMove(x=0, y=3), GomokuPlayer.WHITE): 4893823867596672933,
    (GomokuMove(x=0, y=4), GomokuPlayer.BLACK): 2726236934715534854,
    (GomokuMove(x=0, y=4), GomokuPlayer.WHITE): 5618301539324386424,
    (GomokuMove(x=0, y=5), GomokuPlayer.BLACK): 8018145959971959321,
    (GomokuMove(x=0, y=5), GomokuPlayer.WHITE): 1843079636245088349,
    (GomokuMove(x=0, y=6), GomokuPlayer.BLACK): 8398094241537125950,
    (GomokuMove(x=0, y=6), GomokuPlayer.WHITE): 1550423550372241642,
    (GomokuMove(x=1, y=0), GomokuPlayer.BLACK): 7267666635062985469,
    (GomokuMove(x=1, y=0), GomokuPlayer.WHITE): 581173385980337258,
    (GomokuMove(x=1, y=1), GomokuPlayer.BLACK): 2755804029137791514,
    (GomokuMove(x=1, y=1), GomokuPlayer.WHITE): 35904717542091710,
    (GomokuMove(x=1, y=2), GomokuPlayer.BLACK): 218228689450734997,
    (GomokuMove(x=1, y=2), GomokuPlayer.WHITE): 2115833085983140724,
    (GomokuMove(x=1, y=3), GomokuPlayer.BLACK): 5518135631188550442,
    (GomokuMove(x=1, y=3), GomokuPlayer.WHITE): 7499550989115490579,
    (GomokuMove(x=1, y=4), GomokuPlayer.BLACK): 3797300871189850364,
    (GomokuMove(x=1, y=4), GomokuPlayer.WHITE): 2191567852829475937,
    (GomokuMove(x=1, y=5), GomokuPlayer.BLACK): 880844307675595395,
    (GomokuMove(x=1, y=5), GomokuPlayer.WHITE): 3552713522320320654,
    (GomokuMove(x=1, y=6), GomokuPlayer.BLACK): 2822951760699762578,
    (GomokuMove(x=1, y=6), GomokuPlayer.WHITE): 416910930979715988,
    (GomokuMove(x=2, y=0), GomokuPlayer.BLACK): 2009231457471665294,
    (GomokuMove(x=2, y=0), GomokuPlayer.WHITE): 3762352618030823404,
    (GomokuMove(x=2, y=1), GomokuPlayer.BLACK): 5984913548168861776,
    (GomokuMove(x=2, y=1), GomokuPlayer.WHITE): 6503516235504236127,
    (GomokuMove(x=2, y=2), GomokuPlayer.BLACK): 1229806532811088600,
    (GomokuMove(x=2, y=2), GomokuPlayer.WHITE): 6403667378488753139,
    (GomokuMove(x=2, y=3), GomokuPlayer.BLACK): 6834898459088232233,
    (GomokuMove(x=2, y=3), GomokuPlayer.WHITE): 6720950737464664131,
    (GomokuMove(x=2, y=4), GomokuPlayer.BLACK): 4330601661321377809,
    (GomokuMove(x=2, y=4), GomokuPlayer.WHITE): 983202811732660786,
    (GomokuMove(x=2, y=5), GomokuPlayer.BLACK): 6144541759721195135,
    (GomokuMove(x=2, y=5), GomokuPlayer.WHITE): 6394553813639702302,
    (GomokuMove(x=2, y=6), GomokuPlayer.BLACK): 3545361177610053601,
    (GomokuMove(x=2, y=6), GomokuPlayer.WHITE): 7197069403095775101,
    (GomokuMove(x=3, y=0), GomokuPlayer.BLACK): 3568942150040948314,
    (GomokuMove(x=3, y=0), GomokuPlayer.WHITE): 320373272878198391,
    (GomokuMove(x=3, y=1), GomokuPlayer.BLACK): 6443600588606445282,
    (GomokuMove(x=3, y=1), GomokuPlayer.WHITE): 7620407476899619038,
    (GomokuMove(x=3, y=2), GomokuPlayer.BLACK): 8642984663253708948,
    (GomokuMove(x=3, y=2), GomokuPlayer.WHITE): 1022459853614314365,
    (GomokuMove(x=3, y=3), GomokuPlayer.BLACK): 915807995535135409,
    (GomokuMove(x=3, y=3), GomokuPlayer.WHITE): 5829333440143641651,
    (GomokuMove(x=3, y=4), GomokuPlayer.BLACK): 8187493544513946830,
    (GomokuMove(x=3, y=4), GomokuPlayer.WHITE): 5044726141028400781,
    (GomokuMove(x=3, y=5), GomokuPlayer.BLACK): 6965253869990056317,
    (GomokuMove(x=3, y=5), GomokuPlayer.WHITE): 8403717502644864312,
    (GomokuMove(x=3, y=6), GomokuPlayer.BLACK): 9021643757703772728,
    (GomokuMove(x=3, y=6), GomokuPlayer.WHITE): 6313095002041670608,
    (GomokuMove(x=4, y=0), GomokuPlayer.BLACK): 147336757761969811,
    (GomokuMove(x=4, y=0), GomokuPlayer.WHITE): 1910494126085310410,
    (GomokuMove(x=4, y=1), GomokuPlayer.BLACK): 6984091560889233111,
    (GomokuMove(x=4, y=1), GomokuPlayer.WHITE): 466524083597063997,
    (GomokuMove(x=4, y=2), GomokuPlayer.BLACK): 3441479182355175061,
    (GomokuMove(x=4, y=2), GomokuPlayer.WHITE): 2746095180737756554,
    (GomokuMove(x=4, y=3), GomokuPlayer.BLACK): 2664637909960193648,
    (GomokuMove(x=4, y=3), GomokuPlayer.WHITE): 7291341194521703100,
    (GomokuMove(x=4, y=4), GomokuPlayer.BLACK): 8154697655695747094,
    (GomokuMove(x=4, y=4), GomokuPlayer.WHITE): 2114104028429241034,
    (GomokuMove(x=4, y=5), GomokuPlayer.BLACK): 1835289597382317042,
    (GomokuMove(x=4, y=5), GomokuPlayer.WHITE): 7227505892898888232,
    (GomokuMove(x=4, y=6), GomokuPlayer.BLACK): 3004645288011388507,
    (GomokuMove(x=4, y=6), GomokuPlayer.WHITE): 1495356981576480351,
    (GomokuMove(x=5, y=0), GomokuPlayer.BLACK): 4951620421028691821,
    (GomokuMove(x=5, y=0), GomokuPlayer.WHITE): 8123449973056489223,
    (GomokuMove(x=5, y=1), GomokuPlayer.BLACK): 2664222284018282314,
    (GomokuMove(x=5, y=1), GomokuPlayer.WHITE): 3537608799066017715,
    (GomokuMove(x=5, y=2), GomokuPlayer.BLACK): 8306916970644611869,
    (GomokuMove(x=5, y=2), GomokuPlayer.WHITE): 410392700898272387,
    (GomokuMove(x=5, y=3), GomokuPlayer.BLACK): 4991353435794258179,
    (GomokuMove(x=5, y=3), GomokuPlayer.WHITE): 2148282771265496014,
    (GomokuMove(x=5, y=4), GomokuPlayer.BLACK): 6183697000055371163,
    (GomokuMove(x=5, y=4), GomokuPlayer.WHITE): 7910104653303428172,
    (GomokuMove(x=5, y=5), GomokuPlayer.BLACK): 6285883028428268987,
    (GomokuMove(x=5, y=5), GomokuPlayer.WHITE): 8086095269928664128,
    (GomokuMove(x=5, y=6), GomokuPlayer.BLACK): 2403276042699612124,
    (GomokuMove(x=5, y=6), GomokuPlayer.WHITE): 7664651586574515693,
    (GomokuMove(x=6, y=0), GomokuPlayer.BLACK): 3956646841639183460,
    (GomokuMove(x=6, y=0), GomokuPlayer.WHITE): 6652304463549046347,
    (GomokuMove(x=6, y=1), GomokuPlayer.BLACK): 6303858011723010979,
    (GomokuMove(x=6, y=1), GomokuPlayer.WHITE): 7811649627072386059,
    (GomokuMove(x=6, y=2), GomokuPlayer.BLACK): 943884219679996980,
    (GomokuMove(x=6, y=2), GomokuPlayer.WHITE): 6002480261800803925,
    (GomokuMove(x=6, y=3), GomokuPlayer.BLACK): 8888833231149615610,
    (GomokuMove(x=6, y=3), GomokuPlayer.WHITE): 730138218776755486,
    (GomokuMove(x=6, y=4), GomokuPlayer.BLACK): 5664084051140084591,
    (GomokuMove(x=6, y=4), GomokuPlayer.WHITE): 2284608952441839284,
    (GomokuMove(x=6, y=5), GomokuPlayer.BLACK): 4499308249641073209,
    (GomokuMove(x=6, y=5), GomokuPlayer.WHITE): 8150312859618236882,
    (GomokuMove(x=6, y=6), GomokuPlayer.BLACK): 8855075870559370006,
    (GomokuMove(x=6, y=6), GomokuPlayer.WHITE): 2473535247903845189,
}

EMPTY_BOARD = 0
