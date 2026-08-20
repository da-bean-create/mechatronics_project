from machine import Pin

button1 = Pin(15, Pin.IN, Pin.PULL_DOWN)
led1 = Pin(18, Pin.OUT)
led2 = Pin(19, Pin.OUT)
led3 = Pin(20, Pin.OUT)
# All 3 LED's are seperate; seperate functions
while True:
     while button1.value() == 1:
       led1.value(1)
       led2.value(1)
       led3.value(1)
     else:
       led1.value(0)
       led2.value(0)
       led3.value(0)
""" This is our first code sample to make a working system where 3 LED's
will turn on if a button is pressed, ensuring we can get the basis of our 
layout done and also keep all 3 LED's seperate to incorporate different roles"""




from machine import Pin
import machine
import time
import math

# Initialize ADC on GP26 (ADC 0)
adc = machine.ADC(26)
LED = Pin (18, Pin.OUT)
LED2 = Pin (19, Pin.OUT)
LED3 = Pin (20, Pin.OUT)
# Calibration values (Adjust these based on your room noise)
# Cheap microphone modules lack factory calibration, so we establish a baseline.
DB_BASELINE = 40.0   # Decibel estimation for a dead-silent room
ADC_BASELINE = 10.0  # Minimum raw amplitude variation in a dead-silent room

def sample_peak_to_peak(duration_ms=50):
    """
    Samples the microphone rapidly for a fixed window to find the max wave amplitude.
    """
    max_val = 0
    min_val = 65535
    
    start_time = time.ticks_ms()
    
    # Read as fast as possible for the duration window (default 50ms)
    while time.ticks_diff(time.ticks_ms(), start_time) < duration_ms:
        sample = adc.read_u16()
        if sample > max_val:
            max_val = sample
        if sample < min_val:
            min_val = sample
            
    # Calculate peak-to-peak amplitude difference
    peak_to_peak = max_val - min_val
    return peak_to_peak

print("Calibrating/Starting Decibel Meter...")
time.sleep(1)

while True:
    # 1. Capture the amplitude of the audio wave
    amplitude = sample_peak_to_peak(50)
    
    # 2. Prevent mathematical domain errors if amplitude is zero or below baseline
    if amplitude < ADC_BASELINE:
        amplitude = ADC_BASELINE
        
    # 3. Logarithmic formula: dB = Baseline_dB + 20 * log10(Current_Amplitude / Baseline_Amplitude)
    # Sound pressure scales logarithmically relative to your reference point.
    decibels = DB_BASELINE + (20 * math.log10(amplitude / ADC_BASELINE))
    if decibels >= 75 and decibels <= 80:
        LED.value(1)
        LED2.value(0)
        LED3.value(0)
        
    elif decibels >= 80 and decibels <= 85:
        LED.value(0)
        LED2.value(1)
        LED3.value(0)
        
    elif decibels >= 85:
        LED.value(0)
        LED2.value(0)
        LED3.value(1)

        
    else:
        LED.value(0)
        LED2.value(0)
        LED3.value(0)
    # Print the values to the Plotter, code from website
    print(f"Raw Amplitude: {amplitude} | Estimated dB: {decibels:.1f}")









from machine import Pin, ADC, PWM
import machine
import time
import math
import neopixel


num_LEDs = 5
Pin = macnum_LEDs = 5
pin_neopixel = machine.Pin(22, machine.Pin.OUT)
strip = neopixel.NeoPixel(pin_neopixel, num_LEDs)
button1 = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_counter = 0
buzzer = machine.Pin(18, machine.Pin.OUT)
buzza = PWM(buzzer)
buzza.duty_u16(0)
current_time = time.ticks_ms()
def buzza_process():
            buzza.freq(1000)
            buzza.duty_u16(32000)
            buzzer_end_time = time.ticks_add(current_time, 2000)
            buzza.duty_u16(0)

def sound_detector():
        # If the button is NOT pressed, run the microphone logic
        # 1. Capture the amplitude of the audio wave
        amplitude = sample_peak_to_peak(50)

        # 2. Prevent mathematical domain errors if amplitude is zero or below baseline
        if amplitude < ADC_BASELINE:
            amplitude = ADC_BASELINE

        # 3. Logarithmic formula: dB = Baseline_dB + 20 * log10(Current_Amplitude / Baseline_Amplitude)
        decibels = DB_BASELINE + (20 * math.log10(amplitude / ADC_BASELINE))


if button1.value(1):
    button_counter = button_counter + 1

# Initialize ADC on GP26 (ADC 0)
adc = machine.ADC(26)

# Calibration values (Adjust these based on your room noise)
# Cheap microphone modules lack factory calibration, so we establish a baseline.
DB_BASELINE = 40.0   # Decibel estimation for a dead-silent room
ADC_BASELINE = 10.0  # Minimum raw amplitude variation in a dead-silent room


def sample_peak_to_peak(duration_ms=50):
    """
    Samples the microphone rapidly for a fixed window to find the max wave amplitude.
    """
    max_val = 0
    min_val = 65535

    start_time = time.ticks_ms()
    # Read as fast as possible for the duration window (default 50ms)
    while time.ticks_diff(time.ticks_ms(), start_time) < duration_ms:
        sample = adc.read_u16()
        if sample > max_val:
            max_val = sample
        if sample < min_val:
            min_val = sample

    # Calculate peak-to-peak amplitude difference
    peak_to_peak = max_val - min_val
    return peak_to_peak


print("Calibrating/Starting Decibel Meter...")
time.sleep(1)

# SINGLE MAIN LOOP FOR BOTH FEATURES
while True:
    # Check the button state FIRST using an 'if' statement, not a 'while' statement
    if button1.value() == 1:
        strip[0] = (255, 0, 0)
        strip[1] = (0, 255, 0)
        strip[2] = (0, 0, 255)
        strip.write()
        time.sleep(0.1) # Small delay to avoid hammering the button read
       
    else:

        if decibels >= 75 and decibels <= 80:
            strip[0] = (255, 0, 0)
            strip[1] = (0, 0, 0)
            strip[2] = (0, 0, 0)
            strip.write()

        elif decibels >= 80 and decibels <= 85:
            strip[0] = (0, 0, 0)
            strip[1] = (0, 255, 0)
            strip[2] = (0, 0, 0)
            strip.write()
            buzza.freq(1000)
            buzza.duty_u16(32000)
            time.sleep(2)
            buzza.duty_u16(0)

        elif decibels >= 85:
            strip[0] = (0, 0, 0)
            strip[1] = (0, 0, 0)
            strip[2] = (0, 0, 255)
            strip.write()

        

        else:
            strip[0] = (0, 0, 0)
            strip[1] = (0, 0, 0)
            strip[2] = (0, 0, 0)
            strip.write()

        # Print the values so Thonny's Plotter can see them
    print(f"Raw Amplitude: {amplitude} | Estimated dB: {decibels:.1f}")
# Tells th Pico the number of LEDs and which pin it's in


strip = neopixel.NeoPixel(Pin, num_LEDs)

strip[0] = (255,0,0)
strip[1] = (0,255,0)
strip[2] = (0,0,255)

strip.write()
# This is how you access the different RGB LEDs on the strip







from machine import Pin, ADC, PWM
import machine
import time
import math
import neopixel









selectMode = 0
confirmMode = 0


def modeOne():
 while True:
         sound_detector()
         if decibels >= 75:
            strip[0] = (255, 0, 0)
            strip[1] = (0, 0, 0)
            strip[2] = (0, 0, 0)
            strip.write()

def modeTwo():
 while True:
        sound_detector()
        if decibels >= 80:
            strip[0] = (0, 0, 0)
            strip[1] = (0, 255, 0)
            strip[2] = (0, 0, 0)
            strip.write()
def modeThree():
 while True:
        sound_detector()
        if decibels >= 85:
            strip[0] = (0, 0, 0)
            strip[1] = (0, 0, 0)
            strip[2] = (0, 0, 255)
            strip.write()

while True:
    if button1.value(1):
       selectMode = selectMode + 1
    if selectMode > 3:
           selectMode = 1
    if button2.value(1):
       confirmMode = selectMode
       
    if selectMode == 1:
      strip[0] = (255, 0, 0)
      strip[1] = (0, 0, 0)
      strip[2] = (0, 0, 0)
      strip.write()
    elif selectMode == 2:
      strip[0] = (0, 0, 0)
      strip[1] = (0, 255, 0)
      strip[2] = (0, 0, 0)
      strip.write()    
    elif selectMode == 3:
      strip[0] = (0, 0, 0)
      strip[1] = (0, 0, 0)
      strip[2] = (0, 0, 255)
      strip.write()    
    elif confirmMode == 1:
      modeOne()
    elif confirmMode ==2:
      modeTwo()
    elif confirmMode == 3:
      modeThree()
    else:













from machine import Pin, ADC, PWM
import machine
import time
import math
import neopixel


num_LEDs = 5
Pin = macnum_LEDs = 5
pin_neopixel = machine.Pin(22, machine.Pin.OUT)
strip = neopixel.NeoPixel(pin_neopixel, num_LEDs)
button1 = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_counter = 0
buzzer = machine.Pin(18, machine.Pin.OUT)
buzza = PWM(buzzer)
buzza.duty_u16(0)
current_time = time.ticks_ms()
selectMode = 0
confirmMode = 0


def modeOne():
 while True:
         sound_detector()
         if decibels >= 75:
            strip[0] = (255, 0, 0)
            strip[1] = (0, 0, 0)
            strip[2] = (0, 0, 0)
            strip.write()

def modeTwo():
 while True:
        sound_detector()
        if decibels >= 80:
            strip[0] = (0, 0, 0)
            strip[1] = (0, 255, 0)
            strip[2] = (0, 0, 0)
            strip.write()
def modeThree():
 while True:
        sound_detector()
        if decibels >= 85:
            strip[0] = (0, 0, 0)
            strip[1] = (0, 0, 0)
            strip[2] = (0, 0, 255)
            strip.write()

def buzza_process():
            buzza.freq(1000)
            buzza.duty_u16(32000)
            buzzer_end_time = time.ticks_add(current_time, 2000)
            buzza.duty_u16(0)

def sound_detector():
        # If the button is NOT pressed, run the microphone logic
        # 1. Capture the amplitude of the audio wave
        amplitude = sample_peak_to_peak(50)

        # 2. Prevent mathematical domain errors if amplitude is zero or below baseline
        if amplitude < ADC_BASELINE:
            amplitude = ADC_BASELINE

        # 3. Logarithmic formula: dB = Baseline_dB + 20 * log10(Current_Amplitude / Baseline_Amplitude)
        decibels = DB_BASELINE + (20 * math.log10(amplitude / ADC_BASELINE))


if button1.value(1):
    button_counter = button_counter + 1

# Initialize ADC on GP26 (ADC 0)
adc = machine.ADC(26)

# Calibration values (Adjust these based on your room noise)
# Cheap microphone modules lack factory calibration, so we establish a baseline.
DB_BASELINE = 40.0   # Decibel estimation for a dead-silent room
ADC_BASELINE = 10.0  # Minimum raw amplitude variation in a dead-silent room


def sample_peak_to_peak(duration_ms=50):
    """
    Samples the microphone rapidly for a fixed window to find the max wave amplitude.
    """
    max_val = 0
    min_val = 65535

    start_time = time.ticks_ms()
    # Read as fast as possible for the duration window (default 50ms)
    while time.ticks_diff(time.ticks_ms(), start_time) < duration_ms:
        sample = adc.read_u16()
        if sample > max_val:
            max_val = sample
        if sample < min_val:
            min_val = sample

    # Calculate peak-to-peak amplitude difference
    peak_to_peak = max_val - min_val
    return peak_to_peak


print("Calibrating/Starting Decibel Meter...")
time.sleep(1)

# SINGLE MAIN LOOP FOR BOTH FEATURES
while True:
    if button1.value(1):
       selectMode = selectMode + 1
    if selectMode > 3:
           selectMode = 1
    if button2.value(1):
       confirmMode = selectMode
       
    if selectMode == 1:
      strip[0] = (255, 0, 0)
      strip[1] = (0, 0, 0)
      strip[2] = (0, 0, 0)
      strip.write()
    elif selectMode == 2:
      strip[0] = (0, 0, 0)
      strip[1] = (0, 255, 0)
      strip[2] = (0, 0, 0)
      strip.write()    
    elif selectMode == 3:
      strip[0] = (0, 0, 0)
      strip[1] = (0, 0, 0)
      strip[2] = (0, 0, 255)
      strip.write()    
    elif confirmMode == 1:
      modeOne()
    elif confirmMode ==2:
      modeTwo()
    elif confirmMode == 3:
      modeThree()
    else:

        # Print the values so Thonny's Plotter can see them
    print(f"Raw Amplitude: {amplitude} | Estimated dB: {decibels:.1f}")