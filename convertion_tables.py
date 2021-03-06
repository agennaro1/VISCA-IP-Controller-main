from adjust_commands import KNEE_MODE


conversion_table = dict()
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',  8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


iris_table = dict()
iris_table = { 
    0: '00 05',
    1: '00 06',
    2: '00 07', 
    3: '00 08',
    4: '00 09',
    5: '00 0A',
    6: '00 0B',
    7: '00 0C',
    8: '00 0D',
    9: '00 0E',
    10: '00 0F',
    11: '01 00',
    12: '01 01',
    13: '01 02',
    14: '01 03',
    15: '01 04',
    16: '01 05'    
    }

iris_Focal = dict()
iris_Focal = {
    0: 'F2.8',	
    1: 'F3.1',	
    2: 'F3.4',
    3: 'F3.7',
    4: 'F4.0',
    5: 'F4.4',
    6: 'F4.8',
    7: 'F5.2',
    8: 'F5.6',
    9: 'F6.2',
    10: 'F6.8',
    11: 'F7.3',
    12: 'F8.0',
    13: 'F8.7',
    14: 'F9.6',
    15: 'F10',
    16: 'F11'
    }

gain_table = dict()
gain_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',  8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C'}

gain_lbl = dict()
gain_lbl = {0: '–3dB', 1: '0dB', 2: '3dB', 3: '6dB', 4: '9dB', 5: '12dB', 6: '15dB', 7: '18dB',  8: '21dB', 9: '24dB', 10: '27dB', 11: '30dB', 12: '33dB'}

shutter_table = dict()
shutter_table = {
    0: '00 00',
    1: '00 01',
    2: '00 02',
    3: '00 03',
    4: '00 04',
    5: '00 05',
    6: '00 06',
    7: '00 07',
    8: '00 08',
    9: '00 09',
    10: '00 0A',
    11: '00 0B',
    12: '00 0C',
    13: '00 0D',
    14: '00 0E',
    15: '00 0F',
    16: '01 00',
    17: '01 01',
    18: '01 02',
    19: '01 03',
    20: '01 04',
    21: '01 05', 
}

shutter_lbl = dict()
shutter_lbl = {
    0: '1/1s - 1/1s',
    1: '1/2s - 1/2s',
    2: '1/3s - 1/4s',
    3: '1/6s - 1/8s',
    4: '1/12s - 1/15s', 
    5: '1/25s - 1/30s',
    6: '1/50s - 1/60s',
    7: '1/75s - 1/90s',
    8: '1/100s - 1/100s',
    9: '1/120s - 1/125s',
    10: '1/150s - 1/180s',
    11: '1/215s - 1/250s',
    12: '1/300s - 1/350s',
    13: '1/425s - 1/500s',
    14: '1/600s - 1/725s',
    15: '1/1000s - 1/1000s',
    16: '1/1250s - 1/1500s',
    17: '1/1750s - 1/2000s',
    18: '1/2500s - 1/3000s',
    19: '1/3500s - 1/4000s',
    20: '1/6000s - 1/6000s',
    21: '1/10000s - 1/10000s',
}


black_table = dict()
black_table = { -48: '00 00', -47: '00 01', -46: '00 02', -45: '00 03', -44: '00 04', -43: '00 05', -42: '00 06', -41: '00 07', -40: '00 08', -39: '00 09', -38: '00 0A', -37: '00 0B', -36: '00 0C', -35: '00 0D', -34: '00 0E', -33: '00 0F', 
                -32: '01 00', -31: '01 01', -30: '01 02', -29: '01 03', -28: '01 04', -27: '01 05', -26: '01 06', -25: '01 07', -24: '01 08', -23: '01 09', -22: '01 0A', -21: '01 0B', -20: '01 0C', -19: '01 0D', -18: '01 0E', -17: '01 0F', 
                -16: '02 00', -15: '02 01', -14: '02 02', -13: '02 03', -12: '02 04', -11: '02 05', -10: '02 06', -9: '02 07', -8: '02 08', -7: '02 09', -6: '02 0A', -5: '02 0B', -4: '02 0C', -3: '02 0D', -2: '02 0E', -1: '02 0F', 
                 0: '03 00', 1: '03 01', 2: '03 02', 3: '03 03', 4: '03 04', 5: '03 05', 6: '03 06', 7: '03 07', 8: '03 08', 9: '03 09', 10: '03 0A', 11: '03 0B', 12: '03 0C', 13: '03 0D', 14: '03 0E', 15: '03 0F', 
                 16: '04 00', 17: '04 01', 18: '04 02', 19: '04 03', 20: '04 04', 21: '04 05', 22: '04 06', 23: '04 07', 24: '04 08', 25: '04 09', 26: '04 0A', 27: '04 0B', 28: '04 0C', 29: '04 0D', 30: '04 0E', 31: '04 0F',
                32: '05 00', 33: '05 01', 34: '05 02', 35: '05 03', 36: '05 04', 37: '05 05', 38: '05 06', 39: '05 07', 40: '05 08', 41: '05 09', 42: '05 0A', 43: '05 0B', 44: '05 0C', 45: '05 0D', 46: '05 0E', 47: '05 0F', 48: '06 00'

                }






cg_table = dict()
cg_table = {
    0: '00 00', 1: '00 01', 2: '00 02', 3: '00 03', 4: '00 04', 5: '00 05', 6: '00 06', 7: '00 07', 8: '00 08', 9: '00 09', 10: '00 0A', 11: '00 0B', 12: '00 0C', 13: '00 0D', 14: '00 0E', 15: '00 0F',
    16: '01 00', 17: '01 01', 18: '01 02', 19: '01 03', 20: '01 04', 21: '01 05', 22: '01 06', 23: '01 07', 24: '01 08', 25: '01 09', 26: '01 0A', 27: '01 0B', 28: '01 0C', 29: '01 0D', 30: '01 0E', 31: '01 0F',
    32: '02 00', 33: '02 01', 34: '02 02', 35: '02 03', 36: '02 04', 37: '02 05', 38: '02 06', 39: '02 07', 40: '02 08', 41: '02 09', 42: '02 0A', 43: '02 0B', 44: '02 0C', 45: '02 0D', 46: '02 0E', 47: '02 0F',
    48: '03 00', 49: '03 01', 50: '03 02', 51: '03 03', 52: '03 04', 53: '03 05', 54: '03 06', 55: '03 07', 56: '03 08', 57: '03 09', 58: '03 0A', 59: '03 0B', 60: '03 0C', 61: '03 0D', 62: '03 0E', 63: '03 0F',
    64: '04 00', 65: '04 01', 66: '04 02', 67: '04 03', 68: '04 04', 69: '04 05', 70: '04 06', 71: '04 07', 72: '04 08', 73: '04 09', 74: '04 0A', 75: '04 0B', 76: '04 0C', 77: '04 0D', 78: '04 0E', 79: '04 0F',
    80: '05 00', 81: '05 01', 82: '05 02', 83: '05 03', 84: '05 04', 85: '05 05', 86: '05 06', 87: '05 07', 88: '05 08', 89: '05 09', 90: '05 0A', 91: '05 0B', 92: '05 0C', 93: '05 0D', 94: '05 0E', 95: '05 0F',
    96: '06 00', 97: '06 01', 98: '06 02', 99: '06 03', 100: '06 04', 101: '06 05', 102: '06 06', 103: '06 07', 104: '06 08', 105: '06 09', 106: '06 0A', 107: '06 0B', 108: '06 0C', 109: '06 0D', 110: '06 0E', 111: '06 0F',
    112: '07 00', 113: '07 01', 114: '07 02', 115: '07 03', 116: '07 04', 117: '07 05', 118: '07 06', 119: '07 07', 120: '07 08', 121: '07 09', 122: '07 0A', 123: '07 0B', 124: '07 0C', 125: '07 0D', 126: '07 0E', 127: '07 0F',
    128: '08 00', 129: '08 01', 130: '08 02', 131: '08 03', 132: '08 04', 133: '08 05', 134: '08 06', 135: '08 07', 136: '08 08', 137: '08 09', 138: '08 0A', 139: '08 0B', 140: '08 0C', 141: '08 0D', 142: '08 0E', 143: '08 0F',
    144: '09 00', 145: '09 01', 146: '09 02', 147: '09 03', 148: '09 04', 149: '09 05', 150: '09 06', 151: '09 07', 152: '09 08', 153: '09 09', 154: '09 0A', 155: '09 0B', 156: '09 0C', 157: '09 0D', 158: '09 0E', 159: '09 0F',
    160: '0A 00', 161: '0A 01', 162: '0A 02', 163: '0A 03', 164: '0A 04', 165: '0A 05', 166: '0A 06', 167: '0A 07', 168: '0A 08', 169: '0A 09', 170: '0A 0A', 171: '0A 0B', 172: '0A 0C', 173: '0A 0D', 174: '0A 0E', 175: '0A 0F',
    176: '0B 00', 177: '0B 01', 178: '0B 02', 179: '0B 03', 180: '0B 04', 181: '0B 05', 182: '0B 06', 183: '0B 07', 184: '0B 08', 185: '0B 09', 186: '0B 0A', 187: '0B 0B', 188: '0B 0C', 189: '0B 0D', 190: '0B 0E', 191: '0B 0F',
    192: '0C 00', 193: '0C 01', 194: '0C 02', 195: '0C 03', 196: '0C 04', 197: '0C 05', 198: '0C 06', 199: '0C 07', 200: '0C 08', 201: '0C 09', 202: '0C 0A', 203: '0C 0B', 204: '0C 0C', 205: '0C 0D', 206: '0C 0E', 207: '0C 0F',
    208: '0D 00', 209: '0D 01', 210: '0D 02', 211: '0D 03', 212: '0D 04', 213: '0D 05', 214: '0D 06', 215: '0D 07', 216: '0D 08', 217: '0D 09', 218: '0D 0A', 219: '0D 0B', 220: '0D 0C', 221: '0D 0D', 222: '0D 0E', 223: '0D 0F',
    224: '0E 00', 225: '0E 01', 226: '0E 02', 227: '0E 03', 228: '0E 04', 229: '0E 05', 230: '0E 06', 231: '0E 07', 232: '0E 08', 233: '0E 09', 234: '0E 0A', 235: '0E 0B', 236: '0E 0C', 237: '0E 0D', 238: '0E 0E', 239: '0E 0F',
    240: '0F 00', 241: '0F 01', 242: '0F 02', 243: '0F 03', 244: '0F 04', 245: '0F 05', 246: '0F 06', 247: '0F 07', 248: '0F 08', 249: '0F 09', 250: '0F 0A', 251: '0F 0B', 252: '0F 0C', 253: '0F 0D', 254: '0F 0E', 255: '0F 0F',
}

cg_lbl = dict()
cg_lbl = {

    0: ' 1-128', 1: '-127', 2: '-126', 3: '-125', 4: '-124', 5: '-123', 6: '-122', 7: '-121', 8: '-120', 9: '-119', 10: '-118', 11: '-117', 12: '-116', 13: '-115', 14: '-114', 15: '-113',
    16: '-112', 17: '-111', 18: '-110', 19: '-109', 20: '-108', 21: '-107', 22: '-106', 23: '-105', 24: '-104', 25: '-103', 26: '-102', 27: '-101', 28: '-100', 29: '-99', 30: '-98', 31: '-97',
    32: '-96', 33: '-95', 34: '-94', 35: '-93', 36: '-92', 37: '-91', 38: '-90', 39: '-89', 40: '-88', 41: '-87', 42: '-86', 43: '-85', 44: '-84', 45: '-83', 46: '-82', 47: '-81',
    48: '-80', 49: '-79', 50: '-78', 51: '-77', 52: '-76', 53: '-75', 54: '-74', 55: '-73', 56: '-72', 57: '-71', 58: '-70', 59: '-69', 60: '-68', 61: '-67', 62: '-66', 63: '-65',
    64: '-64', 65: '-63', 66: '-62', 67: '-61', 68: '-60', 69: '-59', 70: '-58', 71: '-57', 72: '-56', 73: '-55', 74: '-54', 75: '-53', 76: '-52', 77: '-51', 78: '-50', 79: '-49',
    80: '-48', 81: '-47', 82: '-46', 83: '-45', 84: '-44', 85: '-43', 86: '-42', 87: '-41', 88: '-40', 89: '-39', 90: '-38', 91: '-37', 92: '-36', 93: '-35', 94: '-34', 95: '-33',
    96: '-32', 97: '-31', 98: '-30', 99: '-29', 100: '-28', 101: '-27', 102: '-26', 103: '-25', 104: '-24', 105: '-23', 106: '-22', 107: '-21', 108: '-20', 109: '-19', 110: '-18', 111: '-17',
    112: '-16', 113: '-15', 114: '-14', 115: '-13', 116: '-12', 117: '-11', 118: '-10', 119: '-9', 120: '-8', 121: '-7', 122: '-6', 123: '-5', 124: '-4', 125: '-3', 126: '-2', 127: '-1',
    128: '0', 129: '1', 130: '2', 131: '3', 132: '4', 133: '5', 134: '6', 135: '7', 136: '8', 137: '9', 138: '10', 139: '11', 140: '12', 141: '13', 142: '14', 143: '15',
    144: '16', 145: '17', 146: '18', 147: '19', 148: '20', 149: '21', 150: '22', 151: '23', 152: '24', 153: '25', 154: '26', 155: '27', 156: '28', 157: '29', 158: '30', 159: '31',
    160: '32', 161: '33', 162: '34', 163: '35', 164: '36', 165: '37', 166: '38', 167: '39', 168: '40', 169: '41', 170: '42', 171: '43', 172: '44', 173: '45', 174: '46', 175: '47',
    176: '48', 177: '49', 178: '50', 179: '51', 180: '52', 181: '53', 182: '54', 183: '55', 184: '56', 185: '57', 186: '58', 187: '59', 188: '60', 189: '61', 190: '62', 191: '63',
    192: '64', 193: '65', 194: '66', 195: '67', 196: '68', 197: '69', 198: '70', 199: '71', 200: '72', 201: '73', 202: '74', 203: '75', 204: '76', 205: '77', 206: '78', 207: '79',
    208: '80', 209: '81', 210: '82', 211: '83', 212: '84', 213: '85', 214: '86', 215: '87', 216: '88', 217: '89', 218: '90', 219: '91', 220: '92', 221: '93', 222: '94', 223: '95',
    224: '96', 225: '97', 226: '98', 227: '99', 228: '100', 229: '101', 230: '102', 231: '103', 232: '104', 233: '105', 234: '106', 235: '107', 236: '108', 237: '109', 238: '110', 239: '111',
    240: '112', 241: '113', 242: '114', 243: '115', 244: '116', 245: '117', 246: '118', 247: '119', 248: '120', 249: '121', 250: '122', 251: '123', 252: '124', 253: '125', 254: '126', 255: '127',
} 


HUE_lbl = dict()
HUE_lbl = { 0: '–7 degrees', 1: '–6 degrees', 2: '–5 degrees', 3: '–4 degrees', 4: '–3 degrees', 5: '–2 degrees', 6: '–1 degrees', 7: '0 degrees', 8: '1 degrees', 9: '2 degrees', 10: '3 degrees', 11: '4 degrees', 12: '5 degrees', 13: '6 degrees', 14: '7 degrees' }

HUE_table = dict()
HUE_table = { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',  8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E' }

COLOR_table = dict()
COLOR_table = { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',  8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E' }

MATRIX_table = dict()
MATRIX_table = { 
    -99: '00 00', -98: '00 01', -97: '00 02', -96: '00 03', -95: '00 04', -94: '00 05', -93: '00 06', -92: '00 07', -91: '00 08', -90: '00 09', -89: '00 0A', -88: '00 0B', -87: '00 0C', -86: '00 0D', -85: '00 0E', -84: '00 0F', 
    -83: '01 00', -82: '01 01', -81: '01 02', -80: '01 03', -79: '01 04', -78: '01 05', -77: '01 06', -76: '01 07', -75: '01 08', -74: '01 09', -73: '01 0A', -72: '01 0B', -71: '01 0C', -70: '01 0D', -69: '01 0E', -68: '01 0F', 
    -67: '02 00', -66: '02 01', -65: '02 02', -64: '02 03', -63: '02 04', -62: '02 05', -61: '02 06', -60: '02 07', -59: '02 08', -58: '02 09', -57: '02 0A', -56: '02 0B', -55: '02 0C', -54: '02 0D', -53: '02 0E', -52: '02 0F',
    -51: '03 00', -50: '03 01', -49: '03 02', -48: '03 03', -47: '03 04', -46: '03 05', -45: '03 06', -44: '03 07', -43: '03 08', -42: '03 09', -41: '03 0A', -40: '03 0B', -39: '03 0C', -38: '03 0D', -37: '03 0E', -36: '03 0F',
    -35: '04 00', -34: '04 01', -33: '04 02', -32: '04 03', -31: '04 04', -30: '04 05', -29: '04 06', -28: '04 07', -27: '04 08', -26: '04 09', -25: '04 0A', -24: '04 0B', -23: '04 0C', -22: '04 0D', -21: '04 0E', -20: '04 0F',
    -19: '05 00', -18: '05 01', -17: '05 02', -16: '05 03', -15: '05 04', -14: '05 05', -13: '05 06', -12: '05 07', -11: '05 08', -10: '05 09', -9: '05 0A', -8: '05 0B', -7: '05 0C', -6: '05 0D', -5: '05 0E', -4: '05 0F',
    -3: '06 00', -2: '06 01', -1: '06 02', 0: '06 03', 1: '06 04', 2: '06 05', 3: '06 06', 4: '06 07', 5: '06 08', 6: '06 09', 7: '06 0A', 8: '06 0B', 9: '06 0C', 10: '06 0D', 11: '06 0E', 12: '06 0F',
    13: '07 00', 14: '07 01', 15: '07 02', 16: '07 03', 17: '07 04', 18: '07 05', 19: '07 06', 20: '07 07', 21: '07 08', 22: '07 09', 23: '07 0A', 24: '07 0B', 25: '07 0C', 26: '07 0D', 27: '07 0E', 28: '07 0F',
    29: '08 00', 30: '08 01', 31: '08 02', 32: '08 03', 33: '08 04', 34: '08 05', 35: '08 06', 36: '08 07', 37: '08 08', 38: '08 09', 39: '08 0A', 40: '08 0B', 41: '08 0C', 42: '08 0D', 43: '08 0E', 44: '08 0F',
    45: '09 00', 46: '09 01', 47: '09 02', 48: '09 03', 49: '09 04', 50: '09 05', 51: '09 06', 52: '09 07', 53: '09 08', 54: '09 09', 55: '09 0A', 56: '09 0B', 57: '09 0C', 58: '09 0D', 59: '09 0E', 60: '09 0F',
    61: '0A 00', 62: '0A 01', 63: '0A 02', 64: '0A 03', 65: '0A 04', 66: '0A 05', 67: '0A 06', 68: '0A 07', 69: '0A 08', 70: '0A 09', 71: '0A 0A', 72: '0A 0B', 73: '0A 0C', 74: '0A 0D', 75: '0A 0E', 76: '0A 0F',
    77: '0B 00', 78: '0B 01', 79: '0B 02', 80: '0B 03', 81: '0B 04', 82: '0B 05', 83: '0B 06', 84: '0B 07', 85: '0B 08', 86: '0B 09', 87: '0B 0A', 88: '0B 0B', 89: '0B 0C', 90: '0B 0D', 91: '0B 0E', 92: '0B 0F',
    93: '0C 00', 94: '0C 01', 95: '0C 02', 96: '0C 03', 97: '0C 04', 98: '0C 05', 99: '0C 06'

}



DETAIL_LEVEL_lbl = dict()
DETAIL_LEVEL_lbl = { 0: '–7 ', 1: '–6 ', 2: '–5 ', 3: '–4 ', 4: '–3 ', 5: '–2 ', 6: '–1 ', 7: '0 ', 8: '1 ', 9: '2 ', 10: '3 ', 11: '4 ', 12: '5 ', 13: '6 ', 14: '7 ' , 15 : '8'}

DETAIL_LEVEL_table = dict()
DETAIL_LEVEL_table = { -7: '0', -6: '1', -5: '2', -4: '3', -3: '4', -2: '5', -1: '6', 0: '7', 1: '8', 2: '9', 3: 'A', 4: 'B', 5: 'C', 6: 'D', 7: 'E', 8: 'F'}


DETAIL_BANDWIDTH_lbl = dict()
DETAIL_BANDWIDTH_lbl = { 0: 'DEFAULT',  1: 'LOW', 2: 'MEDIUM', 3: 'HIGH', 4: 'WIDE'}

DETAIL_BANDWIDTH_table = dict()
DETAIL_BANDWIDTH_table = { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

DETAIL_H_V_BALANCE_lbl = dict()
DETAIL_H_V_BALANCE_lvl =  { 5: '-2' , 6: '-1' , 7: '0' , 8: '+1' , 9: '+2' }

DETAIL_B_W_BALANCE_lbl = dict()
DETAIL_B_W_BALANCE_lvl =  { 0: 'TYPE1' , 1: 'TYPE2' , 2: 'TYPE3' , 3: 'TYPE4' , 4: 'TYPE5' }

