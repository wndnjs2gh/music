import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buzzer_pin = 12
GPIO.setup(buzzer_pin, GPIO.OUT)

scale = [261, 294, 329, 349, 392, 440, 493, 523]
list = [4,4,5,5,4,4,2,4,4,2,2,1]
term = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 1]

scale2 = [261, 294, 329, 349, 392, 440, 493, 523]
list = [3,2,1,2,3,3,3,2]
term = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 1]

try:
    p = GPIO.PWM(buzzer_pin, 100)
    p.start(100)
    p.ChangeDutyCycle(90)
    while True:
    
        for i in range(8):
            p.ChangeFrequency(scale[list[i]])
            time.sleep(term[i])
            
        
        for i in range(8):
            p.ChangeFrequency(scale2[list[i]])
            time.sleep(term[i])
            
        p.stop()
    
finally:
    GPIO.cleanup()
