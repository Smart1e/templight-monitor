function BrightPercent (num: number) {
    return num * (255 / 100)
}
function swap () {
    if (Service == 0) {
        Service = 1
        basic.showLeds(`
            # . . . .
            # . . . .
            # . . . .
            # . . . .
            # # # # .
            `)
        basic.pause(1000)
        basic.clearScreen()
    } else {
        Service = 0
        basic.showLeds(`
            # # # # #
            . . # . .
            . . # . .
            . . # . .
            . . # . .
            `)
        basic.pause(1000)
        basic.clearScreen()
    }
}
function Load () {
    basic.showLeds(`
        . . # . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . # # # .
        . . # . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        # # # # #
        . # # # .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        . . . . .
        `)
    basic.showLeds(`
        # # . # #
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        `)
    basic.showLeds(`
        # . . . #
        # # . # #
        # # # # #
        # # # # #
        . # # # .
        `)
    basic.showLeds(`
        . . . . .
        # . . . #
        # # . # #
        # # # # #
        # # # # #
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        # . . . #
        # # . # #
        # # # # #
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        # . . . #
        # # . # #
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        # . . . #
        `)
    basic.clearScreen()
}
input.onButtonPressed(Button.A, function () {
    if (Show != true) {
        basic.clearScreen()
        Show = true
        basic.showIcon(IconNames.Yes)
        basic.pause(100)
        basic.clearScreen()
    } else {
        basic.clearScreen()
        Show = false
        basic.showIcon(IconNames.No)
        basic.pause(100)
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
    Show = false
    if (AutoBright == 1) {
        AutoBright = 0
        led.setBrightness(10)
        basic.showLeds(`
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.pause(100)
        basic.clearScreen()
    } else if (led.brightness() == 10) {
        led.setBrightness(40)
        basic.showLeds(`
            # # . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.pause(100)
        basic.clearScreen()
    } else if (led.brightness() == 40) {
        led.setBrightness(100)
        basic.showLeds(`
            # # # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.pause(100)
        basic.clearScreen()
    } else if (led.brightness() == 100) {
        led.setBrightness(200)
        basic.showLeds(`
            # # # # .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.pause(100)
        basic.clearScreen()
    } else if (led.brightness() == 200) {
        led.setBrightness(255)
        basic.showLeds(`
            # # # # #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.pause(100)
        basic.clearScreen()
    } else if (led.brightness() == 255) {
        AutoBright = 1
        basic.showLeds(`
            # # # # #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            # # # # #
            # # # # #
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            # # # # #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            # # # # #
            # # # # #
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.clearScreen()
    }
    Show = true
})
input.onButtonPressed(Button.B, function () {
    swap()
})
let AutoBright = 0
let Show = false
let Service = 0
Service = 1
Show = true
AutoBright = 0
Load()
swap()
basic.forever(function () {
    while (Show != false) {
        basic.pause(10000)
        if (AutoBright == 1) {
            if (input.lightLevel() < 216) {
                led.setBrightness(input.lightLevel() + 10)
            } else {
                led.setBrightness(input.lightLevel())
            }
        }
        if (Service == 0) {
            basic.showNumber(input.temperature())
        } else {
            basic.showNumber(input.lightLevel())
        }
    }
})
