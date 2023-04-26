from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_RGB332
import jpegdec
import time


display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, rotate=0)
display.set_backlight(1.0)

WHITE = display.create_pen(255, 255, 255)
def clear():
    display.set_pen(WHITE)
    display.clear()
    display.update()
clear()

j = jpegdec.JPEG(display)
j.open_file("img/gu_l_s.jpg")
def display_image_j(x: int, y:int):
    j.decode(x, y, jpegdec.JPEG_SCALE_FULL)

k = jpegdec.JPEG(display)
k.open_file("img/ti_l_s.jpg")
def display_image_k(x: int, y:int):
    k.decode(x, y, jpegdec.JPEG_SCALE_FULL)

l = jpegdec.JPEG(display)
l.open_file("img/pa_l_s.jpg")
def display_image_l(x: int, y:int):
    l.decode(x, y, jpegdec.JPEG_SCALE_FULL)

start_time = time.time()
for num in range(205):
    display_image_j(0 + num, 5)
    display_image_k(0 + num, 50)
    display_image_l(0 + num, 95)
#    print(f"{num=}")

    # Display the result
    display.update()

end_time = time.time()

print('time = {} Seconds'.format(end_time - start_time))