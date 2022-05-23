def BrightPercent(num: number):
    return num * (255 / 100)
def swap():
    global Service
    if Service == 0:
        Service = 1
        basic.show_leds("""
            # . . . .
                        # . . . .
                        # . . . .
                        # . . . .
                        # # # # .
        """)
        basic.pause(1000)
        basic.clear_screen()
    else:
        Service = 0
        basic.show_leds("""
            # # # # #
                        . . # . .
                        . . # . .
                        . . # . .
                        . . # . .
        """)
        basic.pause(1000)
        basic.clear_screen()
def Load():
    basic.show_leds("""
        . . # . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . # # # .
                . . # . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        # # # # #
                . # # # .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        # # # # #
                # # # # #
                . # # # .
                . . # . .
                . . . . .
    """)
    basic.show_leds("""
        # # . # #
                # # # # #
                # # # # #
                . # # # .
                . . # . .
    """)
    basic.show_leds("""
        # . . . #
                # # . # #
                # # # # #
                # # # # #
                . # # # .
    """)
    basic.show_leds("""
        . . . . .
                # . . . #
                # # . # #
                # # # # #
                # # # # #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                # . . . #
                # # . # #
                # # # # #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                # . . . #
                # # . # #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                # . . . #
    """)
    basic.clear_screen()

def on_button_pressed_a():
    global Show
    if Show != True:
        basic.clear_screen()
        Show = True
        basic.show_icon(IconNames.YES)
        basic.pause(100)
        basic.clear_screen()
    else:
        basic.clear_screen()
        Show = False
        basic.show_icon(IconNames.NO)
        basic.pause(100)
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Show, AutoBright
    basic.clear_screen()
    Show = False
    if AutoBright == 1:
        AutoBright = 0
        led.set_brightness(10)
        basic.show_leds("""
            # . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.pause(100)
        basic.clear_screen()
    elif led.brightness() == 10:
        led.set_brightness(40)
        basic.show_leds("""
            # # . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.pause(100)
        basic.clear_screen()
    elif led.brightness() == 40:
        led.set_brightness(100)
        basic.show_leds("""
            # # # . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.pause(100)
        basic.clear_screen()
    elif led.brightness() == 100:
        led.set_brightness(200)
        basic.show_leds("""
            # # # # .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.pause(100)
        basic.clear_screen()
    elif led.brightness() == 200:
        led.set_brightness(255)
        basic.show_leds("""
            # # # # #
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.pause(100)
        basic.clear_screen()
    elif led.brightness() == 255:
        AutoBright = 1
        basic.show_leds("""
            # # # # #
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # # # # #
                        # # # # #
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # # # # #
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # # # # #
                        # # # # #
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.clear_screen()
    Show = True
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    swap()
input.on_button_pressed(Button.B, on_button_pressed_b)

AutoBright = 0
Show = False
Service = 0
Service = 1
Show = True
AutoBright = 0
Load()
swap()

def on_forever():
    while Show != False:
        if AutoBright == 1:
            led.set_brightness(input.light_level())
        if Service == 0:
            basic.show_number(input.temperature())
            basic.pause(10000)
        else:
            basic.show_number(input.light_level())
            basic.pause(10000)
basic.forever(on_forever)
