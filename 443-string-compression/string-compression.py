class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        right = 0
        left = 0
        s = ""
        count = 0

        while right < n:

            while right < n and chars[left] == chars[right]:
                count+=1
                right+=1

            if count > 1:
                s += chars[left] + str(count)

            else:
                s += chars[left]
            count = 0
            left = right

        while chars:
            chars.pop()
        for i in s:
            chars.append(i)
        