def solution(S): 
    
    freqOfLetter = [0] * 26
  
    for i in range(len(S)): 
        freqOfLetter[ord(S[i]) - ord('a')] += 1

    LetterFreqMap = dict() 
  
    for i in range(26): 
  
        if (freqOfLetter[i] != 0): 
            LetterFreqMap[freqOfLetter[i]] = LetterFreqMap.get(freqOfLetter[i], 0) + 1
  
    
    deletions = 0
  
    a = list(LetterFreqMap.keys()) 
    a = a[::-1] 
    a.sort() 

    while len(a) > 0:

        it = a.pop() 
  
        if (it == 0): 
            break
  
        while (LetterFreqMap[it] > 1): 
  
            deletions += 1
            LetterFreqMap[it] -= 1
  
            if (it - 1) in LetterFreqMap.keys(): 
                LetterFreqMap[it - 1] += 1
            elif (it -1) > 0: 
                a.insert(0,it-1) 
                LetterFreqMap[it-1] = 1
  
    return deletions