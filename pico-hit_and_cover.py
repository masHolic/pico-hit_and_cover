import random
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_RGB332
import jpegdec

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, rotate=0)
display.set_backlight(1.0)

WIDTH, HEIGHT = display.get_bounds()

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

class Hand:
    def __init__(self, side: str):
        self.side = side
        if self.side == 'left':
            self.small_x = 30
            self.small_y1 =12 
            self.small_y2 =52 
            self.small_y3 =92 
            self.img_s = ['img/gu_l_s.jpg', 'img/ti_l_s.jpg', 'img/pa_l_s.jpg']
#            self.img_s[0] = 'img/gu_l_s.jpg'
#            self.img_s[1] = 'img/ti_l_s.jpg'
#            self.img_s[2] = 'img/pa_l_s.jpg'
            self.large_x = 40
            self.large_y =27 
            self.img_l = ['img/gu_l_l.jpg', 'img/ti_l_l.jpg', 'img/pa_l_l.jpg']
#            self.img_l[0] = 'img/gu_l_l.jpg'
#            self.img_l[1] = 'img/ti_l_l.jpg'
#            self.img_l[2] = 'img/pa_l_l.jpg'
            self.line_a = [0, 2, 4, 2]
            self.line_b = [2, 4, 2, 0]
            self.line_c = [4, 2, 0, 2]
            self.count_a = [  0,  5, 10, 15, 20, 25, 30, 35, 30, 25, 20, 15, 10,  5,  0,
                              0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                              0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
            self.count_b = [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                              0,  5, 10, 15, 20, 25, 30, 35, 30, 25, 20, 15, 10,  5,  0,
                              0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
            self.count_c = [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                              0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                              0,  5, 10, 15, 20, 25, 30, 35, 30, 25, 20, 15, 10,  5,  0]
        elif self.side == 'right':
            self.small_x = 170
            self.small_y1 =92 
            self.small_y2 =52 
            self.small_y3 =12 
            self.img_s = ['img/gu_r_s.jpg', 'img/ti_r_s.jpg', 'img/pa_r_s.jpg']
#            self.img_s[0] = 'img/gu_r_s.jpg'
#            self.img_s[1] = 'img/ti_r_s.jpg'
#            self.img_s[2] = 'img/pa_r_s.jpg'
            self.large_x = 120
            self.large_y =27 
            self.img_l = ['img/gu_r_l.jpg', 'img/ti_r_l.jpg', 'img/pa_r_l.jpg']
#            self.img_l[0] = 'img/gu_r_l.jpg'
#            self.img_l[1] = 'img/ti_r_l.jpg'
#            self.img_l[2] = 'img/pa_r_l.jpg'
            self.line_a = [-0, -2, -4, -2]
            self.line_b = [-2, -4, -2, -0]
            self.line_c = [-4, -2, -0, -2]
            self.count_a = [ -0, -5,-10,-15,-20,-25,-30,-35,-30,-25,-20,-15,-10,-5, -0,
                             -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0,
                             -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0]
            self.count_b = [ -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0,
                             -0, -5,-10,-15,-20,-25,-30,-35,-30,-25,-20,-15,-10, -5, -0,
                             -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0,  0]
            self.count_c = [ -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0,
                             -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0,
                             -0, -5,-10,-15,-20,-25,-30,-35,-30,-25,-20,-15,-10, -5, -0]
        self.status = 'wait'
        self.ready_count = 0
        self.line_a = [0, 2, 4, 2]
        self.line_b = [2, 4, 2, 0]
        self.line_c = [4, 2, 0, 2]
        self.ready_count = 0
        self.countdown_count = 0
        print(f'side:[{self.side}, {self.status}]')

    def push_button1(self):
        if self.status == 'wait':
            self.status = 'ready'
        print(f'side:[{self.side}, {self.status}]')

    def push_button2(self):
        if self.status == 'wait':
            self.status = 'ready'
        print(f'side:[{self.side}, {self.status}]')

    def is_ready(self):
        if self.status == 'ready':
            return True
        else:
            return False

    def is_countdown(self):
        if self.status == 'countdown':
            return True
        else:
            return False

    def is_show(self):
        if self.status == 'show':
            return True
        else:
            return False

    def ready(self):
        if self.status == 'ready':
            self.status = 'wait'
        else:
            self.status = 'ready'
        print(f'side:[{self.side}, {self.status}]')

    def countdown(self):
        if self.status == 'ready':
            self.status = 'countdown'
            self.countdown_count = 0
        print(f'side:[{self.side}, {self.status}]')

    def update(self):
        if self.status == 'ready' or self.status == 'countdown':
            display_image(self.img_s[0], self.small_x+self.line_a[self.ready_count]+self.count_a[self.countdown_count], self.small_y1)
            display_image(self.img_s[1], self.small_x+self.line_b[self.ready_count]+self.count_b[self.countdown_count], self.small_y2)
            display_image(self.img_s[2], self.small_x+self.line_c[self.ready_count]+self.count_c[self.countdown_count], self.small_y3)

            if self.ready_count >= 3:
                self.ready_count = 0
            else:
                self.ready_count += 1

            if self.is_countdown():
                self.countdown_count += 1
                if self.countdown_count >= 45:
                    self.countdown_count = 0
                    self.get_result()
        
        elif self.is_show():
            display_image(self.img_l[self.result], self.large_x, self.large_y)

    def get_result(self):
        self.hand_dic = ['gu', 'ti', 'pa']
        self.result = random.randint(0,2)
        self.status = 'show'
        print(f'side:[{self.side}, {self.status}, {self.result}]')

WHITE = display.create_pen(255, 255, 255)
def clear():
    display.set_pen(WHITE)
    display.clear()
    display.update()
clear()

# Create a new JPEG decoder for our PicoGraphics
j = jpegdec.JPEG(display)

def display_image(filename: str, x: int, y:int):
    j.open_file(filename)
    j.decode(x, y, jpegdec.JPEG_SCALE_FULL)
#    display.update()

def show_icon():
    display_image("img/sheld_l_s.jpg", 0, 10)
    display_image("img/sword_l_s.jpg", 0, 95)
    display_image("img/sheld_r_s.jpg", 210, 95)
    display_image("img/sword_r_s.jpg", 210, 10)

show_icon()

left_hand = Hand('left')
right_hand = Hand('right')

while True:
    display.rectangle(30,0,180,135)
    if button_a.read():
#        j.open_file("img/sheld_l_l.jpg")
#        j.decode(40, 27, jpegdec.JPEG_SCALE_FULL)
#        left_hand.ready()
        left_hand.push_button2()
    elif button_b.read():
#        j.open_file("img/sword_l_l.jpg")
#        j.decode(40, 27, jpegdec.JPEG_SCALE_FULL)
#        left_hand.ready()
        left_hand.push_button1()

    if button_x.read():
#        j.open_file("img/sword_r_l.jpg")
#        j.decode(120, 27, jpegdec.JPEG_SCALE_FULL)
#        right_hand.ready()
        right_hand.push_button1()
    elif button_y.read():
#        j.open_file("img/sheld_r_l.jpg")
#        j.decode(120, 27, jpegdec.JPEG_SCALE_FULL)
#        right_hand.ready()
        right_hand.push_button2()

    if left_hand.is_ready() and right_hand.is_ready():
        left_hand.countdown()
        right_hand.countdown()


    left_hand.update()
    right_hand.update()

    # Display the result
    display.update()
