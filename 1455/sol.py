

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        i = 0
        while i < len(words):
            j = 0
            while words[i][j] == searchWord[j]:
                if j == len(searchWord)-1:
                    return i+1
                j += 1
                if j >= len(words[i]):
                    break
            i += 1
        return -1


if __name__ == "__main__":
    sentence = "i love eating burger"
    searchWord = "burg"
    sentence2 = "hello helohellohello"
    searchWord2 = "ello"
    sentence3 = "i am tired"
    searchWord3 = "you"
    s = Solution()
    print(s.isPrefixOfWord(sentence, searchWord))
    print(s.isPrefixOfWord(sentence2, searchWord2))
    print(s.isPrefixOfWord(sentence3, searchWord3))