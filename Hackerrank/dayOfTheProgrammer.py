#return date of 256th day of the year (in Russia, taking into account Julian and Gregorian calendars)


#Check if the year is the one when they changed calendars, 1918

    
def dayOfProgrammer(year):
    if year < 1700 or year > 2700:
            return 
            
    elif year==1918:
        return '26.09.1918' #156th day of the year for 1918, when the calendar change was made
    #check rest of the conditions: if the year is before 1917, Julian calendar, or not a leap year
        
    elif year < 1918:
        if year%4==0:
            return '12.09.'+str(year)
                    
        else:
            return '13.09.'+str(year)
                    
    elif year > 1918:
        if year%400==0 or year%4==0 and year%100!=0:
            return '12.09.'+str(year) 
        
        else:
            return '13.09.'+str(year)