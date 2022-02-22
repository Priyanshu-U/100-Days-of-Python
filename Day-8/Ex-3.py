from math import ceil
def paint_calc(height,width,cover):
    paint_cans=int(ceil(height*width/cover))
    print(f"You will need {paint_cans} number of paint cans")
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

