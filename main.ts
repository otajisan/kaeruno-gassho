input.onButtonPressed(Button.A, function () {
    sing()
})
function sing () {
    basic.showIcon(IconNames.EigthNote)
    note = kaerunouta()
    for (let value of note) {
        music.playMelody(value, 240)
        radio.sendString(value)
    }
    basic.showIcon(IconNames.Heart)
}
input.onButtonPressed(Button.B, function () {
    sing()
})
radio.onReceivedString(function (note) {
    console.log(note)
music.playMelody(note, 240)
})
function kaerunouta () {
    return ["C - D - E - F - E - D - C - - -", "E - F - G - A - G - F - E - - -", "C - - - C - - - C - - - C - - -", "C C D D E E F F E - D - C - - -"]
}
let note: string[] = []
radio.setGroup(1)
basic.showIcon(IconNames.Heart)
