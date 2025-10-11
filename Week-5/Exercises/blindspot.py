from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_UP, K_LEFT, K_DOWN, K_RIGHT, K_1, K_2, K_SPACE

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
def make_circle(pos1, size1,fixation,eye):
    x,y = pos1
    size=size1
    
    while True:

        exp.screen.clear()
        fixation.present(clear=False, update=False)
        c = stimuli.Circle(radius=size, position=(x,y), anti_aliasing=10)
        c.present(clear=False, update=True)
        key = exp.keyboard.check([K_UP, K_LEFT, K_DOWN, K_RIGHT, K_1, K_2, K_SPACE])

        #adjust ssize or position depending on pressed key
        if key == K_LEFT:
            x -= 10
        elif key ==K_RIGHT:
            x += 10
        elif key ==K_UP:
            y += 10
        elif key ==K_DOWN:
            y -= 10
        elif key ==K_1:
            size -= 5
        elif key ==K_2:
            size += 5
        
        #log data
        exp.data.add([eye,key,size,x,y])

        if key ==K_SPACE:
            break

    return (x,y,size)

""" Experiment """
def run_trial(side):
    #position circle on side depending on the trial
    if side=="left":
        pos1=(-300,0)
        fix_pos=(300,0)
        instructions_text = ("Cover your left eye and focus on the cross. \n""Use arrows to adjust the circles position. 1=reduce circle 2=enlarge circle.\n""press space when you no longer see the circle")
        eye = "left"
    else:
        pos1=(300,0)
        fix_pos=(-300,0)
        instructions_text = ("Cover your right eye and focus on the cross. \n""Use arrows to adjust the circles position. 1=reduce circle 2=enlarge circle.\n""press space when you no longer see the circle")
        eye = "right"
    
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=fix_pos)
    fixation.preload()

    instructions = stimuli.TextScreen("blindspot",instructions_text)
    instructions.preload()
    instructions.present()
    exp.keyboard.wait(K_SPACE)

    x,y,size = make_circle(pos1,size1=30,fixation=fixation,eye=eye)

    #add data at end
    #exp.data.add([eye,size,x,y])
    

control.start(subject_id=1)
exp.add_data_variable_names(["eye","key pressed", "radius", "position x", "position y"])
run_trial("left")
run_trial("right")
    
control.end()