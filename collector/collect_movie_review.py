import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# anaconda prompt
# > conda activate cnu_python
# > pip install beautifulSoup
# > pip install selenium
# > pip install webdriver_manager

# Selenium: 동적 페이지에서 웹 크롤링 가능!
#           -> 원래 용도: 웹 브라우저 테스트 용



movie_id = 160244
url = f"https://movie.daum.net/moviedb/grade?movieId={movie_id}"

########################################
# 1. install ChromeDRiver for selenium #
########################################
# Selenium -> webdriver(chrome)
# 1. 최신버전 사용해서 code로 다운로드(최신버전)
# 2. chrome driver 다운로드 후 주입(구버전)
# Selenium -> 개인 웹 브라우저 사용!(우리는 웹 브라우저 중 Chrome 사용)
driver = webdriver.Chrome()

########################
# 2. Open ChromeDriver #
########################

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)




