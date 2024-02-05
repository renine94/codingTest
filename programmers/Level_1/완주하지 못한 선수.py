def solution(participant, completion):    
    # participant.sort()
    # completion.sort()
    participant = sorted(participant)
    completion = sorted(completion)
    
    for p, c in zip(participant, completion):
        if p != c:
            return p
    
    return participant[-1]


from collections import Counter

def solution(participant, completion):
    par = Counter(participant)
    com = Counter(completion)
    
    for p, c in par.items():
        if com.get(p) != par[p] or com.get(p) == None:
            return p