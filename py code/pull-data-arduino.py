import serial
import time

arduino = serial.Serial('COM5', 9600, timeout=.15)

while True:
    data = arduino.readline()[:-2]
    if data :
        time.sleep(2)
        print(data)