#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor, Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait


ev3 = EV3Brick()
sensor_color = ColorSensor(Port.S3)
mi = Motor(Port.B)
md = Motor(Port.C)

robot = DriveBase(mi,md,55.5,104)

umbral = 30 

codigo_barras = ""

robot.drive(50, 0)

while True:
    longitud_barra = 0
    

    while True:
        reflectancia = sensor_color.reflection()
        if reflectancia < umbral:
            longitud_barra += 1
        else:
            if longitud_barra > 0:
                break
        wait(10) 
    
 
    if longitud_barra > umbral / 2:
        codigo_barras += "1"
    else:
        codigo_barras += "0"
    
  
    espacio_blanco = 0
    while sensor_color.reflection() >= umbral:
        espacio_blanco += 1
        wait(10)  

        if espacio_blanco > 20: 
            robot.stop(Stop.BRAKE)
            break


    ev3.screen.clear()
    ev3.screen.print("Código de barras:")
    ev3.screen.print(codigo_barras)
