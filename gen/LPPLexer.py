# Generated from C:/Users/Kira/PycharmProjects/pythonProject/grammar/LPP.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,93,980,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,
        84,2,85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,
        91,7,91,2,92,7,92,2,93,7,93,2,94,7,94,2,95,7,95,2,96,7,96,2,97,7,
        97,2,98,7,98,2,99,7,99,2,100,7,100,2,101,7,101,2,102,7,102,2,103,
        7,103,2,104,7,104,2,105,7,105,2,106,7,106,2,107,7,107,2,108,7,108,
        2,109,7,109,2,110,7,110,2,111,7,111,2,112,7,112,2,113,7,113,2,114,
        7,114,2,115,7,115,2,116,7,116,2,117,7,117,2,118,7,118,2,119,7,119,
        2,120,7,120,2,121,7,121,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,
        1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,
        1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,
        1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,
        1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,
        1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,
        1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,
        1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,1,36,
        1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,38,1,38,
        1,38,1,39,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,41,
        1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,
        1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,44,1,44,
        1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,45,1,45,1,45,1,45,1,45,1,46,
        1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,47,1,47,
        1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,
        1,47,1,47,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,
        1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,49,1,49,1,49,1,49,1,49,1,49,
        1,49,1,49,1,49,1,49,1,49,1,49,1,50,1,50,1,50,1,50,1,50,1,50,1,50,
        1,50,1,50,1,51,1,51,1,51,1,51,1,51,1,52,1,52,1,52,1,52,1,52,1,52,
        1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,
        1,52,1,52,1,52,1,53,1,53,1,53,1,53,1,53,1,53,1,54,1,54,1,54,1,54,
        1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,55,1,55,1,55,1,55,1,55,
        1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,56,1,56,1,56,1,56,1,57,1,57,
        1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,
        1,57,1,58,1,58,1,58,1,58,1,58,1,58,1,58,1,58,1,58,1,58,1,59,1,59,
        1,59,1,59,1,59,1,59,1,59,1,59,1,59,1,59,1,59,1,59,1,59,1,59,1,59,
        1,59,1,59,1,60,1,60,1,60,1,60,1,60,1,60,1,60,1,60,1,60,1,60,1,60,
        1,60,1,60,1,60,1,60,1,60,1,61,1,61,1,61,1,61,1,61,1,61,1,61,1,61,
        1,61,1,61,1,61,1,61,1,61,1,61,1,62,1,62,1,62,1,62,1,62,1,62,1,62,
        1,62,1,62,1,62,1,62,1,62,1,62,1,62,1,62,1,62,1,62,1,63,1,63,1,63,
        1,63,1,63,1,63,1,63,1,63,1,63,1,63,1,63,1,63,1,64,1,64,1,64,1,64,
        1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,65,1,65,
        1,65,1,65,1,65,1,65,1,65,1,65,1,65,1,66,1,66,1,67,1,67,1,68,1,68,
        1,69,1,69,1,69,1,69,1,70,1,70,1,70,1,70,1,71,1,71,1,72,1,72,1,73,
        1,73,1,74,1,74,1,74,1,75,1,75,1,76,1,76,1,76,1,77,1,77,1,78,1,78,
        1,78,1,79,1,79,1,80,1,80,1,81,1,81,1,81,1,82,4,82,814,8,82,11,82,
        12,82,815,1,82,1,82,5,82,820,8,82,10,82,12,82,823,9,82,1,82,1,82,
        4,82,827,8,82,11,82,12,82,828,3,82,831,8,82,1,83,4,83,834,8,83,11,
        83,12,83,835,1,84,1,84,1,85,1,85,5,85,842,8,85,10,85,12,85,845,9,
        85,1,85,1,85,1,86,1,86,1,86,1,86,1,86,3,86,854,8,86,1,87,1,87,1,
        87,1,87,1,88,1,88,1,88,1,88,1,88,3,88,865,8,88,1,89,1,89,1,89,1,
        89,1,89,1,89,1,89,1,89,1,89,1,89,1,90,1,90,1,90,1,90,1,90,1,90,1,
        91,1,91,1,92,1,92,1,93,1,93,1,94,1,94,1,95,1,95,1,96,1,96,1,97,1,
        97,1,98,1,98,1,99,1,99,1,100,1,100,1,101,1,101,1,102,1,102,1,103,
        1,103,1,104,1,104,1,105,1,105,1,106,1,106,1,107,1,107,1,108,1,108,
        1,109,1,109,1,110,1,110,1,111,1,111,1,112,1,112,1,113,1,113,1,114,
        1,114,1,115,1,115,1,116,1,116,1,117,1,117,5,117,937,8,117,10,117,
        12,117,940,9,117,1,118,4,118,943,8,118,11,118,12,118,944,1,118,1,
        118,1,119,4,119,950,8,119,11,119,12,119,951,1,119,1,119,1,120,1,
        120,1,120,1,120,5,120,960,8,120,10,120,12,120,963,9,120,1,120,1,
        120,1,120,1,120,1,120,1,121,1,121,1,121,1,121,5,121,974,8,121,10,
        121,12,121,977,9,121,1,121,1,121,1,961,0,122,1,1,3,2,5,3,7,4,9,5,
        11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,
        17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,
        28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,
        39,79,40,81,41,83,42,85,43,87,44,89,45,91,46,93,47,95,48,97,49,99,
        50,101,51,103,52,105,53,107,54,109,55,111,56,113,57,115,58,117,59,
        119,60,121,61,123,62,125,63,127,64,129,65,131,66,133,67,135,68,137,
        69,139,70,141,71,143,72,145,73,147,74,149,75,151,76,153,77,155,78,
        157,79,159,80,161,81,163,82,165,83,167,84,169,0,171,85,173,0,175,
        86,177,0,179,87,181,88,183,0,185,0,187,0,189,0,191,0,193,0,195,0,
        197,0,199,0,201,0,203,0,205,0,207,0,209,0,211,0,213,0,215,0,217,
        0,219,0,221,0,223,0,225,0,227,0,229,0,231,0,233,0,235,89,237,90,
        239,91,241,92,243,93,1,0,33,1,0,48,57,1,0,34,34,1,0,39,39,2,0,65,
        65,97,97,2,0,66,66,98,98,2,0,67,67,99,99,2,0,68,68,100,100,2,0,69,
        69,101,101,2,0,70,70,102,102,2,0,71,71,103,103,2,0,72,72,104,104,
        2,0,73,73,105,105,2,0,74,74,106,106,2,0,75,75,107,107,2,0,76,76,
        108,108,2,0,77,77,109,109,2,0,78,78,110,110,2,0,79,79,111,111,2,
        0,80,80,112,112,2,0,81,81,113,113,2,0,82,82,114,114,2,0,83,83,115,
        115,2,0,84,84,116,116,2,0,85,85,117,117,2,0,86,86,118,118,2,0,87,
        87,119,119,2,0,88,88,120,120,2,0,89,89,121,121,2,0,90,90,122,122,
        4,0,36,36,65,90,95,95,97,122,5,0,36,36,48,57,65,90,95,95,97,122,
        2,0,10,10,13,13,2,0,9,9,32,32,965,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,
        0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,
        0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,
        0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,
        0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,
        0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,
        0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,
        0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,
        0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,
        0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,
        1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,
        0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,
        0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,0,
        133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,0,139,1,0,0,0,0,141,1,0,
        0,0,0,143,1,0,0,0,0,145,1,0,0,0,0,147,1,0,0,0,0,149,1,0,0,0,0,151,
        1,0,0,0,0,153,1,0,0,0,0,155,1,0,0,0,0,157,1,0,0,0,0,159,1,0,0,0,
        0,161,1,0,0,0,0,163,1,0,0,0,0,165,1,0,0,0,0,167,1,0,0,0,0,171,1,
        0,0,0,0,175,1,0,0,0,0,179,1,0,0,0,0,181,1,0,0,0,0,235,1,0,0,0,0,
        237,1,0,0,0,0,239,1,0,0,0,0,241,1,0,0,0,0,243,1,0,0,0,1,245,1,0,
        0,0,3,247,1,0,0,0,5,249,1,0,0,0,7,251,1,0,0,0,9,253,1,0,0,0,11,255,
        1,0,0,0,13,257,1,0,0,0,15,260,1,0,0,0,17,263,1,0,0,0,19,265,1,0,
        0,0,21,272,1,0,0,0,23,276,1,0,0,0,25,284,1,0,0,0,27,288,1,0,0,0,
        29,295,1,0,0,0,31,298,1,0,0,0,33,307,1,0,0,0,35,312,1,0,0,0,37,317,
        1,0,0,0,39,326,1,0,0,0,41,331,1,0,0,0,43,336,1,0,0,0,45,342,1,0,
        0,0,47,349,1,0,0,0,49,363,1,0,0,0,51,367,1,0,0,0,53,375,1,0,0,0,
        55,383,1,0,0,0,57,388,1,0,0,0,59,391,1,0,0,0,61,399,1,0,0,0,63,410,
        1,0,0,0,65,417,1,0,0,0,67,422,1,0,0,0,69,431,1,0,0,0,71,440,1,0,
        0,0,73,447,1,0,0,0,75,456,1,0,0,0,77,464,1,0,0,0,79,467,1,0,0,0,
        81,473,1,0,0,0,83,478,1,0,0,0,85,488,1,0,0,0,87,496,1,0,0,0,89,503,
        1,0,0,0,91,512,1,0,0,0,93,517,1,0,0,0,95,529,1,0,0,0,97,546,1,0,
        0,0,99,564,1,0,0,0,101,576,1,0,0,0,103,585,1,0,0,0,105,590,1,0,0,
        0,107,612,1,0,0,0,109,618,1,0,0,0,111,630,1,0,0,0,113,642,1,0,0,
        0,115,646,1,0,0,0,117,662,1,0,0,0,119,672,1,0,0,0,121,689,1,0,0,
        0,123,705,1,0,0,0,125,719,1,0,0,0,127,736,1,0,0,0,129,748,1,0,0,
        0,131,763,1,0,0,0,133,772,1,0,0,0,135,774,1,0,0,0,137,776,1,0,0,
        0,139,778,1,0,0,0,141,782,1,0,0,0,143,786,1,0,0,0,145,788,1,0,0,
        0,147,790,1,0,0,0,149,792,1,0,0,0,151,795,1,0,0,0,153,797,1,0,0,
        0,155,800,1,0,0,0,157,802,1,0,0,0,159,805,1,0,0,0,161,807,1,0,0,
        0,163,809,1,0,0,0,165,830,1,0,0,0,167,833,1,0,0,0,169,837,1,0,0,
        0,171,839,1,0,0,0,173,853,1,0,0,0,175,855,1,0,0,0,177,864,1,0,0,
        0,179,866,1,0,0,0,181,876,1,0,0,0,183,882,1,0,0,0,185,884,1,0,0,
        0,187,886,1,0,0,0,189,888,1,0,0,0,191,890,1,0,0,0,193,892,1,0,0,
        0,195,894,1,0,0,0,197,896,1,0,0,0,199,898,1,0,0,0,201,900,1,0,0,
        0,203,902,1,0,0,0,205,904,1,0,0,0,207,906,1,0,0,0,209,908,1,0,0,
        0,211,910,1,0,0,0,213,912,1,0,0,0,215,914,1,0,0,0,217,916,1,0,0,
        0,219,918,1,0,0,0,221,920,1,0,0,0,223,922,1,0,0,0,225,924,1,0,0,
        0,227,926,1,0,0,0,229,928,1,0,0,0,231,930,1,0,0,0,233,932,1,0,0,
        0,235,934,1,0,0,0,237,942,1,0,0,0,239,949,1,0,0,0,241,955,1,0,0,
        0,243,969,1,0,0,0,245,246,5,40,0,0,246,2,1,0,0,0,247,248,5,41,0,
        0,248,4,1,0,0,0,249,250,5,58,0,0,250,6,1,0,0,0,251,252,5,91,0,0,
        252,8,1,0,0,0,253,254,5,93,0,0,254,10,1,0,0,0,255,256,5,44,0,0,256,
        12,1,0,0,0,257,258,5,60,0,0,258,259,5,45,0,0,259,14,1,0,0,0,260,
        261,5,45,0,0,261,262,5,62,0,0,262,16,1,0,0,0,263,264,5,46,0,0,264,
        18,1,0,0,0,265,266,3,199,99,0,266,267,3,209,104,0,267,268,3,199,
        99,0,268,269,3,187,93,0,269,270,3,199,99,0,270,271,3,211,105,0,271,
        20,1,0,0,0,272,273,3,193,96,0,273,274,3,199,99,0,274,275,3,209,104,
        0,275,22,1,0,0,0,276,277,3,191,95,0,277,278,3,219,109,0,278,279,
        3,187,93,0,279,280,3,217,108,0,280,281,3,199,99,0,281,282,3,185,
        92,0,282,283,3,183,91,0,283,24,1,0,0,0,284,285,3,205,102,0,285,286,
        3,191,95,0,286,287,3,183,91,0,287,26,1,0,0,0,288,289,3,205,102,0,
        289,290,3,205,102,0,290,291,3,183,91,0,291,292,3,207,103,0,292,293,
        3,183,91,0,293,294,3,217,108,0,294,28,1,0,0,0,295,296,3,219,109,
        0,296,297,3,199,99,0,297,30,1,0,0,0,298,299,3,191,95,0,299,300,3,
        209,104,0,300,301,3,221,110,0,301,302,3,211,105,0,302,303,3,209,
        104,0,303,304,3,187,93,0,304,305,3,191,95,0,305,306,3,219,109,0,
        306,32,1,0,0,0,307,308,3,219,109,0,308,309,3,199,99,0,309,310,3,
        209,104,0,310,311,3,211,105,0,311,34,1,0,0,0,312,313,3,187,93,0,
        313,314,3,183,91,0,314,315,3,219,109,0,315,316,3,211,105,0,316,36,
        1,0,0,0,317,318,3,207,103,0,318,319,3,199,99,0,319,320,3,191,95,
        0,320,321,3,209,104,0,321,322,3,221,110,0,322,323,3,217,108,0,323,
        324,3,183,91,0,324,325,3,219,109,0,325,38,1,0,0,0,326,327,3,197,
        98,0,327,328,3,183,91,0,328,329,3,195,97,0,329,330,3,183,91,0,330,
        40,1,0,0,0,331,332,3,213,106,0,332,333,3,183,91,0,333,334,3,217,
        108,0,334,335,3,183,91,0,335,42,1,0,0,0,336,337,3,197,98,0,337,338,
        3,183,91,0,338,339,3,219,109,0,339,340,3,221,110,0,340,341,3,183,
        91,0,341,44,1,0,0,0,342,343,3,217,108,0,343,344,3,191,95,0,344,345,
        3,213,106,0,345,346,3,199,99,0,346,347,3,221,110,0,347,348,3,183,
        91,0,348,46,1,0,0,0,349,350,3,213,106,0,350,351,3,217,108,0,351,
        352,3,211,105,0,352,353,3,187,93,0,353,354,3,191,95,0,354,355,3,
        189,94,0,355,356,3,199,99,0,356,357,3,207,103,0,357,358,3,199,99,
        0,358,359,3,191,95,0,359,360,3,209,104,0,360,361,3,221,110,0,361,
        362,3,211,105,0,362,48,1,0,0,0,363,364,3,225,112,0,364,365,3,183,
        91,0,365,366,3,217,108,0,366,50,1,0,0,0,367,368,3,193,96,0,368,369,
        3,223,111,0,369,370,3,209,104,0,370,371,3,187,93,0,371,372,3,199,
        99,0,372,373,3,211,105,0,373,374,3,209,104,0,374,52,1,0,0,0,375,
        376,3,217,108,0,376,377,3,191,95,0,377,378,3,221,110,0,378,379,3,
        211,105,0,379,380,3,217,108,0,380,381,3,209,104,0,381,382,3,191,
        95,0,382,54,1,0,0,0,383,384,3,221,110,0,384,385,3,199,99,0,385,386,
        3,213,106,0,386,387,3,211,105,0,387,56,1,0,0,0,388,389,3,191,95,
        0,389,390,3,219,109,0,390,58,1,0,0,0,391,392,3,183,91,0,392,393,
        3,217,108,0,393,394,3,187,93,0,394,395,3,197,98,0,395,396,3,199,
        99,0,396,397,3,225,112,0,397,398,3,211,105,0,398,60,1,0,0,0,399,
        400,3,219,109,0,400,401,3,191,95,0,401,402,3,187,93,0,402,403,3,
        223,111,0,403,404,3,191,95,0,404,405,3,209,104,0,405,406,3,187,93,
        0,406,407,3,199,99,0,407,408,3,183,91,0,408,409,3,205,102,0,409,
        62,1,0,0,0,410,411,3,191,95,0,411,412,3,209,104,0,412,413,3,221,
        110,0,413,414,3,191,95,0,414,415,3,217,108,0,415,416,3,211,105,0,
        416,64,1,0,0,0,417,418,3,217,108,0,418,419,3,191,95,0,419,420,3,
        183,91,0,420,421,3,205,102,0,421,66,1,0,0,0,422,423,3,187,93,0,423,
        424,3,183,91,0,424,425,3,217,108,0,425,426,3,183,91,0,426,427,3,
        187,93,0,427,428,3,221,110,0,428,429,3,191,95,0,429,430,3,217,108,
        0,430,68,1,0,0,0,431,432,3,185,92,0,432,433,3,211,105,0,433,434,
        3,211,105,0,434,435,3,205,102,0,435,436,3,191,95,0,436,437,3,183,
        91,0,437,438,3,209,104,0,438,439,3,211,105,0,439,70,1,0,0,0,440,
        441,3,187,93,0,441,442,3,183,91,0,442,443,3,189,94,0,443,444,3,191,
        95,0,444,445,3,209,104,0,445,446,3,183,91,0,446,72,1,0,0,0,447,448,
        3,217,108,0,448,449,3,191,95,0,449,450,3,195,97,0,450,451,3,199,
        99,0,451,452,3,219,109,0,452,453,3,221,110,0,453,454,3,217,108,0,
        454,455,3,211,105,0,455,74,1,0,0,0,456,457,3,183,91,0,457,458,3,
        217,108,0,458,459,3,217,108,0,459,460,3,191,95,0,460,461,3,195,97,
        0,461,462,3,205,102,0,462,463,3,211,105,0,463,76,1,0,0,0,464,465,
        3,189,94,0,465,466,3,191,95,0,466,78,1,0,0,0,467,468,3,183,91,0,
        468,469,3,185,92,0,469,470,3,217,108,0,470,471,3,199,99,0,471,472,
        3,217,108,0,472,80,1,0,0,0,473,474,3,187,93,0,474,475,3,211,105,
        0,475,476,3,207,103,0,476,477,3,211,105,0,477,82,1,0,0,0,478,479,
        3,191,95,0,479,480,3,219,109,0,480,481,3,187,93,0,481,482,3,217,
        108,0,482,483,3,199,99,0,483,484,3,221,110,0,484,485,3,223,111,0,
        485,486,3,217,108,0,486,487,3,183,91,0,487,84,1,0,0,0,488,489,3,
        205,102,0,489,490,3,191,95,0,490,491,3,187,93,0,491,492,3,221,110,
        0,492,493,3,223,111,0,493,494,3,217,108,0,494,495,3,183,91,0,495,
        86,1,0,0,0,496,497,3,187,93,0,497,498,3,191,95,0,498,499,3,217,108,
        0,499,500,3,217,108,0,500,501,3,183,91,0,501,502,3,217,108,0,502,
        88,1,0,0,0,503,504,3,191,95,0,504,505,3,219,109,0,505,506,3,187,
        93,0,506,507,3,217,108,0,507,508,3,199,99,0,508,509,3,185,92,0,509,
        510,3,199,99,0,510,511,3,217,108,0,511,90,1,0,0,0,512,513,3,205,
        102,0,513,514,3,191,95,0,514,515,3,191,95,0,515,516,3,217,108,0,
        516,92,1,0,0,0,517,518,3,209,104,0,518,519,3,223,111,0,519,520,3,
        191,95,0,520,521,3,225,112,0,521,522,3,183,91,0,522,523,5,95,0,0,
        523,524,3,205,102,0,524,525,3,199,99,0,525,526,3,209,104,0,526,527,
        3,191,95,0,527,528,3,183,91,0,528,94,1,0,0,0,529,530,3,205,102,0,
        530,531,3,199,99,0,531,532,3,207,103,0,532,533,3,213,106,0,533,534,
        3,199,99,0,534,535,3,183,91,0,535,536,3,217,108,0,536,537,5,95,0,
        0,537,538,3,213,106,0,538,539,3,183,91,0,539,540,3,209,104,0,540,
        541,3,221,110,0,541,542,3,183,91,0,542,543,3,205,102,0,543,544,3,
        205,102,0,544,545,3,183,91,0,545,96,1,0,0,0,546,547,3,213,106,0,
        547,548,3,211,105,0,548,549,3,219,109,0,549,550,3,199,99,0,550,551,
        3,187,93,0,551,552,3,199,99,0,552,553,3,211,105,0,553,554,3,209,
        104,0,554,555,3,183,91,0,555,556,3,217,108,0,556,557,5,95,0,0,557,
        558,3,187,93,0,558,559,3,223,111,0,559,560,3,217,108,0,560,561,3,
        219,109,0,561,562,3,211,105,0,562,563,3,217,108,0,563,98,1,0,0,0,
        564,565,3,199,99,0,565,566,3,217,108,0,566,567,5,95,0,0,567,568,
        3,183,91,0,568,569,5,95,0,0,569,570,3,199,99,0,570,571,3,209,104,
        0,571,572,3,199,99,0,572,573,3,187,93,0,573,574,3,199,99,0,574,575,
        3,211,105,0,575,100,1,0,0,0,576,577,3,199,99,0,577,578,3,217,108,
        0,578,579,5,95,0,0,579,580,3,183,91,0,580,581,5,95,0,0,581,582,3,
        193,96,0,582,583,3,199,99,0,583,584,3,209,104,0,584,102,1,0,0,0,
        585,586,3,199,99,0,586,587,3,217,108,0,587,588,5,95,0,0,588,589,
        3,183,91,0,589,104,1,0,0,0,590,591,3,199,99,0,591,592,3,209,104,
        0,592,593,3,199,99,0,593,594,3,187,93,0,594,595,3,199,99,0,595,596,
        3,183,91,0,596,597,3,205,102,0,597,598,3,199,99,0,598,599,3,233,
        116,0,599,600,3,183,91,0,600,601,3,217,108,0,601,602,5,95,0,0,602,
        603,3,183,91,0,603,604,3,205,102,0,604,605,3,191,95,0,605,606,3,
        183,91,0,606,607,3,221,110,0,607,608,3,211,105,0,608,609,3,217,108,
        0,609,610,3,199,99,0,610,611,3,211,105,0,611,106,1,0,0,0,612,613,
        3,213,106,0,613,614,3,183,91,0,614,615,3,223,111,0,615,616,3,219,
        109,0,616,617,3,183,91,0,617,108,1,0,0,0,618,619,3,187,93,0,619,
        620,3,211,105,0,620,621,3,205,102,0,621,622,3,211,105,0,622,623,
        3,217,108,0,623,624,5,95,0,0,624,625,3,221,110,0,625,626,3,191,95,
        0,626,627,3,229,114,0,627,628,3,221,110,0,628,629,3,211,105,0,629,
        110,1,0,0,0,630,631,3,187,93,0,631,632,3,211,105,0,632,633,3,205,
        102,0,633,634,3,211,105,0,634,635,3,217,108,0,635,636,5,95,0,0,636,
        637,3,193,96,0,637,638,3,211,105,0,638,639,3,209,104,0,639,640,3,
        189,94,0,640,641,3,211,105,0,641,112,1,0,0,0,642,643,3,193,96,0,
        643,644,3,189,94,0,644,645,3,183,91,0,645,114,1,0,0,0,646,647,3,
        213,106,0,647,648,3,211,105,0,648,649,3,219,109,0,649,650,3,199,
        99,0,650,651,3,187,93,0,651,652,3,199,99,0,652,653,3,211,105,0,653,
        654,3,209,104,0,654,655,5,95,0,0,655,656,3,183,91,0,656,657,3,187,
        93,0,657,658,3,221,110,0,658,659,3,223,111,0,659,660,3,183,91,0,
        660,661,3,205,102,0,661,116,1,0,0,0,662,663,3,183,91,0,663,664,3,
        205,102,0,664,665,3,191,95,0,665,666,3,183,91,0,666,667,3,221,110,
        0,667,668,3,211,105,0,668,669,3,217,108,0,669,670,3,199,99,0,670,
        671,3,211,105,0,671,118,1,0,0,0,672,673,3,211,105,0,673,674,3,185,
        92,0,674,675,3,221,110,0,675,676,3,191,95,0,676,677,3,209,104,0,
        677,678,3,191,95,0,678,679,3,217,108,0,679,680,5,95,0,0,680,681,
        3,187,93,0,681,682,3,183,91,0,682,683,3,217,108,0,683,684,3,183,
        91,0,684,685,3,187,93,0,685,686,3,221,110,0,686,687,3,191,95,0,687,
        688,3,217,108,0,688,120,1,0,0,0,689,690,3,191,95,0,690,691,3,209,
        104,0,691,692,3,221,110,0,692,693,3,191,95,0,693,694,3,217,108,0,
        694,695,3,211,105,0,695,696,5,95,0,0,696,697,3,183,91,0,697,698,
        5,95,0,0,698,699,3,187,93,0,699,700,3,183,91,0,700,701,3,189,94,
        0,701,702,3,191,95,0,702,703,3,209,104,0,703,704,3,183,91,0,704,
        122,1,0,0,0,705,706,3,217,108,0,706,707,3,191,95,0,707,708,3,183,
        91,0,708,709,3,205,102,0,709,710,5,95,0,0,710,711,3,183,91,0,711,
        712,5,95,0,0,712,713,3,187,93,0,713,714,3,183,91,0,714,715,3,189,
        94,0,715,716,3,191,95,0,716,717,3,209,104,0,717,718,3,183,91,0,718,
        124,1,0,0,0,719,720,3,221,110,0,720,721,3,191,95,0,721,722,3,187,
        93,0,722,723,3,205,102,0,723,724,3,183,91,0,724,725,5,95,0,0,725,
        726,3,213,106,0,726,727,3,217,108,0,727,728,3,191,95,0,728,729,3,
        219,109,0,729,730,3,199,99,0,730,731,3,211,105,0,731,732,3,209,104,
        0,732,733,3,183,91,0,733,734,3,189,94,0,734,735,3,183,91,0,735,126,
        1,0,0,0,736,737,3,225,112,0,737,738,3,183,91,0,738,739,3,205,102,
        0,739,740,3,211,105,0,740,741,3,217,108,0,741,742,5,95,0,0,742,743,
        3,183,91,0,743,744,3,219,109,0,744,745,3,187,93,0,745,746,3,199,
        99,0,746,747,3,199,99,0,747,128,1,0,0,0,748,749,3,187,93,0,749,750,
        3,183,91,0,750,751,3,217,108,0,751,752,3,183,91,0,752,753,3,187,
        93,0,753,754,3,221,110,0,754,755,3,191,95,0,755,756,3,217,108,0,
        756,757,5,95,0,0,757,758,3,183,91,0,758,759,3,219,109,0,759,760,
        3,187,93,0,760,761,3,199,99,0,761,762,3,199,99,0,762,130,1,0,0,0,
        763,764,3,205,102,0,764,765,3,211,105,0,765,766,3,209,104,0,766,
        767,3,195,97,0,767,768,3,199,99,0,768,769,3,221,110,0,769,770,3,
        223,111,0,770,771,3,189,94,0,771,132,1,0,0,0,772,773,5,94,0,0,773,
        134,1,0,0,0,774,775,5,42,0,0,775,136,1,0,0,0,776,777,5,47,0,0,777,
        138,1,0,0,0,778,779,3,207,103,0,779,780,3,211,105,0,780,781,3,189,
        94,0,781,140,1,0,0,0,782,783,3,189,94,0,783,784,3,199,99,0,784,785,
        3,225,112,0,785,142,1,0,0,0,786,787,5,43,0,0,787,144,1,0,0,0,788,
        789,5,45,0,0,789,146,1,0,0,0,790,791,5,61,0,0,791,148,1,0,0,0,792,
        793,5,60,0,0,793,794,5,62,0,0,794,150,1,0,0,0,795,796,5,62,0,0,796,
        152,1,0,0,0,797,798,5,62,0,0,798,799,5,61,0,0,799,154,1,0,0,0,800,
        801,5,60,0,0,801,156,1,0,0,0,802,803,5,60,0,0,803,804,5,61,0,0,804,
        158,1,0,0,0,805,806,3,231,115,0,806,160,1,0,0,0,807,808,3,211,105,
        0,808,162,1,0,0,0,809,810,3,209,104,0,810,811,3,211,105,0,811,164,
        1,0,0,0,812,814,3,169,84,0,813,812,1,0,0,0,814,815,1,0,0,0,815,813,
        1,0,0,0,815,816,1,0,0,0,816,817,1,0,0,0,817,821,5,46,0,0,818,820,
        3,169,84,0,819,818,1,0,0,0,820,823,1,0,0,0,821,819,1,0,0,0,821,822,
        1,0,0,0,822,831,1,0,0,0,823,821,1,0,0,0,824,826,5,46,0,0,825,827,
        3,169,84,0,826,825,1,0,0,0,827,828,1,0,0,0,828,826,1,0,0,0,828,829,
        1,0,0,0,829,831,1,0,0,0,830,813,1,0,0,0,830,824,1,0,0,0,831,166,
        1,0,0,0,832,834,3,169,84,0,833,832,1,0,0,0,834,835,1,0,0,0,835,833,
        1,0,0,0,835,836,1,0,0,0,836,168,1,0,0,0,837,838,7,0,0,0,838,170,
        1,0,0,0,839,843,5,34,0,0,840,842,3,173,86,0,841,840,1,0,0,0,842,
        845,1,0,0,0,843,841,1,0,0,0,843,844,1,0,0,0,844,846,1,0,0,0,845,
        843,1,0,0,0,846,847,5,34,0,0,847,172,1,0,0,0,848,854,8,1,0,0,849,
        850,5,92,0,0,850,854,5,34,0,0,851,852,5,92,0,0,852,854,5,92,0,0,
        853,848,1,0,0,0,853,849,1,0,0,0,853,851,1,0,0,0,854,174,1,0,0,0,
        855,856,5,39,0,0,856,857,3,177,88,0,857,858,5,39,0,0,858,176,1,0,
        0,0,859,865,8,2,0,0,860,861,5,92,0,0,861,865,5,39,0,0,862,863,5,
        92,0,0,863,865,5,92,0,0,864,859,1,0,0,0,864,860,1,0,0,0,864,862,
        1,0,0,0,865,178,1,0,0,0,866,867,3,225,112,0,867,868,3,191,95,0,868,
        869,3,217,108,0,869,870,3,189,94,0,870,871,3,183,91,0,871,872,3,
        189,94,0,872,873,3,191,95,0,873,874,3,217,108,0,874,875,3,211,105,
        0,875,180,1,0,0,0,876,877,3,193,96,0,877,878,3,183,91,0,878,879,
        3,205,102,0,879,880,3,219,109,0,880,881,3,211,105,0,881,182,1,0,
        0,0,882,883,7,3,0,0,883,184,1,0,0,0,884,885,7,4,0,0,885,186,1,0,
        0,0,886,887,7,5,0,0,887,188,1,0,0,0,888,889,7,6,0,0,889,190,1,0,
        0,0,890,891,7,7,0,0,891,192,1,0,0,0,892,893,7,8,0,0,893,194,1,0,
        0,0,894,895,7,9,0,0,895,196,1,0,0,0,896,897,7,10,0,0,897,198,1,0,
        0,0,898,899,7,11,0,0,899,200,1,0,0,0,900,901,7,12,0,0,901,202,1,
        0,0,0,902,903,7,13,0,0,903,204,1,0,0,0,904,905,7,14,0,0,905,206,
        1,0,0,0,906,907,7,15,0,0,907,208,1,0,0,0,908,909,7,16,0,0,909,210,
        1,0,0,0,910,911,7,17,0,0,911,212,1,0,0,0,912,913,7,18,0,0,913,214,
        1,0,0,0,914,915,7,19,0,0,915,216,1,0,0,0,916,917,7,20,0,0,917,218,
        1,0,0,0,918,919,7,21,0,0,919,220,1,0,0,0,920,921,7,22,0,0,921,222,
        1,0,0,0,922,923,7,23,0,0,923,224,1,0,0,0,924,925,7,24,0,0,925,226,
        1,0,0,0,926,927,7,25,0,0,927,228,1,0,0,0,928,929,7,26,0,0,929,230,
        1,0,0,0,930,931,7,27,0,0,931,232,1,0,0,0,932,933,7,28,0,0,933,234,
        1,0,0,0,934,938,7,29,0,0,935,937,7,30,0,0,936,935,1,0,0,0,937,940,
        1,0,0,0,938,936,1,0,0,0,938,939,1,0,0,0,939,236,1,0,0,0,940,938,
        1,0,0,0,941,943,7,31,0,0,942,941,1,0,0,0,943,944,1,0,0,0,944,942,
        1,0,0,0,944,945,1,0,0,0,945,946,1,0,0,0,946,947,6,118,0,0,947,238,
        1,0,0,0,948,950,7,32,0,0,949,948,1,0,0,0,950,951,1,0,0,0,951,949,
        1,0,0,0,951,952,1,0,0,0,952,953,1,0,0,0,953,954,6,119,0,0,954,240,
        1,0,0,0,955,956,5,47,0,0,956,957,5,42,0,0,957,961,1,0,0,0,958,960,
        9,0,0,0,959,958,1,0,0,0,960,963,1,0,0,0,961,962,1,0,0,0,961,959,
        1,0,0,0,962,964,1,0,0,0,963,961,1,0,0,0,964,965,5,42,0,0,965,966,
        5,47,0,0,966,967,1,0,0,0,967,968,6,120,0,0,968,242,1,0,0,0,969,970,
        5,47,0,0,970,971,5,47,0,0,971,975,1,0,0,0,972,974,8,31,0,0,973,972,
        1,0,0,0,974,977,1,0,0,0,975,973,1,0,0,0,975,976,1,0,0,0,976,978,
        1,0,0,0,977,975,1,0,0,0,978,979,6,121,0,0,979,244,1,0,0,0,14,0,815,
        821,828,830,835,843,853,864,938,944,951,961,975,1,6,0,0
    ]

class LPPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    INICIO = 10
    FIN = 11
    ESCRIBA = 12
    LEA = 13
    LLAMAR = 14
    SI = 15
    ENTONCES = 16
    SINO = 17
    CASO = 18
    MIENTRAS = 19
    HAGA = 20
    PARA = 21
    HASTA = 22
    REPITA = 23
    PROCEDIMIENTO = 24
    VAR = 25
    FUNCION = 26
    RETORNE = 27
    TIPO = 28
    ES = 29
    ARCHIVO = 30
    SECUENCIAL = 31
    ENTERO = 32
    REAL = 33
    CARACTER = 34
    BOOLEANO = 35
    CADENA = 36
    REGISTRO = 37
    ARREGLO = 38
    DE = 39
    ABRIR = 40
    COMO = 41
    ESCRITURA = 42
    LECTURA = 43
    CERRAR = 44
    ESCRIBIR = 45
    LEER = 46
    PROC_NUEVA_LINEA = 47
    PROC_LIMPIAR_PANTALLA = 48
    PROC_POSICIONAR_CURSOR = 49
    PROC_IR_A_INICIO = 50
    PROC_IR_A_FIN = 51
    PROC_IR_A = 52
    PROC_INICIALIZAR_ALEATORIO = 53
    PROC_PAUSA = 54
    PROC_COLOR_TEXTO = 55
    PROC_COLOR_FONDO = 56
    FUNC_FDA = 57
    FUNC_POSICION_ACTUAL = 58
    FUNC_ALEATORIO = 59
    FUNC_OBTENER_CARACTER = 60
    FUNC_ENTERO_A_CADENA = 61
    FUNC_REAL_A_CADENA = 62
    FUNC_TECLA_PRESIONADA = 63
    FUNC_VALOR_ASCII = 64
    FUNC_CARACTER_ASCII = 65
    FUNC_LONGITUD = 66
    PODER = 67
    MULT = 68
    DIV = 69
    MOD = 70
    DIV_ENTEROS = 71
    SUMA = 72
    RESTA = 73
    IGUAL = 74
    DESIGUAL = 75
    MAYOR = 76
    MAYOR_IGUAL = 77
    MENOR = 78
    MENOR_IGUAL = 79
    OP_Y = 80
    OP_O = 81
    NO = 82
    LITERAL_REAL = 83
    LITERAL_ENTERO = 84
    LITERAL_CADENA = 85
    LITERAL_CARACTER = 86
    VERDADERO = 87
    FALSO = 88
    ID = 89
    NL = 90
    WS = 91
    COMENTARIO = 92
    COMENTARIO_LINEA = 93

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "':'", "'['", "']'", "','", "'<-'", "'->'", "'.'", 
            "'^'", "'*'", "'/'", "'+'", "'-'", "'='", "'<>'", "'>'", "'>='", 
            "'<'", "'<='" ]

    symbolicNames = [ "<INVALID>",
            "INICIO", "FIN", "ESCRIBA", "LEA", "LLAMAR", "SI", "ENTONCES", 
            "SINO", "CASO", "MIENTRAS", "HAGA", "PARA", "HASTA", "REPITA", 
            "PROCEDIMIENTO", "VAR", "FUNCION", "RETORNE", "TIPO", "ES", 
            "ARCHIVO", "SECUENCIAL", "ENTERO", "REAL", "CARACTER", "BOOLEANO", 
            "CADENA", "REGISTRO", "ARREGLO", "DE", "ABRIR", "COMO", "ESCRITURA", 
            "LECTURA", "CERRAR", "ESCRIBIR", "LEER", "PROC_NUEVA_LINEA", 
            "PROC_LIMPIAR_PANTALLA", "PROC_POSICIONAR_CURSOR", "PROC_IR_A_INICIO", 
            "PROC_IR_A_FIN", "PROC_IR_A", "PROC_INICIALIZAR_ALEATORIO", 
            "PROC_PAUSA", "PROC_COLOR_TEXTO", "PROC_COLOR_FONDO", "FUNC_FDA", 
            "FUNC_POSICION_ACTUAL", "FUNC_ALEATORIO", "FUNC_OBTENER_CARACTER", 
            "FUNC_ENTERO_A_CADENA", "FUNC_REAL_A_CADENA", "FUNC_TECLA_PRESIONADA", 
            "FUNC_VALOR_ASCII", "FUNC_CARACTER_ASCII", "FUNC_LONGITUD", 
            "PODER", "MULT", "DIV", "MOD", "DIV_ENTEROS", "SUMA", "RESTA", 
            "IGUAL", "DESIGUAL", "MAYOR", "MAYOR_IGUAL", "MENOR", "MENOR_IGUAL", 
            "OP_Y", "OP_O", "NO", "LITERAL_REAL", "LITERAL_ENTERO", "LITERAL_CADENA", 
            "LITERAL_CARACTER", "VERDADERO", "FALSO", "ID", "NL", "WS", 
            "COMENTARIO", "COMENTARIO_LINEA" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "INICIO", "FIN", "ESCRIBA", "LEA", "LLAMAR", 
                  "SI", "ENTONCES", "SINO", "CASO", "MIENTRAS", "HAGA", 
                  "PARA", "HASTA", "REPITA", "PROCEDIMIENTO", "VAR", "FUNCION", 
                  "RETORNE", "TIPO", "ES", "ARCHIVO", "SECUENCIAL", "ENTERO", 
                  "REAL", "CARACTER", "BOOLEANO", "CADENA", "REGISTRO", 
                  "ARREGLO", "DE", "ABRIR", "COMO", "ESCRITURA", "LECTURA", 
                  "CERRAR", "ESCRIBIR", "LEER", "PROC_NUEVA_LINEA", "PROC_LIMPIAR_PANTALLA", 
                  "PROC_POSICIONAR_CURSOR", "PROC_IR_A_INICIO", "PROC_IR_A_FIN", 
                  "PROC_IR_A", "PROC_INICIALIZAR_ALEATORIO", "PROC_PAUSA", 
                  "PROC_COLOR_TEXTO", "PROC_COLOR_FONDO", "FUNC_FDA", "FUNC_POSICION_ACTUAL", 
                  "FUNC_ALEATORIO", "FUNC_OBTENER_CARACTER", "FUNC_ENTERO_A_CADENA", 
                  "FUNC_REAL_A_CADENA", "FUNC_TECLA_PRESIONADA", "FUNC_VALOR_ASCII", 
                  "FUNC_CARACTER_ASCII", "FUNC_LONGITUD", "PODER", "MULT", 
                  "DIV", "MOD", "DIV_ENTEROS", "SUMA", "RESTA", "IGUAL", 
                  "DESIGUAL", "MAYOR", "MAYOR_IGUAL", "MENOR", "MENOR_IGUAL", 
                  "OP_Y", "OP_O", "NO", "LITERAL_REAL", "LITERAL_ENTERO", 
                  "DIGITO", "LITERAL_CADENA", "CARACTERES_CADENA", "LITERAL_CARACTER", 
                  "CARACTERES_CARACTER", "VERDADERO", "FALSO", "A", "B", 
                  "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", 
                  "Y", "Z", "ID", "NL", "WS", "COMENTARIO", "COMENTARIO_LINEA" ]

    grammarFileName = "LPP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


