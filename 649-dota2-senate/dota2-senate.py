class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = []
        dire = []
        n = len(senate)

        for i in range(len(senate)):
            if senate[i] == "R":
                rad.append(i)
            else:
                dire.append(i)

        while rad and dire:
            if rad[0] < dire[0]:
                rad.append(n)
                n+=1
            else:
                dire.append(n)
                n+=1
          
            rad.pop(0)
            dire.pop(0)

        if rad:
            return "Radiant"
        if dire:
            return "Dire"

                
        
    