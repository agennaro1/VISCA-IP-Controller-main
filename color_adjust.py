
'''

R.GAIN Reset 8x 01 04 03 00 FF         To return to 80 (0) value
Up 8x 01 04 03 02 FF
Down 8x 01 04 03 03 FF
Direct 8x 01 04 43 00 00 0p 0p FF      pp: 00 (–128) - 80 (0) - FF (128)


B.GAIN Reset 8x 01 04 04 00 FF         To return to 80 (0) value
Up 8x 01 04 04 02 FF
Down 8x 01 04 04 03 FF
Direct 8x 01 04 44 00 00 0p 0p FF      pp: 00 (–128) - 80 (0) - FF (128)


PHASE Reset 8x 01 04 0F 00 FF          To return to 7 (0) value
Up 8x 01 04 0F 02 FF
Down 8x 01 04 0F 03 FF
Direct 8x 01 04 4F 00 00 00 0p FF      p: 0 (–7 degrees) - E (+7 degrees)


R-G Direct 8x 01 7E 01 7A 0p 0p FF      pp: 00 (–99) - 63 (00) - C6 (+99)
R-B Direct 8x 01 7E 01 7B 0p 0p FF      pp: 00 (–99) - 63 (00) - C6 (+99)
G-R Direct 8x 01 7E 01 7C 0p 0p FF      pp: 00 (–99) - 63 (00) - C6 (+99)
G-B Direct 8x 01 7E 01 7D 0p 0p FF      pp: 00 (–99) - 63 (00) - C6 (+99)
B-R Direct 8x 01 7E 01 7E 0p 0p FF      pp: 00 (–99) - 63 (00) - C6 (+99)
B-G Direct 81 01 7E 01 7F 0p 0p FF      pp: 00 (–99) - 63 (00) - C6 (+99)

'''



