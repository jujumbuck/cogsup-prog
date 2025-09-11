# Session 2: Introduction to Expyriment

## Preliminaries

First, update the Materials folder on your computer with the latest version of our repository. **Make sure to change ```your-path``` to the correct path!**

```bash
cd your-path/Programming/Materials/
git pull
```

Second, copy the Week-2 subfolder from **Materials** to **Assignments**. **Again, make sure to change ```your-path``` to the correct path!**

```bash
cd your-path/Programming/Assignments/
cp -R ../Materials/Week-2 .
```

## First expyriment script
```bash
cd your-path/Programming/Assignments/
cd Week-2/Exercises
python circle.py
```

```python
from expyriment import design, control, stimuli

exp = design.Experiment(name = "Circle")
control.initialize(exp)

fixation = stimuli.FixCross()
fixation.preload()

circle = stimuli.Circle(radius=50)
circle.preload()

control.start()

fixation.present()
exp.clock.wait(1000)

circle.present()
key, rt = exp.keyboard.wait()

control.end()
```

## Step-by-step explanation of the script
Open **Assignments/Week-2/Exercises/circle.py** in VS Code and comment each line as we go together through the script.

### 1. Import modules

```python
from expyriment import design, control, stimuli
```

Imports Expyriment's main modules:
- **design**: for experiment/session objects
- **control**: for initializing, starting, and ending the experiment
- **stimuli**: for creating visual (and other) stimuli, such as shapes, text, and fixation crosses

### 2. Create the experiment

```python
exp = design.Experiment(name = "Circle")
```

Creates an ```Experiment``` object named "Circle" by calling the **Experiment** class in the **design** module. This object:
- stores the global settings of the experiment
- handles the data and log files, the screen, and the input devices (for instance, the keyboard)

### 3. Initialize the experiment
```python
control.initialize(exp)
```

Initializes the experiment stored in ```exp```:
- Opens the display window
- Presents the startup screen with the countdown—this is there to ensure that the Python interpreter has enough time to start up properly and improves timing accuracy afterwards
- Enables input handling (e.g., keys pressed) and event logging
- Starts an experimental clock for timing purposes

This must be done before any stimulus is presented.

### 4. Create a fixation cross
```python
fixation = stimuli.FixCross()
```

Creates a fixation-cross stimulus of default color and size. At this stage, ```fixation``` is just a Python object and has not been rendered.

### 5. Create a circle
```python
circle = stimuli.Circle(radius=50)
```

Creates a circle with a radius of 50 pixels.

## 6. Start the experiment
```python
control.start(subject_id=1)
```

Starts running the currently active experiment:
- Sets the subject ID to 1
- Creates a data file (more on this later)
- Presents the "Ready" screen

## 7. Present the fixation cross
```python
fixation.present()
```

Displays the fixation cross on screen.

## 8. Wait for 1 second
```python
exp.clock.wait(1000)
```

Waits 1000 ms (1 second), during which the fixation cross remains visible.

## 9. Present the circle
```python
circle.present()
```

Clears the screen and displays the circle stimulus.

## 10. Wait for a key press
```python
exp.keyboard.wait()
```

Waits until the participant presses a key.

## 11. End the experiment
```python
control.end()
```

Since the experiment is over, this quits expyriment:
- Saves data and event files
- Shows the "Ending experiment..." screen
- Closes the display window

## Exercise 1
In **Assignments/Exercises**, you will find a python script called `square.py`. Based on the example script above, create a script that displays the fixation cross for **half a second**, then a **blue** square of length 50 until a key is pressed.

Hint: You might want to have a look at [expyriment's `stimuli.Rectangle` documentation](https://docs.expyriment.org/expyriment.stimuli.Rectangle.html#expyriment.stimuli.Rectangle). The color of the square can be set when initializing the object.

## Exercise 2
Open `two_squares.py`. Write a script that displays two squares side by side, the left one green, the right one red. Leave the fixation cross out. The two squares should be separated by 200 pixels but centered as a whole. Present them on-screen until a key is pressed.

Hints: 
- By default, stimuli are presented at the center of the screen. To modify this, you will need to set the ```position``` attribute of squares either when initializing them, or later (e.g., ```square_1.position = (x, y)```)
- Expyriment takes (0, 0) to be the center of the screen and measures space in pixel units
- Mind the arguments you pass to ```present```

## Exercise 3
Duplicate `two_squares.py` in the same **Assignments/Week-2/Exercises** subfolder and rename it `two_animated_squares.py`. Watch the 
1. Present the two squares side by side for one second. 
2. Then, during the next 10 seconds:
    - Rotate one of the two squares clockwise continuously
    - Scale the other one by a factor of 1.01 up until it reaches a size that is twice the original size, then down until it reaches a size that is half the original size

Hints:
- You will need to turn the `exp.clock.wait` into a while-loop that keeps track of time: 


