from itertools import combinations
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:

        def generate_mask(word):
            masks=set()
            word=list(word)
            n=len(word)

            masks.add("".join(word))

            for i in range(n):
                temp=word[:]
                temp[i]="*"
                masks.add("".join(temp))

            for i,j in combinations(range(n),2):
                temp=word[:]
                temp[i]="*"
                temp[j]="*"
                masks.add("".join(temp))
            return masks

        patterns=set()

        for word in dictionary:
            patterns.update(generate_mask(word))

        result=[]

        for word in queries:
            for mask in generate_mask(word):
                if mask in patterns:
                    result.append(word)
                    break
        return result

