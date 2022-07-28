#count how many times points record has been broken (high points and low points) and return most point records, the least point records
def breakingRecords(scores):
    min = max = 0
    minscore = maxscore=scores[0]
    for i in range(1, len(scores)):
        if minscore < scores[i]:
            minscore = scores[i]
            min +=1
        elif maxscore > scores[i]:
            maxscore = scores[i]
            max +=1
    return min, max