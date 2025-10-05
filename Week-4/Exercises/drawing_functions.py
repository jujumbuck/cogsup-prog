from expyriment import design, control, stimuli
import random

def load(stims):
    for stim in (stims):
        stim.preload()

def timed_draw(stims):
    #initial time
    t0 = exp.clock.time
    #loop through stims and draw them updating only last stim
    for i, stim in enumerate(stims):
        stim.present(clear=(i == 0), update=(i == len(stims) - 1))
    #time of draw
    dt = exp.clock.time - t0
    return dt
    

def present_for(stims, t=1000):
    #time cant be negative
    if t <= 0:
        return 0
    
    t0 = exp.clock.time

    #same as before
    for i, stim in enumerate(stims):
        stim.present(clear=(i == 0), update=(i == len(stims) - 1))
    dt = exp.clock.time - t0
    
    #make sur that its drawn for the time t given
    remainder = t - dt
    if remainder > 0:
        exp.clock.wait(remainder)

    return dt


""" Test functions """
exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
load([fixation])

n = 20
positions = [(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(n)]
squares = [stimuli.Rectangle(size=(50, 50), position = pos) for pos in positions]
load(squares)

durations = []

t0 = exp.clock.time
for square in squares:
    if not square.is_preloaded:
        print("Preloading function not implemneted correctly.")
    stims = [fixation, square] 
    present_for(stims, 500)
    t1 = exp.clock.time
    durations.append(t1-t0)
    t0 = t1

print(durations)

control.end()