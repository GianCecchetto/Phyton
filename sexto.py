fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    input("File cannot be open ", fname)
    quit()
lin = fh.read()
line = lin.strip()
print(line.upper())
