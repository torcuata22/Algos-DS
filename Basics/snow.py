#using dictionry to keep record of snowfall
snow_fall = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}

def print_total_inches(snow_fall):
    total_inches = 0
    for inches in snow_fall.values():
        total_inches += inches
        print("Total snowfall in inches: ", total_inches)

print_total_inches(snow_fall)

#adding records for Thursday
user_input = input("How many inches fell on Thursday?")
snow_fall["Thursday"] = int(user_input)
print_total_inches(snow_fall)
