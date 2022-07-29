#In this game, there are sequentially numbered clouds that can be thunderheads or cumulus clouds.
# Character must jump from cloud to cloud until it reaches the start again. 
#There is an array of clouds,  and an energy level . 
# The character starts from c[0] and uses  unit of energy to make a jump of size k 
# to cloud c(i+k)%n. If it lands on a thundercloud,c[i]=1 , its energy (e) decreases
# by  additional units. The game ends when the character lands back on cloud 0.
#given n,k and array with configuration of clouds c, determine final e

def jumpingClouds(c,k):
    energy=100
    i=0
    while True:
        energy = energy-1-2*c[i] #cost of one jump, if c[i]=1 energy drops -2, otherwise c[i]=0
        #we need to make the route self-closing to avoid infinite loop
        i=(i+k)%n
        if i == 0:
            break
        return energy
        
        