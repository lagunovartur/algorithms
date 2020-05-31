# подключение библиотеки под синонимом gr
from practise.part4 import  graphics as gr

window = gr.GraphWin("task1 - landscape", 1000, 600)

sky = gr.Rectangle(gr.Point(0, 0), gr.Point(1000, 300))
sky.setFill('blue')
sky.draw(window)

home = gr.Rectangle(gr.Point(200, 200), gr.Point(400, 400))
home.setFill('grey')
home.draw(window)

home_wall1 = gr.Line(gr.Point(200, 200), gr.Point(200, 400))
home_wall1.setWidth(5)
home_wall1.setOutline('black')
home_wall1.draw(window)

home_wall2 = gr.Line(gr.Point(200, 200), gr.Point(400, 200))
home_wall2.setWidth(5)
home_wall2.setOutline('black')
home_wall2.draw(window)

home_wall3 = gr.Line(gr.Point(400, 200), gr.Point(400, 400))
home_wall3.setWidth(5)
home_wall3.setOutline('black')
home_wall3.draw(window)

home_wall4 = gr.Line(gr.Point(400, 400), gr.Point(200, 400))
home_wall4.setWidth(5)
home_wall4.setOutline('black')
home_wall4.draw(window)


home_window = gr.Rectangle(gr.Point(250, 250), gr.Point(350, 350))
home_window.setFill('yellow')
home_window.draw(window)

home_window_line1 = gr.Line(gr.Point(300, 250), gr.Point(300, 350))
home_window_line1.setWidth(5)
home_window_line1.setOutline('black')
home_window_line1.draw(window)

home_window_line2 = gr.Line(gr.Point(250, 300), gr.Point(350, 300))
home_window_line2.setWidth(5)
home_window_line2.setOutline('black')
home_window_line2.draw(window)

home_window_line3 = gr.Line(gr.Point(250, 250), gr.Point(250, 350))
home_window_line3.setWidth(5)
home_window_line3.setOutline('black')
home_window_line3.draw(window)

home_window_line4 = gr.Line(gr.Point(250, 250), gr.Point(350, 250))
home_window_line4.setWidth(5)
home_window_line4.setOutline('black')
home_window_line4.draw(window)

home_window_line5 = gr.Line(gr.Point(350, 250), gr.Point(350, 350))
home_window_line5.setWidth(5)
home_window_line5.setOutline('black')
home_window_line5.draw(window)

home_window_line6 = gr.Line(gr.Point(350, 350), gr.Point(250, 350))
home_window_line6.setWidth(5)
home_window_line6.setOutline('black')
home_window_line6.draw(window)

points = [gr.Point(200, 200),gr.Point(400,200),gr.Point(300,100)]
home_roof = gr.Polygon(points)
home_roof.setFill('brown')
home_roof.draw(window)

home_roof_line1 = gr.Line(gr.Point(300, 100), gr.Point(400, 200))
home_roof_line1.setWidth(5)
home_roof_line1.setOutline('black')
home_roof_line1.draw(window)

home_roof_line2 = gr.Line(gr.Point(300, 100), gr.Point(200, 200))
home_roof_line2.setWidth(5)
home_roof_line2.setOutline('black')
home_roof_line2.draw(window)

sun = gr.Circle(gr.Point(750, 100), 60)
sun.setFill('yellow')
sun.draw(window)




# eyebrow1 = gr.Line(gr.Point(100, 120), gr.Point(180, 170))

window.getMouse()

window.close()
