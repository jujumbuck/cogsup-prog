from expyriment import design, control, stimuli
control.set_develop_mode()

exp = design.Experiment(name = "Two Squares")

control.initialize(exp)

fixation = stimuli.FixCross()

red_square = stimuli.Rectangle(size=(50,50),colour=(255,0,0),position=(-150,0))
green_square = stimuli.Rectangle(size=(50,50),colour=(0,255,0), position=(150,0))

control.start(subject_id=1)

fixation.present(clear=True, update=False)

#exp.clock.wait(1000)

red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)

exp.keyboard.wait()

control.end()