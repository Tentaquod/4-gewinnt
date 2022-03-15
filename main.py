def on_button_pressed_a():
    global pos
    led.unplot(pos, 0)
    pos += 1
    led.toggle(pos, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    led.unplot(pos, 0)
    led.plot(pos, 4)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global pos
    led.unplot(pos, 0)
    pos += -1
    led.toggle(pos, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def blinken(rate: number):
    led.plot(pos, 0)
    led.unplot(pos, 0)
pos = 0
led.plot(0, 0)
pos = 0

def on_forever():
    pass
basic.forever(on_forever)
