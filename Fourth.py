largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        nu = int(num)
    except:
        print('Invalid input')
    if largest is None:
        largest = nu
    elif nu > largest:
            largest = nu
    elif smallest is None:
            smallest = nu
    elif nu < smallest:
        num = smallest
print("Maximum is", largest)
print("Minimum is", smallest)
