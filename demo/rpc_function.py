import serial
import time
serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 9600)

while 1:
    s.write(bytes("/LEDControl1/run 3 1\r", 'UTF-8'))
    line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
    print(line)
    line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
    print(line)
    time.sleep(1)

    s.write(bytes("/LEDControl1/run 3 0\r", 'UTF-8'))
    line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
    print(line)
    line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
    print(line)
    time.sleep(1)

    s.write(bytes("/LEDControl2/run 2 1\r", 'UTF-8'))
    line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
    print(line)
    line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
    print(line)
    time.sleep(1)

    s.write(bytes("/LEDControl2/run 2 0\r", 'UTF-8'))
    line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
    print(line)
    line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
    print(line)
    time.sleep(1)