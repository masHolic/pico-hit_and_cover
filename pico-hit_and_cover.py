import random
from pimoroni import Button
# from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_RGB332
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY
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
            self.small_y1 = 12
            self.small_y2 = 52
            self.small_y3 = 92
            self.img_s = ['img/gu_l_s.jpg', 'img/ti_l_s.jpg', 'img/pa_l_s.jpg']
#            self.img_s[0] = 'img/gu_l_s.jpg'
#            self.img_s[1] = 'img/ti_l_s.jpg'
#            self.img_s[2] = 'img/pa_l_s.jpg'
            self.large_x = 40
            self.large_y = 32
            self.img_l = ['img/gu_l_l.jpg', 'img/ti_l_l.jpg', 'img/pa_l_l.jpg']
#            self.img_l[0] = 'img/gu_l_l.jpg'
#            self.img_l[1] = 'img/ti_l_l.jpg'
#            self.img_l[2] = 'img/pa_l_l.jpg'
            self.line_a = [0, 2, 4, 2]
            self.line_b = [2, 4, 2, 0]
            self.line_c = [4, 2, 0, 2]
            self.count_a = [0,  5, 10, 15, 20, 25, 30, 35, 30, 25, 20, 15, 10, 5,  0,
                            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,
                            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0]
            self.count_b = [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,
                            0,  5, 10, 15, 20, 25, 30, 35, 30, 25, 20, 15, 10, 5,  0,
                            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0]
            self.count_c = [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,
                            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,
                            0,  5, 10, 15, 20, 25, 30, 35, 30, 25, 20, 15, 10, 5,  0]
            self.even_shift = [0, 2, 4, 6, 8, 10, 8, 6, 4, 2, 0, 2, 4, 6, 8, 10, 8, 6, 4, 2, 0]
            self.win_shift = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
            self.lose_shift = [0, 0, 0, 0, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -10, -10, -10, -10, -10, -10]
        elif self.side == 'right':
            self.small_x = 170
            self.small_y1 = 92
            self.small_y2 = 52
            self.small_y3 = 12
            self.img_s = ['img/gu_r_s.jpg', 'img/ti_r_s.jpg', 'img/pa_r_s.jpg']
#            self.img_s[0] = 'img/gu_r_s.jpg'
#            self.img_s[1] = 'img/ti_r_s.jpg'
#            self.img_s[2] = 'img/pa_r_s.jpg'
            self.large_x = 130
            self.large_y = 32
            self.img_l = ['img/gu_r_l.jpg', 'img/ti_r_l.jpg', 'img/pa_r_l.jpg']
#            self.img_l[0] = 'img/gu_r_l.jpg'
#            self.img_l[1] = 'img/ti_r_l.jpg'
#            self.img_l[2] = 'img/pa_r_l.jpg'
            self.line_a = [-0, -2, -4, -2]
            self.line_b = [-2, -4, -2, -0]
            self.line_c = [-4, -2, -0, -2]
            self.count_a = [-0, -5, -10, -15, -20, -25, -30, -35, -30, -25, -20, -15, -10, -5, -0,
                            -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0,
                            -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0]
            self.count_b = [-0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0,
                            -0, -5, -10, -15, -20, -25, -30, -35, -30, -25, -20, -15, -10, -5, -0,
                            -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0,  0]
            self.count_c = [-0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0,
                            -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0,
                            -0, -5, -10, -15, -20, -25, -30, -35, -30, -25, -20, -15, -10, -5, -0]
            self.even_shift = [-0, -2, -4, -6, -8, -10, -8, -6, -4, -2, -0, -2, -4, -6, -8, -10, -8, -6, -4, -2, -0]
            self.win_shift = [-0, -2, -4, -6, -8, -10, -12, -14, -16, -18, -20, -22, -24, -26, -28, -30, -32, -34, -36, -38, -40]
            self.lose_shift = [0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10]
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

    def even(self):
        self.status = 'even'
        print(f'side:[{self.side}, {self.status}]')
        self.even_count = 0

    def win(self):
        self.status = 'win'
        print(f'side:[{self.side}, {self.status}]')
        self.win_count = 0

    def lose(self):
        self.status = 'lose'
        print(f'side:[{self.side}, {self.status}]')
        self.lose_count = 0

    def update(self):
        if self.status == 'ready':
            display_image(self.img_s[0], self.small_x+self.line_a[self.ready_count], self.small_y1)
            display_image(self.img_s[1], self.small_x+self.line_b[self.ready_count], self.small_y2)
            display_image(self.img_s[2], self.small_x+self.line_c[self.ready_count], self.small_y3)

            if self.ready_count >= 3:
                self.ready_count = 0
            else:
                self.ready_count += 1

        elif self.status == 'countdown':
            display_image(self.img_s[0], self.small_x+self.count_a[self.countdown_count], self.small_y1)
            display_image(self.img_s[1], self.small_x+self.count_b[self.countdown_count], self.small_y2)
            display_image(self.img_s[2], self.small_x+self.count_c[self.countdown_count], self.small_y3)

            if self.is_countdown():
                self.countdown_count += 1
                if self.countdown_count >= 45:
                    self.countdown_count = 0
                    self.get_result()

        elif self.is_show():
            display_image(self.img_l[self.sign], self.large_x, self.large_y)

        elif self.is_even():
            display_image(self.img_l[self.sign], self.large_x+self.even_shift[self.even_count], self.large_y)
            self.even_count += 1
            if self.even_count > 20:
                self.even_count = 0
                self.get_result()

        elif self.is_win():
            display_image(self.img_l[self.sign], self.large_x+self.win_shift[self.win_count], self.large_y)
            self.win_count += 1
            if self.win_count > 20:
                self.win_count = 0
                self.get_result()

        elif self.is_lose():
            display_image(self.img_l[self.sign], self.large_x+self.lose_shift[self.lose_count], self.large_y)
            self.lose_count += 1
            if self.lose_count > 20:
                self.lose_count = 0
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

while True:
    display.rectangle(30, 0, 180, 135)
    if button_a.read():
        left_hand.push_button2()
    elif button_b.read():
        left_hand.push_button1()

    if button_x.read():
        right_hand.push_button1()
    elif button_y.read():
        right_hand.push_button2()

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
