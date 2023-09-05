# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        result = []
        sorted_word = sorted(self.word.lower())

        for candidate in word_list:
            if sorted_word == sorted(candidate.lower()) and self.word.lower() != candidate.lower():
                result.append(candidate)


        return result
