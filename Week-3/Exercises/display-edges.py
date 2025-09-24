from expyriment import design, control, stimuli

control.set_develop_mode()

exp = design.Experiment(name = "launching function")

control.initialize(exp)

width, height = exp.screen.size

sq_size = 0.05*width

up_l_pos = (-width// 2 + sq_size // 2 , height// 2 - sq_size// 2 )
low_l_pos = (-width //2 + sq_size // 2 , -height //2 + sq_size// 2 )
up_r_pos = (width// 2 - sq_size // 2 , height// 2 - sq_size// 2 )
low_r_pos = (width// 2 - sq_size// 2 , -height// 2+ sq_size// 2 )


up_l_square = stimuli.Rectangle(size=(sq_size,sq_size),colour=(255,0,0),position=up_l_pos, line_width =1) 
low_l_square = stimuli.Rectangle(size=(sq_size,sq_size),colour=(255,0,0),position=low_l_pos, line_width =1) 
up_r_square = stimuli.Rectangle(size=(sq_size,sq_size),colour=(255,0,0),position=up_r_pos, line_width =1) 
low_r_square = stimuli.Rectangle(size=(sq_size,sq_size),colour=(255,0,0),position=low_r_pos, line_width =1) 

up_l_square.present(clear=True, update=False)
low_l_square.present(clear=False, update=False)
up_r_square.present(clear=False, update=False)
low_r_square.present(clear=False, update=True)

exp.keyboard.wait()

control.end()
