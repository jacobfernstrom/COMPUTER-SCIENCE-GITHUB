def inputdata():
    global h
    global r
    hours = input('Hours:')
    h = float(hours)
    rate = input('Rate:')
    r = float(rate)

def computepay(hours, rate):
    print('in computepay', hours, rate)
    if hours > 40:
        ot = (hours - 40) * 1.5
        fullpay = (ot + 40) * rate
    else:
        fullpay = hours * rate
    print(fullpay)
    return fullpay

inputdata()
fullpay = computepay(h, r)
print('fullpay:', fullpay)









