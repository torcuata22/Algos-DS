#def timeConversion(s):
#slice the string to check for AM or PM, then if PM add 12 to the first two values of the string if AM, leave it alone
#s = HH:MM:SSA/PM --> AM/PM: s[:-2], HH is s[:2],  MM:SS will be s[2:-2]
#use split() to separate string into list: split(:)
    # time = s.split(":")
    # time[0] = int(time[0]%12)
    # if "PM" in s[-2]:
    #     time[0] +=12
    # time[0] = '%02d'%time[0]
    # return ":".join(time)[:-2]

def timeConversion(s):
        
    if s[:-2] == "AM" and s[:2]== "12":
        return "00" + s[2:-2]
        
    elif s[-2] == "PM" and s[:2] == 12:
        return s[-2]
    else:
        ans = int(s[:2]) +12
        return str(str(ans)+ s[2:8])

    
 
 
    
s="2:05:45AM"
timeConversion(s)