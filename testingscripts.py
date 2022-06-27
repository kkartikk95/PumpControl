import serial as serial

def test():
    ser = serial.Serial('COM4', 9600, timeout=5)
    ser.write(("/1ZR"+"\r").encode())
    rr = ser.read(10)
    print(rr)
    print(rr[3])
    ser.close()


test()
