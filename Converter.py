import datetime
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
funkcija.clear(ser)
funkcija.cursor(ser, 0)
day = datetime.datetime.today()
print(day.hour)
v1 =str(" Monday")
v2 =str("Tuesday")
v3 =str("Wednesday")
v4 =str("Thursday")
v5 =str(" Friday")
v6 =str("Saturday")
v7 =str(" Sunday")
v8 =str(" Midnight")
v9 =str("  Noon")


# def print_time_to_vfd(serial_port):
#     t = time.strftime('%H:%M:%S', time.localtime())
#     # serial_port.write(t.encode('utf-8'))

def print_time():
  t = time.strftime('%H:%M:%S', time.localtime())
  funkcija.cursor_position(ser, 8, 0, 1, 0)
  funkcija.font_width_x2_y1(ser)
  cmdTest = bytes(t.encode('utf-8'))
  ser.write(cmdTest)
  time.sleep(0.1)
  funkcija.cursor_position(ser, 8,0,0,0)
  funkcija.font_width_x1_y1(ser)
  time.sleep(0.1)

    # funkcija.horizontal_scroll_mode(ser)
    # funkcija.horizontal_scroll_speed(ser,1)


    # if day.hour == 12:
    #    cmdTest = (v9.encode("utf-8"))
    #    ser.write(cmdTest)

  if day.weekday() == 0:
     cmdTest = (v1.encode("utf-8"))  # bytes( [0x20, 0x20, 0x4e, 0x41, 0x4b, 0x41, 0x44, 0x49, 0x20])
     ser.write(cmdTest)

  if day.weekday() == 1:
     cmdTest = (v2.encode("utf-8"))  # bytes( [0x20, 0x20, 0x4e, 0x41, 0x4b, 0x41, 0x44, 0x49, 0x20])
     ser.write(cmdTest)

  if day.weekday() == 2:
     cmdTest = (v3.encode("utf-8"))  # bytes( [0x20, 0x20, 0x4e, 0x41, 0x4b, 0x41, 0x44, 0x49, 0x20])
     ser.write(cmdTest)

  if day.weekday() == 3:
     cmdTest = (v4.encode("utf-8"))  # bytes( [0x20, 0x20, 0x4e, 0x41, 0x4b, 0x41, 0x44, 0x49, 0x20])
     ser.write(cmdTest)

  if day.weekday() == 4:
     cmdTest = (v5.encode("utf-8"))  # bytes( [0x20, 0x20, 0x4e, 0x41, 0x4b, 0x41, 0x44, 0x49, 0x20])
           ser.write(cmdTest)

  if day.weekday() == 5:
     cmdTest = (v6.encode("utf-8"))  # bytes( [0x20, 0x20, 0x4e, 0x41, 0x4b, 0x41, 0x44, 0x49, 0x20])
     ser.write(cmdTest)

  if day.weekday() == 6:
     cmdTest = (v7.encode("utf-8"))  # bytes( [0x20, 0x20, 0x4e, 0x41, 0x4b, 0x41, 0x44, 0x49, 0x20])
     ser.write(cmdTest)

  if  day.hour == 22:
      funkcija.cursor_position(ser, 72,0,0,0)
      funkcija.font_width_x1_y1(ser)
      funkcija.overwrite_mode(ser)
      cmdTest = (v8.encode("utf-8"))
      ser.write(cmdTest)
  else:
      funkcija.back_space(ser)
      cmdTest =  bytes([0x20])
      ser.write(cmdTest)



if __name__ == '__main__':
    while True:
        print_time()

   # import threading

# def printit():
#   threading.Timer(0.5, printit).start()
# #   print ("Hello, World!")
#
# printit()
