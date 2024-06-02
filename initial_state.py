import RPi.GPIO as GPIO
import time
import numpy as np

servo = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo, GPIO.OUT)			
p = GPIO.PWM(servo, 50)  # 50hz frequency
percents=np.arange(2.5,13,.5)
wait=1
p.start(percents[0])
time.sleep(wait)

a=1
while a!=5:
    p.ChangeDutyCycle(percents[20])
    time.sleep(wait)
    p.ChangeDutyCycle(percents[0])
    time.sleep(wait)
    a=a+1
    print(a)

GPIO.cleanup()
