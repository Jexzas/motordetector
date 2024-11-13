from machine import Pin, PWM
import utime
motor = PWM(Pin(16))
cw = Pin(15, Pin.OUT)
ccw = Pin(14, Pin.OUT)
trig = Pin(13, Pin.OUT)
echo = Pin(12, Pin.IN)

def ultra(out, ins):
    out.low()
    utime.sleep_us(2)
    out.high()
    utime.sleep_us(5)
    out.low()
    while ins.value() == 0:
       signaloff = utime.ticks_us()
    while ins.value() == 1:
       signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    print("the distance is ", distance, " cm")
    return max(min(65535, distance * 4000), 1)

def go(pwm, dir, speed):
    print(speed)
    pwm.freq(50)
    dir.value(1)
    pwm.duty_u16(int(speed))

while True:
    go(motor, cw, ultra(trig, echo))
    utime.sleep(.1)
