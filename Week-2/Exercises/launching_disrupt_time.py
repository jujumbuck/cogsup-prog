from expyriment import design, control, stimuli
control.set_develop_mode()

exp = design.Experiment(name = "Two Squares")

control.initialize(exp)

#initial positions
red_square = stimuli.Rectangle(size=(50,50),colour=(255,0,0),position=(-400,0)) #400 pixels to the left
green_square = stimuli.Rectangle(size=(50,50),colour=(0,255,0),position=(0,0))

control.start(subject_id=1)

red_square.present(clear=True, update=False) #dont update so thT both are at same time
green_square.present(clear=False, update=True) #dont clear so that both are on screen

exp.clock.wait(1000) #wait 1s

#move red square to the left by using a loop that moves it 35 times by 10 pixels to the right 
for i in range(35): #stop 50 pixels before so that doesnt overlap with greeb square
    red_square.move((10,0))
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(20) #wait 20ms per frame

exp.clock.wait(50) #temporal delay max 50 ms or else disrupts impression

for i in range(40): #move green square to the left by using a loop that moves it 40 times by 10 pixels to the right 
    green_square.move((10,0))
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(20)

#keep final display 1s
red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)
exp.clock.wait(1000)


control.end()