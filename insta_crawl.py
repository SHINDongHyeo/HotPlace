#작업에 필요한 라이브러리 
from selenium import webdriver 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import urllib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "HotPlace.settings")
import django
django.setup()
from trip.models import InstaHP

# 웹 열기
dr = webdriver.Chrome("C:\MyStudy\chromedriver.exe") #웹드라이버로 크롬 웹 켜기
wait = WebDriverWait(dr, 10)
dr.set_window_size(414, 800) 	#브라우저 크기 414*800으로 고정
dr.get('https://www.instagram.com/') #인스타그램 웹 켜기
wait.until(EC.element_to_be_clickable((By.NAME, "username")))
wait.until(EC.element_to_be_clickable((By.NAME,"password")))
print("아이디입력할수있는상태임")

# 로그인
id_box = dr.find_element(By.NAME,"username")   #아이디 입력창
password_box = dr.find_element(By.NAME,"password")     #비밀번호 입력창
login_button = dr.find_element(By.CLASS_NAME,"sqdOP,L3NKy,y3zKF")      #로그인 버튼


#동작 제어
act = ActionChains(dr)      #동작 명령어 지정
act.send_keys_to_element(id_box, 'shindonghyeo@naver.com').send_keys_to_element(password_box, 'instacrawl2022!').click(login_button).perform()     #아이디 입력, 비밀 번호 입력, 로그인 버튼 클릭 수행
print("로그인보내기")


# 정보 저장하시겠습니까? 넘기기
wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"pV7Qt,DPiy6,qF0y9,Igw0E,IwRSH,eGOV_,acqo5,_4EzTm,qhGB0,ZUqME ")))
later_button = dr.find_element(By.CLASS_NAME,"sqdOP,yWX7d,y3zKF ")
later_button.click()
print("클릭햇음")


# 알림 설정 나중에 하기
wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"_a9--,_a9_1")))
alarm_later_button = dr.find_element(By.CLASS_NAME,"_a9--,_a9_1")
alarm_later_button.click()
print("클릭햇음2")


# keyword 설정
keywords_origin = []
keywords=[]
keywords_origin=[
    "여행",
    "여행스타그램",
    "여행추천",
    "여행에미치다",
]
for keyword in keywords_origin:
    keywords.append(urllib.parse.quote(keyword))


# keywords에 저장된 태그들을 이용해 포스트 검색 및 위치값 뽑아 result_location에 저장하기
result_location = []
for keyword in keywords:
    url = f"https://www.instagram.com/explore/tags/{keyword}/"
    dr.get(url)    


    # 개별 포스트 클릭하고 위치내용 가져오기
    try:
        first_post = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"_aagu")))
        first_post.click()
    except:
        break
    try:
        post_content_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"._aaqm")))
        post_content = post_content_box.text
        if post_content == "":
            pass
        else:
            result_location.append(post_content)
    except:
        pass
 

    # 다음 게시물 넘어가기 버튼 클릭
    try:
        next_post_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"_aaqg,_aaqh")))
        next_post_button.click()
    except:
        break


    # 태그 뽑고 다음 게시물 넘어가기 반복( 횟수 : 10번 )
    for i in range(100):
        try:
            post_content_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"._aaqm")))
            post_content = post_content_box.text
            if post_content == "":
                pass
            else:
                result_location.append(post_content)
        except:
            pass
        try:
            next_post_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"_aaqg,_aaqh")))
            next_post_button.click()
        except:
            break


# Django InstaHP 클래스(모델)에 저장
for loc in result_location:
	InstaHP(location=loc).save()