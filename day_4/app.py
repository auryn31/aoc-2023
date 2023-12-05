
input = """
Card   1: 99 46 62 92 60 37 52 56 41 31 | 83 40 31 33 46  3 10 39 82  8 64 35  5 63 60 72 48 87 11 81 95 34 97 37 99
Card   2: 98 96 50 60  7 40 83 93 55 26 | 45 38 47 98 32 50 55 35 93 11 97 53 74 83 99 60 73 56 40 58 96 66 90 26  7
Card   3: 82  8 12 15 53 23 29 61  5 21 | 21 73  5 65 44 29 61 97 15  4 90 76 53 91 13 27  9 11  2 75 22 92 95 82 86
Card   4: 68 22 77 52 23 60 57 31 74 38 | 22 38 68 79 52 23 40 57 10 74 31 83 24 60 95 17 78 89 39 37 87 26 77 63 54
Card   5: 94 23 38 14 31 47  8 15 19 79 | 94 45 21 70 43 95 79 38 19 67 24 62 71 84 14 87 63 47 36 26  8 66 31 15 23
Card   6: 37 56 14 26 46 19 58 99 41 55 | 95 25 39 19 26 99 21 11 56 46  3 53 33 36  4 15 55 28 58 37 14 50 94 49 44
Card   7: 68 13 44 81 92 43  9 78 85 62 | 19  8 91 71 76 54 72 87 68 16 46 94 92 63 62 67 28 84 18 88 24 14 37 30 81
Card   8: 73 86 24 66 38 95 71 90 88 22 | 44 88 30 24 97 34 99 66 94 26 86 90 52 55 84  7 78 40 71 73 50 95 61 38 22
Card   9: 98 71 24 85 11 74 22 35 65 59 | 18 43 54 36 71 86 22  7 85 78 46  6 77 62 38 98 83 65 88 37 84 70 72 59 23
Card  10:  5 87 77 60 62 86 42 33 43 76 | 86 19 26 77  5 60 21 34 44 76 33 85 78 67 79 13 18 42 87 59 54 43 62 65 16
Card  11: 55 61 40 88 59 58 62 42  9 71 | 83 97 25 49 30 76 82 39 98  5 91 58 38 44  6 90 55 14 62 16 93 15 68 42 70
Card  12: 15 25 80 89 26 44 17 56 82 70 | 29 25 15 33 95 89 85 98 82 66 62 38 97 71 26 70 49 64 57 17 35 56 44 46 72
Card  13: 72 99 42 47 10 66 17 53 49 57 | 66 89 64 88  1 95 42 53 72 57 83 12 49 21 44 17 24 79 73 10 90 47 82 87 99
Card  14: 36 26 75 45 39 10 73  4 52 97 | 17 72 26  4 90 30 10 43 59 64 14 41 34 82 37 25 27 99 32 73 45 75 36 39 93
Card  15: 79 15 53 44 50 57 99 55 61 59 |  5 39  6 15 41  4 94 85 13 58 60 24 36 46 57 33  8 30 25 51 22 38 92 79 16
Card  16:  1 46 37 33 53 23 83 40 95 57 | 12 60 26 36 22 69 68 86 83 42 53 70 63  5 84 29 75 19 61 55 74  9 32 44 73
Card  17: 33 17 50 35 39 95 22 67 76 47 | 44 55 21  3  2  5 51 26 89 39 98 92 29 93 78 42 66 19 28 31 97 81 53 52 86
Card  18: 64 15 40 93 58 22  2 53 30 92 | 64 42 72 39 60 29 10 80 70 91 78 79 37  2 48  3 47 32 30 76 84 11 96 18 23
Card  19: 97 95 42 67 18 69 54 94 10  5 | 22 45 23 35 92  2 75 21  9 68 51 59 25 27 84 28 89 61 76 63 65 14 43  8 13
Card  20: 69 87  4 30 13 63 74 23 83 14 | 26 19 32 64 88 39 25 53 16 48 41 89 22 14 15 83 20 43 59 92 90  5 75 38 37
Card  21: 67 33 16 11 42 10 27 46 72 37 | 52 87 92  8 91 66 38 80 86 35 54  6 72  4 99 25 70 16 55 75 57 30 44 69 45
Card  22: 27 82 94 86 50 91 21 70 14 76 | 10 60 59 35 51 71 34 44 93 28 46 27 12 84 75 74  1 39 79 53 86 37  4 99  8
Card  23: 95 97 54 38 34 16 15  2 64  6 | 96 74 69 62 35 28 88 30 48 84 99 73 43 21 89 24  1 13 58 71  5 19 72 47 12
Card  24: 96 44 79  9 73  3 52 17 63 98 | 61 46 10 24 29 62 55 51 19 83  8 70 26 59 76 48 25 69  2 97 43 22 42 53 54
Card  25: 41 19 88 60 86 50 18 95 24  4 | 41 88 16 33 49 50 95 53 76 35  4 24 45 94 55  9 51 99 60 18 40 93 78 86 19
Card  26:  5 21  3 15 92 96 62 55 41 40 | 63 77 40 15 65  3 96 78 37  4 97  8 33  6 73 11  7 92 55  5 62 72 27 18 47
Card  27: 71 24 54 64 30 27 26 57 55 85 | 35 47 59 71 54 55 37 60 69 77 82 65 21 57  5 24 46  4 49 95 15  3 18 27 64
Card  28: 98 39 92 41 97 71 91 43 40 56 | 39 71 63 44 62 75 97 82  2 92 28 56 20 67 98 69 13 40 86 66 81 60 43 41 91
Card  29: 36 94 22 10 41 40 78 70 95 89 | 37 30  9 72 27 84  2 21 92 38 19 83 31 47  3 12  5 61 16 98 75 57 94 93  4
Card  30: 78 88 77 79 61 56 98 39 68 35 | 78 59 56 49 39 63 90 26 77 40 60 16 14 98 66 79 95 41 35 34 44 73 43 57  5
Card  31: 34 73 75 54 99 27 70 89 62 45 | 90  5 40 18 21 98 70 96 50 81 68 37 74 77 80 43 34 73 39 45  2 82  9 10  8
Card  32: 96 26  4 32 12  6 64  2 58 60 | 18 96 20 23 85  6 12 49 58 54  2 48 98 60 70 59 69 45 99 74 13  4 21 28 64
Card  33: 78 81 10 46 32 16 12 95 53 27 | 61 55  6 63 91 37 34 88 56 80 77 21 38 85 32 92  8  9 28 89 99 94 14 57 46
Card  34: 23 80 22 10 30 50 89  8 21 16 | 45 69 42 28 54 93 85 30 62 21 66 39 72  6 11  8 16 53 59 18 98 29 27 49 73
Card  35: 51 86 59 85 23 42 41 88 83 63 |  5 78 48 35 27 62 82 60 49 33 23 79 91 88  2 11 54 12  8 15  9 67 31  4 47
Card  36: 56 60 49 10 35 38 28 75 21 40 |  5 37 93 17 92 41 66 38 34 47 56 89 35 48 84 76 65 25  8 51 53 16 54 72 52
Card  37: 54 81 13  1 52 34 98 91 65 49 | 36  5 56 18 31 46 59 21 23 25 33 69 51 24 78 39 40 29 52 93 77 13 71 32 97
Card  38:  1 78 73 52 53 64 66 47 96 77 | 94 63 31  3 11 14 97 32 85 45  8 98 82 62 88 28 60 41 84 69 20 75 30 33 44
Card  39: 98 71 74 50 62 59 58 35 49 60 | 89 16 49 11 74 48 30 23 51 65 24  1 38 46 52 84 73 26 96 88 56 18 85 68 14
Card  40:  4 31 39 27 97 41 98  6 43 54 | 32 70 23 34 73 66 52 88 81 71 10 27 14 24 77 59 65 15 78  8 21 30 79  7 50
Card  41: 28 21 88 19 33 36 30 70 64 81 |  9 40  3 91  4 59 41 35 50 95 55 57 52 26 18 12 92 98 44 32 80 68 85 97 61
Card  42:  4 93 74 66 18 27 25 20 32 65 | 54 21 32  4 73 87 27 40 10 64 57 56 74 20 34 92 25 93 88 36 18 66 37 65 67
Card  43: 95 94 41 18 65 93 13 25 12 34 | 93  4 12 43 97 64 82 87 65 16 29 34 67 11 32 57 15 17 14 61 37 13 18 60 98
Card  44: 61 49 74 81  5 91 37 52  6 53 | 15 73  3 66 93 35 33 51 20 74 92 48 72 61 60 27 36 91 97 47 12 75 49 52 53
Card  45: 30  1 29 37 64  4 72 14 78 83 | 64 27 59  3 61 15 71 60 84 29 39  7  2 70 45 36 14 19 33 56 54 95  9 69 11
Card  46: 80 61 25 90 50  5 11 30 35 37 | 90 17  1 80 27 15 30 45 52 39 76 92 60 93 23 89 58 21 18 25 46 61 36 44 88
Card  47: 29 72 76 45 58  2 55 73 12 90 | 88 13 44 25 40 24 84 70 16 66 12 18 10 61 55 29 65 35 93  7 77 82 83 87 90
Card  48: 76  4 75 31 14 41 48 58 51 69 | 27 48 76  4 38 41 68 90 92  5 84 10 31 75 67 58 69 71 14 93 80 24 91 39 51
Card  49: 81 35 86 29 85 28 16  8 18 15 | 29 12 35 45 82 14  9 55  8 64 52 96 48 56 60 66 16 92 72 86 36 23 69 70 37
Card  50: 74  5 11 36 71 92 54  3 26 35 | 16  2 92 11  7 76  8 87 48 54 34 82  3 68 26  5 71 74 97 36 38 28 35 80 53
Card  51: 58 18 51 75 22 48 53 52 77 24 | 72 84 19 62 73 51 11 24 50 92 57 81 36 64 95  1 87 71 25 86 16 54 53 85 45
Card  52: 22 83 45 29 47 18 89 38  5 63 | 71 28 21  2 10 30 59 31 67 12 61 51 87 46 97 75 19 91  8 43 62 27 99 88 72
Card  53: 33 97 73 45 14 56 21 18 17 83 | 17 54 33 39 73 82 83 57 34 45 99 50 21 87 68  8 81 97 76 42 14 18 94 51 31
Card  54: 54 38 17 78  1 59 32  5 41 75 | 79 80 18 36 26 89 66 40 11  1 87 63 14  3  5 48 75 43 13 38 81 72 59 82 54
Card  55: 75 42 62 53 35 84  6 20 40 10 | 22 36 74 30 57 16  1 64 46 58  9  3 45 33 25 60  8 59 41 28 76 15 75 79 37
Card  56: 31 79 49 20  8 56 78 38 96 64 | 59 71  8 79 31 51 88 78 46 20 64 35 27 53 75 21 70 92 28 42 56 33 76 96 99
Card  57: 85 37 76 51  7 60 16 56 27 71 | 68  9 27 14 10 12 19 63 56 67 36 35 71 52 57 51 92 85 75 97 18 23 11 76  5
Card  58: 79 82 21 48 89 88 65 49 30 68 |  2 28 94 49 21  6 60 30  9 64 89 91 97 75 88 12 79 51 36 67 65 82 11 55 26
Card  59: 31 83 87 62 28 76 94 89 22 46 | 14  9 79 63 74 89 83 62 84 37 49 31 99 76 96  7 39  3 18 59 85 28 60 94 29
Card  60: 23 34 26 59 94 24 88 68 77 30 | 52 43 30 81 33 17 73 41 38  3 96 90 65 68 55 64 84 20 85 12 36 79 32 18  8
Card  61: 17 46 97 52 55 51 81 75  4 14 | 12 52 26 13 93 71 33 53  8 38 70 29 66 24 81 51 75 20 54 73 35 32 16 64 11
Card  62: 97 52 29 36 93  3 77 84 45 41 | 61 58 47 10 69  8  6 63 57 51 85  1 53 78 76 40 67  9 62 35 48 95 72 86 12
Card  63:  9 74 61  5 66 95 59 56 51 19 | 52 96 82  3 15 42 69 90 43 10  8 44 86 85 63 18 48 16 34 94  6 38 58 55 35
Card  64: 97 25 57 38 14 15 51 75 16 68 | 48 91 34 16  9 86 42 81 24 98 50 32 80 57  4 93 46 53 73 60 26  7 65 45  5
Card  65: 74 42 66 63 84 41 76 78  8 95 | 21 34 93 27 17 16 78 36 37 67 38 46 31 64 26 72 58 80  6 59 65 19 45  4 86
Card  66: 53 10 22 55 68 30 44 64 38 51 | 26 11 16 70 29 43 35 96 80  6 52 27 71 72 28 13 58 36 76 50 12  4 92 88 57
Card  67: 30 40 95 71 85  2 10 54 58 78 | 20 35 37  5 84 93  2 58 43 21 14  1 25 27 85 13 71 88 78 67 10 68 97 54 32
Card  68: 26 32 31  3 25 65 55 29 24 99 | 97 10 13 61 23 40 19 71 15 72 63 96  8 81 21 33 66 51 85 62  7 44 36 42 49
Card  69: 96 29 40 52 39 73 38 72 90 22 | 50 79 62 52 71 51 22 43 96 29 47 90 19 72 75 58 95 83 61 42  9 59 73 39 49
Card  70: 37 66 45  2 98 67 18 35 61 48 | 45 27 66  2 35 31 44 71 22 37 15  1 61 48 95 91 90 41 18 77 67 70 32 30 98
Card  71: 52 48 91 95  9 55 37 56 34 39 | 45 56 49 39 65 55 32  9 68 88  3 28 34 17 26 30 91 10 42 20 59 18 48 41 44
Card  72: 43 15 49 52 69 77 40 46 78 75 | 55 50  4 12 92  8 89 59 65 37 77 45 36 97 43 28  3 93 22 94 95 20 35  1 13
Card  73: 21 39 86  8 13 66 61 67 96 28 | 20 17 24 48 46 43 19 16 23 95 77 57 60 38 90 14 94  3 71 58 30 93 26  5 52
Card  74: 60 70 73 38 71 16 34 46  6 96 | 72 41 21 96 16 90 42 27 60 51 46 48 24 20 71 55 91 29  4 38 59 23 62 25 68
Card  75: 61 86 47 54 72 37 30 18 39 80 | 29 45 73 84 54 66 37 59 13 39  2 30 63 56 15 18 81 80  9 92 17 53 79 77 83
Card  76: 90  9 82 52 93 51 26 44 33 96 | 57 93 70 48 95 84 25  6 28 59 30 18 47 96 64 55  9 15 31 68 73 36 98 51 79
Card  77: 66 31 11 90 97 12 85 10 87 52 | 60  9  8 88 15 11  2 87 46 21 31  1 40 97  6 30 84 93 91 82 57 96 26  3 78
Card  78: 44 25 92 80  8 73 21 20 83 82 | 88 48 87 18 12 40 19 70 64 53 97 89  7 11 78 68 52  4 99 43 42 67 25 54 60
Card  79: 92 22 37  1  9 98 42 70 71 13 | 51 25 69 53 35 57 21 71 24 86 37 85 88 75  8 64 18 12 13 34 32 95 29 70 91
Card  80: 77 81 91 15  6 22  5 79 98 33 | 77 29 49 62 17 71 78 34 68 21 43 48 99 15 30 22 87  7 94 37 76 13 63 32 65
Card  81:  5 66 94 92 59 42  6 53 60 80 | 35 90 27 22 26 72 30 87 95 10 11 62 74 97 58 39 13 51 50 93 75 34 88 81 19
Card  82:  2 77 93 21  3 51 65 23 83 45 | 13 51 32 48 17 98 33 91 99 30 31 61  8 70 74  6 53 85 50 26 47 71 16 82 73
Card  83: 51 80 73 74 21 64 26 45 46 79 |  3 70 69 35 15 84 30 99 88 28 76 33 53 98 32 12 49 42 58 16 62 27 89 78 52
Card  84: 85 89 20 90 44 38 87 88 55  3 | 85 55 26 87  1 35  5 20 10 43 88 11 89 54 68 38  6  3 44 63 90 31  8 13 93
Card  85: 87 73 32  1 85 92 65 41 93 48 | 42 12 48 26 85 63 20 78 67 65  7 50 62 57 31 72 28 97 36 45  5 27 86 71 77
Card  86: 98 28 76 61 50 97 45 59 57 71 | 73 53 56 61 34 46 72 57 11  9 86 71 33 76 21  3 67 78 36 89 28 91 60 50 59
Card  87:  8 39 56 10 33 91 93 23 79 17 | 18 62 52 45 56  9 33 37 79 10 91 23 36  8 39 29 14 17 86 93 43 94  6  5 61
Card  88: 29 60 20 31 50 38 96 97 54 35 | 66 35  2 20 65 96 56 54 52 84 85 38 43 26 29 72 62 70 31 60 74 50 80 97 94
Card  89: 20 85 33 84 23 24 19 77 68 26 | 85 68 33 77 48 24  5 32 49 45 55 51 23 62 11 80 30 35 61 28 36 81  9 17 86
Card  90: 43 48 92 89 56 12 54 78  9 14 | 39 89  9 12 15 64 83 41 44 65 40 48 79  2 78 16 92 84 76 88 27 54 66 56 49
Card  91: 43  7 86 10 47 66 33 62  8 87 | 87 97 46 25 83 92 23 15 17 42 45 78  1 59 60 67 74 86  9 76 85 55  3  2 53
Card  92: 71 19 66 35 77 74 56 15  8 75 | 69 41 57 14 89 71 40 77 26 12 91 17 38 62 80 60  5 68 93 35 66 39  2  8 21
Card  93: 11 98  2 60 92 77 70 75 53 65 | 65 70 67 75 98 59  2 34 60 62 92 43 11 77 68  1 26 82 76 19 57 28 46 53 86
Card  94: 38 59 82 85 65 51  5 72 37 75 | 47 25 67 79  7 16 44 33 95 52 97 88 89 99 96 53 27 21 71 86 68 55 62 30 70
Card  95: 44 26  1 60 71 88 50 38 27 69 | 88 58 69 60 91 90 26 45 92 33 97 48 99 71  1 78 44 54  2 27 50 83 56 79 38
Card  96: 62 97 57 99 48 91 50 35 78 26 | 60 10 55  4 58  1  7 65 90 44 57 68 89 36 50 17  2 28 37 92 84 82 96 53 74
Card  97: 39 82 45 56 86 88 63 95 52 27 | 24 55 81 67 12 71 57 74 17  3  6 46 21 53 59 27 31 16 43 19 99 79 35 80  4
Card  98: 16  3 72 97 64 68 58 15 37 89 | 44 74  6 75 78 68 38 52 61 23 58 72 21  3 84 46  7 16 62 89 18 85 64 43 19
Card  99: 41 90 11 70 13 92  4 87  6 12 |  9 87 29 57 84 54 80 61 37 18 85 24 78 49 25 43 52 27 50  6 16 99  2 13 88
Card 100: 33 84 70 12 63 95 57 83 66 94 | 89 96 50 99 90 42 27 68 95 15 60 36 92 35 54 98 28 34  6 53 48 37 88 56 17
Card 101: 42 89 68 72 14 20 50 22 71 10 | 45 47 67 13 94 81 52 37 76 48 77 34 70 18 41 87  3 53 49 35 19 30 58 95 11
Card 102: 95 38  4 55 94 50 68 11 56 17 | 75 46 61 54 62 98 59 77 31 97 76 33 80 55 96 66 94 26 41 60 86 73 84 14 50
Card 103: 78 75 96 32 68 33 37 39 28 73 | 64 56 72 18 91 10 25 62 65 86 43  7  9 81  4  5 11 99 27 88 29 36 76 38 24
Card 104: 88 99 34 79 12 14 97 35 75 29 | 55 42 19  2  8 16 51 32  4 50 11  3 38 64 57 86 26  7 56 27 70 74 49  5 46
Card 105: 98  8 99 61 88 84  1 41 31 10 | 97 58  3 74 21 63 48 87 75  7 45 15 46 30 57 40 90  9 35 65 29 23 71 94 16
Card 106: 67 35 98 56 14 24 75 90 83 34 | 55 33 18  8 12 87  6 26 29 66 37 22 21 13 46 86 76 81 59 69 51 11 20 28 50
Card 107: 59 77 79 71  8 73 93 46 18 87 | 20 24 66 10  4 68 59 80 77 49 93 38 18 46 83 71 85 30 87 52 53 69 79  8 73
Card 108: 65 42 53 83 52 28  2 50 17 49 | 17 55  7 42 49 48 26 68 82 43 46 19  5  2 65 94 36 66 25 69 15 76 51 62 52
Card 109:  9 97 46 11 23 91 10 30 58 90 | 79 58 90 91 16 30 60 43 80 51  9 65 13 46 67  8 66 97 10 94  7  2  6 11 23
Card 110: 38 89 44  8 10 61 18 11 47 36 |  8 32 61 93  3 38 74 80 63 67 18 22 13 47 14 59 94 55 86 79 36 44 23 40 53
Card 111:  1  3 62 17 70 69 18 71 90  5 |  5 93  2 13 70 27 88 90 79 65 71 62 46 73 96 74 48 31 83 18 63  1 56 10 28
Card 112:  3 19 30  2  1 23 14  6 95 82 | 33 32 27 67 50 30 68 82  2 77  1 34 36 19 65 64 54 95 47  3  4 91 15 23 51
Card 113: 23 10 40 84 65 76 64 38 74 45 | 44 52 56 59 45 40 12 66 16 64 78 97 72 23 84 74 85 65 27 76 38 10 82 86 48
Card 114: 11 98 33 35 31 14 28 91 81 85 |  9 66 54 65 48 77  7  6 45 38 31 30  8 75 86 93 52 95 76 44 35 17 68 63  1
Card 115: 19 72 36 87 84 13 81  3 90 94 | 84 37 94 40 18 81 13 69 11  2 35 19 42 36  3  5 56 99 24 80 28  4 92 31 83
Card 116: 13 75  5 29 67 65 74 82  8 53 | 89 29 88 94  3 22 41 53 28 27 16 49 90 13 95 85 37 58 86 68 11 67 69 75 73
Card 117: 94 24 87 15 76 70 98 68 41 25 | 67 66 12 37 13  2  5 84 95 69 79 70  1 15 97 39 23 14 41 52 65 83 30  3 45
Card 118: 72 28 73 30 33 36 42 66  4 74 | 28 98 72 46  2 12 25 74 40 37 34 48 43 30 42 79 67 13 57 44 45 16 53 68 70
Card 119:  5 37 38 60 76 78 80 29 34 88 | 63 53 81 38 29 80 83  2 85  5 48 86 21 79 60 37 42 10 55 46 34 96 17 71 33
Card 120:  9 41 14 88 34 28 77 96 42 23 | 49 14 78 91 95 74 45 16 38 61 98 53 51 79 27 88 34  9 90 40 28 21 26 93 20
Card 121: 14 17 97 68  9 18 32  2 46 56 | 18 64  9 86 56 10 79 17 57 87 26 88 46 27 83 84 15 59 65 21 11 85 66  3  2
Card 122: 91 51 99 50 90 60 81 61 94 18 | 44 70 65  9 88  2 48 51 59 82 77  7 75 34  8 17 52 39 57 86 99  1 14 13 25
Card 123: 91 85 26 99 53 10 25 97 76 16 | 47 81 86 58 11 63 82 98 79 12 27  6 85 94 53 40 19 13 48 18 24 74 44 80  3
Card 124: 97 64 48 61 35 45 12 39 89 33 | 93 73 58 11 30 71 82 16 35 53 52 50 59 18  1 39 78 41 63 42  3 12 43 79 49
Card 125: 63 16 92 55  1 61 86 99 21 48 | 76 73 25 74 43 10 21 64 66  6 78 33 56 30 57 69 13 12 50 86 93 31 90 36 27
Card 126: 97 73 82 26  3 33 54 10 29 30 | 14 87  1 38 51 11 36 43 25  5 62 20 95 79 18 57 71 50 37 32 84  7 69 33 45
Card 127: 54 24  8 45 47 88 86  6 35 75 | 60 32 43 76 63 12 56  1 79 44  7 70 42 46 68 51 64 62 31 34 33 99 19 36 53
Card 128: 94 11 73 52 24 36 76 80 93 92 | 10 74 85 62 43 67 18 11 93 40 60 39 96 80 73 92 76 77 35 48 36 66 57 52 24
Card 129: 47 26 37 60 90 93 16 69 52 64 | 63 83 37 19 90 26 67  2 35 96  1 62 98 71  3  7 41 34 64 93 16 48 60 47 94
Card 130: 55 62 26 32 39 38 48 98 52 16 | 77 32 95 80 39 52 98 99 60 79 16 26 19 46  8 97 10 25 92 54 42 62 71 65 48
Card 131: 24 44 79 83 89 39 57 70 92 29 | 61 11 70 10 83 54 97 80 57 39 50 22 58 62 28 92 29 44 79 24 89 45 15  8 14
Card 132:  8  1  2 72 30 68 23 84 49 39 |  2 23 64 49 56 62 72 41  1 30 86 60 75  8 38 53 97 39 14 85 27 45 68 84 67
Card 133: 76 28 92  6 54  2 46 37 59 61 | 31 42 48 82 15 65 37 52 13 78 81 98 38 34  3 28 10 49 61 92 47 41 46 59 70
Card 134: 69 73 87 26  2 63  1 41 88 96 | 13  1 19 97 72 37 80 89 39 23 95 66 69 98 25 74 46 38 67 43 68 40 91 10 36
Card 135: 76 99 25 95 57 93 83 33 62 44 |  9 49 88 45 64 50 87 56  5 24 57 60 96 67 61 26 75 23 18 19 16 81 46 54 32
Card 136: 78 40 11 33 70 76 67 50 56 59 | 18 29 75 99 76 32 56 30 33 70 87 60 78 14 50 80 21 40 65 11 91 67 53 97 59
Card 137: 90 76 40 18 64 17 13 41 27 34 | 58  3 50 94 10 74 79 69  6 33 78 29 28 96 49 38 60  2 62 72 83 43 54 92 93
Card 138: 55 50 90  4 58 12 61 60 99 43 | 64 46 75 41  8 53 24 77 51 11 74 91 32 62 93 35 38  1 14 47 48 67 96 49 22
Card 139: 85 43 37 22 62  2 39 34 38  4 | 87  1 97 23 15 99 78  5  9 47 94 30 85  8 86 92 21 91 27 69 11 13 84 32 79
Card 140: 83 71 63 22 39 91 54 93 66 44 | 96 56 92 64 80 31 85 70 88  7 39 59 65 27  2  6 93 54 62 52 44 10 22 32 79
Card 141: 57 50 28 29 97 79 64 54 43 35 | 98 40 62 42 20 83 33 82 30 91 80 10 99 41 87 66 92 14  7 67 85 22  8 97 51
Card 142: 70 38 32 83 21 44 71 36 56  3 | 84 47 62 20 22 86 41 30 38 67 77 49 61 50  8 90  2 88 69 24 53  4 80 73 52
Card 143: 61 49 17 60 20 69  2  9 13  1 | 54 10 18 89 26 52 27 73 63 71 48 60  1 17  4 84 66 45 13  3  8 72 29 37 50
Card 144: 95 58 31 44 62  5  6  9 69  3 | 55 88 13 28 62 36 35 54 23 24 46 49 53 69 97  1 20 74 30 95 72 29 66 78 39
Card 145: 10 25 94 63 11 96 55 61  9  8 | 32 48 37 85 82 72 63 26 24 91 43 17 15 65  8 23 93 70 51 58 76 77 53 31 61
Card 146:  8 55 37 91 72 20 53 76 60 39 | 70 75 89 46 92 45 10 79 16 82 61 19 21  7 13 22 54  1 81 50 98 15 85 33  2
Card 147: 15 72 61 77 66 10 31 26 59 75 |  4  3  7 32 54 73 30 21 60 77 55 63 23 29 40 97 62 10 76 14 80 51 18 70 49
Card 148: 14 11  9 38 16 51 18 32 97 46 | 58 52 25 37 29 57  1 22 93 94 81 95 27 73 72 13 49 33 20 31 42 62  3 76 77
Card 149: 16 17 18 31 63 39 57 73  8 34 | 55 99 20 84 76 97 46 81 52 26  5 29 96 25  9 12 66 72 10 89  1 15 70 60 75
Card 150: 75 51 17 56 61 52 27 12 18  4 | 10  5 20 28 53 82 22 69 79 89 31 32 14 39 72  2 58 97 54 83 91 70 15 74 65
Card 151:  7 43  8 44 58 93 36 13 69 11 | 48 93 42  4 56 11 71 52 72 36 25 14 55 58 67 28 97 82 62 31 79 53  2 51 69
Card 152: 67  4 77 16 31 97 41 40 39 23 | 52  9 16 45 31 47 41  4  5 50 39 51 66 69 53 37 67 83 97 77 75 23 29 25 42
Card 153:  7 80  4 25 94 99 83 34 37 69 | 10 67 82 39  8 65 89 57 45  9 59 43 29 61 88 74 11 90 70  1 92 19 78 77 41
Card 154: 46  8 45 40  5 72 21 11 27 73 | 83 98 46 33 91 71 61 85 27 45 24 12 21 36 11 54 75  8 76 73 69 40 34 70 10
Card 155:  5 68 92 86 58 19 93 45  3 38 | 40 13 71 96 80 25 41 73 92 82 21 43 42 24  3 39  4 99 29 20 55 35 12 75 59
Card 156:  4 44 95 99 28 65 66 89 85 59 | 69 60 13 58 66 40 18 30 92 86 71 85 90 65 44  2 59 89 55 94  4 26 99 95 28
Card 157:  5 67 81 91 85 20 75 37 12 16 | 94 98 22 90 99 18 38 95 23 69  6 16 96 35  3 86  9 56 26 48 79 24 34 54 91
Card 158: 90 23 70 11 94 36 31 61 13 19 |  7 45 36 11 81 47 50 69 21  2 18 67 27 72 61  8 24 38 13 52 75  9 79 65 19
Card 159: 98  5 17 32 20 22 72 86 26 81 | 76 80 33 35 45 70 86 63 88 87 91 53 64 51 74 29 75 27 42  4 34 90 31 18 14
Card 160: 76 11 61 84 56 31 42 26  3 85 | 62 85 48 47 61 82 42 36 43 58 91 93  5 16 87 18 37 15 39 29 49 86 22 84 17
Card 161: 14 88  6 50 59 86 57 94 10 60 | 33 60 87 49 23 64 42 54 71 56 65 50 39 10 16 13 80 69 22 83  9 85 17 47 88
Card 162: 83 92 59 68 33 17 26 46 99 22 |  5 78 85 26 62 53 48 38 51 57 73 75 60 99 84 89 17 54 59 18 23  9 87 14 21
Card 163: 15 88 91 71 26 12 49 63 97 45 |  1 61 93 32 14 53 56 84 29 25 89 44 27 35 13 80 75 54 49 70 36 65 86 78 46
Card 164: 50 77 98 33  3 42 91 78 53 36 | 54 87 70  6 49 43  8 68 89 84  3 97 36 40 34 16 55 66 44 93 10 51 38 74 76
Card 165: 66 98 52 64 26 45 12 83 57 70 |  9 32 51 73 48 94 68 46 24 87 63 78 27 86 45 79 52 54 65 53 37 75 41 97 89
Card 166: 43  8 23 29 84 19 92 58 73 32 | 65 15 88 62 90  1 36 71 68 57 66 39 91 53 10 35 16 50 85 49 25 46 74 34 13
Card 167: 35 39 75 42 54 60 40 58 79 32 | 36 94 10  1 49 51 15 62 19 65  5 45 17 85 30 73 20 37 26 67 64 97 16 50 89
Card 168: 48 55 26 40 15 64 58 77  1 16 | 28 85 92 25 56 69 46 88 10 98 73 84 70 79 72 63 74 27 68 87 76 78 21 83 97
Card 169: 38 34 64 41 11 37 48 24 14 94 | 62 98 75 40 46 12 48 34 64 14 94 42 33 86 35 37 24 38 73 30 45 11  3  6 41
Card 170: 56 31 25 98 94 49  9 42 18  2 | 38 58 71 57 49 98  9 18 80 20 46 44 54 56 40 92 25 31  2 72 30 42  4 73 94
Card 171: 40 79 27 54 30 43 23  4 76 42 |  4 18 47 29 31 79 59  9 98 23 57 75 85 21  1 61 14 53 54 28 68 77 44 66 80
Card 172: 40 93 79 51 16 39  1 61 80 73 | 96 87 49 90 17 12  3 69 34 62  7 55 52 57 23 72 20 86 22 74 46 42  5  2  8
Card 173: 50 45 56 47 13 89 59 32 40 92 | 49 36  2 13 52 11 35 41 96 68 89 12 60 82 86 56 40 58 37 16 32 39 45 27 92
Card 174: 99 38 67 55 93 51 36 88 63 78 | 27 38 70 95 56 58 86 55 66 79 60 52 30 88 26 39 99 97 67 31 17 61 44 43 53
Card 175: 93  6 27 45 14 49 11  8 12 90 |  3 93 36 33 44 45 56 98 24 14 27 13 12 90 85 49  5 11 70 47 69 20 52  8  6
Card 176: 80 97 64 46 53 76 65 73 18 95 | 54 73 57  4 43 32 95 60 65 21 31 29 37 23 45 82 72 79 56 34 50 97 87  9 25
Card 177:  8  3 62 40 90 23 45 93 27 73 |  3 59  1 92 67 71 62 37  2 29 93 27 90 68 72 12 35 51 44 16 95 96 48 21  8
Card 178: 22 50 59 56 36  8 62 74 52 68 | 28 97 36 74 50 93 20 98 33 90 79 11 39 22 14 35 52 63 21 34 56 17 47 59  8
Card 179: 68 81 47  3 82 89 17 90 49  5 | 68  2  9 76 44 80 17 86 59 49 12  3 81 89  5 84 87 18 66 82 38 14 37 24 48
Card 180: 82 91 64 68 39 21 97  1 84 99 |  2  8 97 71 60 68 40 75 84 82 42  1  9  3 59 38 67 52 17 72 61 27 53 76 70
Card 181: 15 63 14 90 65 33 20  4 86 88 | 12 77 91 46 27  1 10 76 55 59 56  2 40 51  9 62 34 20 74 71 49 30 54  4 86
Card 182: 67 87 26 58 15 13 99  6 70 62 | 21 56 77 11 75 10  2 91 64 35 27  4  8 38 45 72 51  7 65 49 54 39 82 88 83
Card 183: 69 84 68 67 65 45 25  9 15 91 | 79 68 15 69 66 50 84 76 56 45 42 35 52 17 90 71  1 10  3  7 98 65  9 64 27
Card 184: 40 99  5 33 95 72 64 25  2 47 |  5 38 37 98  6 42 56  8 43 24 58 86 44 63 26 72 67 33 95  2 25 85 66 55 48
Card 185: 89 31 98 23 68 79 25  2 10 97 | 54 47 36  8 86 40 33 28 26 55 66 99 31 25  3 97 89 13 60 74 58 51 80 84 68
Card 186: 60 91 49 61 78 93 24 82 16  3 | 46 50 17 96 12 59 11 26 32 41 38 53 19 99 81 25 20 58 52 13 87 14 80 74 34
Card 187: 73 79  8 83 16 62  5 36 77 15 | 32 48 39 64 38 85 50 49 84 19 58  7 86 24 21 30 56 61 72 11 80 68 23 66 34
Card 188: 25 24  6 89 90 55 83 69 58 95 |  9 82 40 96 37  3 91 11 77  7 74 93 51 73  5 19 98 75 54 18 28 10 70 36 30
Card 189: 19 40 78 79 20 99 59 41 89 84 | 30 20 67 16 93 42 22 47 95 25 50 71 62 35 85 70 46 74  7 52 75 24 66 61 28
Card 190: 46 23 88 70 14 62 28 78 74 27 | 67 10 42  9 11  6 75 87 73 54 68 76 39 83 95 49 18  5 20 19 13 97 63 37 12
Card 191: 90 35 49 38 70 92 58 86  2 93 | 67 87 39  9 64 62 54 75 37  6 56 72 42 96 48 84 18 99 33 19  3 76 11 23 74
Card 192:  5  2 17 72 34 86 78 25 67 75 |  7 34 99 91 36  5 14 86 65 75 16 47 25 62 60 98 67  2 22 64 72 74 17 41 78
Card 193: 56 53 16 30 13 21 78  7 45 68 | 78  7 13 20  1 81 69 76 53 71 68 86 58 27 90 30 45 80 16 95 49 21 56 31  8
Card 194: 20 81 99 68 19 43 34 48 24 13 | 99 23 72 20 47 88 90 48 14 78 59 81 43 68 44 32 49 57 19 24 39 61 13 95 34
Card 195: 38 21  8 62 68 50 32 31 92 11 | 32 30 62 38  1 28 21 92 61 73 19 50 49 86 66 60 68 43 31 11 57 82  6 47  8
Card 196: 94 60 26 40 86 38 34 63 88 62 |  3 20 69 49 16 65  4 12 19  2 13 86  6 75 38 50 22 17 28 64 29 88 72 98 52
Card 197: 10 95 30 68 35 36 84 48 57 41 | 70 74 76 56 77 31 25 86 54 91 55  2 57 97 26 44 12 23 15 13 50 10 82 65 98
Card 198: 75 36 27 87 31 34 77 74 95 69 | 75 11 36 70 69 34 45 16 43 61 95 27 81 85 77 29 74 31 87  8 49 94 37 40  3
Card 199: 16 63 44 31 14 38 46 81 64 94 | 48 78 83 19 52 91 96 51 11  1 66 45 14 61  8 16  5 99 55 54 79  4 71 41 60
Card 200:  6 38 13  5 89 32 29 52 48 58 | 29  1 86 79 55 28 98 44 89  4 21 84  3 20 71 48 95 72 14 69 31 39  6 33 13
Card 201: 93 62 78 75 26 45 90 92  7  9 | 58 57 32 56 45 52 26 99 28 30 35  2 24 33  8 67 97 65 60 21 15 98 78 23 38
Card 202: 11 72 93 47 60 35 85 78 26 20 | 64 76  9 13 31  3  4 90 33 73 63 70 25 30 29 98  7 71 92 68 99 74 52 43 62
Card 203: 88  3  9 18 73 10 87 65 17 42 | 33 80 20 61 44 96  6 88 10 47 72 99 71 50 95 21 87 17 34 81 51  2 65 19 36
Card 204: 28  8 64 35 68 84 51  1 58 53 | 68 76 79 75 18 89 90 69 25 72 58 71 83 56 82 32 93 99 16 53 64  6 84 86 98
Card 205: 45 41 57  2 55 54 96 19 46 89 | 13 64 57 20 72 27 21 81 40 75 22 61 46 99 68 89 82 42 67 55 70 39 78 88 15
Card 206: 42 38 95 66 18 93 79 45 49 37 | 80 61 43 70 31 17 13 16 49 73 20 44 90  5 39 97 82 15 68 14 57 21 72 35 79
Card 207: 91 28 69 89 54  6 60 19 44 77 | 27 94 51 47 46 84 99 31 16 58 92 80 67 95 73  5 12 88 40 18 41 72 24 93 39
Card 208:  9 37 78 74 26 99 76 48 16 54 | 98 46 20 92 83 52  1 44 84 41 61 66 74 70 69 71 18 68 77 24 49 31  6 25 50
Card 209:  2 10 11 47 25 81 75 61 27  4 | 79 45 43 29 55 16 91 68 88 52 90 21 13 37 59 31  5  1 14 17 86 84 64 60 70
"""

test_input = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

# sum = 0
# for idx, line in enumerate(input.splitlines()):
#     if len(line) == 0:
#         continue
#     winning_numbers =[]
#     my_numbers = []
#     line = line[line.find(':') + 1:]
#     numbers = line.split("|")
#     winning = numbers[0].strip(" ").split(" ")
#     winning = [p for p in winning if p != '']
#     # winning = filter(lambda x: x != '', winning)
#     # print(winning)
#     # winning = map(int, winning)
#     winning = [int(x) for x in winning]
#     yours = numbers[1].strip(" ").split(" ")
#     # yours = filter(lambda x: x != '', yours)
#     yours = [p for p in yours if p != '']
#     yours = [int(x) for x in yours]
#     # print(yours)
#     current_winning_sum = 0
#     for your in yours:
#         if your in winning:
#             # print(your)
#             if current_winning_sum == 0:
#                 current_winning_sum = 1
#             else:
#                 current_winning_sum = current_winning_sum * 2
#
#     # print(line)
#     # print(current_winning_sum)
#     sum = sum + current_winning_sum
#
#     
# print(sum)

sum = [1]*(len(input.splitlines())-1)
print(sum)
lines = input.splitlines()
for idx, line in enumerate(lines):
    print(line)
    if len(line) == 0:
        continue
    winning_numbers =[]
    my_numbers = []
    line = line[line.find(':') + 1:]
    numbers = line.split("|")
    winning = numbers[0].strip(" ").split(" ")
    winning = [p for p in winning if p != '']
    # winning = filter(lambda x: x != '', winning)
    # print(winning)
    # winning = map(int, winning)
    winning = [int(x) for x in winning]
    yours = numbers[1].strip(" ").split(" ")
    # yours = filter(lambda x: x != '', yours)
    yours = [p for p in yours if p != '']
    yours = [int(x) for x in yours]
    # print(yours)
    current_winning_sum = 0
    for your in yours:
        if your in winning:
            current_winning_sum += 1

    # print(line)
    print(f"idx {idx} sum {current_winning_sum}")

    for i in range(current_winning_sum):
        print(i+idx)
        sum[i+idx] += sum[idx-1]
    print(sum)

result = 0
for val in sum:
    result += val
print("result")
print(result)

