text = "X-DSPAM-Confidence:    0.8475"
numstr = text.find("0")
numstrend = text.find("5")
newstr = text[numstr:numstrend+1]
print(newstr)

