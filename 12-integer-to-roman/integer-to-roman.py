class Solution:
    def intToRoman(self, num: int) -> str:
        maps = {
            
            1000:"M",
            900:"CM",
            500:"D",
            400:"CD",
            100:"C",
            90:"XC",
            50:"L",
            40:"XL",
            10:"X",
            9:"IX",
            5:"V",
            4:"IV",
            1:"I"
        
        }

        # 3749//1000
        ans = ""
        for key, val in maps.items():
            if num == 0:
                break

            count = num // key

            ans = ans + val*count 
            num = num - key*count 
            # print(num)

        return ans


        