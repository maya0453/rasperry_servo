import RPi.GPIO as GPIO
import time
import numpy as np

servo = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo, GPIO.OUT)			
p = GPIO.PWM(servo, 50)  # 50hz frequency
p.start(5)

# in servo motor,
# 1ms pulse for 0 degree (LEFT)
# 1.5ms pulse for 90 degree (MIDDLE)
# 2ms pulse for 180 degree (RIGHT)

# so for 50hz, one frequency is 20ms
# duty cycle for 0 degree = (1/20)*100 = 5%
# duty cycle for 90 degree = (1.5/20)*100 = 7.5%
# duty cycle for 180 degree = (2/20)*100 = 10%
# duty cycle for 270 degree = (2.5/20)*100 = 12.5%
# starting duty cycle ( it set the servo to 0 degree )
percents=np.arange(2.5,13,.5)
try:
    while True:
        for x in percents:
            p.ChangeDutyCycle(x)
            time.sleep(0.4)
            print(x)
except KeyboardInterrupt:
    GPIO.cleanup()