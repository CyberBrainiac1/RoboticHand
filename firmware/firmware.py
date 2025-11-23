import RPi.GPIO as GPIO
import time

# List your servo GPIO pins here
servo_pins = [17, 18, 27, 22, 23]  # Example GPIO pins

GPIO.setmode(GPIO.BCM)
servos = []

# Set up all pins and start PWM at 50Hz
for pin in servo_pins:
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 50)
    pwm.start(0)
    servos.append(pwm)

def set_angle(servo, angle):
    duty = angle / 18 + 2  # Maps angle (0-180) to duty cycle (2-12)
    servo.ChangeDutyCycle(duty)
    time.sleep(0.3)
    servo.ChangeDutyCycle(0)  # Avoid continuous signal

try:
    while True:
        for idx, servo in enumerate(servos):
            angle = float(input(f"Enter angle for servo {idx+1} (0-180): "))
            set_angle(servo, angle)
except KeyboardInterrupt:
    pass
finally:
    for servo in servos:
        servo.stop()
    GPIO.cleanup()
