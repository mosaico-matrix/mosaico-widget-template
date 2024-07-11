from mosaico import widget

# A nice rectangle
rectTop = widget.createRectangle()
rectTop.translateY(10)
rectTop.translateX(-rectTop.getWidth())

# Another nice rectangle
rectTop2 = widget.createRectangle()
rectTop2.translateY(10)
rectTop2.translateX(64+rectTop2.getWidth())

# A nice rectangle
rectBottom = widget.createRectangle()
rectBottom.translateY(40)
rectBottom.translateX(-rectBottom.getWidth())

# Another nice rectangle
rectBottom2 = widget.createRectangle()
rectBottom2.translateY(40)
rectBottom2.translateX(64+rectBottom2.getWidth())

# A nice text
text = widget.createText()
text.setText("GGGGGG")
text.translateX(10)
text.translateY(25)


i = 0
def loop():
    global i
    i += 1
    if i > 70:
        i = 0
    rectTop.moveTo(i, rectTop.getY())
    rectTop2.moveTo(63-i-rectTop2.getWidth(), rectTop2.getY())
    rectBottom.moveTo(i, rectBottom.getY())
    rectBottom2.moveTo(63-i-rectBottom2.getWidth(), rectBottom2.getY())
    pass
        
