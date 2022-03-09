#mbox-short.txt används, behövs
fhand = open('mbox-short.txt')
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0


for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    number = float(line.replace("X-DSPAM-Confidence: ",""))
    total += number
print("Average spam confidence:",total/count)

