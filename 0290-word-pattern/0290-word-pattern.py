class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for i in range(len(pattern)):
            ch = pattern[i]
            word = words[i]

            if ch not in char_to_word and word not in word_to_char:
                char_to_word[ch] = word
                word_to_char[word] = ch
            elif char_to_word.get(ch) != word or word_to_char.get(word) != ch:
                return False

        return True
        