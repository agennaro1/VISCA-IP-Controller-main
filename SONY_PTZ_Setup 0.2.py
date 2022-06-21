#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import socket
import binascii # for printing the messages we send, not really necessary
from time import sleep
from tkinter import messagebox
from tkinter.font import BOLD
import adjust_commands as ac
import convertion_tables as ct

camera_ip = '10.50.2.142' # default 
camera_port = 52381  # default de Sony para Visca
free_D_port = 40000   # puerto de escucha de freeD 
sequence_number = 1

store_y = 10
label_y = 150

Iris_x= 5
Iris_y = 5

gain_x = 5
gain_y = 5

shutter_x = 5
shutter_y = 5

on_off_y = 30
on_off_x = 13
WB_y = 30
WB_x = 13
button_width = 12


store_color = 'red'
recall_color = 'light grey'
iris_color = 'light blue'
gain_color = 'light blue'
shutter_color = 'light blue'
zoom_color = '#fF8204'
focus_color = 'cyan'
on_off_color = 'violet'
WB_color = 'cyan'
colorimetry_color= 'orange'
detail_color= '#93ce54'



#----------------------------------------------------------------------------------------------------------------------

class Aplicacion():
    def __init__(self):


        soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # IPv4, UDP
        buffer_size = 1024
        sequence_number = 1 # a global variable that we'll iterate each command, remember 0x0001
        
        
        # encendido y apagado de la camara

        camera_on = '81 01 04 00 02 FF'
        camera_off = '81 01 04 00 03 FF'
        # encendido y apagado del Display
        information_display_on = '81 01 7E 01 18 02 FF'
        information_display_off = '81 01 7E 01 18 03 FF'

      
        
        def reset_sequence_number_function():
            global sequence_number
            reset_sequence_number_message = bytearray.fromhex('02 00 00 01 00 00 00 01 01')
            soc.sendto(reset_sequence_number_message,(camera_ip, camera_port))
            sequence_number = 1
            return sequence_number

        def store_network_values(ip_value, port_value): # seleccionamos la ip de la camara
            global camera_ip
            global camera_port
            camera_ip = ip_value
            camera_port = port_value
            # IP Label
            lbl2=Label(encabezado, background="gray13", fg="#54f706", width="30", justify="center", text="Connected to:  " +str(camera_ip) +':'+str(camera_port)).place(x=160, y=5)
            print(camera_ip, camera_port)
            return camera_ip, camera_port

        def send_message (message_string):
            global sequence_number 
            global received_message
            global camera_ip
            global camera_port
            message_string = (message_string)
            payload_type = bytearray.fromhex('01 00')
            payload = bytearray.fromhex(message_string)

            print (payload)

            payload_length = len(payload).to_bytes(2, 'big')
            message = payload_type + payload_length + sequence_number.to_bytes(4, 'big') + payload # aca se arma el mensaje a enviar
            sequence_number += 1
            soc.sendto(message, (camera_ip, camera_port))
            print(binascii.hexlify(message), 'sent to', camera_ip, camera_port, sequence_number)
            received_message = 'test'
            return received_message    
            

  


                        
        # ----------------------------- GUI -------------------------------------------------------------------
        root = Tk()
        display_message = StringVar()
        root.title('SONY PTZ SETUP V1')
        root.resizable(False, False)
        root.config(bg="grey")
        root.config(width="900", height="800")
        #-----------------------------------comienzo de menu----------------------------------------------


        # Funciones de Windows menus
        def infoAdicional ():
            messagebox.showinfo("Visca Controler 2021")

        def avisoLicencia ():
            messagebox.showwarning("Licencia", " Producto bajo licencia GNU")

        def avisoSalir():
            salida=messagebox.askquestion("Salir", "Deseas Salir de la aplicacion?") 

            if salida == "yes":
                root.destroy()


        barraMenu = Menu(root)
        root.config(menu=barraMenu)

        archivoMenu = Menu(barraMenu , tearoff=0)
        archivoMenu.add_command(label="Salir",  command=avisoSalir)

        archivoHerraminentas = Menu(barraMenu, tearoff=0)

        archivoAyuda = Menu(barraMenu, tearoff=0)
        archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
        archivoAyuda.add_separator()
        archivoAyuda.add_command(label="Ayuda")
        archivoAyuda.add_command(label="Acerca de ...", command= infoAdicional)

        barraMenu.add_cascade(label="Archivo", menu=archivoMenu )
        barraMenu.add_cascade(label="Herramientas", menu=archivoHerraminentas)
        barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)



        # ----------------------------------Seleccion de  camara ip---------------------------------------------------

        encabezado=Frame(root)
        encabezado.pack(fill="y")
        encabezado.config(bg="grey13")
        encabezado.place(x=10, y=10)
        encabezado.config(width="480", height="40")
        encabezado.config(bd="5")
        encabezado.config(relief="groove") #Groove, sunken etc


        # IP
        lbl1=Label(encabezado,background="gray13", fg="#54f706", width="8", justify="center", text='CAMARA IP').place(x=7, y=5)
        ip_value = Entry(encabezado, width=15, justify="center", background="#54f706", )
        ip_value.place(x=80, y= 5)
        ip_value.insert(0, camera_ip)

        # Save ip
        
        lbl2=Label(encabezado,background="gray13", fg="#54f706", width="20", justify="center", text='---------------------').place(x=160, y=5)
        Button(encabezado,  height=1, width=8, font=('Colibri', 7 ), text='SET', command=lambda: store_network_values(ip_value.get(), camera_port)).place(x=400, y=5)
        
        
        # -----------------------------------------------------------------------CAMERA ON-OFF buttons ----------------------------
        on_off=Frame(root)
        on_off.config(bg="grey")
        on_off.place(x=500, y=10)
        on_off.config(width="250", height="140")
        on_off.config(bd="5")
        on_off.config(relief="sunken") #Groove, sunken etc

        
        Label(on_off, font='Helvetica 9 bold ' ,text='CAMERA', bg=on_off_color, width=button_width).grid(row=0, column=0)
        Button(on_off, font='Helvetica 9 bold ',text='ON', bg=on_off_color, width=button_width, command=lambda: send_message(camera_on)).grid(row=0, column=1)
        Button(on_off,font='Helvetica 9 bold ', text='OFF', bg=on_off_color, width=button_width, command=lambda: send_message(camera_off)).grid(row=0, column=2)
        Button(on_off,font='Helvetica 9 bold ', text='MENU', bg=on_off_color, width=button_width, command=lambda: send_message(ac.MENU_TOGGLE)).grid(row=0, column= 3)


        # -----------------------------------------------------------------------CAMERA MODE --------------------------------------   



        mode=Frame(root)
        mode.config(bg="grey")
        mode.place(x=10, y=50)
        mode.config(width="250", height="140")
        mode.config(bd="5")
        mode.config(relief="sunken") #Groove, sunken etc
        
        Label(mode, text='MODE', bg='yellow', width=button_width).grid(row=0, column=0)
        Button(mode, text='FULL AUTO', bg=on_off_color, width=button_width, command=lambda: send_message(ac.Full_Auto)).grid(row=0, column=1)
        Button(mode, text='MANUAL', bg=on_off_color, width=button_width, command=lambda: send_message(ac.Manual)).grid(row=0, column=2)

        Button(mode,font=('Colibri',8 ), text='SHUTTER Primary', bg=on_off_color, width=14, command=lambda: send_message(ac.Shutter_Priority)).grid(row=1, column=0)
        Button(mode,font=('Colibri',8 ) ,text='IRIS Primary', bg=on_off_color, width=14, command=lambda: send_message(ac.Iris_Priority)).grid(row=1, column=1)
        Button(mode,font=('Colibri',8 ), text='GAIN Primary', bg=on_off_color, width=14, command=lambda: send_message(ac.Gain_Priority)).grid(row=1, column=2)



       
        # -----------------------------------EXPOSURE------------------------------------------------------


        # ----------------------------------Setup IRIS---------------------------------------------------
        iris=Frame(root)
        iris.config(bg="grey")
        iris.place(x=10, y=115)
        iris.config(width="290", height="130")
        iris.config(bd="5")
        iris.config(relief="sunken") #Groove, sunken etc

        lbl_iris = Label(iris, bg='gray13', fg='#54f706', width=38, text='F2.8').place(x=Iris_x+2, y=Iris_y+65)
        
 
        def iris_setup(iris_value):
            show_iris = ct.iris_Focal.get(int(iris_value))
            lbl_iris=Label(iris,background="gray13", fg="#54f706", width=38, justify="center", text= show_iris).place(x=Iris_x+2, y=Iris_y+65)
            print (show_iris)
            iris_convertido = ct.iris_table.get(int(iris_value))
            iris_message = ac.IRIS_Direct.replace('pp qq', str(iris_convertido))
            print (iris_message)
            send_message(iris_message)

        # variable with integer values only
        var = IntVar()
        # set scale default value as 50
        var.set(0)
        si = Scale(iris, label='IRIS CONTROL', from_=0, to=16,variable=var, orient=HORIZONTAL, length=270, showvalue=0,tickinterval=2, resolution=1, command=iris_setup).place(x=5, y=5)
       
       
        Button(iris,font=('Colibri',8 ), text='UP', width=13, bg=iris_color, command=lambda: send_message(ac.IRIS_Up)).place(x=Iris_x, y=Iris_y+90)
        Button(iris,font=('Colibri',8 ), text='RESET IRIS', width=13, bg=iris_color,  command=lambda: send_message(ac.IRIS_Reset)).place(x=Iris_x+92, y=Iris_y+90)
        Button(iris,font=('Colibri',8 ), text='DOWN', width=13, bg=iris_color, command=lambda: send_message(ac.IRIS_Down)).place(x=Iris_x+184, y=Iris_y+90)



        # ----------------------------------Setup GAIN ---------------------------------------------------


        gain=Frame(root)
        gain.config(bg="grey")
        gain.place(x=10, y=248)
        gain.config(width="290", height="130")
        gain.config(bd="5")
        gain.config(relief="sunken") #Groove, sunken etc

        lbl_gain = Label(gain, bg='gray13', fg='#54f706', width="38", justify="center", text='0 dB').place(x=5, y=70)

        def gain_setup(gain_value):
            show_gain= ct.gain_lbl.get(int(gain_value))
            lbl_gain = Label(gain, bg='gray13', fg='#54f706', width="38", justify="center", text=show_gain).place(x=5, y=70)
            print (show_gain)
            gain_convertido= ct.gain_table.get(int(gain_value))
            gain_message = ac.GAIN_Direct.replace('p', str(gain_convertido))
            print (gain_message)
            send_message(gain_message)
        # variable with integer values only
        var = IntVar()

        # set scale default value as 1
        var.set(1)
        sg = Scale(gain, label='GAIN CONTROL', from_=0, to=12,variable=var, orient=HORIZONTAL, length=270, showvalue=0,tickinterval=2, resolution=1, command=gain_setup).place(x=5, y=5)
       
       
        Button(gain,font=('Colibri',8 ), text='UP', width=13, bg=gain_color, command=lambda: send_message(ac.GAIN_Up)).place(x=gain_x, y=gain_y+90)
        Button(gain,font=('Colibri',8 ), text='RESET GAIN', width=13, bg=gain_color,  command=lambda: gain_setup(1)).place(x=gain_x+92, y=gain_y+90)
        Button(gain,font=('Colibri',8 ), text='DOWN', width=13, bg=gain_color, command=lambda: send_message(ac.GAIN_Down)).place(x=gain_x+184, y=gain_y+90)



        # ----------------------------------Setup shutter ---------------------------------------------------


        shutter=Frame(root)
        shutter.config(bg="grey")
        shutter.place(x=10, y=383)
        shutter.config(width="290", height="130")
        shutter.config(bd="5")
        shutter.config(relief="sunken") #Groove, sunken etc

        lbl_shutter = Label(shutter, bg='gray13', fg='#54f706', width="38", justify="center", text='1/1s').place(x=5, y=70)

        def shutter_setup(shutter_value):
            show_shutter= ct.shutter_lbl.get(int(shutter_value))
            lbl_shutter = Label(shutter, bg='gray13', fg='#54f706', width="38", justify="center", text=show_shutter).place(x=5, y=70)
            print (show_shutter)
            shutter_convertido= ct.shutter_table.get(int(shutter_value))
            shutter_message = ac.SHUTTER_Direct.replace('pp qq', str(shutter_convertido))
            print (shutter_message)
            send_message(shutter_message)
        # variable with integer values only
        var = IntVar()

        # set scale default value as 1
        var.set(0)
        sg = Scale(shutter, label='SHUTTER CONTROL', from_=0, to=21,variable=var, orient=HORIZONTAL, length=270, showvalue=0,tickinterval=2, resolution=1, command=shutter_setup).place(x=5, y=5)
       
       
        Button(shutter,font=('Colibri',8 ), text='UP', width=13, bg=shutter_color, command=lambda: send_message(ac.SHUTTER_Up)).place(x=shutter_x, y=shutter_y+90)
        Button(shutter,font=('Colibri',8 ), text='RESET shutter', width=13, bg=shutter_color,  command=lambda: shutter_setup(1)).place(x=shutter_x+92, y=shutter_y+90)
        Button(shutter,font=('Colibri',8 ), text='DOWN', width=13, bg=shutter_color, command=lambda: send_message(ac.SHUTTER_Down)).place(x=shutter_x+184, y=shutter_y+90)

        # ----------------------------------BLACK Setup  ---------------------------------------------------

        black=Frame(root)
        black.config(bg="grey")
        black.place(x=10, y=518)
        black.config(width="290", height="130")
        black.config(bd="5")
        black.config(relief="sunken") #Groove, sunken etc

        lbl_black = Label(black, bg='gray13', fg='#54f706', width="38", justify="center", text='0').place(x=5, y=70)
        
        def black_setup(black_value):
            
            lbl_black = Label(black, bg='gray13', fg='#54f706', width="38", justify="center", text=black_value).place(x=5, y=70)
            black_convertido= ct.black_table.get(int(black_value)) 
            black_message = ac.BLACK_Direct.replace('pp qq', str(black_convertido))
            print (black_message)
            send_message(black_message)
        


        
        # variable with integer values only
        BL_var = IntVar()
        # set scale default value as 0
        BL_var.set(0)


        def reset_BL():
            BL_var.set(0)
            lbl_black = Label(black, bg='gray13', fg='#54f706', width="38", justify="center", text='0').place(x=5, y=70)
            send_message(ac.BLACK_Reset)

        sb = Scale(black, label='BLACK CONTROL', from_=-48, to=48,variable=BL_var, orient=HORIZONTAL, length=270, showvalue=0,tickinterval=2, resolution=1, command=black_setup).place(x=5, y=5)
        Button(black,font=('Colibri',8 ), text='UP', width=13, bg=gain_color, command=lambda: send_message(ac.BLACK_Up)).place(x=gain_x, y=gain_y+90)
        Button(black,font=('Colibri',8 ), text='RESET BLACK', width=13, bg=gain_color,  command=lambda: reset_BL()).place(x=gain_x+92, y=gain_y+90)
        Button(black,font=('Colibri',8 ), text='DOWN', width=13, bg=gain_color, command=lambda: send_message(ac.BLACK_Down)).place(x=gain_x+184, y=gain_y+90)










        # -------------------------- WHITE BALANCE COMANDS ----------------------------

        WB=Frame(root)
        WB.config(bg="grey")
        WB.place(x=305, y=50)
        WB.config(width="250", height="210")
        WB.config(bd="5")
        WB.config(relief="sunken") #Groove, sunken etc

        
        Button(WB, text='ONE PUSH WB', bg=WB_color, width=button_width, command=lambda: send_message(ac.One_Push_WB)).grid(row=1, column=1)
        Button(WB, text='Indoor', bg=WB_color, width=button_width, command=lambda: send_message(ac.Indoor)).grid(row=1, column=2)
        Button(WB, text='Outdoor', bg=WB_color, width=button_width, command=lambda: send_message(ac.Outdoor)).grid(row=1, column=3)

        Button(WB, text='Manual WB', bg=WB_color, width=button_width, command=lambda: send_message(ac.WB_Manual)).grid(row=2, column=1)
        Button(WB, text='Auto1', bg=WB_color, width=button_width, command=lambda: send_message(ac.Auto1)).grid(row=2, column=2)
        Button(WB, text='Auto2', bg=WB_color, width=button_width, command=lambda: send_message(ac.Auto2)).grid(row=2, column=3)
        

        #Button(WB, text='ONE PUSH TRIGGER ', bg=WB_color, width=20, command=lambda: send_message(ac.WB_One_Push_Trigger)).grid(row=3, column=1)





        # ----------------------------------COLORIMETRIA  ---------------------------------------------------

        colorimetry=Frame(root)     
        colorimetry.config(bg="orange")
        colorimetry.place(x=305, y=115)
        colorimetry.config(width="290", height="570")
        colorimetry.config(bd="5")
        colorimetry.config(relief="sunken") #Groove, sunken etc

        Label(colorimetry, text='COLORIMETRIA', font='Helvetica 10 bold ', bg=colorimetry_color).place(x=gain_x+10, y=gain_y+2)
         
        # ---------------------------------  control de ROJO  ---------------------------------------------------

        def RGain(rg_value):
            show_rg= ct.cg_lbl.get(int(rg_value))
            lbl_rg = Label(colorimetry, bg='gray13', fg='#54f706', width="22", justify="center", text=show_rg).place(x=gain_x+100, y=gain_y+25)
            rg_convertido= ct.cg_table.get(int(rg_value))
            rg_message = ac.R_GAIN_Direct.replace('pp qq', str(rg_convertido))
            print (rg_message)
            send_message(rg_message)
            return rg_message


        # variable with integer values only
        RED = IntVar()
        # set scale default value as 80
        RED.set(127)

        def reset_red():
            RED.set(127)
            lbl_rg = Label(colorimetry, bg='gray13', fg='#54f706', width="22", justify="center", text='0').place(x=gain_x+100, y=gain_y+26)
            send_message(ac.R_GAIN_Reset)

        
        rg = Scale(colorimetry, label='R.GAIN', from_=0, to=255,variable=RED, orient=HORIZONTAL, length=260, showvalue=0, resolution=1, command=RGain).place(x=gain_x, y=gain_y+25)
        Button(colorimetry,font=('Colibri',8 ), text='UP', width=13, bg='red', command=lambda: send_message(ac.R_GAIN_Up)).place(x=gain_x, y=gain_y+70)
        Button(colorimetry,font=('Colibri',8 ), text='RESET R.GAIN', width=13, bg='red',  command=lambda:reset_red()).place(x=Iris_x+90, y=Iris_y+70)
        Button(colorimetry,font=('Colibri',8 ), text='DOWN', width=13, bg='red', command=lambda: send_message(ac.R_GAIN_Down)).place(x=gain_x+180, y=gain_y+70)
        lbl_rg = Label(colorimetry, bg='gray13', fg='#54f706', width="22", justify="center", text='0').place(x=gain_x+100, y=gain_y+26)
        

        # ---------------------------------  control de AZUL ---------------------------------------------------

        
        
        def BGain(bg_value):
            show_bg= ct.cg_lbl.get(int(bg_value))
            lbl_bg = Label(colorimetry, bg='gray13', fg='#54f706', width="22", justify="center", text=show_bg).place(x=gain_x+100, y=gain_y+99)
            bg_convertido= ct.cg_table.get(int(bg_value))
            bg_message = ac.R_GAIN_Direct.replace('pp qq', str(bg_convertido))
            print (bg_message)
            send_message(bg_message)
            return bg_message


        # variable with integer values only
        BLU = IntVar()
        # set scale default value as 80
        BLU.set(127)

        def reset_blue():
            BLU.set(127)
            lbl_bg = Label(colorimetry, bg='gray13', fg='#54f706', width="22", justify="center", text='0').place(x=gain_x+100, y=gain_y+99)
            send_message(ac.B_GAIN_Reset)


        bgain = Scale(colorimetry, label='B.GAIN', from_=0, to=255,variable=BLU, orient=HORIZONTAL, length=260, showvalue=0, resolution=1, command=BGain).place(x=gain_x, y=gain_y+98)

        Button(colorimetry,font=('Colibri',8 ), text='UP', width=13, bg='blue', command=lambda: send_message(ac.B_GAIN_Up)).place(x=gain_x, y=gain_y+138)
        Button(colorimetry,font=('Colibri',8 ), text='RESET B.GAIN', width=13, bg='blue',  fg= 'white' ,command=lambda:reset_blue()).place(x=Iris_x+90, y=Iris_y+138)
        Button(colorimetry,font=('Colibri',8 ), text='DOWN', width=13, bg='blue', command=lambda: send_message(ac.B_GAIN_Down)).place(x=gain_x+180, y=gain_y+138)
        lbl_bg = Label(colorimetry, bg='gray13', fg='#54f706', width="22", justify="center", text='0').place(x=gain_x+100, y=gain_y+99)



        # ---------------------------------  control de SATURATION ---------------------------------------------------
      
        def Saturation(sat_value):
            lbl_saturation = Label(colorimetry, bg='gray13', fg='#54f706', width="22", justify="center", text=sat_value).place(x=gain_x+100, y=gain_y+165)
            saturation_convertido= ct.COLOR_table.get(int(sat_value))
            saturation_message = ac.SATURATION_Direct.replace('p', str(saturation_convertido))
            print (saturation_message)
            send_message(saturation_message)
            return saturation_message
       

        # variable with integer values only
        SAT= IntVar()
        # set scale default value as 7

        def reset_SAT():
            SAT.set(4)
            lbl_SAT = Label(colorimetry, bg='gray13', fg='#54f706', width="22", justify="center", text='4').place(x=gain_x+100, y=gain_y+165)
            send_message(ac.SATURATION_Reset)


        SAT.set(4)
        
        sat_value = Scale(colorimetry, label='SATURATION', from_=0, to=14,variable=SAT, orient=HORIZONTAL, length=260, showvalue=0, resolution=1, command=Saturation).place(x=gain_x, y=gain_y+165)
   
        Button(colorimetry,font=('Colibri',8 ), text='SAT UP', width=13, bg='cyan', command=lambda: send_message(ac.SATURATION_Up)).place(x=gain_x, y=gain_y+210)
        Button(colorimetry,font=('Colibri',8 ), text='RESET SAT', width=13, bg='cyan' ,command=lambda:reset_SAT()).place(x=Iris_x+90, y=Iris_y+210)
        Button(colorimetry,font=('Colibri',8 ), text='SAT DOWN', width=13, bg='cyan', command=lambda: send_message(ac.SATURATION_Down)).place(x=gain_x+180, y=gain_y+210)
        lbl_saturation = Label(colorimetry, bg='gray13', fg='#54f706', width="22", justify="center", text='0').place(x=gain_x+100, y=gain_y+165)


        # ---------------------------------  control de HUE ---------------------------------------------------

        def HUEGain(hue_value):
            show_HUE= ct.HUE_lbl.get(int(hue_value))
            lbl_HUE = Label(colorimetry, bg='gray13', fg='#54f706', width="22", justify="center", text=show_HUE).place(x=gain_x+100, y=gain_y+236)
            HUE_convertido= ct.HUE_table.get(int(hue_value))
            HUE_message = ac.HUE_Direct.replace('p', str(HUE_convertido))
            print (HUE_message)
            send_message(HUE_message)
            return HUE_message


        # variable with integer values only
        HUE= IntVar()
        # set scale default value as 80

        def reset_HUE():
            HUE.set(7)
            lbl_HUE = Label(colorimetry, bg='gray13', fg='#54f706', width="22", justify="center", text='0').place(x=gain_x+100, y=gain_y+236)
            send_message(ac.HUE_Reset)


        HUE.set(7)
        
        hue_value = Scale(colorimetry, label='HUE PHASE', from_=0, to=14,variable=HUE, orient=HORIZONTAL, length=260, showvalue=0, resolution=1, command=HUEGain).place(x=gain_x, y=gain_y+235)
        Button(colorimetry,font=('Colibri',8 ), text='HUE UP', width=13, bg='red', command=lambda: send_message(ac.HUE_Up)).place(x=gain_x, y=gain_y+280)
        Button(colorimetry,font=('Colibri',8 ), text='RESET HUE', width=13, bg='white',  command=lambda:reset_HUE()).place(x=Iris_x+90, y=Iris_y+280)
        Button(colorimetry,font=('Colibri',8 ), text='HUE DOWN', width=13, bg='blue', command=lambda: send_message(ac.HUE_Down)).place(x=gain_x+180, y=gain_y+280)
        lbl_HUE = Label(colorimetry, bg='gray13', fg='#54f706', width="22", justify="center", text='0').place(x=gain_x+100, y=gain_y+236)


        # ---------------------------------  MATRIX R_G   ---------------------------------------------------


        Button(colorimetry,font=('Colibri',8 ), text='RESET RG', width=13, bg='white',  command=lambda:reset_RG()).place(x=gain_x+150, y=gain_y+310)

        def R_G_control(R_G_value):
            lbl_R_G = Label(colorimetry, bg='gray13', fg='#54f706', width="8", justify="center", text=R_G_value).place(x=gain_x+100, y=gain_y+310)
            R_G_convertido= ct.MATRIX_table.get(int(R_G_value))
            R_G_message =ac.R_B.replace('pp qq', str(R_G_convertido))
            print (R_G_message)
            send_message(R_G_message)
            return R_G_message

        RG = IntVar()

        def reset_RG():
            RG.set(0)
            lbl_R_G = Label(colorimetry, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+310)
            RG_Reset_Message = '81 01 7E 01 7B 06 03 FF'
            send_message(RG_Reset_Message)

        RG.set(0)

        RG_value = Scale(colorimetry, label='R_G', from_=-99, to=99,variable=RG, orient=HORIZONTAL, length=260, showvalue=0, resolution=1, command=R_G_control).place(x=gain_x, y=gain_y+310)
        Button(colorimetry,font=('Colibri',7 ), text='RESET RG', width=13, bg='white',  command=lambda:reset_RG()).place(x=gain_x+170, y=gain_y+310)
        lbl_R_G = Label(colorimetry, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+310)

        # ---------------------------------  MATRIX  R_B---------------------------------------------------

        Button(colorimetry,font=('Colibri',8 ), text='RESET RB', width=13, bg='white',  command=lambda: reset_RB()).place(x=gain_x+150, y=gain_y+350)

        def R_B_control(R_B_value):
            lbl_R_B = Label(colorimetry, bg='gray13', fg='#54f706', width="8", justify="center", text=R_B_value).place(x=gain_x+100, y=gain_y+351)
            R_B_convertido= ct.MATRIX_table.get(int(R_B_value))
            R_B_message = ac.R_B.replace('pp qq', str(R_B_convertido))
            print (R_B_message)
            send_message(R_B_message)
            return R_B_message

        RB= IntVar()
        
        def reset_RB():
            RB.set(0)
            lbl_R_B = Label(colorimetry, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+351)
            RB_Reset_Message = '81 01 7E 01 7B 06 03 FF'
            send_message(RB_Reset_Message)

        RB.set(0)
        
        R_B_value = Scale(colorimetry, label='R_B', from_=-99, to=99,variable=RB, orient=HORIZONTAL, length=260, showvalue=0, resolution=1, command=R_B_control).place(x=gain_x, y=gain_y+350)
        Button(colorimetry,font=('Colibri',7 ), text='RESET RB', width=13, bg='white', command=lambda:reset_RB()).place(x=gain_x+170, y=gain_y+350)
        lbl_R_B = Label(colorimetry, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+351)



        # ---------------------------------  MATRIX  G_R ---------------------------------------------------

        Button(colorimetry,font=('Colibri',8 ), text='RESET GR', width=13, bg='white',  command=lambda:reset_GR()).place(x=gain_x+150, y=gain_y+392)

        def G_R_control(G_R_value):
            lbl_G_R = Label(colorimetry, bg='gray13', fg='#54f706', width="8", justify="center", text=G_R_value).place(x=gain_x+100, y=gain_y+393)
            G_R_convertido= ct.MATRIX_table.get(int(G_R_value))
            G_R_message = ac.G_R.replace('pp qq', str(G_R_convertido))
            print (G_R_message)
            send_message(G_R_message)
            return G_R_message


        GR= IntVar()
        # set scale default value as 80

        def reset_GR():
            GR.set(0)
            lbl_G_R = Label(colorimetry, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+393)
            RB_Reset_Message = '81 01 7E 01 7C 06 03 FF'
            send_message(RB_Reset_Message)

        GR.set(0)
        
        G_R_value = Scale(colorimetry, label='G_R', from_=-99, to=99,variable=GR, orient=HORIZONTAL, length=260, showvalue=0, resolution=1, command=G_R_control).place(x=gain_x, y=gain_y+392)
        Button(colorimetry,font=('Colibri',7 ), text='RESET GR', width=13, bg='white',  command=lambda:reset_GR()).place(x=gain_x+170, y=gain_y+392)
        lbl_G_R = Label(colorimetry, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+393)

           # ---------------------------------  MATRIX  G_B ---------------------------------------------------

        Button(colorimetry,font=('Colibri',8 ), text='RESET GB', width=13, bg='white',  command=lambda:reset_GB()).place(x=gain_x+150, y=gain_y+432)

        def G_B_control(G_B_value):
            lbl_G_B = Label(colorimetry, bg='gray13', fg='#54f706', width="8", justify="center", text=G_B_value).place(x=gain_x+100, y=gain_y+433)
            G_B_convertido= ct.MATRIX_table.get(int(G_B_value))
            G_B_message = ac.G_B.replace('pp qq', str(G_B_convertido))
            print (G_B_message)
            send_message(G_B_message)
            return G_B_message


        GB= IntVar()

        def reset_GB():
            GB.set(0)
            lbl_G_B = Label(colorimetry, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+432)
            GB_Reset_Message = '81 01 7E 01 7D 06 03 FF'
            send_message(GB_Reset_Message)

        GB.set(0)

        G_B_value = Scale(colorimetry, label='G_B', from_=-99, to=99,variable=GB, orient=HORIZONTAL, length=260, showvalue=0, resolution=1, command=G_B_control).place(x=gain_x, y=gain_y+432)
        Button(colorimetry,font=('Colibri',7 ), text='RESET GB', width=13, bg='white',  command=lambda:reset_GB()).place(x=gain_x+170, y=gain_y+432)
        lbl_G_B = Label(colorimetry, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+432)

        # ---------------------------------  MATRIX  B_R ---------------------------------------------------

        Button(colorimetry,font=('Colibri',8 ), text='RESET BR', width=13, bg='white',  command=lambda:reset_BR()).place(x=gain_x+150, y=gain_y+472)

        def B_R_control(B_R_value):
            lbl_B_R = Label(colorimetry, bg='gray13', fg='#54f706', width="8", justify="center", text=B_R_value).place(x=gain_x+100, y=gain_y+473)
            B_R_convertido= ct.MATRIX_table.get(int(B_R_value))
            B_R_message = ac.B_R.replace('pp qq', str(B_R_convertido))
            print (B_R_message)
            send_message(B_R_message)

        BR= IntVar()
        # set scale default value as 80

        def reset_BR():
            BR.set(0)
            lbl_B_R = Label(colorimetry, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+473)
            BR_Reset_Message = '81 01 7E 01 7E 06 03 FF'
            send_message(BR_Reset_Message)


        BR.set(0)

        B_R_value = Scale(colorimetry, label='B_R', from_=-99, to=99,variable=BR, orient=HORIZONTAL, length=260, showvalue=0, resolution=1, command=B_R_control).place(x=gain_x, y=gain_y+472)
        Button(colorimetry,font=('Colibri',7 ), text='RESET BR', width=13, bg='white',  command=lambda:reset_BR()).place(x=gain_x+170, y=gain_y+472)
        lbl_B_R = Label(colorimetry, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+473)
        
        # ---------------------------------  MATRIX  B_G ---------------------------------------------------

        Button(colorimetry,font=('Colibri',8 ), text='RESET BG', width=13, bg='white',  command=lambda:reset_BG()).place(x=gain_x+150, y=gain_y+512)

        def B_G_control(B_G_value):
            lbl_B_G = Label(colorimetry, bg='gray13', fg='#54f706', width="8", justify="center", text=B_G_value).place(x=gain_x+100, y=gain_y+513)
            B_G_convertido= ct.MATRIX_table.get(int(B_G_value))
            B_G_message = ac.B_G.replace('pp qq', str(B_G_convertido))
            print (B_G_message)
            send_message(B_G_message)

        BG= IntVar()

        def reset_BG():
            BG.set(0)
            lbl_B_G = Label(colorimetry, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+513)
            BG_Reset_Message = '81 01 7E 01 7E 06 03 FF'
            send_message(BG_Reset_Message)

        BG.set(0)


        B_G_value = Scale(colorimetry, label='B_G', from_=-99, to=99,variable=BG, orient=HORIZONTAL, length=260, showvalue=0, resolution=1, command=B_G_control).place(x=gain_x, y=gain_y+512)
        Button(colorimetry,font=('Colibri',7 ), text='RESET BG', width=13, bg='white',  command=lambda:reset_BG()).place(x=gain_x+170, y=gain_y+512)
        lbl_B_G = Label(colorimetry, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+513)





        # ----------------------------------DETAIL ---------------------------------------------------

        detail=Frame(root)     
        detail.config(bg=detail_color)
        detail.place(x=600, y=115)
        detail.config(width="290", height="305")
        detail.config(bd="5")
        detail.config(relief="sunken") #Groove, sunken etc

        Label(detail, text='DETAIL', font='Helvetica 10 bold ', bg=detail_color).place(x=gain_x+10, y=gain_y+2)

        Label(detail, font='Helvetica 10 bold ',text='MODE', bg='#ffffcc', width=button_width).place(x=5, y=30)
        Button(detail, text='AUTO', bg='#ffffcc', width=button_width, command=lambda: send_message(ac.DETAIL_LEVEL_MODE_AUTO)).place(x=92, y=30)
        Button(detail, text='MANUAL', bg='#ffffcc', width=button_width, command=lambda: send_message(ac.DETAIL_LEVEL_MODE_MANUAL)).place(x=185, y=30)

        # ---------------------------------  LEVEL DETAIL  ---------------------------------------------------


        Button(detail,font=('Colibri',8 ), text='RESET DETAIL', width=13, bg='white',  command=lambda:reset_detail()).place(x=gain_x+150, y=gain_y+50)

        def LEVEL_detail(level_value):
            lbl_level = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text=level_value).place(x=gain_x+100, y=gain_y+50)
            level_convertido= ct.DETAIL_LEVEL_table.get(int(level_value))
            level_message =ac.DETAIL_LEVEL_Direct.replace('p', str(level_convertido)) #'81 01 04 42 00 00 00 pp FF'  # pp: 00 - 0F (0 - 15)
            print (level_message)
            send_message(level_message)
            return level_message

        RG = IntVar()

        def reset_detail():
            RG.set(0)
            lbl_R_G = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+50)
            detail_Reset_Message = '81 01 04 02 00 FF'  
            send_message(detail_Reset_Message)

        RG.set(0)

        RG_value = Scale(detail, label='LEVEL', from_=-7, to=8,variable=RG, orient=HORIZONTAL, length=260, showvalue=0, resolution=1, command=LEVEL_detail).place(x=gain_x, y=gain_y+50)
        Button(detail,font=('Colibri',7 ), text='RESET DETAIL', width=13, bg='white',  command=lambda:reset_detail()).place(x=gain_x+170, y=gain_y+50)
        lbl_R_G = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+50)


        # ---------------------------------  BANDWIDTH DETAIL  ---------------------------------------------------

        def BANDWIDTH_detail(bw_value):
            show_bd= ct.DETAIL_BANDWIDTH_lbl.get(int(bw_value)) # OBTIENE EL VALOR A MOSTRAR
            lbl_bw = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text=show_bd).place(x=gain_x+100, y=gain_y+90) #MUESTA EL VALOR EN LA PANTALLA CONVERTIDO
            bw_convertido= ct.DETAIL_BANDWIDTH_table.get(int(bw_value))
            bw_message = ac.DETAIL_LEVEL_BANDWIDTH.replace('p', str(bw_value))
            print (bw_message)
            send_message(bw_message)
            return bw_message

        BW = IntVar()

        def reset_bw():
            BW.set(0)
            lbl_bw = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text='DEFAULT').place(x=gain_x+100, y=gain_y+90)
            bw_Reset_Message = '81 01 04 03 00 FF'
            send_message(bw_Reset_Message)

        BW.set(0)

        BW_value = Scale(detail, label='BANDWIDTH', from_=0, to=4,variable=BW, orient=HORIZONTAL, length=260, showvalue=0, resolution=1, command=BANDWIDTH_detail).place(x=gain_x, y=gain_y+90)
        Button(detail,font=('Colibri',7 ), text='RESET BW', width=13, bg='white',  command=lambda:reset_bw()).place(x=gain_x+170, y=gain_y+90)
        #lbl_bw = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text='DEFAULT').place(x=gain_x+100, y=gain_y+90)







        # ---------------------------------  DETAIL_LEVEL_CRISPENING  ---------------------------------------------------

        Button(detail,font=('Colibri',8 ), text='RESET CRISP.', width=13, bg='white',  command=lambda:reset_crispening()).place(x=gain_x+150, y=gain_y+130)     

        def DETAIL_LEVEL_CRISPENING(crispening_value):
            lbl_crispening = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text=crispening_value).place(x=gain_x+100, y=gain_y+130)      
            #crispening_convertido= ct.DETAIL_LEVEL_CRISPENING_table.get(int(crispening_value))
            crispening_message = ac.DETAIL_LEVEL_CRISPENING.replace('p', str(crispening_value))
            print (crispening_message)
            send_message(crispening_message)
            return crispening_message

        CR = IntVar()

        def reset_crispening():
            CR.set(0)
            lbl_crispening = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+130)
            crispening_Reset_Message = '81 01 05 42 03 00 FF'
            send_message(crispening_Reset_Message)

        CR.set(0)

        CR_value = Scale(detail, label='CRISPENING', from_=0, to=7,variable=CR, orient=HORIZONTAL, length=260, showvalue=0, resolution=1, command=DETAIL_LEVEL_CRISPENING).place(x=gain_x, y=gain_y+130)
        Button(detail,font=('Colibri',7 ), text='RESET CRISP.', width=13, bg='white',  command=lambda:reset_crispening()).place(x=gain_x+170, y=gain_y+130)
        lbl_crispening = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+130)


        # ---------------------------------  DETAIL_H_V_BALANCE  ---------------------------------------------------

        Button(detail,font=('Colibri',8 ), text='RESET HV', width=13, bg='white',  command=lambda:reset_hv()).place(x=gain_x+150, y=gain_y+170)

        def DETAIL_H_V_BALANCE(hv_value):
            show_hv= ct.DETAIL_H_V_BALANCE_lvl.get(int(hv_value)) # OBTIENE EL VALOR A MOSTRAR
            lbl_hv = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text=show_hv).place(x=gain_x+100, y=gain_y+170) # MUESTA EL VALOR EN LA PANTALLA CONVERTIDO en string
            hv_message = ac.DETAIL_H_V_BALANCE.replace('p', str(hv_value))
            print (hv_message)
            send_message(hv_message)
            return hv_message

        HV = IntVar()

        def reset_hv():
            HV.set(7)
            lbl_hv = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+170)
            hv_Reset_Message = '81 01 05 42 04 07 FF'
            send_message(hv_Reset_Message)


        HV.set(7)

        HV_value = Scale(detail, label='HV', from_=5, to=9,variable=HV, orient=HORIZONTAL, length=260, showvalue=0, resolution=1, command=DETAIL_H_V_BALANCE).place(x=gain_x, y=gain_y+170)
        Button(detail,font=('Colibri',7 ), text='RESET HV', width=13, bg='white',  command=lambda:reset_hv()).place(x=gain_x+170, y=gain_y+170)
        lbl_hv = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+170)


        # ---------------------------------  DETAIL_B_W_BALANCE ---------------------------------------------------


        Button(detail,font=('Colibri',8 ), text='RESET BW', width=13, bg='white',  command=lambda:reset_bw()).place(x=gain_x+150, y=gain_y+210)

        def DETAIL_B_W_BALANCE(bw_value):
            show_bw= ct.DETAIL_B_W_BALANCE_lvl.get(int(bw_value))
            lbl_bw = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text=show_bw).place(x=gain_x+100, y=gain_y+210)
            bw_message = ac.DETAIL_B_W_BALANCE.replace('p', str(bw_value))
            print (bw_message)
            send_message(bw_message)
            return bw_message

        BW = IntVar()

        def reset_bw():
            BW.set(0)
            lbl_bw = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text='TYPE1').place(x=gain_x+100, y=gain_y+210)
            bw_Reset_Message = '81 01 05 42 05 00 FF'
            send_message(bw_Reset_Message)

        BW.set(0)

        BW_value = Scale(detail, label='BW', from_=0, to=4,variable=BW, orient=HORIZONTAL, length=260, showvalue=0, resolution=1, command=DETAIL_B_W_BALANCE).place(x=gain_x, y=gain_y+210)
        Button(detail,font=('Colibri',7 ), text='RESET BW', width=13, bg='white',  command=lambda:reset_bw()).place(x=gain_x+170, y=gain_y+210)
        lbl_bw = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text='TYPE1').place(x=gain_x+100, y=gain_y+210)


        # ---------------------------------  DETAIL_LIMIT ---------------------------------------------------

        Button(detail,font=('Colibri',8 ), text='RESET LIMIT', width=13, bg='white',  command=lambda:reset_limit()).place(x=gain_x+150, y=gain_y+250)

        def DETAIL_LIMIT(limit_value):  
            #show_limit= ct.DETAIL_LIMIT_lvl.get(int(limit_value))
            lbl_limit = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text=limit_value).place(x=gain_x+100, y=gain_y+250)
            limit_message = ac.DETAIL_LIMIT.replace('p', str(limit_value))
            print (limit_message)
            send_message(limit_message)
            return limit_message

        LIMIT = IntVar()

        def reset_limit():
            LIMIT.set(0)
            lbl_limit = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+250)
            limit_Reset_Message = '81 01 05 42 06 00 FF'
            send_message(limit_Reset_Message)

        LIMIT.set(0)
        
        LIMIT_value = Scale(detail, label='LIMIT', from_=0, to=7,variable=LIMIT, orient=HORIZONTAL, length=260, showvalue=0, resolution=1, command=DETAIL_LIMIT).place(x=gain_x, y=gain_y+250)
        Button(detail,font=('Colibri',7 ), text='RESET LIMIT', width=13, bg='white',  command=lambda:reset_limit()).place(x=gain_x+170, y=gain_y+250)
        lbl_limit = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+250)


        # ---------------------------------  HIGHLIGHT_DETAIL ---------------------------------------------------

        Button(detail,font=('Colibri',8 ), text='RESET HLT', width=13, bg='white',  command=lambda:reset_HLT()).place(x=gain_x+150, y=gain_y+250)

        def DETAIL_HLT(HLT_value):  
            lbl_HLT = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text=HLT_value).place(x=gain_x+100, y=gain_y+250)
            HLT_message = ac.DETAIL_HLT.replace('p', str(HLT_value))
            print (HLT_message)
            send_message(HLT_message)
            return HLT_message

        HLT = IntVar()

        def reset_HLT():
            HLT.set(0)
            lbl_HLT = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+250)
            HLT_Reset_Message = '81 01 05 42 07 00 FF'
            send_message(HLT_Reset_Message)

        HLT.set(0)

        HLT_value = Scale(detail, label='HLT', from_=0, to=4,variable=HLT, orient=HORIZONTAL, length=260, showvalue=0, resolution=1, command=DETAIL_HLT).place(x=gain_x, y=gain_y+250)
        Button(detail,font=('Colibri',7 ), text='RESET HLT', width=13, bg='white',  command=lambda:reset_HLT()).place(x=gain_x+170, y=gain_y+250)
        lbl_HLT = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+250)

        
        # ---------------------------------  SUPERLOW_Direct ---------------------------------------------------

        Button(detail,font=('Colibri',8 ), text='RESET SLOW', width=13, bg='white',  command=lambda:reset_SLOW()).place(x=gain_x+150, y=gain_y+250)

        def DETAIL_SLOW(SLOW_value):
            lbl_SLOW = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text=SLOW_value).place(x=gain_x+100, y=gain_y+250)
            SLOW_message = ac.DETAIL_SLOW.replace('p', str(SLOW_value))
            print (SLOW_message)
            send_message(SLOW_message)
            return SLOW_message


        SLOW = IntVar()

        def reset_SLOW():
            SLOW.set(0)
            lbl_SLOW = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+250)
            SLOW_Reset_Message = '81 01 05 42 08 00 FF'
            send_message(SLOW_Reset_Message)

        SLOW.set(0)

        SLOW_value = Scale(detail, label='SLOW', from_=0, to=7,variable=SLOW, orient=HORIZONTAL, length=260, showvalue=0, resolution=1, command=DETAIL_SLOW).place(x=gain_x, y=gain_y+250)
        Button(detail,font=('Colibri',7 ), text='RESET SLOW', width=13, bg='white',  command=lambda:reset_SLOW()).place(x=gain_x+170, y=gain_y+250)
        lbl_SLOW = Label(detail, bg='gray13', fg='#54f706', width="8", justify="center", text='0').place(x=gain_x+100, y=gain_y+250)



    













        root.mainloop()



def main():
    mi_app_1 = Aplicacion()
    return 0



if __name__ == '__main__':
    main()
