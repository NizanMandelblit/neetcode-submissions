class TrieNode():
    def __init__(self):
        self.children={}
        self.endOfWord=False


class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        curr=self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        curr=self.root

        def dfs(i ,curr):
            if not curr:
                return False
            if i == len(word):
                return curr.endOfWord
            
            c = word[i]
            if c == '.':
                for key in curr.children.keys():
                    if dfs(i+1, curr.children[key]):
                        return True
                return False
            elif c not in curr.children:
                return False
            else:
                return dfs(i+1, curr.children[c])

        return dfs(0,curr)


            
        
