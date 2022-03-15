input.onButtonPressed(Button.A, function () {
    led.unplot(pos, 0)
    pos += 1
    led.toggle(pos, 0)
})
input.onButtonPressed(Button.AB, function () {
    led.unplot(pos, 0)
    led.plot(pos, 4)
})
input.onButtonPressed(Button.B, function () {
    led.unplot(pos, 0)
    pos += -1
    led.toggle(pos, 0)
})
function blinken (rate: number) {
    led.plot(pos, 0)
    basic.pause(rate)
    led.unplot(pos, 0)
}
let pos = 0
led.plot(0, 0)
pos = 0
loops.everyInterval(500, function () {
    blinken(500)
})
basic.forever(function () {
	
})
