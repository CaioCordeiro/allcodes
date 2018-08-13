def isreturn():
    s1 = input('')
    s2 = input('')
    lens1 = len(s1)
    lens2 = len(s2)
    lens1iter = lens1 -1
    if lens1 != lens2:
        return False
    else:
        for i in range(0,(lens1iter)):
            char = s1[i]
            chars = s1[i+1]
            for x in range (0,(lens1iter)):
                
                char2 = s2[x]
                
                y = x+1
                
                if y >= lens1iter:
                    y = 0
                char2s = s2[y]
                
                if char == char2:
                    continue
                else:
                    return False
        return True



res = isreturn()
if res == True :
    print("True")
else:
    print("False")

