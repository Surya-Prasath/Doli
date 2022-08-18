import serial


arduinoData=serial.Serial('/dev/ttyACM0',9600)

def talk(duration):
    for x in range(int(duration*2)+2):
        arduinoData.write(bytes('0',"utf-8"))

def hi():
    for x in range(2):
        arduinoData.write(bytes('1','utf-8'))

