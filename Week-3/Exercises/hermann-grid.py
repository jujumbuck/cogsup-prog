from expyriment import design, control, stimuli

control.set_develop_mode()

def hermann_grid(sq_size, gap, num_rows, num_cols, sq_color, background):

    exp = design.Experiment(name="hermann grid",background_colour=background)

    control.initialize(exp)
    
    for row in range(num_rows):
        for col in range(num_cols):

            #position
            x = gap * (col - (num_cols - 1) / 2)
            y = gap * ((num_rows - 1) / 2 - row)

            square = stimuli.Rectangle(size=(sq_size, sq_size),colour=sq_color, position=(x, y))
            
            # only update on last square
            if row == num_rows - 1 and col == num_cols - 1:
                square.present(clear=(row == 0 and col == 0), update=True)
            else:
                square.present(clear=(row == 0 and col == 0), update=False)

    exp.keyboard.wait()


hermann_grid(sq_size=50, gap=60, num_rows=10, num_cols=10, sq_color=(0,0,0),background=(255, 255, 255))

control.end()

