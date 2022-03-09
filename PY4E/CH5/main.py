largest = None
smallest = None
count = 0

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        int(num)
        if count == 0:
            largest = int(num)
            smallest = int(num)

    except ValueError:
        print('Invalid input')
        continue
    num = int(num)
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num
    count += 1


print("Maximum is", largest)
print('Minimum is', smallest)