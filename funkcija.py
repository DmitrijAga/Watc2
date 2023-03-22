def initialize(serial_port):
    cmd = bytes([0x1b, 0x40])
    serial_port.write(cmd)

def clear(serial_port):
    cmd = bytes ([0x0c])
    serial_port.write(cmd)

def move_left(serial_port):
    cmd = bytes ([0x08])
    serial_port.write(cmd)

def move_right(serial_port):
    cmd = bytes ([0x09])
    serial_port.write(cmd)

def move_down(serial_port):
    cmd = bytes ([0x0a])
    serial_port.write(cmd)

def move_home(serial_port):
    cmd = bytes ([0x0b])
    serial_port.write(cmd)

def move_line_left_start(serial_port):
    cmd = bytes ([0x0d])
    serial_port.write(cmd)

def back_space(serial_port):
    cmd = bytes  ([0x08])

def cursor(serial_port, cursor_state): # Перепроверить это. Функция включения выключения курсора
    cmd = bytearray([0x1f, 0x43, 0x00])
    if cursor_state != 0x00:
        cmd[2] = 0x01
    serial_port.write(cmd)

def cursor_position(serial_port, x_low, x_high, y_low, y_high):
    cmd = bytearray ([0x1f, 0x24, 0x00, 0x00, 0x00, 0x00]) #Вместо нолей надо внести переменные вид xL,xH, eL, eH
    cmd[2] = x_low
    cmd[3] = x_high
    cmd[4] = y_low
    cmd[5]= y_high
    serial_port.write(cmd)



def font_width_fixed(serial_port, font_with):
    cmd = bytearray ([0x1f, 0x28, 0x67, 0x03, 0x03]) #последний аргумент может иметь значения 0x00, 0x01, 0x02, 0x03 (стр 27 мануала)
    if font_with !=0x00:
        cmd[2] = 0x03
        serial_port.write(cmd)

def font_width_x1_y1(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x67, 0x40, 0x01, 0x01]) #последние аргументы надо задать отдельно (стр 27 мануала)
    serial_port.write(cmd)

def font_width_x2_y1(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x67, 0x40, 0x02, 0x01]) #последние аргументы надо задать отдельно (стр 27 мануала)
    serial_port.write(cmd)

def font_width_x1_y2(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x67, 0x40, 0x01, 0x02]) #последние аргументы надо задать отдельно (стр 27 мануала)
    serial_port.write(cmd)
def font_width_x2_y2(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x67, 0x40, 0x02, 0x02]) #последние аргументы надо задать отдельно (стр 27 мануала)
    serial_port.write(cmd)

def overwrite_mode(serial_port):
    cmd = bytes ([0x1f, 0x01]) #Over-write mode
    serial_port.write(cmd)

def vertical_scroll_mode(serial_port):
    cmd = bytes ([0x1f, 0x02]) #Vertical scrol mode
    serial_port.write(cmd)

def horizontal_scroll_mode(serial_port):
    cmd = bytes ([0x1f, 0x03]) #Horizontal scrol mode
    serial_port.write(cmd)

def horizontal_scroll_speed(serial_port, scroll_speed): # 0< n < 31
    cmd = bytearray ([0x1f, 0x73, 0x00])
    if scroll_speed !=0x00:
        cmd[2] = 0x01
    #Вместо ноля вписываем значение скорости (28 стр мануала)
    serial_port.write(cmd)

def reverse_display(serial_port, reverse):
    cmd = bytearray ([0x1f, 0x72, 0x00]) #(28 стр мануала)
    if reverse !=0:
        cmd [2] = 0x01
    serial_port.write(cmd)

def write_mixture_display(serial_port, newly_written):
    cmd = bytearray ([0x1f, 0x77, 0x00]) #(28 стр мануала)
    if newly_written != 0x00:
        cmd[2] = 0x03
    serial_port.write(cmd)

def brightness_level(serial_port):
    cmd = bytes ([0x1f, 0x58, 0x04]) #(29 стр мануала) 8 is maximum
    serial_port.write(cmd)

def wait_mode(serial_port, pause_time):
    cmd = bytearray ([0x1f, 0x28, 0x61, 0x01, 0x02]) #(29 стр мануала) 255 is maximum
    serial_port.write(cmd)

def scroll_display_actiob(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x61, 0x10, 0, 0, 0, 0, 0]) #(29 стр мануала) takes aktion after setting two or more shifts
    serial_port.write(cmd)

def blink_mode(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x61, 0x10, 0, 0]) #(29 стр мануала)
    serial_port.write(cmd)

def write_screen_mode_base_window_cancel(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x77, 0x10, 0x00]) #(29 стр мануала)
    serial_port.write(cmd)

def write_screen_mode_base_window_allscreen(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x77, 0x10, 0x01]) #(29 стр мануала)
    serial_port.write(cmd)

def write_screen_mode_base_window_screen(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x77, 0x10, 0x00]) #(29 стр мануала)
    serial_port.write(cmd)
def write_screen_mode_1_window_allscreen(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x77, 0x11, 0x01]) #(29 стр мануала)
    serial_port.write(cmd)

def write_screen_mode_1_window_cancel(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x77, 0x11, 0x01]) #(29 стр мануала)
    serial_port.write(cmd)

def write_screen_mode_1_window_screen(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x77, 0x11, 0x00]) #(29 стр мануала)
    serial_port.write(cmd)

def write_screen_mode_2_window_cancel(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x77, 0x12, 0x01]) #(29 стр мануала)
    serial_port.write(cmd)

def write_screen_mode_2_window_allscreen(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x77, 0x12, 0x01]) #(29 стр мануала)
    serial_port.write(cmd)
def write_screen_mode_2_window_screen(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x77, 0x12, 0x00]) #(29 стр мануала)
    serial_port.write(cmd)

def write_screen_mode_3_window_cancel(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x77, 0x13, 0x01]) #(29 стр мануала)
    serial_port.write(cmd)
def write_screen_mode_3_window_allscreen(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x77, 0x13, 0x01]) #(29 стр мануала)
    serial_port.write(cmd)

def write_screen_mode_3_window_screen(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x77, 0x13, 0x00]) #(29 стр мануала)
    serial_port.write(cmd)

def write_screen_mode_4_window_cancel(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x77, 0x14, 0x01]) #(29 стр мануала)
    serial_port.write(cmd)

def write_screen_mode_4_window_allscreen(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x77, 0x14, 0x01]) #(29 стр мануала)
    serial_port.write(cmd)
def write_screen_mode_4_window_screen(serial_port):
    cmd = bytes ([0x1f, 0x28, 0x77, 0x14, 0x00]) #(29 стр мануала)
    serial_port.write(cmd)

# def real_time_bit_image_display(serial_port)
#     cmd = bytes ([0x1F, 0x28, 0x66, 0x11, xL xH yL yH g d1...dk])
#     serial_port.write(cmd)