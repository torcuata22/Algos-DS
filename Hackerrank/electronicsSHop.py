#determine most expensive keyboard and USB drive that you can buy with budget b
#keyboards and drives are list of prices
#need to add all keyboards[i] with drives[i] and verify which combinations are <=b

def getMoneySpent(keyboards, drives, b):
    result = -1
    for i in range(1, len(keyboards)):
        for j in range(1, len(drives)):
            if result < keyboards[i] + drives[j] <= b:
                result = keyboards[i] + drives[j]
    return result