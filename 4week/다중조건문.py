Korean = int(input("국어성적:"))
English = int(input("영어성적:"))
Math = int(input("수학성적:"))

Mean = (Korean + English + Math)/3

if Korean<50 or English<50 or Math<50:
    pirnt("과락")

elif Mean>=60:
    print("합격")

else:
    print("불합격")


mon = int(input("월을 입력하세요:"))

if mon in [1,3,5,7,8,10,12]:
     print("31일 까지")

elif mon==2:
    print("28일 또는 29일까지")

elif mon in [4,6,9,11]:
    print("30일 까지")

else :
    print("입력오류")
