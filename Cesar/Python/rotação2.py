def rotacao():
    s1 = input('S1 : ')
    s2 = input('S2 : ')
    s22 = s2 + s2
    lens22 = len(s22)
    lens1 = len(s1)
    if (lens1*2) == lens22 : 
            if s22.find(s1) != -1 :
                print(s2 ," é rotação de ",s1)
                return True
            else:
                print(s2," não é rotação de ", s1)
                return False
    else:
        print(s2," não é rotação de ", s1)
        return False

rotacao()
