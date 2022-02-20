import sys
import pigpio

LED_R_PIN = 12
LED_G_PIN = 13
LED_B_PIN = 19
LED_PWM_FREQUENCY = 8000
LED_PWM_RANGE = 100
r_pwm_duty = float(sys.argv[1])
g_pwm_duty = float(sys.argv[2])
b_pwm_duty = float(sys.argv[3])

pi = pigpio.pi()
pi.set_mode(LED_R_PIN, pigpio.OUTPUT)
pi.set_mode(LED_G_PIN, pigpio.OUTPUT)
pi.set_mode(LED_B_PIN, pigpio.OUTPUT)
pi.set_PWM_frequency(LED_R_PIN, LED_PWM_FREQUENCY)
pi.set_PWM_frequency(LED_G_PIN, LED_PWM_FREQUENCY)
pi.set_PWM_frequency(LED_B_PIN, LED_PWM_FREQUENCY)
pi.set_PWM_range(LED_R_PIN, LED_PWM_RANGE)
pi.set_PWM_range(LED_G_PIN, LED_PWM_RANGE)
pi.set_PWM_range(LED_B_PIN, LED_PWM_RANGE)
pi.set_PWM_dutycycle(LED_R_PIN, int(r_pwm_duty * LED_PWM_RANGE))
pi.set_PWM_dutycycle(LED_G_PIN, int(g_pwm_duty * LED_PWM_RANGE))
pi.set_PWM_dutycycle(LED_B_PIN, int(b_pwm_duty * LED_PWM_RANGE))
