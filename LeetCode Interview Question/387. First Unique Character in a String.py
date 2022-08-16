class Solution:
    def firstUniqChar(self, s: str) -> int:
        dictn = {}

        for str in s:
            if str in dictn:
                dictn[str] = dictn[str] + 1
            else:
                dictn[str] = 1

        #print(dictn)
        # for k in dictn.values():
        #     print('values: ', k)
        #     if k == 1:
        #         #return dictn.keys()
        #         print('keys' , dictn.keys())
        #         break

        for name, c in dictn.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
            if c == 1:
                #print(name)
                #break
                return s.index(name)

        return -1


a1= Solution()
print(a1.firstUniqChar("aabb"))