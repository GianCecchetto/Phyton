text = "X-DSPAM-Confidence:    0.8475"
tex = text.find('0')
te = text[tex : ]
t = float(te)
print(t)
