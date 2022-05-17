import serial as serial

def serial():
    ser = serial.Serial('COM4', 9600, timeout=5)
    ser.write(("/1ZR"+"\r").encode())
    test = ser.read(10)
    print(test)
    print(test[3])
    ser.close()

serial()