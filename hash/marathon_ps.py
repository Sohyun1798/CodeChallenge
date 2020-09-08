def solution(participant, completion):
    
    for person in completion:
        if person in participant:
            participant.remove(person)
            
    answer = participant[0]

    return answer

# accuraccy is fine, but efficency is not good

import collections

def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer)[0]