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
import configparser as parser
import random
import traceback
import os
import django
from trip.models import InstaHP


class insta:
    dr = 0
    wait = 0

    def setting():
        global dr
        global wait

        os.environ.setdefault('DJANGO_SETTINGS_MODULE', "HotPlace.settings")
        django.setup()
        # 웹 열기
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True) # 해당함수가 종료되어도 크롬창은 꺼지지 않고 유지되게 옵션설정
        dr = webdriver.Chrome("C:\MyStudy\chromedriver.exe", options=options) #웹드라이버로 크롬 웹 켜기
        wait = WebDriverWait(dr, 10)
        dr.maximize_window()	#브라우저 화면 크기 최대로
        dr.get('https://www.instagram.com/') #인스타그램 웹 켜기    
        wait.until(EC.element_to_be_clickable((By.NAME, "username")))
        wait.until(EC.element_to_be_clickable((By.NAME,"password")))
        print("아이디입력할수있는상태임")

        # 로그인
        id_box = dr.find_element(By.NAME,"username")   #아이디 입력창
        password_box = dr.find_element(By.NAME,"password")     #비밀번호 입력창
        login_button = dr.find_element(By.CLASS_NAME,"sqdOP,L3NKy,y3zKF")      #로그인 버튼


        #동작 제어
        properties = parser.ConfigParser()
        properties.read("./config.ini")
        Account = properties["ACCOUNT"]
        # act = ActionChains(dr)      #동작 명령어 지정
        # act.send_keys_to_element(id_box, Account["id"]).send_keys_to_element(password_box, Account["pw"]).click(login_button).perform()     #아이디 입력, 비밀 번호 입력, 로그인 버튼 클릭 수행
        id_box.send_keys(Account["id"])
        time.sleep(random.uniform(1,3))
        password_box.send_keys(Account["pw"])
        time.sleep(random.uniform(1,3))
        login_button.click()
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
    

    def crawling(keyword_arg, number_of_posts):
        global dr
        global wait
        result_location = []

        keyword=urllib.parse.quote(keyword_arg)
        
        url = f"https://www.instagram.com/explore/tags/{keyword}/"
        dr.get(url)    

        # 개별 포스트 클릭하고 위치내용 가져오기
        try:
            first_post = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"_aagu")))
            first_post.click()
        except Exception as e:
            print("1번문제", e)
            pass
        try:
            post_content_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"._aaqm")))
            post_content = post_content_box.text
            
            likeit1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"._aacl._aaco._aacw._adda._aacx._aada._aade")))
            likeit = likeit1.find_element(By.TAG_NAME,"span")

            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"._a9ym")))
            comments = dr.find_elements(By.CSS_SELECTOR,"._a9ym")
            num_comments = len(comments) # 댓글 갯수

            # for i in comments:
            #     comment = i.find_element(By.CSS_SELECTOR,"._aacl._aaco._aacu._aacx._aad7._aade")
            #     print(comment.text) # 댓글 내용

            if post_content == "":
                pass
            else:
                result_location.append((post_content, dr.current_url, likeit.text.replace(",",""), num_comments))
        except Exception as e:
            print("2번문제",e)
            pass
        print("첫번째게시물수집완료")

        # 다음 게시물 넘어가기 버튼 클릭
        try:
            next_post_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"_aaqg,_aaqh")))
            next_post_button.click()
        except Exception as e:
            print("3번문제",e)
            pass


        # 태그 뽑고 다음 게시물 넘어가기 반복( 횟수 : 10번 ) ############################################################################
        for i in range(int(number_of_posts)-1):
            try:
                post_content_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"._aaqm")))
                post_content = post_content_box.text
                
                try:
                    # likeit1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"._aacl._aaco._aacw._adda._aacx._aada._aade")))
                    likeit1 = dr.find_element(By.CSS_SELECTOR,"._aacl._aaco._aacw._adda._aacx._aada._aade")
                    likeit = likeit1.find_element(By.TAG_NAME,"span")
                    like = likeit.text.replace(",","")
                except:
                    like=0

                try:
                    # comments_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"._a9ym")))
                    comments_box = dr.find_element(By.CSS_SELECTOR,"._a9ym")
                    num_comments = len(comments_box) # 댓글 갯수
                except:
                    num_comments = 0


                if post_content == "":
                    pass
                else:
                    result_location.append((post_content,dr.current_url, like, num_comments))
            except Exception as e:
                print("4번문제",e)
                print(traceback.format_exc())
            try:
                next_post_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"_aaqg,_aaqh")))
                next_post_button.click()
            except Exception as e:
                print("5번문제",e)
                break
            print(i,"번째게시물수집완료")
        
            # Django InstaHP 클래스(모델)에 저장
        print(result_location)
        for loc,url,like,comments in result_location:
            InstaHP(location=loc, url=url, like=like, comments=comments).save()