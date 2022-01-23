score = input("Enter Score: ")
try:
    scor = float(score)
    if scor > 1.0:
        print("Put the right grade")
    elif scor >= 0.9:
        print("A")
    elif scor >= 0.8:
        print("B")
    elif scor >= 0.7:
        print("C")
    elif scor >= 0.6:
        print("D")
    elif scor < 0.6:
        print("F")
except:
    print("Put the right grade")
    quit()
