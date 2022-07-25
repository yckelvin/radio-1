input.onButtonPressed(Button.A, function () {
    radio.sendValue("GET", 0)
})
input.onButtonPressed(Button.B, function () {
    radio.sendValue("POST", 1)
})
radio.onReceivedValue(function (name, value) {
    if (name == "GET") {
        basic.showNumber(value)
        radio.sendValue("POST", 999)
    } else if (name == "POST") {
        basic.showNumber(value)
    }
})
basic.showNumber(1)
radio.setGroup(1)
