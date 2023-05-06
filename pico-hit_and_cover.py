import random
# from pimoroni import Button
from machine import Pin
# from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_RGB332
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY
import jpegdec

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, rotate=0)
display.set_backlight(1.0)

WIDTH, HEIGHT = display.get_bounds()


class Hand:
    def __init__(self, side: str):
        self.side = side
        if self.side == 'left':
            self.direction = 1
            self.small_x = 30
            self.small_y1 = 12
            self.small_y2 = 52
            self.small_y3 = 92
            self.img_s = ['img/gu_l_s.jpg', 'img/ti_l_s.jpg', 'img/pa_l_s.jpg']
            self.large_x = 40
            self.large_y = 32
            self.img_l = ['img/gu_l_l.jpg', 'img/ti_l_l.jpg', 'img/pa_l_l.jpg']
            self.sword_l = 'img/sword_l_l.jpg'
            self.sheld_l = 'img/sheld_l_l.jpg'
            # self.wepon_move = 4
        elif self.side == 'right':
            self.direction = -1
            self.small_x = 170
            self.small_y1 = 92
            self.small_y2 = 52
            self.small_y3 = 12
            self.img_s = ['img/gu_r_s.jpg', 'img/ti_r_s.jpg', 'img/pa_r_s.jpg']
            self.large_x = 130
            self.large_y = 32
            self.img_l = ['img/gu_r_l.jpg', 'img/ti_r_l.jpg', 'img/pa_r_l.jpg']
            self.sword_l = 'img/sword_r_l.jpg'
            self.sheld_l = 'img/sheld_r_l.jpg'
            # self.wepon_move = -4
        self.status = 'wait'
        self.count = 0
        print(f'side:[{self.side}, {self.status}]')

    def push_button1(self):
        if self.is_wait():
            self.ready()
        elif self.is_ready():
            self.wait()
        elif self.is_win():
            self.status = 'win-sword'
            self.count = 0
        elif self.is_lose():
            self.status = 'lose-sword'
            self.count = 0
        print(f'side:[{self.side}, {self.status}]')

    def push_button2(self):
        if self.is_wait():
            self.ready()
        elif self.is_ready():
            self.wait()
        elif self.is_win():
            self.status = 'win-sheld'
            self.count = 0
        elif self.is_lose():
            self.status = 'lose-sheld'
            self.count = 0
        print(f'side:[{self.side}, {self.status}]')

    def is_wait(self):
        if self.status == 'wait':
            return True
        else:
            return False

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

    def is_even(self):
        if self.status == 'even':
            return True
        else:
            return False

    def is_win(self):
        if self.status == 'win':
            return True
        else:
            return False

    def is_lose(self):
        if self.status == 'lose':
            return True
        else:
            return False

    def wait(self):
        self.count = 0
        self.status = 'wait'
        print(f'side:[{self.side}, {self.status}]')

    def ready(self):
        self.count = 0
        self.status = 'ready'
        print(f'side:[{self.side}, {self.status}]')

    def countdown(self):
        if self.status == 'ready':
            self.count = 0
            self.status = 'countdown'
        print(f'side:[{self.side}, {self.status}]')

    def even(self):
        self.status = 'even'
        print(f'side:[{self.side}, {self.status}]')
        self.count = 0

    def win(self):
        self.status = 'win'
        print(f'side:[{self.side}, {self.status}]')
        self.count = 0

    def lose(self):
        self.status = 'lose'
        print(f'side:[{self.side}, {self.status}]')
        self.count = 0

    def update(self):
        if self.is_ready():
            self.rdy_move_a = (self.count + 2) % 4
            if self.rdy_move_a >= 3:
                self.rdy_move_a -= 2
            self.rdy_move_b = (self.count + 1) % 4
            if self.rdy_move_b >= 3:
                self.rdy_move_b -= 2
            self.rdy_move_c = self.count % 4
            if self.rdy_move_c >= 3:
                self.rdy_move_c -= 2
            display_image(self.img_s[0], self.small_x+self.rdy_move_a, self.small_y1)
            display_image(self.img_s[1], self.small_x+self.rdy_move_b, self.small_y2)
            display_image(self.img_s[2], self.small_x+self.rdy_move_c, self.small_y3)

            self.count += 1

        elif self.is_countdown():
            self.cdown_move_a = self.count * 5
            if self.cdown_move_a > 35:
                self.cdown_move_a = 70 - self.cdown_move_a
            if self.cdown_move_a < 0:
                self.cdown_move_a = 0
            self.cdown_move_a = self.cdown_move_a * self.direction
            self.cdown_move_b = (self.count - 7) * 5
            if self.cdown_move_b > 35:
                self.cdown_move_b = 70 - self.cdown_move_b
            if self.cdown_move_b < 0:
                self.cdown_move_b = 0
            self.cdown_move_b = self.cdown_move_b * self.direction
            self.cdown_move_c = (self.count - 15) * 5
            if self.cdown_move_c > 35:
                self.cdown_move_c = 70 - self.cdown_move_c
            if self.cdown_move_c < 0:
                self.cdown_move_c = 0
            self.cdown_move_c = self.cdown_move_c * self.direction
            display_image(self.img_s[0], self.small_x+self.cdown_move_a, self.small_y1)
            display_image(self.img_s[1], self.small_x+self.cdown_move_b, self.small_y2)
            display_image(self.img_s[2], self.small_x+self.cdown_move_c, self.small_y3)

            self.count += 1
            if self.count >= 31:
                self.count = 0
                self.get_result()

        elif self.is_show():
            display_image(self.img_l[self.sign], self.large_x, self.large_y)

        elif self.is_even():
            self.move = self.count * 2
            while self.move > 10:
                self.move = abs(self.move - 20)
            self.move = self.move * self.direction
            display_image(self.img_l[self.sign], self.large_x+self.move, self.large_y)
            self.count += 1
            if self.count > 20:
                self.count = 0
                self.get_result()

        elif self.is_win():
            self.move = self.count * 2 * self.direction
            display_image(self.img_l[self.sign], self.large_x+self.move, self.large_y)
            self.count += 1
            if self.count > 20:
                self.count = 0
                self.get_result()

        elif self.is_lose():
            self.move = -min(max(self.count - 5, 0), 10) * self.direction
            display_image(self.img_l[self.sign], self.large_x+self.move, self.large_y)
            self.count += 1
            if self.count > 20:
                self.count = 0
                self.get_result()

        elif self.status == 'win-sword':
            self.move = self.count * 4 * self.direction
            # display_image(self.sword_l, self.large_x+(self.count * self.wepon_move), self.large_y)
            display_image(self.sword_l, self.large_x+self.move, self.large_y)
            self.count += 1
            if self.count > 10:
                self.count = 0
                self.get_result()

        elif self.status == 'win-sheld':
            self.move = self.count * 4 * self.direction
            #display_image(self.sheld_l, self.large_x+(self.count * self.wepon_move), self.large_y)
            display_image(self.sheld_l, self.large_x+self.move, self.large_y)
            self.count += 1
            if self.count > 10:
                self.count = 0
                self.get_result()

        elif self.status == 'lose-sword':
            self.move = self.count * 4 * self.direction
            # display_image(self.sword_l, self.large_x+(self.count * self.wepon_move), self.large_y)
            display_image(self.sword_l, self.large_x+self.move, self.large_y)
            self.count += 1
            if self.count > 10:
                self.count = 0
                self.get_result()

        elif self.status == 'lose-sheld':
            self.move = self.count * 4 * self.direction
            #display_image(self.sheld_l, self.large_x+(self.count * self.wepon_move), self.large_y)
            display_image(self.sheld_l, self.large_x+self.move, self.large_y)
            self.count += 1
            if self.count > 10:
                self.count = 0
                self.get_result()

    def get_result(self):
        self.hand_dic = ['gu', 'ti', 'pa']
        self.sign = random.randint(0, 2)
        self.status = 'show'
        print(f'side:[{self.side}, {self.status}, {self.sign}]')


WHITE = display.create_pen(255, 255, 255)


def clear():
    display.set_pen(WHITE)
    display.clear()
    display.update()


clear()

# Create a new JPEG decoder for our PicoGraphics
j = jpegdec.JPEG(display)


def display_image(filename: str, x: int, y: int):
    j.open_file(filename)
    j.decode(x, y, jpegdec.JPEG_SCALE_FULL)


def show_icon():
    display_image("img/sheld_l_s.jpg", 0, 10)
    display_image("img/sword_l_s.jpg", 0, 95)
    display_image("img/sheld_r_s.jpg", 210, 95)
    display_image("img/sword_r_s.jpg", 210, 10)


show_icon()

left_hand = Hand('left')
right_hand = Hand('right')


def button_a_handler(p):
    left_hand.push_button2()


def button_b_handler(p):
    left_hand.push_button1()


def button_x_handler(p):
    right_hand.push_button1()


def button_y_handler(p):
    right_hand.push_button2()


button_a = Pin(12, Pin.IN, Pin.PULL_UP)
button_a.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=button_a_handler)

button_b = Pin(13, Pin.IN, Pin.PULL_UP)
button_b.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=button_b_handler)

button_x = Pin(14, Pin.IN, Pin.PULL_UP)
button_x.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=button_x_handler)

button_y = Pin(15, Pin.IN, Pin.PULL_UP)
button_y.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=button_y_handler)


while True:
    display.rectangle(30, 0, 180, 135)

    if left_hand.is_ready() and right_hand.is_ready():
        left_hand.countdown()
        right_hand.countdown()

    if left_hand.is_show():
        print(f'{left_hand.sign=}')

    if right_hand.is_show():
        print(f'{right_hand.sign=}')

    if left_hand.is_show() and right_hand.is_show():
        if left_hand.sign == right_hand.sign:
            left_hand.even()
            right_hand.even()
        elif left_hand.sign == 0 and right_hand.sign == 2:
            left_hand.lose()
            right_hand.win()
        elif left_hand.sign == 2 and right_hand.sign == 0:
            left_hand.win()
            right_hand.lose()
        elif left_hand.sign < right_hand.sign:
            left_hand.win()
            right_hand.lose()
        else:
            left_hand.lose()
            right_hand.win()

    left_hand.update()
    right_hand.update()

    # Display the result
    display.update()
