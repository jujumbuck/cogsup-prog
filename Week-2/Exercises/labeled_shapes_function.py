from expyriment import design, control, stimuli
from expyriment.misc import geometry

def labeled_regular_polygon(num_sides,length_side,color,position):
    vertices = geometry.vertices_regular_polygon(num_sides,length_side)
    


control.set_develop_mode()

exp = design.Experiment(name = "Two Squares")

control.initialize(exp)

fixation = stimuli.FixCross()

purple_triangle = stimuli.Shape(vertex_list=geometry.vertices_regular_polygon(3, 50), colour=(128,0,128),position=(-150,0))
yellow_square = stimuli.Shape(vertex_list=geometry.vertices_regular_polygon(6, 25), colour=(255,255,0),position=(150,0))

line_triangle = stimuli.Line(start_point=(-150,22),end_point=(-150,50),line_width=3)
line_hexagon = stimuli.Line(start_point=(150,22),end_point=(150,50),line_width=3)

text_tri = stimuli.TextLine("triangle",position=(-150,70))
text_sq = stimuli.TextLine("square",position=(150,70))
control.start(subject_id=1)



exp.clock.wait(1000)

purple_triangle.present(clear=False, update=False)
yellow_square.present(clear=False, update=False)
line_triangle.present(clear=False, update=False)
line_hexagon.present(clear=False, update=False) 
text_tri.present(clear=False, update=False)
text_sq.present(clear=False, update=False)

exp.screen.update()

exp.keyboard.wait()


control.end()