import sys
import pigpio

LED_PIN = 12
LED_PWM_FREQUENCY = 8000
pwm_duty = float(sys.argv[1])

pi = pigpio.pi()
pi.set_mode(LED_PIN, pigpio.OUTPUT)
pi.hardware_PWM(LED_PIN, int(LED_PWM_FREQUENCY), int(pwm_duty * 1e6))
