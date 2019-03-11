#turtle 함수 선언
import turtle
#좌표 input받기
x1 ,y1 ,x2,y2 = eval(input("Enter x1: ")),eval(input("Enter y1: ")),eval(input("Enter x2: ")),eval(input("Enter y2: "))
#turtle 그리기
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()

turtle.write("Point 1")

turtle.goto(x2,y2)

turtle.write("Point 2")
#거리구하는 공식
distance = ((x2 - x1)**2 + (y2-y1)**2)**0.5
#write로 출력하기
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
#소숫점 2째자리 까지만 구하기
turtle.write(int(distance)*100/100)




turtle.done()