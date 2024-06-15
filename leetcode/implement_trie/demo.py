class Trie:

    def __init__(self):
        self.root={}
        
    def insert(self, word: str) -> None:

        cur=self.root

        for letter in word:
            if letter not in cur:
                cur[letter]={}
            cur=cur[letter]

        cur['*']=''

    def search(self, word: str) -> bool:

        cur=self.root
        for letter in word:
            if letter not in cur:
                return False
            cur=cur[letter]

        return '*' in cur
        
    def startsWith(self, prefix: str) -> bool:

        cur=self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur=cur[letter]

        return True

# class Trie:
#     def __init__(self):
#         self.words = {}
#         self.prefixes = {}

#     def insert(self, word: str) -> None:
#         self.words[word] = True

#     def search(self, word: str) -> bool:
#         return self.words.get(word, False)

#     def startsWith(self, prefix: str) -> bool:
#         if self.prefixes.get(prefix, False):
#             return True

#         for word in self.words:
#             if word.startswith(prefix):
#                 self.prefixes[prefix] = True
#                 return True

#         return False

# Your Trie object will be instantiated and called as such:
word = "apple"
prefix = "app"
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.search("app")
param_4 = obj.startsWith(prefix)

print(
    f"search({word}) = {param_2} |search(app) = {param_3} |startsWith({prefix}) = {param_4}"
)

obj.insert("app")
param_3 = obj.search("app")
print(f"search(app) = {param_3}")
