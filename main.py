kąt = 0
tm = TM1637.create(DigitalPin.P8, DigitalPin.P12, 2, 4)
servos.P0.set_angle(0)

def on_forever():
    global kąt
    if 0 == pins.digital_read_pin(DigitalPin.P14):
        basic.show_arrow(ArrowNames.NORTH)
        pins.digital_write_pin(DigitalPin.P15, 0)
        basic.pause(100)
        kąt += 10
        servos.P0.set_angle(kąt)
        pins.digital_write_pin(DigitalPin.P15, 1)
    else:
        if 0 < kąt:
            basic.show_arrow(ArrowNames.SOUTH)
            pins.digital_write_pin(DigitalPin.P15, 1)
            kąt += -10
            servos.P0.set_angle(kąt)
    tm.show_number(kąt)
basic.forever(on_forever)
