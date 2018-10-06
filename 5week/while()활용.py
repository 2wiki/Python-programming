

#이르믕ㄹ 입력 받아서 성이 김 최 이 이면 통과
#아니면 다시 입력받음
#입력받는 횟수가 5회 이상이면
#더이상 입력받지않고 종료


firstname = int(input("성을 입력하세요"))
count=1



while firstname != 김 or 이 or 최  and count<=5:
    firstname = int(input("성을 입력하시오:"))
    count = count + 1
    
           
if count>5:
    print("비밀번호 입력 오류가 3번 발생하여 처리할수 없습니다")
else:
    print("비밀번호가 정확합니다!")      
           
