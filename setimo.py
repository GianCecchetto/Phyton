fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    input("File cannot be open: ", fname)
    quit()
count = 0
add = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    elif line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
    add = add + float(line[20:26])
print("Average spam confidence:", add/count)
print("Done")
