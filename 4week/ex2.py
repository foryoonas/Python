#반복하여 동작하는 자판기를 while 반복문으로 정의한다.
while True:

#사용자에게 메뉴를 알려주고 동전 액수와 메뉴 입력 받기
    print('음료목록 1. 오렌지주스(100원), 2.커피(200원), 3.콜라(300원)')
    coin = int(input('동전을 넣으세요: '))
    drink = int(input('음료를 고르세요: '))
    
#오렌지 주스를 선택했을 떄
    if drink ==1:
        if coin>=100: 
            remain=coin-100  #거스름돈
            print('오렌지주스가 곧 제공됩니다.')
            print('거스름돈은 {}원 입니다.'.format(remain))
        else:
            print('잔액이 부족합니다.')

#커피를 선택했을 때      
    elif drink==2:
        if coin>=200:
            remain=coin-200
            print('커피가 곧 제공됩니다.')
            print('거스름돈은 {}원 입니다.'.format(remain))
        else:
            print('잔액이 부족합니다.')

# 콜라를 선택했을 때         
    elif drink==3:
        if coin>=300:
            remain=coin-300
            print('콜리가 곧 제공됩니다.')
            print('거스름돈은 {}원 입니다.'.format(remain))
        else:
            print('잔액이 부족합니다.')

# 메뉴를 잘못입력했을 떄
    else:
        print('없는 메뉴입니다. 다시 입력해주세요.')