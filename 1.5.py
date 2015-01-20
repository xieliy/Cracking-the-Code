'''
1.5
'''       
def func(String):
    i = 0
    List = []
    flag = 0#two ending case
    while i <= len(String)-1:
        count = 1
        while String[i] == String[i+1]:
            count = count + 1
            i = i + 1
            if i == len(String)-1:
                flag = 1
                break
        List.append(String[i])
        List.append(count)
        i = i + 1
        if i == len(String)-1 and flag == 0: 
            List.append(String[i])
            List.append(1)
            break
    
    if len(String) <= len(List):
        return String
    else:
        return ''.join(str(v) for v in List)
        
    



