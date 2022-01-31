
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import socket
import struct
import binascii # for printing the messages we send, not really necessary
from time import sleep
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from tkinter import ttk

camera_ip = '10.50.2.145' # default 
camera_port = 52381  # default de Sony para Visca
free_D_port = 40000   # puerto de escucha de freeD 
pan_speed = "10"  # asigno misma velocidad al pan y al tilt
tilt_speed = "10"
zoom_speed = "3"
zoom_tele_variable = '81 01 04 07 23 FF' # p=0 (Low) to 7 (High)
zoom_wide_variable = '81 01 04 07 33 FF' # p=0 (Low) to 7 (High)

class Aplicacion():
    def __init__(self):




        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # IPv4, UDP
        # for receiving
        buffer_size = 1024
        #s.bind(('', camera_port)) # use the port one higher than the camera's port
        #s.settimeout(1) # only wait for a response for 1 second


        # Payloads
        #received_message = '' # a place to store the OSC messages we'll receive
        sequence_number = 1 # a global variable that we'll iterate each command, remember 0x0001
        #reset_sequence_number = '02 00 00 01 00 00 00 01 01'

        # encendido y apagado de la camara

        camera_on = '81 01 04 00 02 FF'
        camera_off = '81 01 04 00 03 FF'
        # encendido y apagado del Display
        information_display_on = '81 01 7E 01 18 02 FF'
        information_display_off = '81 01 7E 01 18 03 FF'

        # movimientos del Zoom

        zoom_stop =          '81 01 04 07 00 FF'
        zoom_tele =          '81 01 04 07 02 FF'
        zoom_wide =          '81 01 04 07 03 FF'

        zoom_direct = '81 01 04 47 0p 0q 0r 0s FF' # pqrs: Zoom Position

        zoomx1 = '81 01 04 47 00 00 00 00 FF' 
        zoomx2 = '81 01 04 47 01 08 00 00 FF' 
        zoomx3 = '81 01 04 47 02 03 04 00 FF' 
        zoomx4 = '81 01 04 47 02 0A 04 00 FF' 
        zoomx5 = '81 01 04 47 02 0F 00 00 FF' 
        zoomx6 = '81 01 04 47 03 03 00 00 FF' 
        zoomx7 = '81 01 04 47 03 06 00 00 FF' 
        zoomx8 = '81 01 04 47 03 08 08 00 FF' 
        zoomx9 = '81 01 04 47 03 0A 0C 00 FF' 
        zoomx10 = '81 01 04 47 03 0C 0C 00 FF' 
        zoomx11 = '81 01 04 47 03 0E 08 00 FF' 
        zoomx12 = '81 01 04 47 04 00 00 00 FF' 





        # manejo de Memorias

        memory_reset = '81 01 04 3F 00 0p FF'
        memory_set = '81 01 04 3F 01 0p FF' # p: Memory number (=0 to F)
        memory_recall = '81 01 04 3F 02 0p FF' # p: Memory number (=0 to F)


        #def memory_reset_function(memory_reset):
        #    message = send_message( '81 01 04 3F 00 0p FF')
        #    return message


        #Pan-tilt Drive
        # VV: Pan speed setting 0x01 (low speed) to 0x18
        # WW: Tilt speed setting 0x01 (low speed) to 0x17

        # YYYY: Pan Position DE00 to 2200 (CENTER 0000)
        # ZZZZ: Tilt Position FC00 to 1200 (CENTER 0000)
        #YYYY = '0000'
        #ZZZZ = '0000'






        pan_up = '81 01 06 01 VV WW 03 01 FF'
        pan_down = '81 01 06 01 VV WW 03 02 FF'
        pan_left = '81 01 06 01 VV WW 01 03 FF'
        pan_right = '81 01 06 01 VV WW 02 03 FF'
        pan_up_left = '81 01 06 01 VV WW 01 01 FF'
        pan_up_right = '81 01 06 01 VV WW 02 01 FF'
        pan_down_left = '81 01 06 01 VV WW 01 02 FF'
        pan_down_right = '81 01 06 01 VV WW 02 02 FF'
        pan_stop = '81 01 06 01 VV WW 03 03 FF'



        #pan_absolute_position = '81 01 06 02 VV WW 0Y 0Y 0Y 0Y 0Z 0Z 0Z 0Z FF'.replace('VV', str(VV)) #YYYY[0]
        #pan_relative_position = '81 01 06 03 VV WW 0Y 0Y 0Y 0Y 0Z 0Z 0Z 0Z FF'.replace('VV', str(VV))
        pan_home = '81 01 06 04 FF'
        pan_reset = '81 01 06 05 FF'
        zoom_direct = '81 01 04 47 0p 0q 0r 0s FF' # pqrs: Zoom Position
        zoom_focus_direct = '81 01 04 47 0p 0q 0r 0s 0t 0u 0v 0w FF' # pqrs: Zoom Position  tuvw: Focus Position

        inquiry_lens_control = '81 09 7E 7E 00 FF'
        # response: 81 50 0p 0q 0r 0s 0H 0L 0t 0u 0v 0w 00 xx xx FF
        inquiry_camera_control = '81 09 7E 7E 01 FF'

        focus_stop = '81 01 04 08 00 FF'
        focus_far = '81 01 04 08 01 FF'
        focus_near = '81 01 04 08 01 FF'
        focus_far_variable = '81 01 04 08 2p FF'.replace('p', '2') # 0 low to 7 high
        focus_near_variable = '81 01 04 08 3p FF'.replace('p', '2') # 0 low to 7 high
        focus_direct = '81 01 04 48 0p 0q 0r 0s FF' #.replace('p', ) q, r, s
        focus_auto = '81 01 04 38 02 FF'
        focus_manual = '81 01 04 38 03 FF'
        focus_infinity = '81 01 04 18 02 FF'

        def show_values():
            print (zoom_speed_slider.get())

        def scaleFunc(val):
            scaleVal = int(zoom_speed_slider.get())
            if int(scaleVal) != scaleVal:
                zoom_speed_slider.set(int(val))

        def memory_reset_function(memory_number):
            message_string = memory_set.replace('p', str(memory_number))
            message = send_message(message_string)
            return message

        def memory_recall_function(memory_number):
            message_string = memory_recall.replace('p', str(memory_number))
            send_message(information_display_off) # otherwise we see a message on the camera output
            sleep(0.25)
            message = send_message(message_string)
            sleep(1)
            send_message(information_display_off)
            return message

        def memory_set_function(memory_number):
            message_string = memory_set.replace('p', str(memory_number))
            message = send_message(message_string)
            return message

        def send_message(message_string):
            global sequence_number
            global received_message
            message_string = (message_string).replace('VV', str(pan_speed)).replace('WW', str(tilt_speed))
            print(message_string)
            payload_type = bytearray.fromhex('01 00')
            payload = bytearray.fromhex(message_string)
            payload_length = len(payload).to_bytes(2, 'big')
            message = payload_type + payload_length + sequence_number.to_bytes(4, 'big') + payload # aca se arma el mensaje 
            sequence_number += 1
            s.sendto(message, (camera_ip, camera_port))
            print(binascii.hexlify(message), 'sent to', camera_ip, camera_port, sequence_number)
            received_message = 'test'
            return received_message

        def reset_sequence_number_function():
            global sequence_number
            reset_sequence_number_message = bytearray.fromhex('02 00 00 01 00 00 00 01 01')
            s.sendto(reset_sequence_number_message,(camera_ip, camera_port))
            sequence_number = 1
            return sequence_number

        def store_network_values(ip_value, port_value): # seleccionamos la ip de la camara
            global camera_ip
            global camera_port
            camera_ip = ip_value
            camera_port = port_value
            # IP Label
            lbl2=Label(ip_port_1, background="gray13", fg="#54f706", width="30", justify="center", text="Connected to:  " +str(camera_ip) +':'+str(camera_port)).place(x=15, y=26)
            print(camera_ip, camera_port)
            return camera_ip, camera_port

        # esto esta  para completar mas tarde

        def read_freeD ():
            global free_D_data

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind(('', 40001))
            mreq = struct.pack("=4sl", socket.inet_aton("10.50.2.6"), socket.INADDR_ANY)
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
            while True:
                codigo = sock.recv(1024)
                print(binascii.b2a_hex(codigo))


        def set_pt_speed():
            zoom_speed = "1"
            global zoom_tele_variable , zoom_wide_variable , pan_speed , tilt_speed

            pan_speed = 1 # asigno al pan y al tilt
            tilt_speed = 1

            pan_speed = hex(pan_speed_slider.get())[2:]
            tilt_speed = hex(tilt_speed_slider.get())[2:]


            if len(pan_speed) == 1:
                pan_speed = '0'+pan_speed # asigno al pan 
            if len(tilt_speed) == 1:
                tilt_speed = '0'+tilt_speed # asigno al tilt

            pan_up = '81 01 06 01 VV WW 03 01 FF'.replace('VV', str(pan_speed)).replace('WW', str(tilt_speed))
            pan_down = '81 01 06 01 VV WW 03 02 FF'.replace('VV', str(pan_speed)).replace('WW', str(tilt_speed))
            pan_left = '81 01 06 01 VV WW 01 03 FF'.replace('VV', str(pan_speed)).replace('WW', str(tilt_speed))
            pan_right = '81 01 06 01 VV WW 02 03 FF'.replace('VV', str(pan_speed)).replace('WW', str(tilt_speed))
            pan_up_left = '81 01 06 01 VV WW 01 01 FF'.replace('VV', str(pan_speed)).replace('WW', str(tilt_speed))
            pan_up_right = '81 01 06 01 VV WW 02 01 FF'.replace('VV', str(pan_speed)).replace('WW', str(tilt_speed))
            pan_down_left = '81 01 06 01 VV WW 01 02 FF'.replace('VV', str(pan_speed)).replace('WW', str(tilt_speed))
            pan_down_right = '81 01 06 01 VV WW 02 02 FF'.replace('VV', str(pan_speed)).replace('WW', str(tilt_speed))
            pan_stop = '81 01 06 01 VV WW 03 03 FF'.replace('VV', str(pan_speed)).replace('WW', str(tilt_speed))
            
            print( pan_speed,  tilt_speed )


        def get_current_value():
            return '{: .2f}'.format(current_value.get())

        def slider_changed(event):
            value_label.configure(text=get_current_value())

       

        def set_zoom_speed():
           
            global zoom_tele_variable , zoom_wide_variable 
           
            zoom_speed= zoom_speed_slider.get()

            zoom_tele_variable = '81 01 04 07 2p FF'.replace('p', str(zoom_speed)) # p=0 (Low) to 7 (High)
            zoom_wide_variable = '81 01 04 07 3p FF'.replace('p', str(zoom_speed)) # p=0 (Low) to 7 (High)
            
            print( zoom_speed)


        # start by resetting the sequence number
        reset_sequence_number_function()


        store_y = 10
        label_y = 150
        recall_y = 5
        recall_x= 5
        pan_tilt_y = 5
        pan_tilt_x = 10
        speed_y =1000
        speed_x =100
        zoom_y = 5
        zoom_x = 4
        focus_y = 9
        focus_x = 10
        on_off_y = 30
        on_off_x = 13
        button_width = 8

        store_color = 'red'
        recall_color = 'light grey'
        pan_tilt_color = 'light blue'
        zoom_color = '#fF8204'
        focus_color = 'cyan'
        on_off_color = 'violet'





        
        # ----------------------------- GUI -------------------------------------------------------------------
        root = Tk()
        display_message = StringVar()
        root.title('Visca Conntroler V1')
        #Label(root, text='CONTROL DE CAMARAS CANAL DE LA CIUDAD Version 0.0.7').place(x=10, y=200)
        root.resizable(False, False)
        root.config(bg="grey")
        root.config(width="255", height="800")
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

        ip_port_1=Frame(root)
        ip_port_1.pack(fill="y")
        ip_port_1.config(bg="grey13")
        ip_port_1.place(x=10, y=10)
        ip_port_1.config(width="240", height="60")
        ip_port_1.config(bd="5")
        ip_port_1.config(relief="groove") #Groove, sunken etc


        # IP
        lbl1=Label(ip_port_1,background="gray13", fg="#54f706", width="8", justify="center", text='CAMARA IP').place(x=7, y=5)
        ip_value = Entry(ip_port_1, width=15, justify="center", background="#54f706", )
        ip_value.place(x=80, y= 5)
        ip_value.insert(0, camera_ip)

        # Save ip
        Button(ip_port_1,  height=1, width=8, font=('Colibri', 7 ), text='SET', command=lambda: store_network_values(ip_value.get(), camera_port)).place(x=170, y=5)
        lbl2=Label(ip_port_1,background="gray13", fg="#54f706", width="20", justify="center", text='---------------------').place(x=25, y=26)


        # Pan and tilt buttons

        move=Frame(root)
        move.config(bg="grey")
        move.place(x=10, y=70)
        move.config(width="120", height="140")
        move.config(bd="5")
        move.config(relief="sunken") #Groove, sunken etc

        Button(move, text='↑', width=3, bg=pan_tilt_color, command=lambda: send_message(pan_up)).place(x=pan_tilt_x+35, y=pan_tilt_y)
        Button(move, text='←', width=3, bg=pan_tilt_color, command=lambda: send_message(pan_left)).place(x=pan_tilt_x, y=pan_tilt_y+35)
        Button(move, text='→', width=3, bg=pan_tilt_color, command=lambda: send_message(pan_right)).place(x=pan_tilt_x+70, y=pan_tilt_y+35)
        Button(move, text='↓', width=3, bg=pan_tilt_color, command=lambda: send_message(pan_down)).place(x=pan_tilt_x+35, y=pan_tilt_y+70)
        Button(move, text='↖', width=3, bg=pan_tilt_color, command=lambda: send_message(pan_up_left)).place(x=pan_tilt_x, y=pan_tilt_y)
        Button(move, text='↗', width=3, bg=pan_tilt_color, command=lambda: send_message(pan_up_right)).place(x=pan_tilt_x+70, y=pan_tilt_y)
        Button(move, text='↙', width=3, bg=pan_tilt_color, command=lambda: send_message(pan_down_left)).place(x=pan_tilt_x, y=pan_tilt_y+70)
        Button(move, text='↘', width=3, bg=pan_tilt_color, command=lambda: send_message(pan_down_right)).place(x=pan_tilt_x+70, y=pan_tilt_y+70)
        Button(move, text='■', width=3, bg=pan_tilt_color, command=lambda: send_message(pan_stop)).place(x=pan_tilt_x+35, y=pan_tilt_y+35)
        Button(move,font=('Colibri', 7 ),width=11, bg=pan_tilt_color, text='Home', command=lambda: send_message(pan_home)).place(x=pan_tilt_x+15, y=pan_tilt_y+103)



        #------------------ Pan speed and Tilt speed-----------------------




        pts=Frame(root)
        #pts.pack(fill="y", expand="true")
        pts.config(bg="grey")
        pts.place(x=135, y=70)
        pts.config(width="110", height="140")
        pts.config(bd="5")
        pts.config(relief="sunken") #Groove, sunken etc


        #Label(pts, text='P Speed', bg=pan_tilt_color).place(x= pan_tilt_x , y= pan_tilt_y)

        #pan_speed_slider = ttk.Scale(pts, from_= 18, to=0, command=scaleFunc, length=None , orient = 'vertical' )
        pan_speed_slider = Scale(pts, from_=18, to=0, bg=pan_tilt_color , font=('Colibri', 7 ),width=10, length=90 )
        pan_speed_slider.set(10)
        pan_speed_slider.place(x= pan_tilt_x, y= pan_tilt_y)

        #Label(pts, text='T Speed', bg=pan_tilt_color).place(x= pan_tilt_x +55 , y= pan_tilt_y)

        tilt_speed_slider = Scale(pts, from_=18, to=0, bg=pan_tilt_color ,  font=('Colibri', 7 ),width=10, length=90)
        tilt_speed_slider.set(10)
        tilt_speed_slider.place(x= pan_tilt_x +50, y= pan_tilt_y)


        Button(pts, font=('Colibri', 7 ),width=11, text='Set PT Speed', bg="light green", command=lambda: set_pt_speed()).place(x= pan_tilt_x+5 , y= pan_tilt_y+103)

        # -------------------------- controles de zoom   ------------------


        zoom=Frame(root)
        zoom.pack(fill="y")
        zoom.config(bg="grey")
        zoom.place(x=10, y=210)
        zoom.config(width="235", height="140")
        zoom.config(bd="5")
        zoom.config(relief="sunken") #Groove, sunken etc

        Button(zoom,font=('Colibri', 7 ), text='Zoom In', height=2, width=10, bg= zoom_color, justify ="center", command=lambda: send_message(zoom_tele_variable)).place(x=zoom_x, y=zoom_y)
        Button(zoom, font=('Colibri', 7 ),text='Zoom Stop',height=2,width=10, bg= zoom_color, justify ="center",command=lambda: send_message(zoom_stop)).place(x=zoom_x+75, y=zoom_y)
        Button(zoom, font=('Colibri', 7 ),text='Zoom Out', height=2, width=10, bg= zoom_color, justify ="center", command=lambda: send_message(zoom_wide_variable)).place(x=zoom_x+150, y=zoom_y)

        #Label(pts, text='Z Speed', bg=zoom_color).place(x= pan_tilt_x +110 , y= pan_tilt_y)

        zoom_speed_slider = Scale(zoom, from_=0, to=7, bg=zoom_color ,font=('Colibri', 7 ), orient= 'horizontal', width=10, length=125 )
        zoom_speed_slider.set(3)
        zoom_speed_slider.place(x= pan_tilt_x +2, y= pan_tilt_y+35)

        Button(zoom, font=('Colibri', 7 ),width=12, height=2, text='Set Zoom speed', bg=zoom_color, command=lambda: set_zoom_speed()).place(x= pan_tilt_x+135 , y= pan_tilt_y+35)

        Label(zoom, font=('Colibri', 7 ), width=35,background="gray13", fg="#54f706", text='Zoom Ratio X ').place(x=recall_x, y= recall_y+80)

        Button(zoom, font=('Colibri', 7 ), bg=zoom_color, width=1, text=1, command=lambda: send_message(zoomx1)).place(x=recall_x, y= recall_y+100)
        Button(zoom, font=('Colibri', 7 ), bg=zoom_color, width=1, text=2, command=lambda: send_message(zoomx2)).place(x=recall_x+20, y= recall_y+100)
        Button(zoom, font=('Colibri', 7 ), bg=zoom_color, width=1, text=3, command=lambda: send_message(zoomx3)).place(x=recall_x+40, y=recall_y+100)
        Button(zoom, font=('Colibri', 7 ), bg=zoom_color, width=1, text=4, command=lambda: send_message(zoomx4)).place(x=recall_x+60, y=recall_y+100)
        Button(zoom, font=('Colibri', 7 ), bg=zoom_color, width=1, text=5, command=lambda: send_message(zoomx5)).place(x=recall_x+80, y=recall_y+100)
        Button(zoom, font=('Colibri', 7 ), bg=zoom_color, width=1, text=6, command=lambda: send_message(zoomx6)).place(x=recall_x+100, y=recall_y+100)
        Button(zoom, font=('Colibri', 7 ), bg=zoom_color, width=1, text=7, command=lambda: send_message(zoomx7)).place(x=recall_x+120, y= recall_y+100)
        Button(zoom, font=('Colibri', 7 ), bg=zoom_color, width=1, text=8, command=lambda: send_message(zoomx8)).place(x=recall_x+140, y= recall_y+100)
        Button(zoom, font=('Colibri', 7 ), bg=zoom_color, width=1, text=9, command=lambda: send_message(zoomx9)).place(x=recall_x+160, y=recall_y+100)
        Button(zoom, font=('Colibri', 7 ), bg=zoom_color, width=1, text=10, command=lambda: send_message(zoomx10)).place(x=recall_x+180, y=recall_y+100)
        Button(zoom, font=('Colibri', 7 ), bg=zoom_color, width=1, text=11, command=lambda: send_message(zoomx11)).place(x=recall_x+200, y=recall_y+100)


        # ----------------------------------------------------------------BOTONES DE FOCO -------------------------------------

        foc=Frame(root)
        #foc.pack(fill="y", expand="true")
        foc.config(bg="grey")
        foc.place(x=10, y=380)
        foc.config(width="235", height="140")
        foc.config(bd="5")
        foc.config(relief="sunken") #Groove, sunken etc


        Button(foc,font=('Colibri', 7 ),width=10, text='Focus Auto', bg=focus_color, command=lambda: send_message(focus_auto)).place(x=focus_x, y=focus_y)
        Button(foc,font=('Colibri', 7 ),width=10, text='Focus Manual',bg=focus_color, command=lambda: send_message(focus_manual)).place(x=focus_x+120, y=focus_y)

        Button(foc, font=('Colibri', 7 ),width=10, text='FOCUS ↑', bg=focus_color, command=lambda: send_message(focus_far_variable)).place(x=focus_x, y=focus_y+30)
        Button(foc,font=('Colibri', 7 ),width=10, text='STOP', bg=focus_color, command=lambda: send_message(focus_stop)).place(x=focus_x, y=focus_y+60)
        Button(foc, font=('Colibri', 7 ),width=10, text='FOCUS ↓', bg=focus_color, command=lambda: send_message(focus_near_variable)).place(x=focus_x, y=focus_y+90)

        Button(foc,font=('Colibri', 7 ),width=10, text='Focus Far', bg=focus_color, command=lambda: send_message(focus_far)).place(x=focus_x +120, y=focus_y+30)
        Button(foc,font=('Colibri', 7 ),width=10, text='Focus Near', bg=focus_color, command=lambda: send_message(focus_near)).place(x=focus_x+120, y=focus_y+60)
        Button(foc, font=('Colibri', 7 ),width=10,text='Focus Infinity', bg=focus_color, command=lambda: send_message(focus_infinity)).place(x=focus_x+120, y=focus_y+90)


        # --------------------------On off connect buttons ----------------------------


        on_off=Frame(root)
        #on_off.pack(fill="y", expand="true")
        on_off.config(bg="grey")
        on_off.place(x=25, y=560)
        on_off.config(width="235", height="140")
        on_off.config(bd="5")
        on_off.config(relief="sunken") #Groove, sunken etc

        Button(on_off, text='On', bg=on_off_color, width=button_width, command=lambda: send_message(camera_on)).grid(row=on_off_x, column=on_off_y)

        Label(on_off, text='Camera', bg=on_off_color, width=button_width).grid(row=on_off_x, column=on_off_y+30)
        #Button(on_off, text='Connect', bg=on_off_color, width=button_width, command=reset_sequence_number_function()).grid(row=on_off_x, column=on_off_y+30)
        Button(on_off, text='Off', bg=on_off_color, width=button_width, command=lambda: send_message(camera_off)).grid(row=on_off_x, column=on_off_y+60)




        # ----------------------llamada a memorias ----------------------------------------------------------------

        Label(root,width="30",background="gray13", fg="#54f706", text='Presets Recall ').place(x=20, y=600)
        mem=Frame(root)
        mem.pack(fill="y")
        mem.config(bg="grey")
        mem.place(x=20, y=620)
        mem.config(width="218", height="75")
        mem.config(bd="5")
        mem.config(relief="sunken") #Groove, sunken etc


        Button(mem, font=('Colibri', 7 ), width=2, text=1, command=lambda: memory_recall_function(0)).place(x=recall_x, y= recall_y)
        Button(mem, font=('Colibri', 7 ), width=2, text=2, command=lambda: memory_recall_function(1)).place(x=recall_x+25, y= recall_y)
        Button(mem, font=('Colibri', 7 ), width=2, text=3, command=lambda: memory_recall_function(2)).place(x=recall_x+50, y=recall_y)
        Button(mem, font=('Colibri', 7 ), width=2, text=4, command=lambda: memory_recall_function(3)).place(x=recall_x+75, y=recall_y)
        Button(mem, font=('Colibri', 7 ), width=2, text=5, command=lambda: memory_recall_function(4)).place(x=recall_x+100, y=recall_y)
        Button(mem, font=('Colibri', 7 ), width=2, text=6, command=lambda: memory_recall_function(5)).place(x=recall_x+125, y=recall_y)
        Button(mem, font=('Colibri', 7 ), width=2, text=7, command=lambda: memory_recall_function(6)).place(x=recall_x+150, y= recall_y)
        Button(mem, font=('Colibri', 7 ), width=2, text=8, command=lambda: memory_recall_function(7)).place(x=recall_x+175, y= recall_y)
        Button(mem, font=('Colibri', 7 ), width=2, text=9, command=lambda: memory_recall_function(8)).place(x=recall_x, y=recall_y+30)
        Button(mem, font=('Colibri', 7 ), width=2, text=10, command=lambda: memory_recall_function(9)).place(x=recall_x+25, y=recall_y+30)
        Button(mem, font=('Colibri', 7 ), width=2, text=11, command=lambda: memory_recall_function(10)).place(x=recall_x+50, y=recall_y+30)
        Button(mem, font=('Colibri', 7 ), width=2, text=12, command=lambda: memory_recall_function(11)).place(x=recall_x+75, y= recall_y+30)
        Button(mem, font=('Colibri', 7 ), width=2, text=13, command=lambda: memory_recall_function(12)).place(x=recall_x+100, y=recall_y+30)
        Button(mem, font=('Colibri', 7 ), width=2, text=14, command=lambda: memory_recall_function(13)).place(x=recall_x+125, y=recall_y+30)
        Button(mem, font=('Colibri', 7 ), width=2, text=15, command=lambda: memory_recall_function(14)).place(x=recall_x+150, y=recall_y+30)
        Button(mem, font=('Colibri', 7 ), width=2, text=16, command=lambda: memory_recall_function(15)).place(x=recall_x+175, y=recall_y+30)



        # ----------------------grabado a memorias ----------------------------------------------------------------

        Label(root,width="30",background="gray13", fg="#54f706", text='Presets Store ').place(x=20, y=700)
        mem_rec=Frame(root)
        mem_rec.pack(fill="y")
        mem_rec.config(bg="grey")
        mem_rec.place(x=20, y=720)
        mem_rec.config(width="218", height="75")
        mem_rec.config(bd="5")
        mem_rec.config(relief="sunken") #Groove, sunken etc



        Button(mem_rec, font=('Colibri', 7 ), width=2, bg=store_color, text=1, command=lambda: memory_set_function(0)).place(x=recall_x, y= recall_y)
        Button(mem_rec, font=('Colibri', 7 ), width=2, bg=store_color, text=2, command=lambda: memory_set_function(1)).place(x=recall_x+25, y= recall_y)
        Button(mem_rec, font=('Colibri', 7 ), width=2, bg=store_color, text=3, command=lambda: memory_set_function(2)).place(x=recall_x+50, y=recall_y)
        Button(mem_rec, font=('Colibri', 7 ), width=2, bg=store_color, text=4, command=lambda: memory_set_function(3)).place(x=recall_x+75, y=recall_y)
        Button(mem_rec, font=('Colibri', 7 ), width=2, bg=store_color, text=5, command=lambda: memory_set_function(4)).place(x=recall_x+100, y=recall_y)
        Button(mem_rec, font=('Colibri', 7 ), width=2, bg=store_color, text=6, command=lambda: memory_set_function(5)).place(x=recall_x+125, y=recall_y)
        Button(mem_rec, font=('Colibri', 7 ), width=2, bg=store_color, text=7, command=lambda: memory_set_function(6)).place(x=recall_x+150, y= recall_y)
        Button(mem_rec, font=('Colibri', 7 ), width=2, bg=store_color, text=8, command=lambda: memory_set_function(7)).place(x=recall_x+175, y= recall_y)
        Button(mem_rec, font=('Colibri', 7 ), width=2, bg=store_color, text=9, command=lambda: memory_set_function(8)).place(x=recall_x, y=recall_y+30)
        Button(mem_rec, font=('Colibri', 7 ), width=2, bg=store_color, text=10, command=lambda: memory_set_function(9)).place(x=recall_x+25, y=recall_y+30)
        Button(mem_rec, font=('Colibri', 7 ), width=2, bg=store_color, text=11, command=lambda: memory_set_function(10)).place(x=recall_x+50, y= recall_y+30)
        Button(mem_rec, font=('Colibri', 7 ), width=2, bg=store_color, text=12, command=lambda: memory_set_function(11)).place(x=recall_x+75, y= recall_y+30)
        Button(mem_rec, font=('Colibri', 7 ), width=2, bg=store_color, text=13, command=lambda: memory_set_function(12)).place(x=recall_x+100, y=recall_y+30)
        Button(mem_rec, font=('Colibri', 7 ), width=2, bg=store_color, text=14, command=lambda: memory_set_function(13)).place(x=recall_x+125, y=recall_y+30)
        Button(mem_rec, font=('Colibri', 7 ), width=2, bg=store_color, text=15, command=lambda: memory_set_function(14)).place(x=recall_x+150, y=recall_y+30)
        Button(mem_rec, font=('Colibri', 7 ), width=2, bg=store_color, text=16, command=lambda: memory_set_function(15)).place(x=recall_x+175, y=recall_y+30)



        root.mainloop()



def main():
    mi_app_1 = Aplicacion()
    return 0



if __name__ == '__main__':
    main()