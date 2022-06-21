#Command Set Command Command Packet Comments




# --------------------- EXPOSURE  ---------------------

MENU_ON = '81 01 06 06 02 FF'  # p: 2=On, 3=Off, 10=Toggle
MENU_OFF = '81 01 06 06 03 FF'  # p: 2=On, 3=Off, 10=Toggle
MENU_TOGGLE = '81 01 06 06 10 FF'  # p: 2=On, 3=Off, 10=Toggle


'''
MODE (modo de exposición)
FULL AUTO: La exposición se ajusta automáticamente mediante la sensibilidad, la velocidad del obturador electrónico y el ajuste de la apertura.
MANUAL: La sensibilidad, la velocidad del obturador electrónico y la apertura se ajustan manualmente.
SHUTTER Pri: Puede ajustar la velocidad del obturador electrónico de forma manual. Ajusta la exposición de forma automática mediante la ganancia y la apertura.
IRIS Pri: Puede ajustar la apertura de forma manual. Ajusta la exposición de forma automática mediante la ganancia y la velocidad del obturador electrónico.
GAIN Pri: Puede ajustar la sensibilidad de forma manual. Ajusta la exposición de forma automática mediante la velocidad


'''

#MODE 
Full_Auto = '81 01 04 39 00 FF'  # '
Manual= '81 01 04 39 03 FF'  # '
Shutter_Priority =  ' 81 01 04 39 0A FF'  # Shutter Priority
Iris_Priority =  ' 81 01 04 39 0B FF'  # Iris Priority
Gain_Priority =  ' 81 01 04 39 0E FF'  # Gain Priority

'''
IRIS: Cuando EXPOSURE MODE es MANUAL o IRIS Pri, se puede elegir el ajuste de apertura.
Puede elegir entre F2.8/F3.1/F3.4/F3.7/F4.0/F4.4/F4.8/F5.2/F5.6/F6.2/F6.8/F7.3/F8.0/F8.7/ F9.6/F10/F11.
'''
#IRIS_
IRIS_Reset =  ' 81 01 04 0B 00 FF'  # To return to 15 (F2.8) value
IRIS_Up  =  ' 81 01 04 0B 02 FF'  #
IRIS_Down =  ' 81 01 04 0B 03 FF'  #
#IRIS_Direct =  ' 81 01 04 4B 00 00 0p 0p FF'  # pp: Iris Position 05 - 15
IRIS_Direct =  ' 81 01 04 4B 00 00 pp qq FF'  # pp: Iris Position 05 - 15


'''
GAIN: Seleccione la ganancia.
Si EXPOSURE MODE está ajustado en MANUAL o GAIN Pri, puede seleccionar un valor de –3 a 33 dB en incrementos de 3 dB.
GAIN –3dB, 0dB, 3dB, 6dB, 9dB, 12dB, 15dB, 18dB, 21dB, 24dB, 27dB, 30dB, 33dB
'''

#GAIN_
GAIN_Reset =  ' 81 01 04 0C 00 FF'  # To return to 01 (0 dB) value
GAIN_Up =  ' 81 01 04 0C 02 FF'  #
GAIN_Down =  ' 81 01 04 0C 03 FF'  #
GAIN_Direct =  ' 81 01 04 4C 00 00 00 0p FF'  # p: 0 (–3 dB) - C (33 dB)

GAIN_LIMIT_Direct =  ' 81 01 04 2C 0p FF'  # p: 4 (9 dB) - 9 (24 dB), F (OFF'  #)
GAIN_POINT_On_OFF =  ' 81 01 05 0C 0p FF'  # p: 2=On, 3=OFF'  #
GAIN_POINT_POSITION_Direct =  ' 81 01 05 4C 0p 0p FF'  # pp: 01 (0 dB) - 09 (24 dB)


BLACK_Reset = '81 01 7E 04 15 00 FF' # To return to 30 (0) value
BLACK_Up = '81 01 7E 04 15 02 FF'
BLACK_Down = '81 01 7E 04 15 03 FF'
BLACK_Direct = '81 01 7E 04 45 pp qq FF' # pp : 00 (–48) - 60 (48)


'''
SPEED: Si EXPOSURE MODE está ajustado en MANUAL o SHUTTER Pri, seleccione la velocidad del obturador electrónico.

SPEED Para la velocidad de fotogramas 59.94 de la salida de vídeo: 
1/8, 1/15, 1/30, 1/50, 1/60, 1/90, 1/100, 1/125, 1/180, 1/250, 1/350, 1/500, 1/725, 1/1000, 1/1500, 1/2000, 1/3000, 1/4000, 1/6000, 1/10000

Para la velocidad de fotogramas 29.27 de la salida de vídeo:
1/8, 1/15, 1/30, 1/50, 1/60, 1/90, 1/100, 1/125, 1/180, 1/250, 1/350, 1/500, 1/725, 1/1000, 1/1500, 1/2000, 1/3000, 1/4000, 1/6000, 1/10000

Para la velocidad de fotogramas 50 de la salida de vídeo: 
1/6, 1/12, 1/25, 1/30, 1/50, 1/60, 1/100, 1/120,1/150, 1/215, 1/300, 1/425, 1/600, 1/1000, 1/1250, 1/1750, 1/2500, 1/3500, 1/6000, 1/10000

Para la velocidad de fotogramas 25 de la salida de vídeo: 
1/6, 1/12, 1/25, 1/30, 1/50, 1/60, 1/100, 1/120,1/150, 1/215, 1/300, 1/425, 1/600, 1/1000, 1/1250, 1/1750, 1/2500, 1/3500, 1/6000, 1/10000

Para la velocidad de fotogramas 23.98 de la salida de vídeo: 
1/6, 1/12, 1/24, 1/25, 1/40, 1/48, 1/50, 1/60, 1/96, 1/100, 1/120, 1/144, 1/192, 1/200, 1/288, 1/400, 1/576, 1/1200, 1/2400, 1/4800, 1/10000



shutter values:

  pq
0x00 = 1/1s / 0x00 = 1/1s
0x01 = 1/2s / 0x01 = 1/2s
0x02 = 1/3s / 0x02 = 1/4s
0x03 = 1/6s / 0x03 = 1/8s
0x04 = 1/12s / 0x04 = 1/15s
0x05 = 1/25s / 0x05 = 1/30s
0x06 = 1/50s / 0x06 = 1/60s
0x07 = 1/75s / 0x07 = 1/90s
0x08 = 1/100s / 0x08 = 1/100s
0x09 = 1/120s / 0x09 = 1/125s
0x0A = 1/150s / 0x0A = 1/180s
0x0B = 1/215s / 0x0B = 1/250s
0x0C = 1/300s / 0x0C = 1/350s
0x0D = 1/425s / 0x0D = 1/500s
0x0E = 1/600s / 0x0E = 1/725s
0x0F = 1/1000s / 0x0F = 1/1000s
0x10 = 1/1250s / 0x10 = 1/1500s
0x11 = 1/1750s / 0x11 = 1/2000s
0x12 = 1/2500s / 0x12 = 1/3000s
0x13 = 1/3500s / 0x13 = 1/4000s
0x14 = 1/6000s / 0x14 = 1/6000s
0x15 = 1/10000s / 0x15 = 1/10000s
'''

#SHUTTER_
SHUTTER_Reset =  ' 81 01 04 0A 00 FF'  # Return to the default value depending on the #frame rate of video output
SHUTTER_Up =  ' 81 01 04 0A 02 FF'  #
SHUTTER_Down  =  ' 81 01 04 0A 03 FF'  #
SHUTTER_Direct =  ' 81 01 04 4A 00 00 pp qq FF'  # pp: Shutter - See the VISCA Command Setting Values (SHUTTER/MIN SHUTTER) section
SHUTTER_MAX_Direct =  ' 81 01 05 2A 00 0p 0p FF'  # pp: High speed shutter limit - See the VISCA Command Setting Values (MAX SHUTTER) section 
SHUTTER_MIN_Direct =  ' 81 01 05 2A 01 0p 0p FF'  # pp: Low speed shutter limit - See the VISCA Command Setting Values (MIN SHUTTER) section

AE_SPEED_Direct =  ' 81 01 04 5D pp FF'  # pp: 01 - 30

#EXP_COMP_
EXP_COMP_On_OFF=  ' 81 01 04 3E 0p FF'  # p: 2=On, 3=OFF
EXP_COMP_Reset =  ' 81 01 04 0E 00 FF'  # To return to 07 (Correction Level 0) value
EXP_COMP_Up =  ' 81 01 04 0E 02 FF'  #
EXP_COMP_Down =  ' 81 01 04 0E 03 FF'  #
EXP_COMP_Direct =  ' 81 01 04 4E 00 00 0p 0p FF'  # pp: 00 - 0E
BACK_LIGHT_On_OFF =  ' 81 01 04 33 0p FF'  # p: 2=On, 3=OFF  
SPOT_LIGHT_On_OFF =  ' 81 01 04 3A 0p FF'  # p: 2=On, 3=OFF

#VISIBILITY_ENHANCER
VISIBILITY_ENHANCER_OFF =  ' 81 01 04 3D 03 FF'  # OFF'  
VISIBILITY_ENHANCER_ON =  ' 81 01 04 3D 06 FF'  # On
VISIBILITY_ENHANCER =  ' 81 01 04 2D 00 0p 0q 0r 00 00 00 00 FF'  

''' 

Replace with the following commands:
p: EFF'  #ect level 0 (Dark) - 6 (Bright) -
q: Brightness compensation selection 0 (Very dark), 1 (Dark), 2 (Standard), 3 (Bright)
r: Compensation level 0 (Low), 1 (Mid), 2 (High)
'''


ND_FILTER =  ' 81 01 7E 01 53 0p FF'  # replace p: 0=OFF, 1=1/4, 2=1/16, 3=1/64


# ------------------------- COLOR CORRECTION --------------------------------

#WHITE BALANCE
Auto1 =  '81 01 04 35 00 FF'
Indoor =  '81 01 04 35 01 FF'
Outdoor =  '81 01 04 35 02 FF'
One_Push_WB =  '81 01 04 35 03 FF'
Auto2 =  '81 01 04 35 04 FF'
WB_Manual = '81 01 04 35 05 FF'


#ONE PUSH TRIGGER
WB_One_Push_Trigger =  '81 01 04 10 05 FF' # One Push WB Trigger

R_GAIN_Reset =  '81 01 04 03 00 FF' # To return to 80 (0) value
R_GAIN_Up =  '81 01 04 03 02 FF'
R_GAIN_Down =  '81 01 04 03 03 FF'
R_GAIN_Direct =  '81 01 04 43 00 00 pp qq FF' #pp: 00 (–128) - 80 (0) - FF' (128)

B_GAIN_Reset =  '81 01 04 04 00 FF' # To return to 80 (0) value
B_GAIN_Up =  '81 01 04 04 02 FF'
B_GAIN_Down =  '81 01 04 04 03 FF'  #
B_GAIN_Direct =  '81 01 04 44 00 00 0p 0p FF'  # pp: 00 (–128) - 80 (0) - FF' (128)
#SPEED =  '81 01 04 56 0p FF'  # p: 1 (Slow) - 5 (Fast)






HUE_Reset =  '81 01 7E 01 2E 00 00 FF'  # To return to 7 (0) value
HUE_Up =     '81 01 7E 01 2E 00 02 FF'  #REvisar
HUE_Down =    '81 01 7E 01 2E 00 03 FF'
HUE_Direct =  '81 01 7E 01 2E 01 0p FF'  # p: 0 (–7) - 7 (0) - E (+7)

CHROMA_SUPPRESS =  '81 01 04 5F 0p FF' # p: 0 (Off), 1 (Weak) - 3 (Strong)
MATRIX_Select =  '81 01 7E 01 3D 0p FF' # p: Matrix Setting (2=STD, 3=OFF, 4=HIGH SAT, 5=FL LIGHT, 6=MOVIE, 7=STILL, 8=CINEMA, 9=PRO, A=ITU709, B=B/W)


SATURATION_Reset =  '81 01 04 09 00 FF'  # To return to 4 value
SATURATION_Up =  '81 01 04 09 02 FF'
SATURATION_Down =  '81 01 04 09 03 FF'
SATURATION_Direct =  '81 01 04 49 00 00 00 0p FF'  # p: 0 (0) - E (14)



COLOR_PHASE_Reset =  '81 01 04 0F 00 FF'  # To return to 7 (0) value
COLOR_PHASE_Up =  '81 01 04 0F 02 FF'
COLOR_PHASE_Down =  '81 01 04 0F 03 FF'
COLOR_PHASE_Direct =  '81 01 04 4F 00 00 00 0p FF'  # p: 0 (–7 degrees) - E (+7 degrees)

R_G =  '81 09 7E 01 7A pp qq FF'  # pp  00 (–99) - 63 (00) - C6 (+99)
R_B =  '81 01 7E 01 7B pp qq FF'  # pp: 00 (–99) - 63 (00) - C6 (+99)
G_R =  '81 01 7E 01 7C pp qq FF'  # pp: 00 (–99) - 63 (00) - C6 (+99)
G_B =  '81 01 7E 01 7D pp qq FF'  # pp: 00 (–99) - 63 (00) - C6 (+99)
B_R =  '81 01 7E 01 7E pp qq FF'  # pp: 00 (–99) - 63 (00) - C6 (+99)
B_G =  '81 01 7E 01 7F pp qq FF'  # pp: 00 (–99) - 63 (00) - C6 (+99)


DETAIL_LEVEL_Reset =  '81 01 04 02 00 FF'  # To return to 7 (0) value
DETAIL_LEVEL_Up =  '81 01 04 02 02 FF'
DETAIL_LEVEL_Down =  '81 01 04 02 03 FF'
DETAIL_LEVEL_Direct =  '81 01 04 42 00 00 00 0p FF'  # pp: 00 - 0F 
DETAIL_LEVEL_MODE_AUTO =  '81 01 05 42 01 00 FF'  
DETAIL_LEVEL_MODE_MANUAL =  '81 01 05 42 01 01 FF'
DETAIL_LEVEL_BANDWIDTH =  '81 01 05 42 02 0p FF'  # p: 0 - 4
DETAIL_LEVEL_CRISPENING =  '81 01 05 42 03 0p FF'  # p: 0 - 7
DETAIL_H_V_BALANCE =  '81 01 05 42 04 0p FF'  # p: 5 - 9  (5 = -2 , 7 = 0,  9 = +2)
DETAIL_B_W_BALANCE =  '81 01 05 42 05 0p FF'  # p: 0 - 4
DETAIL_LIMIT =  '81 01 05 42 06 0p FF'  # p: 0 - 7
DETAIL_HLT =  '81 01 05 42 07 0p FF'  # p: 0 - 4
DETAIL_SLOW =  '81 01 05 42 08 0p FF'  # p: 0 - 7


#KNEE

KNEE_SETTING = '81 01 7E 01 6D 0p FF' # p: 2=On, 3=Off
KNEE_MODE = '81 01 7E 01 54 0p FF' # p: 0=Auto, 4=Manual
KNEE_SLOPE = '81 01 7E 01 6F 00 0p FF' # pp: 00 - 0E
KNEE_POINT = '81 01 7E 01 6E 00 0p FF' # pp: 00 - 0C



#GAMMA

GAMMA_MODE  = '81 01 04 5B 0p FF'         #  p: GAMMA Setting (0=STD, 1=STRAIGHT, 2=PATTERN, 8=MOVIE, 9=STILL, A=CINE1, B=CINE2, C=CINE3, D=CINE4, E=ITU709)
PATTERN_Direct = '81 01 05 5B 0p 0p 0p FF' #  ppp: 001 - 200
OFFSET_Direct = '81 01 04 1E 00 00 00 0p 0q 0q FF' #p: Offset polarity 0 (+), 1 (–)qq: Offset width 00 - 40
LEVEL_Direct = '81 01 7E 01 71 0p 0p FF' # pp : 00 - 0E
BLACK_GAMMA_LEVEL_Direct = '81 01 7E 01 72 0p 0p FF' # pp : 00 - 0E
BLACK_GAMMA_RANGE_Direct = '81 01 05 5C 0p FF' # p: Correction range 0 (Low), 1 (Mid), 2 (High)

PICTURE_PROFILE_MODE  = '81 01 7E 04 5F 0p FF' # p: Picture profile setting (0=PP1, 1=PP2,2=PP3, 3=PP4, 4=PP5, 5=PP6)

FLICKER_REDUCTION_MODE = '81 01 04 32 0p FF' # p: Flicker reduction mode (0=OFF, 1=ON)

NOISE_REDUCTION_MODE_LEVEL  = '81 01 04 53 pp FF' # pp : NR Setting 00 (Off), 01 (Weak) - 05 (Strong), 7F (Advanced)
NR_MANUAL_SETTING = '81 01 05 53 0p 0q FF' # p: 2D NR Level 0 (Off), 1 (Weak) - 5 (Strong) q: 3D NR Level 0 (Off), 1 (Weak) - 5 (Strong)