#Calculate library fines:
#if on time, no fine. If late but within same month, 15 per day. If not same month but same year, 500
#per month late, and if returned in different year, 10000
#return date: d1,m1, y1 
#due date: d2, m2, y2
#to be on time, d1, m1, y1 < d2, m2, y2


def libraryFine(d1, m1, y1, d2, m2, y2):
    total = 0
    if y1 > y2:
        total +=10000
    elif y1 == y2 and m1 > m2:
        total += 500 * (m1-m2)
    elif y1 == y2 and m1 == m2 and d1>d2:
        total += 15*(d1-d2)
    return total