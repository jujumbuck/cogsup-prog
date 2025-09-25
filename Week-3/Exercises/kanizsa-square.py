from expyriment import design, control, stimuli

control.set_develop_mode()

exp = design.Experiment(name = "kanizsa square", background_colour = (128,128,128))

control.initialize(exp)

width, height = exp.screen.size

# size wrt display
sq_size = 0.25*width
circle_radius = 0.05*width

#create 4 circles
up_l_circle = stimuli.Circle(radius=circle_radius, colour=(0,0,0),position=(-sq_size//2,sq_size//2))
low_l_circle = stimuli.Circle(radius=circle_radius, colour=(255,255,255),position=(-sq_size//2,-sq_size//2))
up_r_circle = stimuli.Circle(radius=circle_radius, colour=(0,0,0),position=(sq_size//2,sq_size//2)) 
low_r_circle = stimuli.Circle(radius=circle_radius, colour=(255,255,255),position=(sq_size//2,-sq_size//2))

#create square
k_square = red_square = stimuli.Rectangle(size=(sq_size,sq_size),colour=(128,128,128))

#present all at once
up_l_circle.present(clear=True, update=False)
low_l_circle.present(clear=False, update=False)
up_r_circle.present(clear=False, update=False)
low_r_circle.present(clear=False, update=False)
k_square.present(clear=False, update=True)

exp.keyboard.wait()

control.end()
