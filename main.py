list2: List[str] = []

def on_button_pressed_a():
    global note
    basic.show_icon(IconNames.EIGTH_NOTE)
    note = kaerunouta()
    for value in list2:
        music.play_melody(value, 240)
        radio.send_string(value)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(note):
    radio.send_string("" + (note))
radio.on_received_string(on_received_string)

def kaerunouta():
    return ["C - D - E - F - E - D - C - - -",
        "E - F - G - A - G - F - E - - -",
        "C - - - C - - - C - - - C - - -",
        "C C D D E E F F E - D - C - - -"]
note: List[str] = []
radio.set_group(1)

def on_forever():
    basic.show_icon(IconNames.HEART)
basic.forever(on_forever)
