import serial
import time


ser = serial.Serial('COM5', 9600, timeout=.15) # sesuaikan port ('COM#') dan baud rate

#while True:
#    data = ser.readline()[:-2]
#    if data :
#        time.sleep(0.5)
#        print(data)

#print("BEDA LAGI BANG\n")

while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip() # Read data until a newline character is reciever

        if data:
            commaIndex = data.find(',') # Find the index of the delimiter
    
            if commaIndex != 1:
                temp_str = data[:commaIndex]
                hum_str = data[commaIndex + 1:]

                temp = float(temp_str)
                hum = float(hum_str)
        
                print(f"Temp: {temp}°C, Hum: {hum}%")
            else:
                print("Invalid data format - no delimiter found")
        else :
           print("no data found")
    

