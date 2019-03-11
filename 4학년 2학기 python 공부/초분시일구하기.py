#time 함수를 사용하겠다
import time
#GTM의 시간으로 부터 지금까지 흘러온 시간
totalSecondes = int(time.time())
#현재 초 구하기
curruntSecondes = totalSecondes % 60
#현재 분을 구하기 위해 tatalMinute 구하기
totalMinute = totalSecondes // 60
#현재 분 구하기
curruntMinute = totalMinute % 60
#현재 시를 구하기 위해 totalHour 구하기
totalHour = totalMinute // 60
#현재 시 구하기
curruntHour = totalHour % 24
#현재 일을 구하기 위해  totalDay 구하기
totalDay = totalHour // 24
#현재 일 구하기
curruntDay = totalDay % 30
#현재 달을 구하기 위해 totalMonth 구하기
totalMonth = totalDay // 30
#현재 달 구하기
currunMonth = totalDay % 12

print(currunMonth,"개월",curruntDay,"일",curruntHour,"시",curruntMinute,"분",curruntSecondes,"초")