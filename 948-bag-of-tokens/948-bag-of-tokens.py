class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score=0
        tokens.sort()
        start=0
        end=len(tokens)-1
        Max=0
        while start<=end:
            if tokens[start]<=power:
                power-=tokens[start]
                score+=1
                start+=1
                Max=max(Max,score)
            elif score>0:
                power+=tokens[end]
                score-=1
                end-=1
            else:
                break
        return Max
            