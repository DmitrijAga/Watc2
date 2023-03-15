import time

def print_time_to_vfd(serial_port):
    t = time.strftime('%H:%M:%S', time.localtime())
    serial_port.write(t.encode('utf-8'))
a=input()

def print_time():
    t = time.strftime('%H:%M:%S', time.localtime())
    print(t)
    print(t.encode('utf-8'))
#    for character in t:
#        print(character.encode('utf-8').hex(), end='')

if __name__ == '__main__':
    print_time()


import threading

def printit():
  threading.Timer(5.0, printit).start()
  print "Hello, World!"

printit()
