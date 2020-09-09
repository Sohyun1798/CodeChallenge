answer = 0

def bfs(index, result, target, numbers):
    global answer
    
    if index == len(numbers):
        if result == target:
            answer += 1
        return
    
    bfs(index+1, result+numbers[index], target, numbers )
    bfs(index+1, result-numbers[index], target, numbers )

def solution(numbers, target):
    global answer
    bfs(0, 0, target, numbers)
    
    return answer