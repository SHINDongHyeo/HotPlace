# 🎉 HotPlace
<b>주제 :</b> 인스타그램 크롤링을 통해 사람들이 많이 찾는 지역을 찾아 추천해준다.               
<b>사용한 도구 :</b> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/> <img src="https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=selenium&logoColor=white"/> <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/> <img src="https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white"/>    
<b>핵심폴더 :</b> 루트 디렉토리에서 `trip` 이라는 application(폴더)을 만들고 해당 폴더에 코드를 작성했습니다.

## 1. 크롤링🔍️
웹 크롤링을 위해 <img src="https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=selenium&logoColor=white"/> 라이브러리를 사용했고, <img src="https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white"/>에서 `#여행`, `#핫플` 등의 태그를 검색해 나온 게시물에 적힌 장소 정보를 수집했습니다.

>< 루트 디렉토리에 있는 `insta_crawl.py`파일 실행 결과 >       
>1)`config.ini`파일에 적힌 내 계정 정보를 이용해 인스타그램에 로그인                
>( `config.ini`파일은 개인정보이므로 `.gitignore`파일에 설정되어 github에는 올라와 있지 않습니다! )            
><img src="https://github.com/SHINDongHyeo/HotPlace/blob/main/images/1.png" width="400" height="600"/>                   
>                     
>2)미리 설정한 "#여행" 태그를 검색하여 나온 게시물을 클릭하고 게시물 상단 부분에 있는 위치정보와 해당 게시물의 url을 수집, 이후 다음 게시물 버튼 클릭과 정보 수집 그리고 태그 검색을 원하는 만큼 반복 실행               
><img src="https://github.com/SHINDongHyeo/HotPlace/blob/main/images/2.png" width="400" height="600"/>              
>
>3)Django의 Model로 만들어 놓은 InstaHP클래스에 저장
>```python
># result_location는 게시물의 위치정보와 url을 쌍으로 저장해놓은 리스트이다.
>for loc,url in result_location:
>            InstaHP(location=loc, url=url).save()
>```




## 2. 분석🧐
데이터 분석을 위해 <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white"/> 라이브러리를 사용했습니다.


## 3. 웹 페이지🌐
<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/>를 이용해 웹 페이지를 구성했고, <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/>도 사용해 동적인 요소를 넣었습니다.               
>1)`index.html`파일에서 자바스크립트 부분으로 `async function`과 `ajax`, `jquery`를 사용해 웹 페이지의 UI변경(ex.로딩바 움직이기) 및 비동기 처리(ex.특정 태그로 인스타그램 크롤링하기)가 모두 순차적으로 일어나게 하여 비동기 처리로 크롤링이 완료될 때마다 로딩바가 움직이게 꾸몄습니다.                
><img src="https://github.com/SHINDongHyeo/HotPlace/blob/main/images/3.png" width="800" height="200"/>
