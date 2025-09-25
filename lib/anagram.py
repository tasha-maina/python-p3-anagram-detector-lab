# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, candidates):
        """
        Return all words from `candidates` that are anagrams of self.word.
        
        """
        #Normalize the word: sorted letters
        target = sorted(self.word)

        matches = []
        for candidate in candidates:
            if sorted(candidate) == target:
                matches.append(candidate)
        return matches 
        