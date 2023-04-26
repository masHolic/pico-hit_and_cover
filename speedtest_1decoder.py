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

def display_image(filename: str, x: int, y:int):
    j.open_file(filename)
    j.decode(x, y, jpegdec.JPEG_SCALE_FULL)

start_time = time.time()
for num in range(205):
    display_image("img/gu_l_s.jpg", 0 + num, 5)
    display_image("img/ti_l_s.jpg", 0 + num, 50)
    display_image("img/pa_l_s.jpg", 0 + num, 95)
#    print(f"{num=}")

    # Display the result
    display.update()

end_time = time.time()

print('time = {} Seconds'.format(end_time - start_time))