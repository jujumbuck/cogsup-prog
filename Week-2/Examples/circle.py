from expyriment import design, control, stimuli

# 1. Initiate an experiment called "Circle"
exp = design.Experiment(name="Circle")
control.initialize(exp)

# 2. Create the stimuli
fixation = stimuli.FixCross()
circle = stimuli.Circle(radius=50)

# 3. Start the experiment
control.start()

# 4a. Present fixation cross
fixation.present()
exp.clock.wait(1000)

# 4b. Present square
circle.present()
exp.keyboard.wait()

# 5. End experiment
control.end()