from machine import Pin, ADC, PWM
import machine
import time
import math
import neopixel


num_LEDs = 5
# Number of LEDs on the strip
pin_neopixel = machine.Pin(22, machine.Pin.OUT)
strip = neopixel.NeoPixel(pin_neopixel, num_LEDs)
# Makes strip the function where we put the RGB colours

button1 = Pin(14, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(15, Pin.IN, Pin.PULL_DOWN)
# Le buttons

buzzer = machine.Pin(18, machine.Pin.OUT)
buzza = PWM(buzzer)
buzza.duty_u16(0)
# Since our buzzer is passive (frequenct and pitch can be changed), it requires a different 'turn on'
# And uses a Pulse Width Modulator

current_time = time.ticks_ms()
selectMode = 1
confirmMode = 0

decibels = 0.0
button_counter = 0
'''
This section above sets all necessary variables to 0 (or 1 in the case of selectMode)
This creates the variables, makes them global and assigns them a value to be changed
'''

# Sets up the 3 different modes
def modeOne():
    strip[0] = (255, 0, 0)
    strip[1] = (0, 0, 0)
    strip[2] = (0, 0, 0)
    strip.write()
    # Red LED

    while True:
        sound_detector()
        print(decibels)

        if decibels >= 75:
            buzza_process()
        else:
            buzza.duty_u16(0)


def modeTwo():
    strip[0] = (0, 0, 0)
    strip[1] = (0, 255, 0)
    strip[2] = (0, 0, 0)
    strip.write()
    # Green LED

    while True:
        sound_detector()
        print(decibels)
        # Prints decibels for testing

        if decibels >= 80:
            buzza_process()
        else:
            buzza.duty_u16(0)


def modeThree():
    strip[0] = (0, 0, 0)
    strip[1] = (0, 0, 0)
    strip[2] = (0, 0, 255)
    strip.write()
    # Blue LED

    while True:
        sound_detector()
        print(decibels)

        if decibels >= 85:
            buzza_process()
        else:
            buzza.duty_u16(0)


def buzza_process():
    buzza.freq(1000)
    buzza.duty_u16(32000)
    # Turns the buzzer action into a process so that it's easier


def sound_detector():
    global decibels, button_counter
    # Makes decibels global so it can be changed outside of the function

    amplitude = sample_peak_to_peak(50)
    # Finds the wavelength

    if amplitude < ADC_BASELINE:
        amplitude = ADC_BASELINE
        # Ensures a value is shown

    decibels = DB_BASELINE + (20 * math.log10(amplitude / ADC_BASELINE))
    # The math behind the rough conversion between amplitude, the baseline and decibels


adc = machine.ADC(26)

# Rough decibel baseline for silence
DB_BASELINE = 40.0

# Calibrated depending on room
ADC_BASELINE = 90.0


def sample_peak_to_peak(duration_ms=50):

    max_val = 0
    min_val = 65535

    start_time = time.ticks_ms()

    while time.ticks_diff(time.ticks_ms(), start_time) < duration_ms:
        # While the process is going (duration is not fulfilled), do this:

        sample = adc.read_u16()

        if sample > max_val:
            max_val = sample
            # Sample WILL be more than max val

        if sample < min_val:
            min_val = sample
            # WILL be less than min val

    peak_to_peak = max_val - min_val

    return peak_to_peak


print("Calibrating/Starting Decibel Meter...")
time.sleep(1)


# ==========================================================
# MODE SELECTION
# ==========================================================

# Turn all LEDs off before starting
strip[0] = (0, 0, 0)
strip[1] = (0, 0, 0)
strip[2] = (0, 0, 0)
strip[3] = (0, 0, 0)
strip[4] = (0, 0, 0)
strip.write()


# Wait for both buttons to be released
while button1.value() == 1 or button2.value() == 1:
    time.sleep(0.01)


while True:
    # Mode selection
    if button1.value() == 1:

        selectMode = selectMode + 1

        if selectMode > 3:
            selectMode = 1

        # Wait for button release
        while button1.value() == 1:
            time.sleep(0.01)
            # Ensures one click isn't read as many in a short time
           
    # Turn corresponding LED on
    if selectMode == 1:

        strip[0] = (255, 0, 0)
        strip[1] = (0, 0, 0)
        strip[2] = (0, 0, 0)

    elif selectMode == 2:

        strip[0] = (0, 0, 0)
        strip[1] = (0, 255, 0)
        strip[2] = (0, 0, 0)

    elif selectMode == 3:

        strip[0] = (0, 0, 0)
        strip[1] = (0, 0, 0)
        strip[2] = (0, 0, 255)

    strip.write()

    # Confirm the selection
    if button2.value() == 1:

        confirmMode = selectMode

        # Wait for button release
        while button2.value() == 1:
            time.sleep(0.01)

        break


    time.sleep(0.05)

# Activate the mode forever
if confirmMode == 1:
    modeOne()

elif confirmMode == 2:
    modeTwo()

elif confirmMode == 3:
    modeThree()