#Arcade game: player with highest score ranks 1 on leaderboard. 
# Players with equal scores receive same ranking number,and the next player(s) receive immediately
#following ranking number.
#ranked: current ranking, player: new scores, which will cause ranked to update based on player scores
#return player's rank after new score
def climbingLeaderBoard(ranked, player):
   ranked=list(set(ranked)) #convert to set (eliminate duplicates), then back to list
   ranked.sort() #sor in ascending order
   n=len(ranked)
   i=0 #to keep track we're staying in range
   result = []
   for play in player:
        while i < n and ranked[i] <= play:
            i+=1
        result.append(n-i+1)
   return result