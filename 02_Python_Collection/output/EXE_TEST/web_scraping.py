from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import math, time

options = Options()
options.add_argument('--window-size=974,1047')
options.add_argument('--window-position=-7,0')
options.add_experimental_option("detach", True)

search = input('검색어를 입력하세요.')

URL = 'https://korean.visitkorea.or.kr/search/search_list.do?keyword='+search

driver = webdriver.Chrome(options=options)
driver.get(URL)
time.sleep(5)

# 여행기사 더보기 클릭
# driver.find_element(By.CSS_SELECTOR, ".more_view > a").click()
driver.find_element(By.CSS_SELECTOR, "#s_recommend > .more_view > a").click()

scrap_cnt = int(input('스크래핑 건수는 몇건입니까?: '))

def FindLastPageNum():
    FindPageNum = True
    BoxNum = 1
    lastpage = 0
    driver.find_element(By.XPATH, f'/html/body/div[3]/div/div[1]/div[14]/a[{1}]').click()
    time.sleep(5)
    while True:
        try:
            strBoxNum = driver.find_element(By.XPATH, f'/html/body/div[3]/div/div[1]/div[14]/a[{BoxNum}]').text
            if strBoxNum.strip() == '끝':
                driver.find_element(By.XPATH, f'/html/body/div[3]/div/div[1]/div[14]/a[{BoxNum}]').click()
                time.sleep(5)
                BoxNum = 1
                continue
            elif strBoxNum.strip() != '':           
                if lastpage < int(strBoxNum.strip()):
                    lastpage = int(strBoxNum.strip())
            else:
                FindPageNum = False
            BoxNum += 1
        except ValueError:
            BoxNum += 1
        except :
            break
            
    time.sleep(5)
    driver.find_element(By.XPATH, f'/html/body/div[3]/div/div[1]/div[14]/a[1]').click()
    time.sleep(5)
    return lastpage

chsngemaxpage = True
NextpPage = 1
lastpage = FindLastPageNum()
Finish = False
NextPageGroup = False

i = 1
while Finish == False:
    NextPageGroup = False
    while NextPageGroup == False:
        strBoxNum = driver.find_element(By.XPATH, f'/html/body/div[3]/div/div[1]/div[14]/a[{i}]').text.strip()
        if strBoxNum == '다음':
            driver.find_element(By.XPATH, f'/html/body/div[3]/div/div[1]/div[14]/a[{i}]').click()
            time.sleep(5)
            i = 1
            break
        elif strBoxNum == '처음' or strBoxNum == '이전' or strBoxNum == '끝':
            i += 1
            continue
        else:
            driver.find_element(By.XPATH, f'/html/body/div[3]/div/div[1]/div[14]/a[{i}]').click()
            print('#'*20 + " " +strBoxNum+" 페이지 결과"+ " "+'#'*20)
            time.sleep(5)
            tit_xpath = '//*[@id="search_result"]/ul/li[*]/div[1]/div[1]/a'
            result = driver.find_elements(By.XPATH, tit_xpath)
            for j, title in enumerate(result, (1 + (len(result)*(int(strBoxNum)-1)))):
                print(j, title.text)
                if j >= scrap_cnt:
                    Finish = True
                    NextPageGroup = True
                    break
            i += 1
            if  int(strBoxNum) == lastpage:
                Finish = True
                break
        if Finish == True:
            break        

print("종료")