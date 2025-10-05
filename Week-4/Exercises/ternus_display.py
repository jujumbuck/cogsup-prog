from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE

exp = design.Experiment(name="Ternus Display")
control.initialize(exp)

def present_for(stimuli_list, frames, isi_frames=0):
    frame_dur = 1000/60

    for v in range(frames):
        exp.screen.clear()   # clear once at the start of each frame
        #present circles
        for stim in stimuli_list:
            stim.present(clear=False, update=False)
        exp.screen.update()
        exp.clock.wait(frame_dur)

    #blinking effect
    if isi_frames > 0:
        exp.screen.clear()
        exp.screen.update()
        exp.clock.wait(isi_frames * frame_dur)


def make_circles(r, tags=False):
    # two fixed middle circles
    c1 = stimuli.Circle(radius=r, position=(-2 * r, 0))
    c2 = stimuli.Circle(radius=r, position=( 2 * r, 0))

    # moving circle left and right
    c_left  = stimuli.Circle(radius=r, position=(-6 * r, 0))
    c_right = stimuli.Circle(radius=r, position=( 6 * r, 0))

    if tags:
        add_tags(c1, (255, 0, 0))
        add_tags(c2, (0, 255, 0))
        add_tags(c_left, (0, 0, 255))
        add_tags(c_right, (0, 0, 255))

    for circle in (c1, c2, c_left, c_right):
        circle.preload()

    return [c1, c2, c_left], [c1, c2, c_right]


def add_tags(circle, color):
    tag = stimuli.Circle(int(circle.radius / 3), colour=color, position=(0, 0))
    tag.plot(circle)
    circle.preload()


def run_trial(r, isi, tags):
    f_left, f_right = make_circles(r, tags=tags)

    while True:
        present_for(f_left, frames=30, isi_frames=isi)  
        present_for(f_right, frames=30, isi_frames=isi) 

        if exp.keyboard.check(K_SPACE):
            break



# Element motion without color tags (low ISI)
run_trial(r=100, isi=1, tags=False)
# Group motion without color tags (high ISI)
run_trial(r=100, isi=15, tags=False)
# Element motion with color tags (high ISI)
run_trial(r=100, isi=15, tags=True)

control.end()
