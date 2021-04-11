def on_button_pressed_a():
    sing()
input.on_button_pressed(Button.A, on_button_pressed_a)

def sing():
    basic.show_icon(IconNames.EIGTH_NOTE)
    note = kaerunouta()
    for value in note:
        music.play_melody(value, 240)
        radio.send_string(value)
    basic.show_icon(IconNames.HEART)

def on_button_pressed_b():
    sing()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_string(note):
    print(note)
    music.play_melody(note, 240)
radio.on_received_string(on_received_string)

def kaerunouta():
    return ["C - D - E - F - E - D - C - - -",
        "E - F - G - A - G - F - E - - -",
        "C - - - C - - - C - - - C - - -",
        "C C D D E E F F E - D - C - - -"]
radio.set_group(1)
basic.show_icon(IconNames.HEART)