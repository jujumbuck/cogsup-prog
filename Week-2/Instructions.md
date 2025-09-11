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

## Step-by-Step explanation of the script

1. Import modules

```python
from expyriment import design, control, stimuli
```

Imports Expyriment's main modules:
- **design**: for experiment/session objects
- **control**: for initializing, starting, and ending the experiment
- **stimuli**: for creating visual (and other) stimuli, such as shapes, text, and fixation crosses

```python
exp = design.Experiment(name = "Circle")
```

Creates an ```Experiment``` object named "Circle". This object:
- stores the global settings of the experiment
- handles the data and log files, the screen, and the input devices (for instance, the keyboard)

```python
control.initialize(exp)
```

Initializes the experiment:
- Creates folders and log files
- Prepares the display window
- Activates input devices

This must be done before any stimulus is presented.

```python
fixation = stimuli.FixCross()
```