# ๐ HotPlace
<b>์ฃผ์  :</b> ์ธ์คํ๊ทธ๋จ ํฌ๋กค๋ง์ ํตํด ์ฌ๋๋ค์ด ๋ง์ด ์ฐพ๋ ์ง์ญ์ ์ฐพ์ ์ถ์ฒํด์ค๋ค.               
<b>์ฌ์ฉํ ๋๊ตฌ :</b> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/> <img src="https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=selenium&logoColor=white"/> <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/> <img src="https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white"/>    
<b>ํต์ฌํด๋ :</b> ๋ฃจํธ ๋๋ ํ ๋ฆฌ์์ `trip` ์ด๋ผ๋ application(ํด๋)์ ๋ง๋ค๊ณ  ํด๋น ํด๋์ ์ฝ๋๋ฅผ ์์ฑํ์ต๋๋ค.

## 1. ํฌ๋กค๋ง๐๏ธ
์น ํฌ๋กค๋ง์ ์ํด <img src="https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=selenium&logoColor=white"/> ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ฅผ ์ฌ์ฉํ๊ณ , <img src="https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white"/>์์ `#์ฌํ`, `#ํซํ` ๋ฑ์ ํ๊ทธ๋ฅผ ๊ฒ์ํด ๋์จ ๊ฒ์๋ฌผ์ ์ ํ ์ฅ์ ์ ๋ณด๋ฅผ ์์งํ์ต๋๋ค.

>< ๋ฃจํธ ๋๋ ํ ๋ฆฌ์ ์๋ `insta_crawl.py`ํ์ผ ์คํ ๊ฒฐ๊ณผ >       
>1)`config.ini`ํ์ผ์ ์ ํ ๋ด ๊ณ์  ์ ๋ณด๋ฅผ ์ด์ฉํด ์ธ์คํ๊ทธ๋จ์ ๋ก๊ทธ์ธ                
>( `config.ini`ํ์ผ์ ๊ฐ์ธ์ ๋ณด์ด๋ฏ๋ก `.gitignore`ํ์ผ์ ์ค์ ๋์ด github์๋ ์ฌ๋ผ์ ์์ง ์์ต๋๋ค! )            
><img src="https://github.com/SHINDongHyeo/HotPlace/blob/main/images/1.png" width="400" height="600"/>                   
>                     
>2)๋ฏธ๋ฆฌ ์ค์ ํ "#์ฌํ" ํ๊ทธ๋ฅผ ๊ฒ์ํ์ฌ ๋์จ ๊ฒ์๋ฌผ์ ํด๋ฆญํ๊ณ  ๊ฒ์๋ฌผ ์๋จ ๋ถ๋ถ์ ์๋ ์์น์ ๋ณด์ ํด๋น ๊ฒ์๋ฌผ์ url์ ์์ง, ์ดํ ๋ค์ ๊ฒ์๋ฌผ ๋ฒํผ ํด๋ฆญ๊ณผ ์ ๋ณด ์์ง ๊ทธ๋ฆฌ๊ณ  ํ๊ทธ ๊ฒ์์ ์ํ๋ ๋งํผ ๋ฐ๋ณต ์คํ               
><img src="https://github.com/SHINDongHyeo/HotPlace/blob/main/images/2.png" width="400" height="600"/>              
>
>3)Django์ Model๋ก ๋ง๋ค์ด ๋์ InstaHPํด๋์ค์ ์ ์ฅ
>```python
># result_location๋ ๊ฒ์๋ฌผ์ ์์น์ ๋ณด์ url์ ์์ผ๋ก ์ ์ฅํด๋์ ๋ฆฌ์คํธ์ด๋ค.
>for loc,url,like in result_location:
>            InstaHP(location=loc, url=url, like=like).save()
>```




## 2. ๋ถ์๐ง
๋ฐ์ดํฐ ๋ถ์์ ์ํด <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white"/> ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ฅผ ์ฌ์ฉํ์ต๋๋ค. ๋ชฉํ๋ ๊ฐ์ฅ ํซํ ์ง์ญ์ ๋ถ์ํด์ฃผ๋ ๊ฒ์ด์์ง๋ง ์ธ์คํ๊ทธ๋จ ๊ฒ์๋ฌผ์ ์ ํ์๋ ์์น์ ๋ณด ์์ฒด๊ฐ ์ ํํ์ง ์์ ๊ฒฝ์ฐ๊ฐ ๋ง์๊ณ , ๊ฐ์ ์ง์ญ์ด๋ผ๋ ํํ์ด ์กฐ๊ธ์ด๋ผ๋ ๋ค๋ฅด๋ฉด(ex.์๋ฒ๋๋ vs ํ์์๋๋ผ ์๋ฒ๋๋) ์์น๊ฐ ๊ฒ์์ด ๋์ง ์๊ฑฐ๋ ๊ฐ์ ์ฅ์๋ก ์ธ์ํ๊ธฐ๊ฐ ์ด๋ ค์ด ์ ์ด ์์ด์ ๋งค์ฐ ๊ฐ๋จํ๊ฒ ์ข์์ ์์ผ๋ก ์์๋ง ๋งค๊ฒจ์ ํ๋ก ์ ๋ฆฌํ๋ค.
> <๋ฃจํธ ๋๋ ํ ๋ฆฌ์ ์๋ analyze.py ์คํ๊ฒฐ๊ณผ>                        
> 1)`InstaHP`๊ฐ์ฒด๋ก ์ ์ฅ๋ ์ ๋ณด๋ฅผ `result`๋ณ์์ ๋ฐ์ดํฐํ๋ ์ ํ์์ผ๋ก ์ ์ฅ              
> ```
> result = pd.DataFrame(loc_url) # loc_url์ InstaHP๊ฐ์ฒด ์ ๋ณด ๋ฃ์ด๋ 
> ```
> 2)์ปฌ๋ผ๋ช ์๋กญ๊ฒ ์ง์                   
> ```
> result.columns=["location","url","like"]
> ```                  
> 3)๊ฐ๋ ๊ฐ์ ๊ฒ์๋ฌผ์ด ๊ฒ์๋๋ ๊ฒฝ์ฐ๊ฐ ์๊ธฐ ๋๋ฌธ์ url์ ๊ธฐ์ค์ผ๋ก ์ค๋ณต๋๋ ๋ ์ฝ๋๋ฅผ ์ญ์                 
> ```
> result.drop_duplicates(["url"], inplace=True)
> ```                 
> 4)์ข์์ ์์ผ๋ก ๋ด๋ฆผ์ฐจ์ ์ ๋ ฌ
> ```
> result.sort_values(by="like",ascending=False, inplace=True)
> ```           
> 5)์ถ๋ ฅํ๋ฉด            
> <img src="https://github.com/SHINDongHyeo/HotPlace/blob/main/images/%ED%8C%90%EB%8B%A4%EC%8A%A4%EA%B2%B0%EA%B3%BC.png"/>           


## 3. ์น ํ์ด์ง๐
<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/>๋ฅผ ์ด์ฉํด ์น ํ์ด์ง๋ฅผ ๊ตฌ์ฑํ๊ณ , <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/>๋ ์ฌ์ฉํด ๋์ ์ธ ์์๋ฅผ ๋ฃ์์ต๋๋ค.               
>1)`index.html`ํ์ผ์์ ์๋ฐ์คํฌ๋ฆฝํธ ๋ถ๋ถ์ผ๋ก `async function`๊ณผ `ajax`, `jquery`๋ฅผ ์ฌ์ฉํด ์น ํ์ด์ง์ UI๋ณ๊ฒฝ(ex.๋ก๋ฉ๋ฐ ์์ง์ด๊ธฐ) ๋ฐ ๋น๋๊ธฐ ์ฒ๋ฆฌ(ex.ํน์  ํ๊ทธ๋ก ์ธ์คํ๊ทธ๋จ ํฌ๋กค๋งํ๊ธฐ)๊ฐ ๋ชจ๋ ์์ฐจ์ ์ผ๋ก ์ผ์ด๋๊ฒ ํ์ฌ ๋น๋๊ธฐ ์ฒ๋ฆฌ๋ก ํฌ๋กค๋ง์ด ์๋ฃ๋  ๋๋ง๋ค ๋ก๋ฉ๋ฐ๊ฐ ์์ง์ด๊ฒ ๊พธ๋ช์ต๋๋ค.                
><img src="https://github.com/SHINDongHyeo/HotPlace/blob/main/images/3.png" width="800" height="200"/>
