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

#BG = display.create_pen(0, 0, 0)
#FG = display.create_pen(255, 255, 255)
WHITE = display.create_pen(255, 255, 255)
display.set_pen(WHITE)
display.clear()

# Create a new JPEG decoder for our PicoGraphics
j = jpegdec.JPEG(display)

# Open the JPEG file
#j.open_file("human_normal.jpg")
#j.open_file("testbitmap.jpg")

# Decode the JPEG
#j.decode(0, 0, jpegdec.JPEG_SCALE_FULL)


left_line = 30
right_line = 170

j.open_file("img/sheld_l_s.jpg")
j.decode(0, 10, jpegdec.JPEG_SCALE_FULL)

j.open_file("img/sword_l_s.jpg")
j.decode(0, 95, jpegdec.JPEG_SCALE_FULL)

j.open_file("img/sheld_r_s.jpg")
j.decode(210, 95, jpegdec.JPEG_SCALE_FULL)

j.open_file("img/sword_r_s.jpg")
j.decode(210, 10, jpegdec.JPEG_SCALE_FULL)




j.open_file("img/sword_l_l.jpg")
j.decode(40, 27, jpegdec.JPEG_SCALE_FULL)

j.open_file("img/sword_r_l.jpg")
j.decode(120, 27, jpegdec.JPEG_SCALE_FULL)


# Display the result
display.update()


line_a = [0, 2, 4, 2]
line_b = [2, 4, 2, 0]
line_c = [4, 2, 0, 2]

number = 0

while True:
    if button_a.read():
        j.open_file("img/sheld_l_l.jpg")
        j.decode(40, 27, jpegdec.JPEG_SCALE_FULL)
    elif button_b.read():
        j.open_file("img/sword_l_l.jpg")
        j.decode(40, 27, jpegdec.JPEG_SCALE_FULL)
    else:
        j.open_file("img/gu_l_s.jpg")
        j.decode(left_line+line_a[number], 12, jpegdec.JPEG_SCALE_FULL)
        j.open_file("img/ti_l_s.jpg")
        j.decode(left_line+line_b[number], 52, jpegdec.JPEG_SCALE_FULL)
        j.open_file("img/pa_l_s.jpg")
        j.decode(left_line+line_c[number], 92, jpegdec.JPEG_SCALE_FULL)

    if button_x.read():
        j.open_file("img/sword_r_l.jpg")
        j.decode(120, 27, jpegdec.JPEG_SCALE_FULL)
    elif button_y.read():
        j.open_file("img/sheld_r_l.jpg")
        j.decode(120, 27, jpegdec.JPEG_SCALE_FULL)
    else:
        j.open_file("img/gu_r_s.jpg")
        j.decode(right_line+line_c[number], 92, jpegdec.JPEG_SCALE_FULL)
        j.open_file("img/ti_r_s.jpg")
        j.decode(right_line+line_b[number], 52, jpegdec.JPEG_SCALE_FULL)
        j.open_file("img/pa_r_s.jpg")
        j.decode(right_line+line_a[number], 12, jpegdec.JPEG_SCALE_FULL)

    display.update()
    if number <= 2:
        number = number + 1
    else:
        number = 0






