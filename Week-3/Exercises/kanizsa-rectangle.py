from expyriment import design, control, stimuli

control.set_develop_mode()

exp = design.Experiment(name = "kanizsa square", background_colour = (128,128,128))

control.initialize(exp)

def kanizsa_rectangle(aspect_ratio,rec_scale,circ_scale):
    display_width, display_height = exp.screen.size
    height = rec_scale * display_width
    width = aspect_ratio * height

    circle_radius = circ_scale * display_width

    #create 4 circles
    up_l_circle = stimuli.Circle(radius=circle_radius, colour=(0,0,0),position=(-width//2, height//2))
    low_l_circle = stimuli.Circle(radius=circle_radius, colour=(255,255,255),position=(-width//2, -height//2))
    up_r_circle = stimuli.Circle(radius=circle_radius, colour=(0,0,0),position=(width//2, height//2))
    low_r_circle = stimuli.Circle(radius=circle_radius, colour=(255,255,255),position=(width//2, -height//2))

    k_square = red_square = stimuli.Rectangle(size=(width,height),colour=(128,128,128))

    up_l_circle.present(clear=True, update=False)
    low_l_circle.present(clear=False, update=False)
    up_r_circle.present(clear=False, update=False)
    low_r_circle.present(clear=False, update=False)
    k_square.present(clear=False, update=True)


    exp.keyboard.wait()


kanizsa_rectangle(2/1,0.25,0.05)

control.end()
