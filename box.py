def box1(): # def함수로 box1이라는 이름으로 함수를 만들어준다
    n = int(input('n? ')) # 숫자를 입력하면 정수형으로 n이라는 변수로 저장한다.
    for y in range(n):#0부터 입력 받은 숫자-1 만큼 반복할수 있도록 변수 y에 저장한다
        for x in range(n):#0부터 입력 받은 숫자-1 만큼 반복할수 있도록 변수 x에 저장한다
            #이제 체크박스를 만들기위한 조건을 만들어준다. 
            condition = y == 0 or x == 0 or x == n - 1 or y == n -1  
            if condition:
                print ("#", end='')#조건을 만족하면 #으로 출력한고 마지막은 ""(빈칸)으로 출력한다
            else:
                print(" ", end= '')#조건을 만족하면 ""(빈칸)으로 출력한고 마지막은 ""(빈칸)으로 출력한다
        print() #지금까지 거쳐온 과정을 출력해준다.
    return box1 #None 값이 출력되지 않게 리턴값을 지정해준다.
def box2():# def함수로 box2이라는 이름으로 함수를 만들어준다
    n = int(input('n? '))# 숫자를 입력하면 정수형으로 n이라는 변수로 저장한다.
    for y in range(n):#0부터 입력 받은 숫자-1 만큼 반복할수 있도록 변수 y에 저장한다
        for x in range(n):#0부터 입력 받은 숫자-1 만큼 반복할수 있도록 변수 x에 저장한다
             #이제 체크박스를 만들기위한 조건을 만들어준다. 
            condition = x == y or n-x-1 == y 
            if condition:
                print ("#", end='')#조건을 만족하면 #으로 출력한고 마지막은 ""(빈칸)으로 출력한다
            else:
                print(" ", end= '')#조건을 만족하면 ""(빈칸)으로 출력한고 마지막은 ""(빈칸)으로 출력한다
        print()#지금까지 거쳐온 과정을 출력해준다.
    return box2 #None 값이 출력되지 않게 리턴값을 지정해준다.
def box3():# def함수로 box3이라는 이름으로 함수를 만들어준다
    n = int(input('n? '))# 숫자를 입력하면 정수형으로 n이라는 변수로 저장한다.
    for y in range(n):#0부터 입력 받은 숫자-1 만큼 반복할수 있도록 변수 y에 저장한다
        for x in range(n):#0부터 입력 받은 숫자-1 만큼 반복할수 있도록 변수 x에 저장한다
            #이제 체크박스를 만들기위한 조건을 만들어준다. 
            condition = y == 0 or x == 0 or x == n - 1 or y == n -1 or x == y or n-x-1 == y 
            if condition:
                print ("#", end='')#조건을 만족하면 #으로 출력한고 마지막은 ""(빈칸)으로 출력한다
            else:
                print(" ", end= '')#조건을 만족하면 ""(빈칸)으로 출력한고 마지막은 ""(빈칸)으로 출력한다
        print()#지금까지 거쳐온 과정을 출력해준다.
    return box3 #None 값이 출력되지 않게 리턴값을 지정해준다.

