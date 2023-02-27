def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  table = sorted(S)
  maxDiners = 0
  socialDis = K + 1
  
  #The prev seated diner minus seating guidlines minus the first seat
  maxDiners += ((table[0] - 1) // socialDis)
  
  #A check to see that there are remaining seats after the last seated diner.
  maxDiners += ((N - table[-1]) // socialDis)
  
  for diners in range(M - 1):
    group1 = table[diners + 1]
    group2 = table[diners]
    
    #To find the next possible seat for a diner
    maxDiners += ((group1 - group2 - socialDis) // socialDis)
      
  return maxDiners
