kor=float(input("국어성적 입력."))
eng=float(input("영어성적 입력."))
math=float(input("수학성적 입력."))

avg=(kor+eng+math)/3

if avg >= 60 and kor >=50 and eng >=50 and math>=50 :
    
    print("성적 평균은", avg,"이며 과락 과목도 없기 때문에 합격입니다")

else:
    if avg >= 60:
        print("성적 평균은", avg,"이지만 50점 미만 과락이 있어서. 불합격입니다")
    else:
        print("성적 평균은",avg,"이며. 불합격입니다")


kor=float(input("국어성적 입력."))
eng=float(input("영어성적 입력."))
math=float(input("수학성적 입력."))

avg=(kor+eng+math)/3

if avg >=60:
    if kor<50 or eng<50 or math<50:
        print("성적 평균은",avg,"이지만 과락목록이 있어 때문에 불합격입니다")
    else:
        print("성적 평균은",avg,"과락과목도 없기 때문에 합격입니다")

height = float(input("키를 m 단위로 입력해 주세요"))
weight = float(input("몸무게 kg 단위로 입력해 주세요"))

bmi = weight/(height*height)

if bmi < 18.5:
    print("BMI지수는", bmi,"이며 저체중 상태입니다")
elif bmi < 23:
    print("BMI지수는", bmi,"이며 정상 상태입니다")
elif bmi < 25:
    print("BMI지수는", bmi,"이며 과체중 상태입니다")
elif bmi < 30:
    print("BMI지수는", bmi,"이며 심각한비만1 상태입니다")
elif bmi < 40:
    print("BMI지수는", bmi,"이며 심각한비만2 상태입니다")
else:
    print("BMI지수는", bmi,"이며 심각한비만3 상태입니다")
         
