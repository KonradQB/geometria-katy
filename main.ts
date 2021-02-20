let kąt = 0
let tm = TM1637.create(
DigitalPin.P8,
DigitalPin.P12,
2,
4
)
servos.P0.setAngle(0)
basic.forever(function () {
    if (0 == pins.digitalReadPin(DigitalPin.P14)) {
        basic.showArrow(ArrowNames.North)
        pins.digitalWritePin(DigitalPin.P15, 0)
        basic.pause(100)
        kąt += 10
        servos.P0.setAngle(kąt)
        pins.digitalWritePin(DigitalPin.P15, 1)
    } else if (0 < kąt) {
        basic.showArrow(ArrowNames.South)
        pins.digitalWritePin(DigitalPin.P15, 1)
        kąt += -10
        servos.P0.setAngle(kąt)
    }
    tm.showNumber(kąt)
})
