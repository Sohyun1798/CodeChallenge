import re

def newID(new_id):
    
    new_id = new_id.lower()
    new_id = re.sub(r'[^a-z\d\-\_\.]+', '',new_id)
    new_id = re.sub(r'[\.]+', '.', new_id)
    new_id = re.sub(r'^[\.]+', '', new_id)
    new_id = re.sub(r'[\.]+$', '', new_id)
            
    if new_id == "": 
        new_id = 'a'
        
    if len(new_id)>=16:
        new_id = new_id[:15]
    
    new_id = re.sub(r'^[\.]+', '', new_id)
    new_id = re.sub(r'[\.]+$', '', new_id)
        
    if len(new_id)<3:
        lastword = new_id[len(new_id)-1]
        while len(new_id)<3:
            new_id = new_id+lastword
        
    return new_id

def solution(new_id):
    answer = newID(new_id)
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))