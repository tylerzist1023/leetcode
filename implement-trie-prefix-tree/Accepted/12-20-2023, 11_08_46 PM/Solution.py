// https://leetcode.com/problems/implement-trie-prefix-tree

class Trie(object):
    def __init__(self):
        self.nodes = {}
        self.accepting = False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if len(word) == 0:
            self.accepting = True
            return
        if word[0] in self.nodes:
            self.nodes[word[0]].insert(word[1:])
        else:
            self.nodes[word[0]] = Trie()
            self.nodes[word[0]].insert(word[1:])

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if len(word) == 0:
            if len(self.nodes) == 0 or self.accepting:
                return True
            else:
                return False
        if word[0] in self.nodes:
            return self.nodes[word[0]].search(word[1:])
        else:
            return False
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        if len(prefix) == 0:
            return True
        if prefix[0] in self.nodes:
            return self.nodes[prefix[0]].startsWith(prefix[1:])
        else:
            return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)