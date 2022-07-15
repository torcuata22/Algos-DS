#Array subdivision: given a birthday and a month, find subarray that: sum elements = day and as many elements as number of the month
def birthday(s,d,m):
      return sum([1 for i in range(len(s)-m+1) if sum(s[i:i+m])==d])