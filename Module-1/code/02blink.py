#Raspberry Pi LED Blink Script

import RPi.GPIO as GPIO
from time import sleep

# ===== Configuration =====
LED_PIN = 8           # Physical (BOARD) pin number where the LED is connected
ON_TIME = 1.0         # Seconds LED stays ON
OFF_TIME = 1.0        # Seconds LED stays OFF

# ===== Setup =====
GPIO.setwarnings(False)       # Disable warnings about GPIO usage from previous runs
GPIO.setmode(GPIO.BOARD)      # Use BOARD numbering (physical pin positions on the header)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
# Configure LED_PIN as an output and ensure it starts LOW (LED off)

def blink_led(on_time: float, off_time: float, pin: int):
    """
    Blink the LED connected to `pin` using the provided on/off durations.
    This function runs indefinitely until interrupted (e.g., Ctrl+C).
    """
    while True:
        GPIO.output(pin, GPIO.HIGH)  # Drive the pin HIGH -> LED ON
        sleep(on_time)               # Keep it ON for `on_time` seconds
        GPIO.output(pin, GPIO.LOW)   # Drive the pin LOW -> LED OFF
        sleep(off_time)              # Keep it OFF for `off_time` seconds

if __name__ == "__main__":
    try:
        # Start blinking with configured durations and pin
        blink_led(ON_TIME, OFF_TIME, LED_PIN)
    except KeyboardInterrupt:
        # Graceful exit when user presses Ctrl+C
        pass
    finally:
        # Always run cleanup to reset GPIO pins to safe state
        GPIO.cleanup()
