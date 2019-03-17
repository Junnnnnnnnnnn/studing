#turtle 함수 사용하기
import turtle
#변수 초기화 input받기
pointX , pointY ,radius= eval(input("Enter pointX: ")),eval(input("Enter pointY: ")),eval(input("Enter radius: "))
#면적구하기 정의
erea = radius * radius * 3.141592

#turtle 함수 이용하여 원 그리기
turtle.penup()
#원그릴때 좌표 위로 그림 그래서 반지름 만큼 밑으로 좌표를 이동
turtle.goto(pointX , pointY-radius)
#원 그리기
turtle.pendown()
turtle.circle(radius)
#좌표 출력하기 위해 이동
turtle.penup()
turtle.goto(pointX , pointY)
#원가운대에 면적 값 출력하기
turtle.pendown()
#소수점 둘째자리 까지만 사용
turtle.write(int(erea*100)/100)
turtle.hideturtle()

turtle.done()