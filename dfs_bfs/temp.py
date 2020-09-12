answer = 0

def dfs(begin, target, words):
    global answer

    for word in words:

        if word == begin:
            return answer

        if len(set(target)-set(word)) == 1:
            temp = word
            answer += 1
            print(word)
            words.remove(word)
            dfs(temp, target, words)

        
def solution(begin, target, words):
    global answer
    
    if target not in words:
        return answer
    else:
        answer = dfs(begin, target, words)

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))