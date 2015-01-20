'''
1.1
'''       
def func(String):
    if len(String) == 1:
        return 'True'
    else:
        str0 = String[0]
        String = String[1:]
        for i in String:
            if i == str0:
                return 'False'    
        tf = func(String)
        return 'True'



