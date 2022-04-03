def walkStright():
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 50)
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        while maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0 and not (maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1):
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 50)
    else:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)

def on_button_pressed_a():
    OLED.clear()
    if pickupDestination == 0:
        OLED.write_string_new_line("[Pickup Destination]")
        if pickupDestinationList[selectingPickupDestination - 1]:
            OLED.write_string("< ")
        OLED.write_num(pickupDestinationList[selectingPickupDestination])
        if pickupDestinationList[selectingPickupDestination + 1]:
            OLED.write_string(" >")
    elif deliveryDestination == 0:
        OLED.write_string_new_line("[Delivery Destination]")
        if deliveryDestinationList[selectingDeliveryDestination - 1]:
            OLED.write_string("< ")
        OLED.write_num(deliveryDestinationList[selectingDeliveryDestination])
        if deliveryDestinationList[selectingDeliveryDestination + 1]:
            OLED.write_string(" >")
input.on_button_pressed(Button.A, on_button_pressed_a)

def promptDestination():
    global selectingDeliveryDestination, deliveryDestination
    selectingDeliveryDestination = 0
    OLED.write_string_new_line("[Delivery Destination]")
    OLED.write_num(deliveryDestinationList[selectingDeliveryDestination])
    OLED.write_string(" >")
    while deliveryDestination == 0:
        if input.button_is_pressed(Button.AB):
            deliveryDestination = selectingDeliveryDestination
            pins.digital_write_pin(DigitalPin.P12, 1)
            serial.write_string("breaking")
            break
        elif input.button_is_pressed(Button.B):
            if deliveryDestinationList[selectingDeliveryDestination + 1]:
                selectingDeliveryDestination = selectingDeliveryDestination + 1
                serial.write_string("+1")
                basic.pause(500)
        elif input.button_is_pressed(Button.A):
            if deliveryDestinationList[selectingDeliveryDestination - 1]:
                selectingDeliveryDestination = selectingDeliveryDestination - 1
                serial.write_string("-1")
                basic.pause(500)
    OLED.clear()
def pathBuilding1():
    pass

def on_button_pressed_b():
    OLED.clear()
    if pickupDestination == 0:
        OLED.write_string_new_line("[Pickup Destination]")
        if pickupDestinationList[selectingPickupDestination - 1]:
            OLED.write_string("< ")
        OLED.write_num(pickupDestinationList[selectingPickupDestination])
        if pickupDestinationList[selectingPickupDestination + 1]:
            OLED.write_string(" >")
    elif deliveryDestination == 0:
        OLED.write_string_new_line("[Delivery Destination]")
        if deliveryDestinationList[selectingDeliveryDestination - 1]:
            OLED.write_string("< ")
        OLED.write_num(deliveryDestinationList[selectingDeliveryDestination])
        if deliveryDestinationList[selectingDeliveryDestination + 1]:
            OLED.write_string(" >")
input.on_button_pressed(Button.B, on_button_pressed_b)

def promptPickup():
    global selectingPickupDestination, pickupDestination
    selectingPickupDestination = 0
    OLED.write_string_new_line("[Pickup Destination]")
    OLED.write_num(pickupDestinationList[selectingPickupDestination])
    OLED.write_string(" >")
    while pickupDestination == 0:
        if input.button_is_pressed(Button.AB):
            pickupDestination = selectingPickupDestination
            pins.digital_write_pin(DigitalPin.P8, 1)
            serial.write_string("breaking")
            break
        elif input.button_is_pressed(Button.B):
            if pickupDestinationList[selectingPickupDestination + 1]:
                selectingPickupDestination = selectingPickupDestination + 1
                serial.write_string("+1")
                basic.pause(500)
        elif input.button_is_pressed(Button.A):
            if pickupDestinationList[selectingPickupDestination - 1]:
                selectingPickupDestination = selectingPickupDestination - 1
                serial.write_string("-1")
                basic.pause(500)
    OLED.clear()
selectingDeliveryDestination = 0
selectingPickupDestination = 0
deliveryDestination = 0
pickupDestination = 0
deliveryDestinationList: List[number] = []
pickupDestinationList: List[number] = []
maqueen.motor_stop(maqueen.Motors.ALL)
basic.show_icon(IconNames.HEART)
OLED.init(128, 64)
pickupDestinationList = [1, 2]
deliveryDestinationList = [1, 2, 3, 4, 5]

def on_forever():
    promptPickup()
    promptDestination()
    basic.pause(2000)
basic.forever(on_forever)
