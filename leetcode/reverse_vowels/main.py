

def reverseVowels(s: str) -> str:
        s.lower()
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        print(s)
        if len(s) == 2:
            if s[0] in vowels and s[1] in vowels:
                s[0], s[1] = s[1], s[0]
        else:
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] not in vowels and l < r:
                    l += 1
                if s[r] not in vowels and l < r:
                    r -= 1
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return "".join(s)


s = input("string = ")
print(reverseVowels(s))