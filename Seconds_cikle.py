import serial
import funkcija
import time
ser = serial.Serial(
    port='COM6',
    baudrate=38400,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

a=0
b=0

funkcija.cursor(ser,0)
funkcija.write_screen_mode_base_window_screen(ser)
funkcija.overwrite_mode(ser)
funkcija.font_width_x2_y2(ser)
cmdTest = bytes([ 0x20, 0x31, 0x33, 0x3a, 0x31, 0x34, 0x3a, 0x30, 0x30]) # initial time
ser.write(cmdTest)
time.sleep(1)
while b < 59:
    while a <86400:

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x30, 0x31])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x30, 0x32])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x30, 0x33])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x30, 0x34])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x30, 0x35])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x30, 0x36])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x30, 0x37])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x30, 0x38])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x30, 0x39])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x31, 0x30])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x31, 0x31])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x31, 0x32])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x31, 0x33])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x31, 0x34])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x31, 0x35])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x31, 0x36])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x31, 0x37])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x31, 0x38])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x31, 0x39])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x32, 0x30])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x32, 0x31])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x32, 0x32])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x32, 0x33])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x32, 0x34])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x32, 0x35])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x32, 0x36])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x32, 0x37])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x32, 0x38])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x32, 0x39])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x33, 0x30])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x33, 0x31])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x33, 0x32])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x33, 0x33])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x33, 0x34])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x33, 0x35])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x33, 0x36])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x33, 0x37])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x33, 0x38])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x33, 0x39])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x34, 0x30])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x34, 0x31])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x34, 0x32])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x34, 0x33])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x34, 0x34])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x34, 0x35])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x34, 0x36])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x34, 0x37])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x34, 0x38])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x34, 0x39])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x35, 0x30])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x35, 0x31])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x35, 0x32])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x35, 0x33])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x35, 0x34])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x35, 0x35])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x35, 0x36])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x35, 0x37])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x3a, 0x31, 0x34, 0x3a, 0x35, 0x38])  # initial time
        ser.write(cmdTest)
        time.sleep(1)

        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        funkcija.move_left(ser)
        cmdTest = bytes([0x20, 0x31, 0x34, 0x20, 0x35, 0x39])  # initial time
        ser.write(cmdTest)
        time.sleep(1)



        a +=1
        print(a)









