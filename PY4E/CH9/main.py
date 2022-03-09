name = input("Enter file:")
handle = open("mbox-short.txt")
sender = dict()
for line in handle:
    words = line.split()
    for x in range(len(words)):
        if "From" == words[x] and "From:" != words[x]:
            if words[x + 1] not in sender:
                sender[words[x + 1]] = 1
            else:
                sender[words[x + 1]] += 1

max_value = max(sender.values())

for email, count in sender.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
    if count == max_value:
        print(email, max_value)

stuff = dict()
print(stuff.get('candy',-1))