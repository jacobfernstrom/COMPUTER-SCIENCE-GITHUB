# Exercise 8.4
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    line = line.split(" ")
    for x in line:
        if x in lst:
            continue
        else:
            lst.append(x)
print(sorted(lst))

# Exercise 8.5
fname = input("Enter file name: ")

fh = open("mbox-short.txt")
count = 0
lst = list()
for line in fh:
    if "From " in line:
        line = line.rstrip()
        line = line.split(" ")
        for x in line:
            lst.append(x)
    else:
        continue
lst1 = list()
for x in range(len(lst)):
    if "From" in lst[x]:
        lst1.append(lst[x+1])
        count += 1
for x in range(len(lst1)):
    print(lst1[x])
print("There were", count, "lines in the file with From as the first word")
