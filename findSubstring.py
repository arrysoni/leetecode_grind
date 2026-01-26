class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words

        if len(s) < total_len:
            return []

        need = {}
        for w in words:
            need[w] = need.get(w, 0) + 1

        res = []

        # We run word_len different sliding windows to align with word boundaries
        for offset in range(word_len):
            left = offset
            seen = {}
            count = 0

            # step through the string in word-sized jumps
            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in need:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    # If we have too many of this word, shrink from the left
                    while seen[word] > need[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    # If window has exactly num_words words, record answer
                    if count == num_words:
                        res.append(left)

                        # move left forward by one word to keep sliding
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    # reset window if word not allowed
                    seen = {}
                    count = 0
                    left = right + word_len

        return res


s1 = "barfoothefoobarman"
words1 = ["foo", "bar"]
print(Solution().findSubstring(s1, words1))  # [0, 9]

s2 = "wordgoodgoodgoodbestword"
words2 = ["word", "good", "best", "word"]
print(Solution().findSubstring(s2, words2))

s3 = "barfoofoobarthefoobarman"
words3 = ["bar", "foo", "the"]
print(Solution().findSubstring(s3, words3))
