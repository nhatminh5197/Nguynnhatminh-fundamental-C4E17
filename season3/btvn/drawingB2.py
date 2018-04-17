from turtle import*
colors = ["red","blue","brown","yellow","gray"]
for i in range(5):
    begin_fill()
    color(colors[i])
    for i in range (4):
        forward(100)
        left(90)


    forward(100)

    end_fill()





mainloop()
