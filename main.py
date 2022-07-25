def on_button_pressed_a():
    radio.send_value("GET", 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_value("POST", 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    if name == "GET":
        basic.show_number(value)
        radio.send_value("POST", 999)
    elif name == "POST":
        basic.show_number(value)
radio.on_received_value(on_received_value)

basic.show_number(1)
radio.set_group(1)