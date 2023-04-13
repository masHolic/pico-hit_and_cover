from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_RGB332
import jpegdec

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, rotate=0)
display.set_backlight(1.0)

WIDTH, HEIGHT = display.get_bounds()

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

j.open_file("sheld_l_s.jpg")
j.decode(0, 10, jpegdec.JPEG_SCALE_FULL)

j.open_file("sword_l_s.jpg")
j.decode(0, 95, jpegdec.JPEG_SCALE_FULL)

j.open_file("sheld_r_s.jpg")
j.decode(210, 95, jpegdec.JPEG_SCALE_FULL)

j.open_file("sword_r_s.jpg")
j.decode(210, 10, jpegdec.JPEG_SCALE_FULL)


# Display the result
display.update()


while True:
    j.open_file("gu_l_s.jpg")
    j.decode(left_line+4, 12, jpegdec.JPEG_SCALE_FULL)
    j.open_file("ti_l_s.jpg")
    j.decode(left_line+2, 52, jpegdec.JPEG_SCALE_FULL)
    j.open_file("pa_l_s.jpg")
    j.decode(left_line+0, 92, jpegdec.JPEG_SCALE_FULL)
    j.open_file("gu_r_s.jpg")
    j.decode(right_line+0  , 92, jpegdec.JPEG_SCALE_FULL)
    j.open_file("ti_r_s.jpg")
    j.decode(right_line+2, 52, jpegdec.JPEG_SCALE_FULL)
    j.open_file("pa_r_s.jpg")
    j.decode(right_line+4, 12, jpegdec.JPEG_SCALE_FULL)
    display.update()

    j.open_file("gu_l_s.jpg")
    j.decode(left_line+2, 12, jpegdec.JPEG_SCALE_FULL)
    j.open_file("ti_l_s.jpg")
    j.decode(left_line+4, 52, jpegdec.JPEG_SCALE_FULL)
    j.open_file("pa_l_s.jpg")
    j.decode(left_line+2, 92, jpegdec.JPEG_SCALE_FULL)
    j.open_file("gu_r_s.jpg")
    j.decode(right_line+2, 92, jpegdec.JPEG_SCALE_FULL)
    j.open_file("ti_r_s.jpg")
    j.decode(right_line+4, 52, jpegdec.JPEG_SCALE_FULL)
    j.open_file("pa_r_s.jpg")
    j.decode(right_line+2, 12, jpegdec.JPEG_SCALE_FULL)
    display.update()

    j.open_file("gu_l_s.jpg")
    j.decode(left_line+0, 12, jpegdec.JPEG_SCALE_FULL)
    j.open_file("ti_l_s.jpg")
    j.decode(left_line+2, 52, jpegdec.JPEG_SCALE_FULL)
    j.open_file("pa_l_s.jpg")
    j.decode(left_line+4, 92, jpegdec.JPEG_SCALE_FULL)
    j.open_file("gu_r_s.jpg")
    j.decode(right_line+4, 92, jpegdec.JPEG_SCALE_FULL)
    j.open_file("ti_r_s.jpg")
    j.decode(right_line+2, 52, jpegdec.JPEG_SCALE_FULL)
    j.open_file("pa_r_s.jpg")
    j.decode(right_line+0, 12, jpegdec.JPEG_SCALE_FULL)
    display.update()

    j.open_file("gu_l_s.jpg")
    j.decode(left_line+2, 12, jpegdec.JPEG_SCALE_FULL)
    j.open_file("ti_l_s.jpg")
    j.decode(left_line+0, 52, jpegdec.JPEG_SCALE_FULL)
    j.open_file("pa_l_s.jpg")
    j.decode(left_line+2, 92, jpegdec.JPEG_SCALE_FULL)
    j.open_file("gu_r_s.jpg")
    j.decode(right_line+2, 92, jpegdec.JPEG_SCALE_FULL)
    j.open_file("ti_r_s.jpg")
    j.decode(right_line+0, 52, jpegdec.JPEG_SCALE_FULL)
    j.open_file("pa_r_s.jpg")
    j.decode(right_line+2, 12, jpegdec.JPEG_SCALE_FULL)
    display.update()




