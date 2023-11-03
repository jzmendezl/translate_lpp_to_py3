# Generated from C:/Users/Kira/PycharmProjects/pythonProject/grammar/LPP.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,93,502,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,1,0,1,0,1,0,1,0,1,0,1,1,1,1,5,1,118,8,1,10,1,
        12,1,121,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,
        5,4,136,8,4,10,4,12,4,139,9,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,147,8,
        5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,158,8,6,1,6,1,6,1,6,1,
        6,1,6,1,7,1,7,1,7,1,7,5,7,169,8,7,10,7,12,7,172,9,7,1,8,3,8,175,
        8,8,1,8,1,8,1,8,1,9,5,9,181,8,9,10,9,12,9,184,9,9,1,10,1,10,1,10,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,197,8,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,212,
        8,11,1,12,1,12,1,12,5,12,217,8,12,10,12,12,12,220,9,12,1,13,1,13,
        1,13,5,13,225,8,13,10,13,12,13,228,9,13,1,14,1,14,1,14,1,14,1,15,
        1,15,1,15,1,15,1,15,1,16,5,16,240,8,16,10,16,12,16,243,9,16,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        3,17,259,8,17,1,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,20,
        1,21,1,21,1,22,1,22,1,22,1,22,3,22,277,8,22,1,22,3,22,280,8,22,1,
        22,1,22,1,22,1,22,3,22,286,8,22,1,22,3,22,289,8,22,1,22,1,22,1,22,
        1,22,3,22,295,8,22,1,22,3,22,298,8,22,3,22,300,8,22,1,23,1,23,1,
        24,1,24,1,24,1,24,1,24,3,24,309,8,24,1,24,1,24,1,24,1,25,1,25,1,
        26,1,26,1,26,1,26,3,26,320,8,26,1,27,1,27,1,27,4,27,325,8,27,11,
        27,12,27,326,1,27,3,27,330,8,27,1,27,1,27,1,27,1,28,1,28,1,28,1,
        28,1,29,1,29,1,29,1,29,5,29,343,8,29,10,29,12,29,346,9,29,1,30,1,
        30,3,30,350,8,30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,33,1,
        33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,
        35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,
        38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,
        40,3,40,401,8,40,1,40,1,40,1,40,1,40,3,40,407,8,40,3,40,409,8,40,
        1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,
        1,44,1,44,1,44,1,44,5,44,428,8,44,10,44,12,44,431,9,44,1,45,1,45,
        1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,3,46,445,8,46,
        1,46,1,46,1,46,1,46,1,46,3,46,452,8,46,1,46,1,46,1,46,1,46,3,46,
        458,8,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,
        1,46,1,46,1,46,1,46,5,46,475,8,46,10,46,12,46,478,9,46,1,47,1,47,
        1,48,1,48,1,49,1,49,1,50,1,50,1,51,1,51,1,52,1,52,1,52,1,53,1,53,
        1,54,1,54,1,54,1,54,1,54,3,54,500,8,54,1,54,0,1,92,55,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,
        54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,
        98,100,102,104,106,108,0,4,1,0,47,56,1,0,67,82,1,0,57,66,1,0,87,
        88,513,0,110,1,0,0,0,2,119,1,0,0,0,4,122,1,0,0,0,6,128,1,0,0,0,8,
        137,1,0,0,0,10,140,1,0,0,0,12,151,1,0,0,0,14,164,1,0,0,0,16,174,
        1,0,0,0,18,182,1,0,0,0,20,185,1,0,0,0,22,211,1,0,0,0,24,213,1,0,
        0,0,26,221,1,0,0,0,28,229,1,0,0,0,30,233,1,0,0,0,32,241,1,0,0,0,
        34,258,1,0,0,0,36,260,1,0,0,0,38,263,1,0,0,0,40,266,1,0,0,0,42,270,
        1,0,0,0,44,299,1,0,0,0,46,301,1,0,0,0,48,303,1,0,0,0,50,313,1,0,
        0,0,52,319,1,0,0,0,54,321,1,0,0,0,56,334,1,0,0,0,58,338,1,0,0,0,
        60,349,1,0,0,0,62,351,1,0,0,0,64,355,1,0,0,0,66,359,1,0,0,0,68,366,
        1,0,0,0,70,368,1,0,0,0,72,378,1,0,0,0,74,381,1,0,0,0,76,386,1,0,
        0,0,78,389,1,0,0,0,80,408,1,0,0,0,82,410,1,0,0,0,84,413,1,0,0,0,
        86,418,1,0,0,0,88,423,1,0,0,0,90,432,1,0,0,0,92,457,1,0,0,0,94,479,
        1,0,0,0,96,481,1,0,0,0,98,483,1,0,0,0,100,485,1,0,0,0,102,487,1,
        0,0,0,104,489,1,0,0,0,106,492,1,0,0,0,108,499,1,0,0,0,110,111,3,
        2,1,0,111,112,3,18,9,0,112,113,3,8,4,0,113,114,3,30,15,0,114,1,1,
        0,0,0,115,118,3,4,2,0,116,118,3,6,3,0,117,115,1,0,0,0,117,116,1,
        0,0,0,118,121,1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,3,1,0,
        0,0,121,119,1,0,0,0,122,123,5,37,0,0,123,124,5,89,0,0,124,125,3,
        18,9,0,125,126,5,11,0,0,126,127,5,37,0,0,127,5,1,0,0,0,128,129,5,
        28,0,0,129,130,5,89,0,0,130,131,5,29,0,0,131,132,3,22,11,0,132,7,
        1,0,0,0,133,136,3,10,5,0,134,136,3,12,6,0,135,133,1,0,0,0,135,134,
        1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,9,1,
        0,0,0,139,137,1,0,0,0,140,141,5,24,0,0,141,146,5,89,0,0,142,143,
        5,1,0,0,143,144,3,14,7,0,144,145,5,2,0,0,145,147,1,0,0,0,146,142,
        1,0,0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,149,3,18,9,0,149,150,
        3,28,14,0,150,11,1,0,0,0,151,152,5,26,0,0,152,157,5,89,0,0,153,154,
        5,1,0,0,154,155,3,14,7,0,155,156,5,2,0,0,156,158,1,0,0,0,157,153,
        1,0,0,0,157,158,1,0,0,0,158,159,1,0,0,0,159,160,5,3,0,0,160,161,
        3,22,11,0,161,162,3,18,9,0,162,163,3,28,14,0,163,13,1,0,0,0,164,
        170,3,16,8,0,165,166,3,90,45,0,166,167,3,16,8,0,167,169,1,0,0,0,
        168,165,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,
        171,15,1,0,0,0,172,170,1,0,0,0,173,175,5,25,0,0,174,173,1,0,0,0,
        174,175,1,0,0,0,175,176,1,0,0,0,176,177,3,22,11,0,177,178,5,89,0,
        0,178,17,1,0,0,0,179,181,3,20,10,0,180,179,1,0,0,0,181,184,1,0,0,
        0,182,180,1,0,0,0,182,183,1,0,0,0,183,19,1,0,0,0,184,182,1,0,0,0,
        185,186,3,22,11,0,186,187,3,24,12,0,187,21,1,0,0,0,188,212,5,32,
        0,0,189,212,5,33,0,0,190,212,5,35,0,0,191,212,5,34,0,0,192,196,5,
        36,0,0,193,194,5,4,0,0,194,195,5,84,0,0,195,197,5,5,0,0,196,193,
        1,0,0,0,196,197,1,0,0,0,197,212,1,0,0,0,198,199,5,38,0,0,199,200,
        5,4,0,0,200,201,3,26,13,0,201,202,5,5,0,0,202,203,5,39,0,0,203,204,
        3,22,11,0,204,212,1,0,0,0,205,206,5,30,0,0,206,212,5,31,0,0,207,
        208,5,30,0,0,208,209,5,39,0,0,209,212,3,22,11,0,210,212,5,89,0,0,
        211,188,1,0,0,0,211,189,1,0,0,0,211,190,1,0,0,0,211,191,1,0,0,0,
        211,192,1,0,0,0,211,198,1,0,0,0,211,205,1,0,0,0,211,207,1,0,0,0,
        211,210,1,0,0,0,212,23,1,0,0,0,213,218,5,89,0,0,214,215,5,6,0,0,
        215,217,5,89,0,0,216,214,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,
        218,219,1,0,0,0,219,25,1,0,0,0,220,218,1,0,0,0,221,226,5,84,0,0,
        222,223,5,6,0,0,223,225,5,84,0,0,224,222,1,0,0,0,225,228,1,0,0,0,
        226,224,1,0,0,0,226,227,1,0,0,0,227,27,1,0,0,0,228,226,1,0,0,0,229,
        230,5,10,0,0,230,231,3,32,16,0,231,232,5,11,0,0,232,29,1,0,0,0,233,
        234,5,10,0,0,234,235,3,32,16,0,235,236,5,11,0,0,236,237,5,0,0,1,
        237,31,1,0,0,0,238,240,3,34,17,0,239,238,1,0,0,0,240,243,1,0,0,0,
        241,239,1,0,0,0,241,242,1,0,0,0,242,33,1,0,0,0,243,241,1,0,0,0,244,
        259,3,36,18,0,245,259,3,38,19,0,246,259,3,40,20,0,247,259,3,44,22,
        0,248,259,3,48,24,0,249,259,3,54,27,0,250,259,3,66,33,0,251,259,
        3,70,35,0,252,259,3,74,37,0,253,259,3,76,38,0,254,259,3,78,39,0,
        255,259,3,82,41,0,256,259,3,84,42,0,257,259,3,86,43,0,258,244,1,
        0,0,0,258,245,1,0,0,0,258,246,1,0,0,0,258,247,1,0,0,0,258,248,1,
        0,0,0,258,249,1,0,0,0,258,250,1,0,0,0,258,251,1,0,0,0,258,252,1,
        0,0,0,258,253,1,0,0,0,258,254,1,0,0,0,258,255,1,0,0,0,258,256,1,
        0,0,0,258,257,1,0,0,0,259,35,1,0,0,0,260,261,5,12,0,0,261,262,3,
        88,44,0,262,37,1,0,0,0,263,264,5,13,0,0,264,265,3,88,44,0,265,39,
        1,0,0,0,266,267,3,92,46,0,267,268,3,42,21,0,268,269,3,92,46,0,269,
        41,1,0,0,0,270,271,5,7,0,0,271,43,1,0,0,0,272,273,5,14,0,0,273,279,
        3,46,23,0,274,276,5,1,0,0,275,277,3,88,44,0,276,275,1,0,0,0,276,
        277,1,0,0,0,277,278,1,0,0,0,278,280,5,2,0,0,279,274,1,0,0,0,279,
        280,1,0,0,0,280,300,1,0,0,0,281,282,5,14,0,0,282,288,3,106,53,0,
        283,285,5,1,0,0,284,286,3,88,44,0,285,284,1,0,0,0,285,286,1,0,0,
        0,286,287,1,0,0,0,287,289,5,2,0,0,288,283,1,0,0,0,288,289,1,0,0,
        0,289,300,1,0,0,0,290,291,5,14,0,0,291,297,5,89,0,0,292,294,5,1,
        0,0,293,295,3,88,44,0,294,293,1,0,0,0,294,295,1,0,0,0,295,296,1,
        0,0,0,296,298,5,2,0,0,297,292,1,0,0,0,297,298,1,0,0,0,298,300,1,
        0,0,0,299,272,1,0,0,0,299,281,1,0,0,0,299,290,1,0,0,0,300,45,1,0,
        0,0,301,302,7,0,0,0,302,47,1,0,0,0,303,304,5,15,0,0,304,305,3,92,
        46,0,305,306,3,50,25,0,306,308,3,32,16,0,307,309,3,52,26,0,308,307,
        1,0,0,0,308,309,1,0,0,0,309,310,1,0,0,0,310,311,5,11,0,0,311,312,
        5,15,0,0,312,49,1,0,0,0,313,314,5,16,0,0,314,51,1,0,0,0,315,316,
        5,17,0,0,316,320,3,48,24,0,317,318,5,17,0,0,318,320,3,32,16,0,319,
        315,1,0,0,0,319,317,1,0,0,0,320,53,1,0,0,0,321,322,5,18,0,0,322,
        324,3,92,46,0,323,325,3,56,28,0,324,323,1,0,0,0,325,326,1,0,0,0,
        326,324,1,0,0,0,326,327,1,0,0,0,327,329,1,0,0,0,328,330,3,64,32,
        0,329,328,1,0,0,0,329,330,1,0,0,0,330,331,1,0,0,0,331,332,5,11,0,
        0,332,333,5,18,0,0,333,55,1,0,0,0,334,335,3,58,29,0,335,336,5,3,
        0,0,336,337,3,32,16,0,337,57,1,0,0,0,338,344,3,60,30,0,339,340,3,
        90,45,0,340,341,3,60,30,0,341,343,1,0,0,0,342,339,1,0,0,0,343,346,
        1,0,0,0,344,342,1,0,0,0,344,345,1,0,0,0,345,59,1,0,0,0,346,344,1,
        0,0,0,347,350,3,62,31,0,348,350,3,92,46,0,349,347,1,0,0,0,349,348,
        1,0,0,0,350,61,1,0,0,0,351,352,3,92,46,0,352,353,5,8,0,0,353,354,
        3,92,46,0,354,63,1,0,0,0,355,356,5,17,0,0,356,357,5,3,0,0,357,358,
        3,32,16,0,358,65,1,0,0,0,359,360,5,19,0,0,360,361,3,92,46,0,361,
        362,3,68,34,0,362,363,3,32,16,0,363,364,5,11,0,0,364,365,5,19,0,
        0,365,67,1,0,0,0,366,367,5,20,0,0,367,69,1,0,0,0,368,369,5,21,0,
        0,369,370,3,92,46,0,370,371,5,7,0,0,371,372,3,92,46,0,372,373,3,
        72,36,0,373,374,5,20,0,0,374,375,3,32,16,0,375,376,5,11,0,0,376,
        377,5,21,0,0,377,71,1,0,0,0,378,379,5,22,0,0,379,380,3,92,46,0,380,
        73,1,0,0,0,381,382,5,23,0,0,382,383,3,32,16,0,383,384,5,22,0,0,384,
        385,3,92,46,0,385,75,1,0,0,0,386,387,5,27,0,0,387,388,3,92,46,0,
        388,77,1,0,0,0,389,390,5,40,0,0,390,391,3,92,46,0,391,392,5,41,0,
        0,392,393,3,92,46,0,393,394,5,21,0,0,394,395,3,80,40,0,395,79,1,
        0,0,0,396,400,5,43,0,0,397,398,3,90,45,0,398,399,5,42,0,0,399,401,
        1,0,0,0,400,397,1,0,0,0,400,401,1,0,0,0,401,409,1,0,0,0,402,406,
        5,42,0,0,403,404,3,90,45,0,404,405,5,43,0,0,405,407,1,0,0,0,406,
        403,1,0,0,0,406,407,1,0,0,0,407,409,1,0,0,0,408,396,1,0,0,0,408,
        402,1,0,0,0,409,81,1,0,0,0,410,411,5,44,0,0,411,412,3,92,46,0,412,
        83,1,0,0,0,413,414,5,45,0,0,414,415,3,92,46,0,415,416,3,90,45,0,
        416,417,3,88,44,0,417,85,1,0,0,0,418,419,5,46,0,0,419,420,3,92,46,
        0,420,421,3,90,45,0,421,422,3,88,44,0,422,87,1,0,0,0,423,429,3,92,
        46,0,424,425,3,90,45,0,425,426,3,92,46,0,426,428,1,0,0,0,427,424,
        1,0,0,0,428,431,1,0,0,0,429,427,1,0,0,0,429,430,1,0,0,0,430,89,1,
        0,0,0,431,429,1,0,0,0,432,433,5,6,0,0,433,91,1,0,0,0,434,435,6,46,
        -1,0,435,436,5,1,0,0,436,437,3,92,46,0,437,438,5,2,0,0,438,458,1,
        0,0,0,439,458,3,108,54,0,440,458,5,89,0,0,441,442,3,106,53,0,442,
        444,5,1,0,0,443,445,3,88,44,0,444,443,1,0,0,0,444,445,1,0,0,0,445,
        446,1,0,0,0,446,447,5,2,0,0,447,458,1,0,0,0,448,449,5,89,0,0,449,
        451,3,94,47,0,450,452,3,88,44,0,451,450,1,0,0,0,451,452,1,0,0,0,
        452,453,1,0,0,0,453,454,3,96,48,0,454,458,1,0,0,0,455,456,5,73,0,
        0,456,458,3,92,46,3,457,434,1,0,0,0,457,439,1,0,0,0,457,440,1,0,
        0,0,457,441,1,0,0,0,457,448,1,0,0,0,457,455,1,0,0,0,458,476,1,0,
        0,0,459,460,10,2,0,0,460,461,3,102,51,0,461,462,3,92,46,2,462,475,
        1,0,0,0,463,464,10,1,0,0,464,465,3,102,51,0,465,466,3,92,46,2,466,
        475,1,0,0,0,467,468,10,7,0,0,468,475,3,104,52,0,469,470,10,6,0,0,
        470,471,3,98,49,0,471,472,3,88,44,0,472,473,3,100,50,0,473,475,1,
        0,0,0,474,459,1,0,0,0,474,463,1,0,0,0,474,467,1,0,0,0,474,469,1,
        0,0,0,475,478,1,0,0,0,476,474,1,0,0,0,476,477,1,0,0,0,477,93,1,0,
        0,0,478,476,1,0,0,0,479,480,5,1,0,0,480,95,1,0,0,0,481,482,5,2,0,
        0,482,97,1,0,0,0,483,484,5,4,0,0,484,99,1,0,0,0,485,486,5,5,0,0,
        486,101,1,0,0,0,487,488,7,1,0,0,488,103,1,0,0,0,489,490,5,9,0,0,
        490,491,5,89,0,0,491,105,1,0,0,0,492,493,7,2,0,0,493,107,1,0,0,0,
        494,500,5,83,0,0,495,500,5,84,0,0,496,500,5,85,0,0,497,500,5,86,
        0,0,498,500,7,3,0,0,499,494,1,0,0,0,499,495,1,0,0,0,499,496,1,0,
        0,0,499,497,1,0,0,0,499,498,1,0,0,0,500,109,1,0,0,0,38,117,119,135,
        137,146,157,170,174,182,196,211,218,226,241,258,276,279,285,288,
        294,297,299,308,319,326,329,344,349,400,406,408,429,444,451,457,
        474,476,499
    ]

class LPPParser ( Parser ):

    grammarFileName = "LPP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':'", "'['", "']'", "','", 
                     "'<-'", "'->'", "'.'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'^'", "'*'", "'/'", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'='", "'<>'", "'>'", "'>='", 
                     "'<'", "'<='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INICIO", "FIN", "ESCRIBA", 
                      "LEA", "LLAMAR", "SI", "ENTONCES", "SINO", "CASO", 
                      "MIENTRAS", "HAGA", "PARA", "HASTA", "REPITA", "PROCEDIMIENTO", 
                      "VAR", "FUNCION", "RETORNE", "TIPO", "ES", "ARCHIVO", 
                      "SECUENCIAL", "ENTERO", "REAL", "CARACTER", "BOOLEANO", 
                      "CADENA", "REGISTRO", "ARREGLO", "DE", "ABRIR", "COMO", 
                      "ESCRITURA", "LECTURA", "CERRAR", "ESCRIBIR", "LEER", 
                      "PROC_NUEVA_LINEA", "PROC_LIMPIAR_PANTALLA", "PROC_POSICIONAR_CURSOR", 
                      "PROC_IR_A_INICIO", "PROC_IR_A_FIN", "PROC_IR_A", 
                      "PROC_INICIALIZAR_ALEATORIO", "PROC_PAUSA", "PROC_COLOR_TEXTO", 
                      "PROC_COLOR_FONDO", "FUNC_FDA", "FUNC_POSICION_ACTUAL", 
                      "FUNC_ALEATORIO", "FUNC_OBTENER_CARACTER", "FUNC_ENTERO_A_CADENA", 
                      "FUNC_REAL_A_CADENA", "FUNC_TECLA_PRESIONADA", "FUNC_VALOR_ASCII", 
                      "FUNC_CARACTER_ASCII", "FUNC_LONGITUD", "PODER", "MULT", 
                      "DIV", "MOD", "DIV_ENTEROS", "SUMA", "RESTA", "IGUAL", 
                      "DESIGUAL", "MAYOR", "MAYOR_IGUAL", "MENOR", "MENOR_IGUAL", 
                      "OP_Y", "OP_O", "NO", "LITERAL_REAL", "LITERAL_ENTERO", 
                      "LITERAL_CADENA", "LITERAL_CARACTER", "VERDADERO", 
                      "FALSO", "ID", "NL", "WS", "COMENTARIO", "COMENTARIO_LINEA" ]

    RULE_programa = 0
    RULE_declaracionesTipos = 1
    RULE_declaracionRegistro = 2
    RULE_declaracionTipo = 3
    RULE_declaracionesSubprogramas = 4
    RULE_declaracionProcedimiento = 5
    RULE_declaracionFuncion = 6
    RULE_parametros = 7
    RULE_parametro = 8
    RULE_declaracionesVariables = 9
    RULE_declaracionVariables = 10
    RULE_tipo = 11
    RULE_listaIDs = 12
    RULE_listaEnteros = 13
    RULE_sentenciasSubprograma = 14
    RULE_sentenciasPrograma = 15
    RULE_sentencias = 16
    RULE_sentencia = 17
    RULE_escriba = 18
    RULE_lea = 19
    RULE_asignar = 20
    RULE_symbolAssing = 21
    RULE_llamar = 22
    RULE_procedimientoLibreriaEstandar = 23
    RULE_si = 24
    RULE_entonces = 25
    RULE_sino = 26
    RULE_caso = 27
    RULE_opcionCaso = 28
    RULE_listaExprOpcion = 29
    RULE_exprOpcion = 30
    RULE_rangoExpr = 31
    RULE_casoSino = 32
    RULE_mientras = 33
    RULE_haga = 34
    RULE_para = 35
    RULE_hasta = 36
    RULE_repita = 37
    RULE_retorne = 38
    RULE_abrir = 39
    RULE_acceso = 40
    RULE_cerrar = 41
    RULE_escribir = 42
    RULE_leer = 43
    RULE_listaExpr = 44
    RULE_coma = 45
    RULE_expr = 46
    RULE_openPar = 47
    RULE_closePar = 48
    RULE_openBra = 49
    RULE_closeBra = 50
    RULE_exponente = 51
    RULE_punto = 52
    RULE_funcionLibreriaEstandar = 53
    RULE_literal = 54

    ruleNames =  [ "programa", "declaracionesTipos", "declaracionRegistro", 
                   "declaracionTipo", "declaracionesSubprogramas", "declaracionProcedimiento", 
                   "declaracionFuncion", "parametros", "parametro", "declaracionesVariables", 
                   "declaracionVariables", "tipo", "listaIDs", "listaEnteros", 
                   "sentenciasSubprograma", "sentenciasPrograma", "sentencias", 
                   "sentencia", "escriba", "lea", "asignar", "symbolAssing", 
                   "llamar", "procedimientoLibreriaEstandar", "si", "entonces", 
                   "sino", "caso", "opcionCaso", "listaExprOpcion", "exprOpcion", 
                   "rangoExpr", "casoSino", "mientras", "haga", "para", 
                   "hasta", "repita", "retorne", "abrir", "acceso", "cerrar", 
                   "escribir", "leer", "listaExpr", "coma", "expr", "openPar", 
                   "closePar", "openBra", "closeBra", "exponente", "punto", 
                   "funcionLibreriaEstandar", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    INICIO=10
    FIN=11
    ESCRIBA=12
    LEA=13
    LLAMAR=14
    SI=15
    ENTONCES=16
    SINO=17
    CASO=18
    MIENTRAS=19
    HAGA=20
    PARA=21
    HASTA=22
    REPITA=23
    PROCEDIMIENTO=24
    VAR=25
    FUNCION=26
    RETORNE=27
    TIPO=28
    ES=29
    ARCHIVO=30
    SECUENCIAL=31
    ENTERO=32
    REAL=33
    CARACTER=34
    BOOLEANO=35
    CADENA=36
    REGISTRO=37
    ARREGLO=38
    DE=39
    ABRIR=40
    COMO=41
    ESCRITURA=42
    LECTURA=43
    CERRAR=44
    ESCRIBIR=45
    LEER=46
    PROC_NUEVA_LINEA=47
    PROC_LIMPIAR_PANTALLA=48
    PROC_POSICIONAR_CURSOR=49
    PROC_IR_A_INICIO=50
    PROC_IR_A_FIN=51
    PROC_IR_A=52
    PROC_INICIALIZAR_ALEATORIO=53
    PROC_PAUSA=54
    PROC_COLOR_TEXTO=55
    PROC_COLOR_FONDO=56
    FUNC_FDA=57
    FUNC_POSICION_ACTUAL=58
    FUNC_ALEATORIO=59
    FUNC_OBTENER_CARACTER=60
    FUNC_ENTERO_A_CADENA=61
    FUNC_REAL_A_CADENA=62
    FUNC_TECLA_PRESIONADA=63
    FUNC_VALOR_ASCII=64
    FUNC_CARACTER_ASCII=65
    FUNC_LONGITUD=66
    PODER=67
    MULT=68
    DIV=69
    MOD=70
    DIV_ENTEROS=71
    SUMA=72
    RESTA=73
    IGUAL=74
    DESIGUAL=75
    MAYOR=76
    MAYOR_IGUAL=77
    MENOR=78
    MENOR_IGUAL=79
    OP_Y=80
    OP_O=81
    NO=82
    LITERAL_REAL=83
    LITERAL_ENTERO=84
    LITERAL_CADENA=85
    LITERAL_CARACTER=86
    VERDADERO=87
    FALSO=88
    ID=89
    NL=90
    WS=91
    COMENTARIO=92
    COMENTARIO_LINEA=93

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionesTipos(self):
            return self.getTypedRuleContext(LPPParser.DeclaracionesTiposContext,0)


        def declaracionesVariables(self):
            return self.getTypedRuleContext(LPPParser.DeclaracionesVariablesContext,0)


        def declaracionesSubprogramas(self):
            return self.getTypedRuleContext(LPPParser.DeclaracionesSubprogramasContext,0)


        def sentenciasPrograma(self):
            return self.getTypedRuleContext(LPPParser.SentenciasProgramaContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = LPPParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.declaracionesTipos()
            self.state = 111
            self.declaracionesVariables()
            self.state = 112
            self.declaracionesSubprogramas()
            self.state = 113
            self.sentenciasPrograma()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionesTiposContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionRegistro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPPParser.DeclaracionRegistroContext)
            else:
                return self.getTypedRuleContext(LPPParser.DeclaracionRegistroContext,i)


        def declaracionTipo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPPParser.DeclaracionTipoContext)
            else:
                return self.getTypedRuleContext(LPPParser.DeclaracionTipoContext,i)


        def getRuleIndex(self):
            return LPPParser.RULE_declaracionesTipos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionesTipos" ):
                listener.enterDeclaracionesTipos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionesTipos" ):
                listener.exitDeclaracionesTipos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionesTipos" ):
                return visitor.visitDeclaracionesTipos(self)
            else:
                return visitor.visitChildren(self)




    def declaracionesTipos(self):

        localctx = LPPParser.DeclaracionesTiposContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracionesTipos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28 or _la==37:
                self.state = 117
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [37]:
                    self.state = 115
                    self.declaracionRegistro()
                    pass
                elif token in [28]:
                    self.state = 116
                    self.declaracionTipo()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionRegistroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REGISTRO(self, i:int=None):
            if i is None:
                return self.getTokens(LPPParser.REGISTRO)
            else:
                return self.getToken(LPPParser.REGISTRO, i)

        def ID(self):
            return self.getToken(LPPParser.ID, 0)

        def declaracionesVariables(self):
            return self.getTypedRuleContext(LPPParser.DeclaracionesVariablesContext,0)


        def FIN(self):
            return self.getToken(LPPParser.FIN, 0)

        def getRuleIndex(self):
            return LPPParser.RULE_declaracionRegistro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionRegistro" ):
                listener.enterDeclaracionRegistro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionRegistro" ):
                listener.exitDeclaracionRegistro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionRegistro" ):
                return visitor.visitDeclaracionRegistro(self)
            else:
                return visitor.visitChildren(self)




    def declaracionRegistro(self):

        localctx = LPPParser.DeclaracionRegistroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracionRegistro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(LPPParser.REGISTRO)
            self.state = 123
            self.match(LPPParser.ID)
            self.state = 124
            self.declaracionesVariables()
            self.state = 125
            self.match(LPPParser.FIN)
            self.state = 126
            self.match(LPPParser.REGISTRO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionTipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO(self):
            return self.getToken(LPPParser.TIPO, 0)

        def ID(self):
            return self.getToken(LPPParser.ID, 0)

        def ES(self):
            return self.getToken(LPPParser.ES, 0)

        def tipo(self):
            return self.getTypedRuleContext(LPPParser.TipoContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_declaracionTipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionTipo" ):
                listener.enterDeclaracionTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionTipo" ):
                listener.exitDeclaracionTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionTipo" ):
                return visitor.visitDeclaracionTipo(self)
            else:
                return visitor.visitChildren(self)




    def declaracionTipo(self):

        localctx = LPPParser.DeclaracionTipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracionTipo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(LPPParser.TIPO)
            self.state = 129
            self.match(LPPParser.ID)
            self.state = 130
            self.match(LPPParser.ES)
            self.state = 131
            self.tipo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionesSubprogramasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionProcedimiento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPPParser.DeclaracionProcedimientoContext)
            else:
                return self.getTypedRuleContext(LPPParser.DeclaracionProcedimientoContext,i)


        def declaracionFuncion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPPParser.DeclaracionFuncionContext)
            else:
                return self.getTypedRuleContext(LPPParser.DeclaracionFuncionContext,i)


        def getRuleIndex(self):
            return LPPParser.RULE_declaracionesSubprogramas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionesSubprogramas" ):
                listener.enterDeclaracionesSubprogramas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionesSubprogramas" ):
                listener.exitDeclaracionesSubprogramas(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionesSubprogramas" ):
                return visitor.visitDeclaracionesSubprogramas(self)
            else:
                return visitor.visitChildren(self)




    def declaracionesSubprogramas(self):

        localctx = LPPParser.DeclaracionesSubprogramasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaracionesSubprogramas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24 or _la==26:
                self.state = 135
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [24]:
                    self.state = 133
                    self.declaracionProcedimiento()
                    pass
                elif token in [26]:
                    self.state = 134
                    self.declaracionFuncion()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionProcedimientoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCEDIMIENTO(self):
            return self.getToken(LPPParser.PROCEDIMIENTO, 0)

        def ID(self):
            return self.getToken(LPPParser.ID, 0)

        def declaracionesVariables(self):
            return self.getTypedRuleContext(LPPParser.DeclaracionesVariablesContext,0)


        def sentenciasSubprograma(self):
            return self.getTypedRuleContext(LPPParser.SentenciasSubprogramaContext,0)


        def parametros(self):
            return self.getTypedRuleContext(LPPParser.ParametrosContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_declaracionProcedimiento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionProcedimiento" ):
                listener.enterDeclaracionProcedimiento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionProcedimiento" ):
                listener.exitDeclaracionProcedimiento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionProcedimiento" ):
                return visitor.visitDeclaracionProcedimiento(self)
            else:
                return visitor.visitChildren(self)




    def declaracionProcedimiento(self):

        localctx = LPPParser.DeclaracionProcedimientoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaracionProcedimiento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(LPPParser.PROCEDIMIENTO)
            self.state = 141
            self.match(LPPParser.ID)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 142
                self.match(LPPParser.T__0)
                self.state = 143
                self.parametros()
                self.state = 144
                self.match(LPPParser.T__1)


            self.state = 148
            self.declaracionesVariables()
            self.state = 149
            self.sentenciasSubprograma()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionFuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCION(self):
            return self.getToken(LPPParser.FUNCION, 0)

        def ID(self):
            return self.getToken(LPPParser.ID, 0)

        def tipo(self):
            return self.getTypedRuleContext(LPPParser.TipoContext,0)


        def declaracionesVariables(self):
            return self.getTypedRuleContext(LPPParser.DeclaracionesVariablesContext,0)


        def sentenciasSubprograma(self):
            return self.getTypedRuleContext(LPPParser.SentenciasSubprogramaContext,0)


        def parametros(self):
            return self.getTypedRuleContext(LPPParser.ParametrosContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_declaracionFuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionFuncion" ):
                listener.enterDeclaracionFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionFuncion" ):
                listener.exitDeclaracionFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionFuncion" ):
                return visitor.visitDeclaracionFuncion(self)
            else:
                return visitor.visitChildren(self)




    def declaracionFuncion(self):

        localctx = LPPParser.DeclaracionFuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_declaracionFuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(LPPParser.FUNCION)
            self.state = 152
            self.match(LPPParser.ID)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 153
                self.match(LPPParser.T__0)
                self.state = 154
                self.parametros()
                self.state = 155
                self.match(LPPParser.T__1)


            self.state = 159
            self.match(LPPParser.T__2)
            self.state = 160
            self.tipo()
            self.state = 161
            self.declaracionesVariables()
            self.state = 162
            self.sentenciasSubprograma()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPPParser.ParametroContext)
            else:
                return self.getTypedRuleContext(LPPParser.ParametroContext,i)


        def coma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPPParser.ComaContext)
            else:
                return self.getTypedRuleContext(LPPParser.ComaContext,i)


        def getRuleIndex(self):
            return LPPParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = LPPParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.parametro()
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 165
                self.coma()
                self.state = 166
                self.parametro()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(LPPParser.TipoContext,0)


        def ID(self):
            return self.getToken(LPPParser.ID, 0)

        def VAR(self):
            return self.getToken(LPPParser.VAR, 0)

        def getRuleIndex(self):
            return LPPParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametro" ):
                return visitor.visitParametro(self)
            else:
                return visitor.visitChildren(self)




    def parametro(self):

        localctx = LPPParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parametro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 173
                self.match(LPPParser.VAR)


            self.state = 176
            self.tipo()
            self.state = 177
            self.match(LPPParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionesVariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionVariables(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPPParser.DeclaracionVariablesContext)
            else:
                return self.getTypedRuleContext(LPPParser.DeclaracionVariablesContext,i)


        def getRuleIndex(self):
            return LPPParser.RULE_declaracionesVariables

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionesVariables" ):
                listener.enterDeclaracionesVariables(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionesVariables" ):
                listener.exitDeclaracionesVariables(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionesVariables" ):
                return visitor.visitDeclaracionesVariables(self)
            else:
                return visitor.visitChildren(self)




    def declaracionesVariables(self):

        localctx = LPPParser.DeclaracionesVariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_declaracionesVariables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & 576460752303423869) != 0):
                self.state = 179
                self.declaracionVariables()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionVariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(LPPParser.TipoContext,0)


        def listaIDs(self):
            return self.getTypedRuleContext(LPPParser.ListaIDsContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_declaracionVariables

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionVariables" ):
                listener.enterDeclaracionVariables(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionVariables" ):
                listener.exitDeclaracionVariables(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionVariables" ):
                return visitor.visitDeclaracionVariables(self)
            else:
                return visitor.visitChildren(self)




    def declaracionVariables(self):

        localctx = LPPParser.DeclaracionVariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_declaracionVariables)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.tipo()
            self.state = 186
            self.listaIDs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTERO(self):
            return self.getToken(LPPParser.ENTERO, 0)

        def REAL(self):
            return self.getToken(LPPParser.REAL, 0)

        def BOOLEANO(self):
            return self.getToken(LPPParser.BOOLEANO, 0)

        def CARACTER(self):
            return self.getToken(LPPParser.CARACTER, 0)

        def CADENA(self):
            return self.getToken(LPPParser.CADENA, 0)

        def LITERAL_ENTERO(self):
            return self.getToken(LPPParser.LITERAL_ENTERO, 0)

        def ARREGLO(self):
            return self.getToken(LPPParser.ARREGLO, 0)

        def listaEnteros(self):
            return self.getTypedRuleContext(LPPParser.ListaEnterosContext,0)


        def DE(self):
            return self.getToken(LPPParser.DE, 0)

        def tipo(self):
            return self.getTypedRuleContext(LPPParser.TipoContext,0)


        def ARCHIVO(self):
            return self.getToken(LPPParser.ARCHIVO, 0)

        def SECUENCIAL(self):
            return self.getToken(LPPParser.SECUENCIAL, 0)

        def ID(self):
            return self.getToken(LPPParser.ID, 0)

        def getRuleIndex(self):
            return LPPParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = LPPParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(LPPParser.ENTERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.match(LPPParser.REAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.match(LPPParser.BOOLEANO)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 191
                self.match(LPPParser.CARACTER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 192
                self.match(LPPParser.CADENA)
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 193
                    self.match(LPPParser.T__3)
                    self.state = 194
                    self.match(LPPParser.LITERAL_ENTERO)
                    self.state = 195
                    self.match(LPPParser.T__4)


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 198
                self.match(LPPParser.ARREGLO)
                self.state = 199
                self.match(LPPParser.T__3)
                self.state = 200
                self.listaEnteros()
                self.state = 201
                self.match(LPPParser.T__4)
                self.state = 202
                self.match(LPPParser.DE)
                self.state = 203
                self.tipo()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 205
                self.match(LPPParser.ARCHIVO)
                self.state = 206
                self.match(LPPParser.SECUENCIAL)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 207
                self.match(LPPParser.ARCHIVO)
                self.state = 208
                self.match(LPPParser.DE)
                self.state = 209
                self.tipo()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 210
                self.match(LPPParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaIDsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LPPParser.ID)
            else:
                return self.getToken(LPPParser.ID, i)

        def getRuleIndex(self):
            return LPPParser.RULE_listaIDs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaIDs" ):
                listener.enterListaIDs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaIDs" ):
                listener.exitListaIDs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaIDs" ):
                return visitor.visitListaIDs(self)
            else:
                return visitor.visitChildren(self)




    def listaIDs(self):

        localctx = LPPParser.ListaIDsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_listaIDs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(LPPParser.ID)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 214
                self.match(LPPParser.T__5)
                self.state = 215
                self.match(LPPParser.ID)
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaEnterosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITERAL_ENTERO(self, i:int=None):
            if i is None:
                return self.getTokens(LPPParser.LITERAL_ENTERO)
            else:
                return self.getToken(LPPParser.LITERAL_ENTERO, i)

        def getRuleIndex(self):
            return LPPParser.RULE_listaEnteros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaEnteros" ):
                listener.enterListaEnteros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaEnteros" ):
                listener.exitListaEnteros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaEnteros" ):
                return visitor.visitListaEnteros(self)
            else:
                return visitor.visitChildren(self)




    def listaEnteros(self):

        localctx = LPPParser.ListaEnterosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_listaEnteros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(LPPParser.LITERAL_ENTERO)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 222
                self.match(LPPParser.T__5)
                self.state = 223
                self.match(LPPParser.LITERAL_ENTERO)
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciasSubprogramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INICIO(self):
            return self.getToken(LPPParser.INICIO, 0)

        def sentencias(self):
            return self.getTypedRuleContext(LPPParser.SentenciasContext,0)


        def FIN(self):
            return self.getToken(LPPParser.FIN, 0)

        def getRuleIndex(self):
            return LPPParser.RULE_sentenciasSubprograma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciasSubprograma" ):
                listener.enterSentenciasSubprograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciasSubprograma" ):
                listener.exitSentenciasSubprograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciasSubprograma" ):
                return visitor.visitSentenciasSubprograma(self)
            else:
                return visitor.visitChildren(self)




    def sentenciasSubprograma(self):

        localctx = LPPParser.SentenciasSubprogramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_sentenciasSubprograma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(LPPParser.INICIO)
            self.state = 230
            self.sentencias()
            self.state = 231
            self.match(LPPParser.FIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciasProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INICIO(self):
            return self.getToken(LPPParser.INICIO, 0)

        def sentencias(self):
            return self.getTypedRuleContext(LPPParser.SentenciasContext,0)


        def FIN(self):
            return self.getToken(LPPParser.FIN, 0)

        def EOF(self):
            return self.getToken(LPPParser.EOF, 0)

        def getRuleIndex(self):
            return LPPParser.RULE_sentenciasPrograma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciasPrograma" ):
                listener.enterSentenciasPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciasPrograma" ):
                listener.exitSentenciasPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciasPrograma" ):
                return visitor.visitSentenciasPrograma(self)
            else:
                return visitor.visitChildren(self)




    def sentenciasPrograma(self):

        localctx = LPPParser.SentenciasProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_sentenciasPrograma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(LPPParser.INICIO)
            self.state = 234
            self.sentencias()
            self.state = 235
            self.match(LPPParser.FIN)
            self.state = 236
            self.match(LPPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPPParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(LPPParser.SentenciaContext,i)


        def getRuleIndex(self):
            return LPPParser.RULE_sentencias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencias" ):
                listener.enterSentencias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencias" ):
                listener.exitSentencias(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencias" ):
                return visitor.visitSentencias(self)
            else:
                return visitor.visitChildren(self)




    def sentencias(self):

        localctx = LPPParser.SentenciasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_sentencias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 238
                    self.sentencia() 
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def escriba(self):
            return self.getTypedRuleContext(LPPParser.EscribaContext,0)


        def lea(self):
            return self.getTypedRuleContext(LPPParser.LeaContext,0)


        def asignar(self):
            return self.getTypedRuleContext(LPPParser.AsignarContext,0)


        def llamar(self):
            return self.getTypedRuleContext(LPPParser.LlamarContext,0)


        def si(self):
            return self.getTypedRuleContext(LPPParser.SiContext,0)


        def caso(self):
            return self.getTypedRuleContext(LPPParser.CasoContext,0)


        def mientras(self):
            return self.getTypedRuleContext(LPPParser.MientrasContext,0)


        def para(self):
            return self.getTypedRuleContext(LPPParser.ParaContext,0)


        def repita(self):
            return self.getTypedRuleContext(LPPParser.RepitaContext,0)


        def retorne(self):
            return self.getTypedRuleContext(LPPParser.RetorneContext,0)


        def abrir(self):
            return self.getTypedRuleContext(LPPParser.AbrirContext,0)


        def cerrar(self):
            return self.getTypedRuleContext(LPPParser.CerrarContext,0)


        def escribir(self):
            return self.getTypedRuleContext(LPPParser.EscribirContext,0)


        def leer(self):
            return self.getTypedRuleContext(LPPParser.LeerContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = LPPParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_sentencia)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.escriba()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.lea()
                pass
            elif token in [1, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 73, 83, 84, 85, 86, 87, 88, 89]:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
                self.asignar()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 247
                self.llamar()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 248
                self.si()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 6)
                self.state = 249
                self.caso()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 7)
                self.state = 250
                self.mientras()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 8)
                self.state = 251
                self.para()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 9)
                self.state = 252
                self.repita()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 10)
                self.state = 253
                self.retorne()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 11)
                self.state = 254
                self.abrir()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 12)
                self.state = 255
                self.cerrar()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 13)
                self.state = 256
                self.escribir()
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 14)
                self.state = 257
                self.leer()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscribaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCRIBA(self):
            return self.getToken(LPPParser.ESCRIBA, 0)

        def listaExpr(self):
            return self.getTypedRuleContext(LPPParser.ListaExprContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_escriba

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscriba" ):
                listener.enterEscriba(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscriba" ):
                listener.exitEscriba(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscriba" ):
                return visitor.visitEscriba(self)
            else:
                return visitor.visitChildren(self)




    def escriba(self):

        localctx = LPPParser.EscribaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_escriba)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(LPPParser.ESCRIBA)
            self.state = 261
            self.listaExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEA(self):
            return self.getToken(LPPParser.LEA, 0)

        def listaExpr(self):
            return self.getTypedRuleContext(LPPParser.ListaExprContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_lea

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLea" ):
                listener.enterLea(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLea" ):
                listener.exitLea(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLea" ):
                return visitor.visitLea(self)
            else:
                return visitor.visitChildren(self)




    def lea(self):

        localctx = LPPParser.LeaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_lea)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(LPPParser.LEA)
            self.state = 264
            self.listaExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPPParser.ExprContext)
            else:
                return self.getTypedRuleContext(LPPParser.ExprContext,i)


        def symbolAssing(self):
            return self.getTypedRuleContext(LPPParser.SymbolAssingContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_asignar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignar" ):
                listener.enterAsignar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignar" ):
                listener.exitAsignar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignar" ):
                return visitor.visitAsignar(self)
            else:
                return visitor.visitChildren(self)




    def asignar(self):

        localctx = LPPParser.AsignarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_asignar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.expr(0)
            self.state = 267
            self.symbolAssing()
            self.state = 268
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymbolAssingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LPPParser.RULE_symbolAssing

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbolAssing" ):
                listener.enterSymbolAssing(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbolAssing" ):
                listener.exitSymbolAssing(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSymbolAssing" ):
                return visitor.visitSymbolAssing(self)
            else:
                return visitor.visitChildren(self)




    def symbolAssing(self):

        localctx = LPPParser.SymbolAssingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_symbolAssing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(LPPParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAMAR(self):
            return self.getToken(LPPParser.LLAMAR, 0)

        def procedimientoLibreriaEstandar(self):
            return self.getTypedRuleContext(LPPParser.ProcedimientoLibreriaEstandarContext,0)


        def listaExpr(self):
            return self.getTypedRuleContext(LPPParser.ListaExprContext,0)


        def funcionLibreriaEstandar(self):
            return self.getTypedRuleContext(LPPParser.FuncionLibreriaEstandarContext,0)


        def ID(self):
            return self.getToken(LPPParser.ID, 0)

        def getRuleIndex(self):
            return LPPParser.RULE_llamar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamar" ):
                listener.enterLlamar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamar" ):
                listener.exitLlamar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamar" ):
                return visitor.visitLlamar(self)
            else:
                return visitor.visitChildren(self)




    def llamar(self):

        localctx = LPPParser.LlamarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_llamar)
        self._la = 0 # Token type
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.match(LPPParser.LLAMAR)
                self.state = 273
                self.procedimientoLibreriaEstandar()
                self.state = 279
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 274
                    self.match(LPPParser.T__0)
                    self.state = 276
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & -144115188075855870) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 66585095) != 0):
                        self.state = 275
                        self.listaExpr()


                    self.state = 278
                    self.match(LPPParser.T__1)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.match(LPPParser.LLAMAR)
                self.state = 282
                self.funcionLibreriaEstandar()
                self.state = 288
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 283
                    self.match(LPPParser.T__0)
                    self.state = 285
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & -144115188075855870) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 66585095) != 0):
                        self.state = 284
                        self.listaExpr()


                    self.state = 287
                    self.match(LPPParser.T__1)


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 290
                self.match(LPPParser.LLAMAR)
                self.state = 291
                self.match(LPPParser.ID)
                self.state = 297
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 292
                    self.match(LPPParser.T__0)
                    self.state = 294
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & -144115188075855870) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 66585095) != 0):
                        self.state = 293
                        self.listaExpr()


                    self.state = 296
                    self.match(LPPParser.T__1)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedimientoLibreriaEstandarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROC_NUEVA_LINEA(self):
            return self.getToken(LPPParser.PROC_NUEVA_LINEA, 0)

        def PROC_LIMPIAR_PANTALLA(self):
            return self.getToken(LPPParser.PROC_LIMPIAR_PANTALLA, 0)

        def PROC_POSICIONAR_CURSOR(self):
            return self.getToken(LPPParser.PROC_POSICIONAR_CURSOR, 0)

        def PROC_IR_A(self):
            return self.getToken(LPPParser.PROC_IR_A, 0)

        def PROC_IR_A_INICIO(self):
            return self.getToken(LPPParser.PROC_IR_A_INICIO, 0)

        def PROC_IR_A_FIN(self):
            return self.getToken(LPPParser.PROC_IR_A_FIN, 0)

        def PROC_INICIALIZAR_ALEATORIO(self):
            return self.getToken(LPPParser.PROC_INICIALIZAR_ALEATORIO, 0)

        def PROC_PAUSA(self):
            return self.getToken(LPPParser.PROC_PAUSA, 0)

        def PROC_COLOR_TEXTO(self):
            return self.getToken(LPPParser.PROC_COLOR_TEXTO, 0)

        def PROC_COLOR_FONDO(self):
            return self.getToken(LPPParser.PROC_COLOR_FONDO, 0)

        def getRuleIndex(self):
            return LPPParser.RULE_procedimientoLibreriaEstandar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedimientoLibreriaEstandar" ):
                listener.enterProcedimientoLibreriaEstandar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedimientoLibreriaEstandar" ):
                listener.exitProcedimientoLibreriaEstandar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedimientoLibreriaEstandar" ):
                return visitor.visitProcedimientoLibreriaEstandar(self)
            else:
                return visitor.visitChildren(self)




    def procedimientoLibreriaEstandar(self):

        localctx = LPPParser.ProcedimientoLibreriaEstandarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_procedimientoLibreriaEstandar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 143974450587500544) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self, i:int=None):
            if i is None:
                return self.getTokens(LPPParser.SI)
            else:
                return self.getToken(LPPParser.SI, i)

        def expr(self):
            return self.getTypedRuleContext(LPPParser.ExprContext,0)


        def entonces(self):
            return self.getTypedRuleContext(LPPParser.EntoncesContext,0)


        def sentencias(self):
            return self.getTypedRuleContext(LPPParser.SentenciasContext,0)


        def FIN(self):
            return self.getToken(LPPParser.FIN, 0)

        def sino(self):
            return self.getTypedRuleContext(LPPParser.SinoContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_si

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSi" ):
                listener.enterSi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSi" ):
                listener.exitSi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSi" ):
                return visitor.visitSi(self)
            else:
                return visitor.visitChildren(self)




    def si(self):

        localctx = LPPParser.SiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_si)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(LPPParser.SI)
            self.state = 304
            self.expr(0)
            self.state = 305
            self.entonces()
            self.state = 306
            self.sentencias()
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 307
                self.sino()


            self.state = 310
            self.match(LPPParser.FIN)
            self.state = 311
            self.match(LPPParser.SI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntoncesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTONCES(self):
            return self.getToken(LPPParser.ENTONCES, 0)

        def getRuleIndex(self):
            return LPPParser.RULE_entonces

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntonces" ):
                listener.enterEntonces(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntonces" ):
                listener.exitEntonces(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntonces" ):
                return visitor.visitEntonces(self)
            else:
                return visitor.visitChildren(self)




    def entonces(self):

        localctx = LPPParser.EntoncesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_entonces)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(LPPParser.ENTONCES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SinoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINO(self):
            return self.getToken(LPPParser.SINO, 0)

        def si(self):
            return self.getTypedRuleContext(LPPParser.SiContext,0)


        def sentencias(self):
            return self.getTypedRuleContext(LPPParser.SentenciasContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_sino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSino" ):
                listener.enterSino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSino" ):
                listener.exitSino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSino" ):
                return visitor.visitSino(self)
            else:
                return visitor.visitChildren(self)




    def sino(self):

        localctx = LPPParser.SinoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_sino)
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.match(LPPParser.SINO)
                self.state = 316
                self.si()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.match(LPPParser.SINO)
                self.state = 318
                self.sentencias()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CasoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASO(self, i:int=None):
            if i is None:
                return self.getTokens(LPPParser.CASO)
            else:
                return self.getToken(LPPParser.CASO, i)

        def expr(self):
            return self.getTypedRuleContext(LPPParser.ExprContext,0)


        def FIN(self):
            return self.getToken(LPPParser.FIN, 0)

        def opcionCaso(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPPParser.OpcionCasoContext)
            else:
                return self.getTypedRuleContext(LPPParser.OpcionCasoContext,i)


        def casoSino(self):
            return self.getTypedRuleContext(LPPParser.CasoSinoContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_caso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaso" ):
                listener.enterCaso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaso" ):
                listener.exitCaso(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaso" ):
                return visitor.visitCaso(self)
            else:
                return visitor.visitChildren(self)




    def caso(self):

        localctx = LPPParser.CasoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_caso)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(LPPParser.CASO)
            self.state = 322
            self.expr(0)
            self.state = 324 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 323
                self.opcionCaso()
                self.state = 326 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & -144115188075855870) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 66585095) != 0)):
                    break

            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 328
                self.casoSino()


            self.state = 331
            self.match(LPPParser.FIN)
            self.state = 332
            self.match(LPPParser.CASO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpcionCasoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaExprOpcion(self):
            return self.getTypedRuleContext(LPPParser.ListaExprOpcionContext,0)


        def sentencias(self):
            return self.getTypedRuleContext(LPPParser.SentenciasContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_opcionCaso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpcionCaso" ):
                listener.enterOpcionCaso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpcionCaso" ):
                listener.exitOpcionCaso(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcionCaso" ):
                return visitor.visitOpcionCaso(self)
            else:
                return visitor.visitChildren(self)




    def opcionCaso(self):

        localctx = LPPParser.OpcionCasoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_opcionCaso)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.listaExprOpcion()
            self.state = 335
            self.match(LPPParser.T__2)
            self.state = 336
            self.sentencias()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaExprOpcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprOpcion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPPParser.ExprOpcionContext)
            else:
                return self.getTypedRuleContext(LPPParser.ExprOpcionContext,i)


        def coma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPPParser.ComaContext)
            else:
                return self.getTypedRuleContext(LPPParser.ComaContext,i)


        def getRuleIndex(self):
            return LPPParser.RULE_listaExprOpcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaExprOpcion" ):
                listener.enterListaExprOpcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaExprOpcion" ):
                listener.exitListaExprOpcion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaExprOpcion" ):
                return visitor.visitListaExprOpcion(self)
            else:
                return visitor.visitChildren(self)




    def listaExprOpcion(self):

        localctx = LPPParser.ListaExprOpcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_listaExprOpcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.exprOpcion()
            self.state = 344
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 339
                self.coma()
                self.state = 340
                self.exprOpcion()
                self.state = 346
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprOpcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rangoExpr(self):
            return self.getTypedRuleContext(LPPParser.RangoExprContext,0)


        def expr(self):
            return self.getTypedRuleContext(LPPParser.ExprContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_exprOpcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprOpcion" ):
                listener.enterExprOpcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprOpcion" ):
                listener.exitExprOpcion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprOpcion" ):
                return visitor.visitExprOpcion(self)
            else:
                return visitor.visitChildren(self)




    def exprOpcion(self):

        localctx = LPPParser.ExprOpcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exprOpcion)
        try:
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.rangoExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangoExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPPParser.ExprContext)
            else:
                return self.getTypedRuleContext(LPPParser.ExprContext,i)


        def getRuleIndex(self):
            return LPPParser.RULE_rangoExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRangoExpr" ):
                listener.enterRangoExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRangoExpr" ):
                listener.exitRangoExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRangoExpr" ):
                return visitor.visitRangoExpr(self)
            else:
                return visitor.visitChildren(self)




    def rangoExpr(self):

        localctx = LPPParser.RangoExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_rangoExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.expr(0)
            self.state = 352
            self.match(LPPParser.T__7)
            self.state = 353
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CasoSinoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINO(self):
            return self.getToken(LPPParser.SINO, 0)

        def sentencias(self):
            return self.getTypedRuleContext(LPPParser.SentenciasContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_casoSino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCasoSino" ):
                listener.enterCasoSino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCasoSino" ):
                listener.exitCasoSino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCasoSino" ):
                return visitor.visitCasoSino(self)
            else:
                return visitor.visitChildren(self)




    def casoSino(self):

        localctx = LPPParser.CasoSinoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_casoSino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(LPPParser.SINO)
            self.state = 356
            self.match(LPPParser.T__2)
            self.state = 357
            self.sentencias()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MientrasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self, i:int=None):
            if i is None:
                return self.getTokens(LPPParser.MIENTRAS)
            else:
                return self.getToken(LPPParser.MIENTRAS, i)

        def expr(self):
            return self.getTypedRuleContext(LPPParser.ExprContext,0)


        def haga(self):
            return self.getTypedRuleContext(LPPParser.HagaContext,0)


        def sentencias(self):
            return self.getTypedRuleContext(LPPParser.SentenciasContext,0)


        def FIN(self):
            return self.getToken(LPPParser.FIN, 0)

        def getRuleIndex(self):
            return LPPParser.RULE_mientras

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMientras" ):
                listener.enterMientras(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMientras" ):
                listener.exitMientras(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMientras" ):
                return visitor.visitMientras(self)
            else:
                return visitor.visitChildren(self)




    def mientras(self):

        localctx = LPPParser.MientrasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_mientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(LPPParser.MIENTRAS)
            self.state = 360
            self.expr(0)
            self.state = 361
            self.haga()
            self.state = 362
            self.sentencias()
            self.state = 363
            self.match(LPPParser.FIN)
            self.state = 364
            self.match(LPPParser.MIENTRAS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HagaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HAGA(self):
            return self.getToken(LPPParser.HAGA, 0)

        def getRuleIndex(self):
            return LPPParser.RULE_haga

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHaga" ):
                listener.enterHaga(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHaga" ):
                listener.exitHaga(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHaga" ):
                return visitor.visitHaga(self)
            else:
                return visitor.visitChildren(self)




    def haga(self):

        localctx = LPPParser.HagaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_haga)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(LPPParser.HAGA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARA(self, i:int=None):
            if i is None:
                return self.getTokens(LPPParser.PARA)
            else:
                return self.getToken(LPPParser.PARA, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPPParser.ExprContext)
            else:
                return self.getTypedRuleContext(LPPParser.ExprContext,i)


        def hasta(self):
            return self.getTypedRuleContext(LPPParser.HastaContext,0)


        def HAGA(self):
            return self.getToken(LPPParser.HAGA, 0)

        def sentencias(self):
            return self.getTypedRuleContext(LPPParser.SentenciasContext,0)


        def FIN(self):
            return self.getToken(LPPParser.FIN, 0)

        def getRuleIndex(self):
            return LPPParser.RULE_para

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPara" ):
                listener.enterPara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPara" ):
                listener.exitPara(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = LPPParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(LPPParser.PARA)
            self.state = 369
            self.expr(0)
            self.state = 370
            self.match(LPPParser.T__6)
            self.state = 371
            self.expr(0)
            self.state = 372
            self.hasta()
            self.state = 373
            self.match(LPPParser.HAGA)
            self.state = 374
            self.sentencias()
            self.state = 375
            self.match(LPPParser.FIN)
            self.state = 376
            self.match(LPPParser.PARA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HastaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HASTA(self):
            return self.getToken(LPPParser.HASTA, 0)

        def expr(self):
            return self.getTypedRuleContext(LPPParser.ExprContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_hasta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHasta" ):
                listener.enterHasta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHasta" ):
                listener.exitHasta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHasta" ):
                return visitor.visitHasta(self)
            else:
                return visitor.visitChildren(self)




    def hasta(self):

        localctx = LPPParser.HastaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_hasta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(LPPParser.HASTA)
            self.state = 379
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepitaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPITA(self):
            return self.getToken(LPPParser.REPITA, 0)

        def sentencias(self):
            return self.getTypedRuleContext(LPPParser.SentenciasContext,0)


        def HASTA(self):
            return self.getToken(LPPParser.HASTA, 0)

        def expr(self):
            return self.getTypedRuleContext(LPPParser.ExprContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_repita

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepita" ):
                listener.enterRepita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepita" ):
                listener.exitRepita(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepita" ):
                return visitor.visitRepita(self)
            else:
                return visitor.visitChildren(self)




    def repita(self):

        localctx = LPPParser.RepitaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_repita)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(LPPParser.REPITA)
            self.state = 382
            self.sentencias()
            self.state = 383
            self.match(LPPParser.HASTA)
            self.state = 384
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetorneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETORNE(self):
            return self.getToken(LPPParser.RETORNE, 0)

        def expr(self):
            return self.getTypedRuleContext(LPPParser.ExprContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_retorne

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetorne" ):
                listener.enterRetorne(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetorne" ):
                listener.exitRetorne(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetorne" ):
                return visitor.visitRetorne(self)
            else:
                return visitor.visitChildren(self)




    def retorne(self):

        localctx = LPPParser.RetorneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_retorne)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(LPPParser.RETORNE)
            self.state = 387
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AbrirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABRIR(self):
            return self.getToken(LPPParser.ABRIR, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPPParser.ExprContext)
            else:
                return self.getTypedRuleContext(LPPParser.ExprContext,i)


        def COMO(self):
            return self.getToken(LPPParser.COMO, 0)

        def PARA(self):
            return self.getToken(LPPParser.PARA, 0)

        def acceso(self):
            return self.getTypedRuleContext(LPPParser.AccesoContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_abrir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbrir" ):
                listener.enterAbrir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbrir" ):
                listener.exitAbrir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbrir" ):
                return visitor.visitAbrir(self)
            else:
                return visitor.visitChildren(self)




    def abrir(self):

        localctx = LPPParser.AbrirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_abrir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(LPPParser.ABRIR)
            self.state = 390
            self.expr(0)
            self.state = 391
            self.match(LPPParser.COMO)
            self.state = 392
            self.expr(0)
            self.state = 393
            self.match(LPPParser.PARA)
            self.state = 394
            self.acceso()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccesoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LECTURA(self):
            return self.getToken(LPPParser.LECTURA, 0)

        def coma(self):
            return self.getTypedRuleContext(LPPParser.ComaContext,0)


        def ESCRITURA(self):
            return self.getToken(LPPParser.ESCRITURA, 0)

        def getRuleIndex(self):
            return LPPParser.RULE_acceso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcceso" ):
                listener.enterAcceso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcceso" ):
                listener.exitAcceso(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcceso" ):
                return visitor.visitAcceso(self)
            else:
                return visitor.visitChildren(self)




    def acceso(self):

        localctx = LPPParser.AccesoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_acceso)
        self._la = 0 # Token type
        try:
            self.state = 408
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.match(LPPParser.LECTURA)
                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 397
                    self.coma()
                    self.state = 398
                    self.match(LPPParser.ESCRITURA)


                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.match(LPPParser.ESCRITURA)
                self.state = 406
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 403
                    self.coma()
                    self.state = 404
                    self.match(LPPParser.LECTURA)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CerrarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CERRAR(self):
            return self.getToken(LPPParser.CERRAR, 0)

        def expr(self):
            return self.getTypedRuleContext(LPPParser.ExprContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_cerrar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCerrar" ):
                listener.enterCerrar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCerrar" ):
                listener.exitCerrar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCerrar" ):
                return visitor.visitCerrar(self)
            else:
                return visitor.visitChildren(self)




    def cerrar(self):

        localctx = LPPParser.CerrarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_cerrar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(LPPParser.CERRAR)
            self.state = 411
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscribirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCRIBIR(self):
            return self.getToken(LPPParser.ESCRIBIR, 0)

        def expr(self):
            return self.getTypedRuleContext(LPPParser.ExprContext,0)


        def coma(self):
            return self.getTypedRuleContext(LPPParser.ComaContext,0)


        def listaExpr(self):
            return self.getTypedRuleContext(LPPParser.ListaExprContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_escribir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscribir" ):
                listener.enterEscribir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscribir" ):
                listener.exitEscribir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscribir" ):
                return visitor.visitEscribir(self)
            else:
                return visitor.visitChildren(self)




    def escribir(self):

        localctx = LPPParser.EscribirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_escribir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(LPPParser.ESCRIBIR)
            self.state = 414
            self.expr(0)
            self.state = 415
            self.coma()
            self.state = 416
            self.listaExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEER(self):
            return self.getToken(LPPParser.LEER, 0)

        def expr(self):
            return self.getTypedRuleContext(LPPParser.ExprContext,0)


        def coma(self):
            return self.getTypedRuleContext(LPPParser.ComaContext,0)


        def listaExpr(self):
            return self.getTypedRuleContext(LPPParser.ListaExprContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_leer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeer" ):
                listener.enterLeer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeer" ):
                listener.exitLeer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeer" ):
                return visitor.visitLeer(self)
            else:
                return visitor.visitChildren(self)




    def leer(self):

        localctx = LPPParser.LeerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_leer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(LPPParser.LEER)
            self.state = 419
            self.expr(0)
            self.state = 420
            self.coma()
            self.state = 421
            self.listaExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPPParser.ExprContext)
            else:
                return self.getTypedRuleContext(LPPParser.ExprContext,i)


        def coma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPPParser.ComaContext)
            else:
                return self.getTypedRuleContext(LPPParser.ComaContext,i)


        def getRuleIndex(self):
            return LPPParser.RULE_listaExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaExpr" ):
                listener.enterListaExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaExpr" ):
                listener.exitListaExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaExpr" ):
                return visitor.visitListaExpr(self)
            else:
                return visitor.visitChildren(self)




    def listaExpr(self):

        localctx = LPPParser.ListaExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_listaExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.expr(0)
            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 424
                self.coma()
                self.state = 425
                self.expr(0)
                self.state = 431
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LPPParser.RULE_coma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComa" ):
                listener.enterComa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComa" ):
                listener.exitComa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComa" ):
                return visitor.visitComa(self)
            else:
                return visitor.visitChildren(self)




    def coma(self):

        localctx = LPPParser.ComaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_coma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(LPPParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPPParser.ExprContext)
            else:
                return self.getTypedRuleContext(LPPParser.ExprContext,i)


        def literal(self):
            return self.getTypedRuleContext(LPPParser.LiteralContext,0)


        def ID(self):
            return self.getToken(LPPParser.ID, 0)

        def funcionLibreriaEstandar(self):
            return self.getTypedRuleContext(LPPParser.FuncionLibreriaEstandarContext,0)


        def listaExpr(self):
            return self.getTypedRuleContext(LPPParser.ListaExprContext,0)


        def openPar(self):
            return self.getTypedRuleContext(LPPParser.OpenParContext,0)


        def closePar(self):
            return self.getTypedRuleContext(LPPParser.CloseParContext,0)


        def RESTA(self):
            return self.getToken(LPPParser.RESTA, 0)

        def exponente(self):
            return self.getTypedRuleContext(LPPParser.ExponenteContext,0)


        def punto(self):
            return self.getTypedRuleContext(LPPParser.PuntoContext,0)


        def openBra(self):
            return self.getTypedRuleContext(LPPParser.OpenBraContext,0)


        def closeBra(self):
            return self.getTypedRuleContext(LPPParser.CloseBraContext,0)


        def getRuleIndex(self):
            return LPPParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LPPParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 435
                self.match(LPPParser.T__0)
                self.state = 436
                self.expr(0)
                self.state = 437
                self.match(LPPParser.T__1)
                pass

            elif la_ == 2:
                self.state = 439
                self.literal()
                pass

            elif la_ == 3:
                self.state = 440
                self.match(LPPParser.ID)
                pass

            elif la_ == 4:
                self.state = 441
                self.funcionLibreriaEstandar()
                self.state = 442
                self.match(LPPParser.T__0)
                self.state = 444
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -144115188075855870) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 66585095) != 0):
                    self.state = 443
                    self.listaExpr()


                self.state = 446
                self.match(LPPParser.T__1)
                pass

            elif la_ == 5:
                self.state = 448
                self.match(LPPParser.ID)
                self.state = 449
                self.openPar()
                self.state = 451
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -144115188075855870) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 66585095) != 0):
                    self.state = 450
                    self.listaExpr()


                self.state = 453
                self.closePar()
                pass

            elif la_ == 6:
                self.state = 455
                self.match(LPPParser.RESTA)
                self.state = 456
                self.expr(3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 476
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 474
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        localctx = LPPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 459
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 460
                        self.exponente()
                        self.state = 461
                        self.expr(2)
                        pass

                    elif la_ == 2:
                        localctx = LPPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 463
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 464
                        self.exponente()
                        self.state = 465
                        self.expr(2)
                        pass

                    elif la_ == 3:
                        localctx = LPPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 467
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 468
                        self.punto()
                        pass

                    elif la_ == 4:
                        localctx = LPPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 469
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 470
                        self.openBra()
                        self.state = 471
                        self.listaExpr()
                        self.state = 472
                        self.closeBra()
                        pass

             
                self.state = 478
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OpenParContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LPPParser.RULE_openPar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpenPar" ):
                listener.enterOpenPar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpenPar" ):
                listener.exitOpenPar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpenPar" ):
                return visitor.visitOpenPar(self)
            else:
                return visitor.visitChildren(self)




    def openPar(self):

        localctx = LPPParser.OpenParContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_openPar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.match(LPPParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CloseParContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LPPParser.RULE_closePar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClosePar" ):
                listener.enterClosePar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClosePar" ):
                listener.exitClosePar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClosePar" ):
                return visitor.visitClosePar(self)
            else:
                return visitor.visitChildren(self)




    def closePar(self):

        localctx = LPPParser.CloseParContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_closePar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.match(LPPParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpenBraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LPPParser.RULE_openBra

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpenBra" ):
                listener.enterOpenBra(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpenBra" ):
                listener.exitOpenBra(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpenBra" ):
                return visitor.visitOpenBra(self)
            else:
                return visitor.visitChildren(self)




    def openBra(self):

        localctx = LPPParser.OpenBraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_openBra)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(LPPParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CloseBraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LPPParser.RULE_closeBra

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCloseBra" ):
                listener.enterCloseBra(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCloseBra" ):
                listener.exitCloseBra(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCloseBra" ):
                return visitor.visitCloseBra(self)
            else:
                return visitor.visitChildren(self)




    def closeBra(self):

        localctx = LPPParser.CloseBraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_closeBra)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(LPPParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExponenteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PODER(self):
            return self.getToken(LPPParser.PODER, 0)

        def MULT(self):
            return self.getToken(LPPParser.MULT, 0)

        def DIV(self):
            return self.getToken(LPPParser.DIV, 0)

        def DIV_ENTEROS(self):
            return self.getToken(LPPParser.DIV_ENTEROS, 0)

        def MOD(self):
            return self.getToken(LPPParser.MOD, 0)

        def SUMA(self):
            return self.getToken(LPPParser.SUMA, 0)

        def RESTA(self):
            return self.getToken(LPPParser.RESTA, 0)

        def IGUAL(self):
            return self.getToken(LPPParser.IGUAL, 0)

        def DESIGUAL(self):
            return self.getToken(LPPParser.DESIGUAL, 0)

        def MENOR_IGUAL(self):
            return self.getToken(LPPParser.MENOR_IGUAL, 0)

        def MAYOR_IGUAL(self):
            return self.getToken(LPPParser.MAYOR_IGUAL, 0)

        def MENOR(self):
            return self.getToken(LPPParser.MENOR, 0)

        def MAYOR(self):
            return self.getToken(LPPParser.MAYOR, 0)

        def OP_Y(self):
            return self.getToken(LPPParser.OP_Y, 0)

        def OP_O(self):
            return self.getToken(LPPParser.OP_O, 0)

        def NO(self):
            return self.getToken(LPPParser.NO, 0)

        def getRuleIndex(self):
            return LPPParser.RULE_exponente

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponente" ):
                listener.enterExponente(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponente" ):
                listener.exitExponente(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponente" ):
                return visitor.visitExponente(self)
            else:
                return visitor.visitChildren(self)




    def exponente(self):

        localctx = LPPParser.ExponenteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_exponente)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            _la = self._input.LA(1)
            if not(((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & 65535) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PuntoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LPPParser.ID, 0)

        def getRuleIndex(self):
            return LPPParser.RULE_punto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPunto" ):
                listener.enterPunto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPunto" ):
                listener.exitPunto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPunto" ):
                return visitor.visitPunto(self)
            else:
                return visitor.visitChildren(self)




    def punto(self):

        localctx = LPPParser.PuntoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_punto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(LPPParser.T__8)
            self.state = 490
            self.match(LPPParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionLibreriaEstandarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_FDA(self):
            return self.getToken(LPPParser.FUNC_FDA, 0)

        def FUNC_POSICION_ACTUAL(self):
            return self.getToken(LPPParser.FUNC_POSICION_ACTUAL, 0)

        def FUNC_ALEATORIO(self):
            return self.getToken(LPPParser.FUNC_ALEATORIO, 0)

        def FUNC_OBTENER_CARACTER(self):
            return self.getToken(LPPParser.FUNC_OBTENER_CARACTER, 0)

        def FUNC_ENTERO_A_CADENA(self):
            return self.getToken(LPPParser.FUNC_ENTERO_A_CADENA, 0)

        def FUNC_REAL_A_CADENA(self):
            return self.getToken(LPPParser.FUNC_REAL_A_CADENA, 0)

        def FUNC_TECLA_PRESIONADA(self):
            return self.getToken(LPPParser.FUNC_TECLA_PRESIONADA, 0)

        def FUNC_VALOR_ASCII(self):
            return self.getToken(LPPParser.FUNC_VALOR_ASCII, 0)

        def FUNC_CARACTER_ASCII(self):
            return self.getToken(LPPParser.FUNC_CARACTER_ASCII, 0)

        def FUNC_LONGITUD(self):
            return self.getToken(LPPParser.FUNC_LONGITUD, 0)

        def getRuleIndex(self):
            return LPPParser.RULE_funcionLibreriaEstandar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncionLibreriaEstandar" ):
                listener.enterFuncionLibreriaEstandar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncionLibreriaEstandar" ):
                listener.exitFuncionLibreriaEstandar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncionLibreriaEstandar" ):
                return visitor.visitFuncionLibreriaEstandar(self)
            else:
                return visitor.visitChildren(self)




    def funcionLibreriaEstandar(self):

        localctx = LPPParser.FuncionLibreriaEstandarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_funcionLibreriaEstandar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            _la = self._input.LA(1)
            if not(((((_la - 57)) & ~0x3f) == 0 and ((1 << (_la - 57)) & 1023) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITERAL_REAL(self):
            return self.getToken(LPPParser.LITERAL_REAL, 0)

        def LITERAL_ENTERO(self):
            return self.getToken(LPPParser.LITERAL_ENTERO, 0)

        def LITERAL_CADENA(self):
            return self.getToken(LPPParser.LITERAL_CADENA, 0)

        def LITERAL_CARACTER(self):
            return self.getToken(LPPParser.LITERAL_CARACTER, 0)

        def VERDADERO(self):
            return self.getToken(LPPParser.VERDADERO, 0)

        def FALSO(self):
            return self.getToken(LPPParser.FALSO, 0)

        def getRuleIndex(self):
            return LPPParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = LPPParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.state = 499
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [83]:
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.match(LPPParser.LITERAL_REAL)
                pass
            elif token in [84]:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
                self.match(LPPParser.LITERAL_ENTERO)
                pass
            elif token in [85]:
                self.enterOuterAlt(localctx, 3)
                self.state = 496
                self.match(LPPParser.LITERAL_CADENA)
                pass
            elif token in [86]:
                self.enterOuterAlt(localctx, 4)
                self.state = 497
                self.match(LPPParser.LITERAL_CARACTER)
                pass
            elif token in [87, 88]:
                self.enterOuterAlt(localctx, 5)
                self.state = 498
                _la = self._input.LA(1)
                if not(_la==87 or _la==88):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[46] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         




