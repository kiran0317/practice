class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)
        if word1_len > word2_len:
            iterr = word2_len
            left_over = word1[word2_len:]
        else:
            iterr = word1_len
            left_over = word2[word1_len:]
        res = []
        for i in range(iterr):
            res.append(word1[i])
            res.append(word2[i])
        return ''.join(res) + left_over