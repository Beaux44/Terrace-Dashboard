import os

pepper_map = {(1, 1): 0, (1, 2): 1, (1, 3): 2, (1, 4): 3, (1, 5): 4, (1, 6): 5, (1, 7): 6, (1, 8): 7, (1, 9): 8, (1, 10): 9, (1, 11): 10, (1, 12): 11, (1, 13): 12, (1, 14): 13, (1, 15): 14, (1, 16): 15, (1, 17): 16, (1, 18): 17, (1, 19): 18, (1, 20): 19, (1, 21): 20, (1, 22): 21, (1, 23): 22, (1, 24): 23, (1, 25): 24, (1, 26): 25, (1, 27): 26, (1, 28): 27, (1, 29): 28, (1, 30): 29, (1, 31): 30, (2, 1): 31, (2, 2): 32, (2, 3): 33, (2, 4): 34, (2, 5): 35, (2, 6): 36, (2, 7): 37, (2, 8): 38, (2, 9): 39, (2, 10): 40, (2, 11): 41, (2, 12): 42, (2, 13): 43, (2, 14): 44, (2, 15): 45, (2, 16): 46, (2, 17): 47, (2, 18): 48, (2, 19): 49, (2, 20): 50, (2, 21): 51, (2, 22): 52, (2, 23): 53, (2, 24): 54, (2, 25): 55, (2, 26): 56, (2, 27): 57, (2, 28): 58, (3, 1): 59, (3, 2): 60, (3, 3): 61, (3, 4): 62, (3, 5): 63, (3, 6): 64, (3, 7): 65, (3, 8): 66, (3, 9): 67, (3, 10): 68, (3, 11): 69, (3, 12): 70, (3, 13): 71, (3, 14): 72, (3, 15): 73, (3, 16): 74, (3, 17): 75, (3, 18): 76, (3, 19): 77, (3, 20): 78, (3, 21): 79, (3, 22): 80, (3, 23): 81, (3, 24): 82, (3, 25): 83, (3, 26): 84, (3, 27): 85, (3, 28): 86, (3, 29): 87, (3, 30): 88, (3, 31): 89, (4, 1): 90, (4, 2): 91, (4, 3): 92, (4, 4): 93, (4, 5): 94, (4, 6): 95, (4, 7): 96, (4, 8): 97, (4, 9): 98, (4, 10): 99, (4, 11): 100, (4, 12): 101, (4, 13): 102, (4, 14): 103, (4, 15): 104, (4, 16): 105, (4, 17): 106, (4, 18): 107, (4, 19): 108, (4, 20): 109, (4, 21): 110, (4, 22): 111, (4, 23): 112, (4, 24): 113, (4, 25): 114, (4, 26): 115, (4, 27): 116, (4, 28): 117, (4, 29): 118, (4, 30): 119, (5, 1): 120, (5, 2): 121, (5, 3): 122, (5, 4): 123, (5, 5): 124, (5, 6): 125, (5, 7): 126, (5, 8): 127, (5, 9): 128, (5, 10): 129, (5, 11): 130, (5, 12): 131, (5, 13): 132, (5, 14): 133, (5, 15): 134, (5, 16): 135, (5, 17): 136, (5, 18): 137, (5, 19): 138, (5, 20): 139, (5, 21): 140, (5, 22): 141, (5, 23): 142, (5, 24): 143, (5, 25): 144, (5, 26): 145, (5, 27): 146, (5, 28): 147, (5, 29): 148, (5, 30): 149, (5, 31): 150, (6, 1): 151, (6, 2): 152, (6, 3): 153, (6, 4): 154, (6, 5): 155, (6, 6): 156, (6, 7): 157, (6, 8): 158, (6, 9): 159, (6, 10): 160, (6, 11): 161, (6, 12): 162, (6, 13): 163, (6, 14): 164, (6, 15): 165, (6, 16): 166, (6, 17): 167, (6, 18): 168, (6, 19): 169, (6, 20): 170, (6, 21): 171, (6, 22): 172, (6, 23): 173, (6, 24): 174, (6, 25): 175, (6, 26): 176, (6, 27): 177, (6, 28): 178, (6, 29): 179, (6, 30): 180, (7, 1): 181, (7, 2): 182, (7, 3): 183, (7, 4): 184, (7, 5): 185, (7, 6): 186, (7, 7): 187, (7, 8): 188, (7, 9): 189, (7, 10): 190, (7, 11): 191, (7, 12): 192, (7, 13): 193, (7, 14): 194, (7, 15): 195, (7, 16): 196, (7, 17): 197, (7, 18): 198, (7, 19): 199, (7, 20): 200, (7, 21): 201, (7, 22): 202, (7, 23): 203, (7, 24): 204, (7, 25): 205, (7, 26): 206, (7, 27): 207, (7, 28): 208, (7, 29): 209, (7, 30): 210, (7, 31): 211, (8, 1): 212, (8, 2): 213, (8, 3): 214, (8, 4): 215, (8, 5): 216, (8, 6): 217, (8, 7): 218, (8, 8): 219, (8, 9): 220, (8, 10): 221, (8, 11): 222, (8, 12): 223, (8, 13): 224, (8, 14): 225, (8, 15): 226, (8, 16): 227, (8, 17): 228, (8, 18): 229, (8, 19): 230, (8, 20): 231, (8, 21): 232, (8, 22): 233, (8, 23): 234, (8, 24): 235, (8, 25): 236, (8, 26): 237, (8, 27): 238, (8, 28): 239, (8, 29): 240, (8, 30): 241, (8, 31): 242, (9, 1): 243, (9, 2): 244, (9, 3): 245, (9, 4): 246, (9, 5): 247, (9, 6): 248, (9, 7): 249, (9, 8): 250, (9, 9): 251, (9, 10): 252, (9, 11): 253, (9, 12): 254, (9, 13): 255, (9, 14): 256, (9, 15): 257, (9, 16): 258, (9, 17): 259, (9, 18): 260, (9, 19): 261, (9, 20): 262, (9, 21): 263, (9, 22): 264, (9, 23): 265, (9, 24): 266, (9, 25): 267, (9, 26): 268, (9, 27): 269, (9, 28): 270, (9, 29): 271, (9, 30): 272, (10, 1): 273, (10, 2): 274, (10, 3): 275, (10, 4): 276, (10, 5): 277, (10, 6): 278, (10, 7): 279, (10, 8): 280, (10, 9): 281, (10, 10): 282, (10, 11): 283, (10, 12): 284, (10, 13): 285, (10, 14): 286, (10, 15): 287, (10, 16): 288, (10, 17): 289, (10, 18): 290, (10, 19): 291, (10, 20): 292, (10, 21): 293, (10, 22): 294, (10, 23): 295, (10, 24): 296, (10, 25): 297, (10, 26): 298, (10, 27): 299, (10, 28): 300, (10, 29): 301, (10, 30): 302, (10, 31): 303, (11, 1): 304, (11, 2): 305, (11, 3): 306, (11, 4): 307, (11, 5): 308, (11, 6): 309, (11, 7): 310, (11, 8): 311, (11, 9): 312, (11, 10): 313, (11, 11): 314, (11, 12): 315, (11, 13): 316, (11, 14): 317, (11, 15): 318, (11, 16): 319, (11, 17): 320, (11, 18): 321, (11, 19): 322, (11, 20): 323, (11, 21): 324, (11, 22): 325, (11, 23): 326, (11, 24): 327, (11, 25): 328, (11, 26): 329, (11, 27): 330, (11, 28): 331, (11, 29): 332, (11, 30): 333, (12, 1): 334, (12, 2): 335, (12, 3): 336, (12, 4): 337, (12, 5): 338, (12, 6): 339, (12, 7): 340, (12, 8): 341, (12, 9): 342, (12, 10): 343, (12, 11): 344, (12, 12): 345, (12, 13): 346, (12, 14): 347, (12, 15): 348, (12, 16): 349, (12, 17): 350, (12, 18): 351, (12, 19): 352, (12, 20): 353, (12, 21): 354, (12, 22): 355, (12, 23): 356, (12, 24): 357, (12, 25): 358, (12, 26): 359, (12, 27): 360, (12, 28): 361, (12, 29): 362, (12, 30): 363, (12, 31): 364, (2, 29): 364}
with open('pepper.txt', "wb") as f:
	for number in range(366):
		f.write(os.urandom(14))


def generate_peppers():
	with open("pepper.txt", "rb") as f:
		peppers = f.read()
		n = 14
	return [(peppers[i:i + n]) for i in range(0, len(peppers), n)]


peppers = generate_peppers()