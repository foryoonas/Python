# 함수사용 안 했을 때 
score=[]
a=int(input("학생수: "))
total=0
for i in range(0,n):
    jumsu=int(input("[%d]영어시험성적: " % (i+1)))
    total +=jumsu
    score.append(jumsu)
    
print("score=",score)
print("total=",total)
print("avg=",total/n)

# 함수사용 했을 때
def printResult(list,t):
    num=len(list)
    print("score=",list)
    print("total=",t)
    print("avg=",t/num)
printResult(score,total)