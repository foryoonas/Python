#방법1
print("수를 입력해 주세요 : ")
num=int(input())


i=1

if num<=9:
    while i<=9:
        a=f"{num}X{i}={num*i}"
        print(a)
        i+=1
else :
        print("1~9 사이의 수를 입력해 주세요.")

#방법2
a= int(input())
if a<=9:
    while i<=9:
        num=a*i
        printf("{num}X{i}={num*i}")
        i=i+1
else:
    print("1~9 사이의 수를 입력해 주세요.")
