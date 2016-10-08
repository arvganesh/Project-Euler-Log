with open("p102_triangles.txt", "r") as f:
    count = 0
    text = f.readlines()
    for line in text:
        line = [int(i) for i in line.split(",")]
        ax, ay, bx, by, cx, cy = line
        a = ax*by - ay*bx > 0
        b = bx*cy - by*cx > 0
        c = cx*ay - cy*ax > 0
        count += a==b==c
        # Vector Calc kappa
print count
