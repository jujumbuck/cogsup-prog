from expyriment import design, control, stimuli
control.set_develop_mode()

exp = design.Experiment(name = "launching function")

control.initialize(exp)

def launching(temp,spatial,speed):
    #initial position
    red_square = stimuli.Rectangle(size=(50,50),colour=(255,0,0),position=(-400,0)) 
    green_square = stimuli.Rectangle(size=(50,50),colour=(0,255,0),position=(spatial,0))

    

    for i in range(35): 
        red_square.move((10,0))
        red_square.present(clear=True, update=False)
        green_square.present(clear=False, update=True)
        exp.clock.wait(20)

    if temp >0 :
        exp.clock.wait(temp)

    for i in range(40): 
        green_square.move((10,0))
        red_square.present(clear=True, update=False)
        green_square.present(clear=False, update=True)
        exp.clock.wait(speed)

    red_square.present(clear=True, update=False) 
    green_square.present(clear=False, update=True) 
    exp.clock.wait(1000)


control.start(subject_id=1)

launching(temp=0, spatial=0, speed=20)

launching(temp=400, spatial=0, speed=20)

launching(temp=0, spatial=100, speed=20)

launching(temp=0, spatial=0, speed=7)

control.end()