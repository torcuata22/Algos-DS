def birthdayCakeCandles(candles):
    candles.sort()
    result = candles.count(candles[len(candles)-1]) #count how many times last item calie appears in the list
    
    print(result)
    
    
candles=[3,2,1,3]
birthdayCakeCandles(candles)
    
        
