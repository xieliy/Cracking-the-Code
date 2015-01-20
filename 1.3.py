'''
1.3
'''       
def func(String1, String2):
    if len(String1) != len(String2):
        return False
    else:
        return all(String1.count(char) == String2.count(char) for char in String1)
    



