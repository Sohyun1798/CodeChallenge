def solution(S): 
    
    ans = 0
    freq_map = dict()
    Letter_num = [0] * 26
  
    for i in range(len(S)):

        Letter_num[ord(S[i]) - ord('a')] += 1

    for i in range(26): 
  
        if (Letter_num[i] != 0): 
            freq_map[Letter_num[i]] = freq_map.get(Letter_num[i], 0) + 1
  
    temp = list(freq_map.keys()) 
    temp = temp[::-1] 
    temp.sort() 

    while len(temp) > 0:

        a = temp.pop()
  
        if (a == 0): 
            break
  
        while (freq_map[a] > 1): 
  
            ans += 1
            freq_map[a] -= 1
  
            if (a - 1) in freq_map.keys(): 
                freq_map[a - 1] += 1
            elif (a -1) > 0: 
                temp.insert(0,a-1) 
                freq_map[a-1] = 1
  
    return ans 