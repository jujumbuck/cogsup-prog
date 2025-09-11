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

# Step-by-Step Explanation of the Expyriment Script

```python
from expyriment import design, control, stimuli
```

Imports Expyriment's main modules:
- design: for experiment/session objects
- control: for initializing, starting, and ending the experiment
- stimuli: for creating visual (and other) stimuli like shapes, text, and fixation crosses

