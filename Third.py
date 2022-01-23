def computepay(h, r):
    return (((h - hs) * r) + (hs * rt))

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
    if h > 40:
        hs = h - 40
        rt = r * 1.5
    p = computepay(h, r)
    print("Pay", p)
except:
    print("Put a number")
