class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mag_dict = {}
        ran_dict = {}

        for i in range(len(ransomNote)):
            if ransomNote[i] not in ran_dict:
                ran_dict[ransomNote[i]]=1
            else:
                ran_dict[ransomNote[i]]+=1
        
        for i in range(len(magazine)):
            if magazine[i] not in mag_dict:
                mag_dict[magazine[i]]=1
            else:
                mag_dict[magazine[i]]+=1
        
        for key, val in ran_dict.items():
            if key not in mag_dict.keys() or mag_dict[key] < val:
                return False

        return True