enum RadioMessage {
    message1 = 49434,
    passed10 = 35537
}
input.onButtonPressed(Button.A, function () {
    OLED.clear()
    if (pickup == 0) {
        OLED.writeStringNewLine("[Pickup Destination]")
        if (pickupArr[selectingPick - 1]) {
            OLED.writeString("< ")
        }
        OLED.writeString("A" + convertToText(pickupArr[selectingPick]))
        if (pickupArr[selectingPick + 1]) {
            OLED.writeString(" >")
        }
    } else if (delivery == 0) {
        OLED.writeStringNewLine("[Pickup Destination]: A" + convertToText(pickup))
        OLED.writeStringNewLine("[Delivery Destination]")
        if (deliveryArr[selectingDeli - 1]) {
            OLED.writeString("< ")
        }
        OLED.writeString("B" + convertToText(deliveryArr[selectingDeli]))
        if (deliveryArr[selectingDeli + 1]) {
            OLED.writeString(" >")
        }
    }
})
function promptDestination () {
    OLED.writeStringNewLine("[Pickup Destination]: A" + convertToText(pickup))
    selectingDeli = 0
    OLED.writeStringNewLine("[Delivery Destination]")
    OLED.writeString("B" + convertToText(deliveryArr[selectingDeli]))
    OLED.writeString(" >")
    while (delivery == 0) {
        if (input.isGesture(Gesture.Shake)) {
            delivery = pickupArr[selectingPick]
            gamePad.vibratorMotor(gamePad.Vibrator.V1)
            basic.pause(100)
            gamePad.vibratorMotor(gamePad.Vibrator.V0)
            break;
        } else if (input.buttonIsPressed(Button.A)) {
            if (deliveryArr[selectingDeli - 1]) {
                selectingDeli = selectingDeli - 1
                basic.pause(500)
            }
        } else if (input.buttonIsPressed(Button.B)) {
            if (deliveryArr[selectingDeli + 1]) {
                selectingDeli = selectingDeli + 1
                basic.pause(500)
            }
        }
    }
    OLED.clear()
}
input.onButtonPressed(Button.B, function () {
    OLED.clear()
    if (pickup == 0) {
        OLED.writeStringNewLine("[Pickup Destination]")
        if (pickupArr[selectingPick - 1]) {
            OLED.writeString("< ")
        }
        OLED.writeString("A" + convertToText(pickupArr[selectingPick]))
        if (pickupArr[selectingPick + 1]) {
            OLED.writeString(" >")
        }
    } else if (delivery == 0) {
        OLED.writeStringNewLine("[Pickup Destination]: A" + convertToText(pickup))
        OLED.writeStringNewLine("[Delivery Destination]")
        if (deliveryArr[selectingDeli - 1]) {
            OLED.writeString("< ")
        }
        OLED.writeString("B" + convertToText(deliveryArr[selectingDeli]))
        if (deliveryArr[selectingDeli + 1]) {
            OLED.writeString(" >")
        }
    }
})
function promptPickup () {
    selectingPick = 0
    OLED.writeStringNewLine("[Pickup Destination]")
    OLED.writeString("A" + pickupArr[selectingPick])
    OLED.writeString(" >")
    while (pickup == 0) {
        if (input.isGesture(Gesture.Shake)) {
            pickup = pickupArr[selectingPick]
            gamePad.vibratorMotor(gamePad.Vibrator.V1)
            basic.pause(100)
            gamePad.vibratorMotor(gamePad.Vibrator.V0)
            break;
        } else if (input.buttonIsPressed(Button.A)) {
            if (pickupArr[selectingPick - 1]) {
                selectingPick = selectingPick - 1
                basic.pause(500)
            }
        } else if (input.buttonIsPressed(Button.B)) {
            if (pickupArr[selectingPick + 1]) {
                selectingPick = selectingPick + 1
                basic.pause(500)
            }
        }
    }
    OLED.clear()
}
let selectingDeli = 0
let selectingPick = 0
let delivery = 0
let pickup = 0
let deliveryArr: number[] = []
let pickupArr: number[] = []
basic.showIcon(IconNames.Yes)
basic.pause(1000)
basic.clearScreen()
OLED.init(128, 64)
pickupArr = [1, 2]
deliveryArr = [1, 2, 3]
radio.setGroup(10)
promptPickup()
promptDestination()
