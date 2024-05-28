def insert_year(p,r,n):    #원리금을 계산하는 insert_year()함수 정의하기
    return p * (1+r)**n    #원금 p,연간 이율 r, 거치연수n을 입력 받아 원리금 result를 반환

#난생이가 가입한 예금 상품의 원금, 연간 이율, 거치 연수를 변수에 할당하고 함수의 입력을 사용
p=30000000
r=0.051
n=3

result=insert_year(p,r,n) 

print(('원금:{0}','이자:{1}'.format(p,result-p)))
