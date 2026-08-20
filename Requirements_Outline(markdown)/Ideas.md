<h1>Gaming noise monitor</h1>
Alerts if you’re being too loud<br>
+ Features two different Raspberry Pi PICOs<br>
+ One for detection of people nearby<br>
+ Another for noise monitoring<br>
+ Has different settings for noise detection; baby, parents, casual<br>
+ All modes have their own buttons<br>
+ Baby has red LED; 60dB<br>
+ Parents has yellow LED; 70dB<br>
+ Casual has green LED; 80dB<br>
***<em>DECIBEL VALUES MAY VARY</em>***<br>
+Have an ultrasonic detector with a laser next to it so people can see where it points

All requirements should be able to be turned on and switched between modes by a button or switch.


<h2>Project Management:</h2>
<p>I feel project management was handles pretty well, though we underestimated how long some aspects would take. Factors such as code testing, practical assessment and ensuring all hardware equipment was working as it should all took a little longer than anticipated, but still allowed for enough time to complete and have a few days to work on the documentation. For example, while testing the sound detector, it took us multiple lessons and help from an anonymous peer to realise that we had to calibrate the detector via a screw on the top until it was sensitive to the level of noise and vibration we wanted. Overall, this had little effect on our ability to complete the various other tasks required throughout the assignment.</p>

<h2>TEST CASE:</h2>
<h3>BUTTON MODE CHANGER</h3>
<p>This particular segment of my code was dedicated to ensuring the two buttons were able to change the mode (sensitivity) of the sound detector. Originally, I began with a small setup that was purely on/off:</p><br>

<em>from machine import Pin

button1 = Pin(15, Pin.IN, Pin.PULL_DOWN)
led1 = Pin(18, Pin.OUT)<br>
led2 = Pin(19, Pin.OUT)<br>
led3 = Pin(20, Pin.OUT)<br>
while True:<br>
    while button1.value() == 1:<br>
       led1.value(1)<br>
       led2.value(1)<br>
       led3.value(1)<br>
     else:<br>
       led1.value(0)<br>
       led2.value(0)<br>
       led3.value(0)</em>

This allowed three different LEDs (functions) to be controlled by one button and formed the basis of my approach.

<em> if button1.value() == 1:<br>
        strip[0] = (255, 0, 0)<br>
        strip[1] = (0, 255, 0)<br>
        strip[2] = (0, 0, 255)<br>
        strip.write()<br>
        time.sleep(0.1)</em>

This is a similar code block that uses an LED strip instead of individual LEDs.

   <em> if button1.value(1):<br>
       selectMode = selectMode + 1<br>
    if selectMode > 3:<br>
           selectMode = 1<br>
    if button2.value(1):<br>
       confirmMode = selectMode</em>

With this new setup (above), I was able to toggle between different functions visible via the LED selection aid. This worked by using a counter connected to the mode selection and resetting it once it got past 3 (only 3 modes).

This setup was basically what I kept throughout the whole experimentation phase, but this was added:

 <em>  if selectMode == 1:<br>
      strip[0] = (255, 0, 0)<br>
      strip[1] = (0, 0, 0)<br>
      strip[2] = (0, 0, 0)<br>
      strip.write()<br>
    elif selectMode == 2:<br>
      strip[0] = (0, 0, 0)<br>
      strip[1] = (0, 255, 0)<br>
      strip[2] = (0, 0, 0)<br>
      strip.write()    <br>
    elif selectMode == 3:<br>
      strip[0] = (0, 0, 0)<br>
      strip[1] = (0, 0, 0)<br>
      strip[2] = (0, 0, 255)<br>
      strip.write()    <br>
    elif confirmMode == 1:<br>
      modeOne()<br>
    elif confirmMode ==2:<br>
      modeTwo()<br>
    elif confirmMode == 3:<br>
      modeThree()<br>
    else:</em>

This actually activated the LED strip and let the confirmation activate the modes (they were turned into functions).
However, the "if" statement never made it past the first 3 "selectMode" if's, so it was later seperated into two different statements.

<h2>FUNCTIONAL EVALUATION:</h2>
In the end, our project lacked some additional planned features such as an ultrasonic distance sensor, laser guiding and a super-exact decibel measure. However, our major component was completed and our mode system was functional, allowing our machine to complete its original task successfully. For instance, when our project is turned to its chosen mode and decibel alert (75dB, 80dB and 85dB) it will turn on the buzzer and turn on the LED strip.

<h2>NON-FUNCTIONAL EVALUATION:</h2>
Our button mode function I believe also counts as a non-functional component due to the effort we put into ensuring it was clean, easy-to-read, noticeable and provided enough information to give the user a good estimate of how loud they were. The Raspberry Pi PICO workspace (breadboard, components, wiring etc) was kept relatively clean as well so it's easy to navigate if hardware change is needed. Overall, our non-functional requirements were pretty much met but maybe could've used a more cosmetic eye.

<h2>ORIGINAL NEED EVALUATION:</h2>
Our original need (a device that can detect if you're being too loud) was met with complete code varying accuracy. Since decibels cannot be read diectly from the sound detector and it is more used for detecting short, sharp noises, we had to find and equation and calibrate the base noise levels in order for it to work. This can sometimes cause slightly off results but provides a good enough estimate for its purpose to be served. 



