hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Coloque um número")
    quit()
if h > 40:
    hs = h - 40
    rs = r * 1.5
    print(((h - hs) * r) + (hs * rs))
else:
    print(h * r)
