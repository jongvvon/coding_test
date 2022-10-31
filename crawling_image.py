from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
import time, os, random
import urllib.request
from bs4 import BeautifulSoup


def chromeWebdriver():
    options = Options()
    options.add_argument("lang=ko_KR")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(executable_path='/home/jwjang/chromedriver', options=options)
    return driver

def collect_image(search_word):
    url = 'https://www.google.co.kr'

    now = time.localtime()
    today_time = f'{now.tm_year}{now.tm_mon}{now.tm_mday}_{now.tm_hour}{now.tm_min}{now.tm_sec}'
    print(today_time)

    file_path = os.getcwd() + '/'

    os.chdir(file_path)
    os.makedirs(file_path + today_time + '_' + search_word)
    os.chdir(file_path + today_time + '_' + search_word)
    file_save_dir = file_path + today_time + '_' + search_word
    print(file_save_dir)

    driver = chromeWebdriver()
    driver.get(url)
    time.sleep(random.uniform(2, 3))
    elem = driver.find_element(By.NAME, 'q')
    elem.send_keys(search_word)
    elem.submit()

    driver.find_element(By.LINK_TEXT, '이미지').click()
    time.sleep(random.uniform(1, 2))

    file_no = 1
    count = 1
    img_src = []

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    imgs = driver.find_elements(By.CSS_SELECTOR, '#islrg > div.islrc > div a.wXeWr.islib.nfEiy')
    print(len(imgs))

    for img in imgs:
        img_src1 = img.click()  # 이미지 클릭 시 display 되는 url을 찾기 위해 클릭함
        img_src2 = driver.find_element(By.CSS_SELECTOR, '#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.qdnLaf.isv-id > div > a')
        time.sleep(random.uniform(0.2, 0.5))
        img_src3 = img_src2.find_element(By.TAG_NAME, 'img').get_attribute('src')
        if img_src3[:4] != 'http':
            continue
        print(count, img_src3, '\n')
        img_src.append(img_src3)
        count += 1

    for i in range(len(img_src)):
        extention = img_src[i].split('.')[-1]
        ext = ''
        print(extention)
        if extention in ('jpg', 'JPG', 'jpeg', 'JPEG', 'png', 'PNG', 'gif', 'GIF'):
            ext = '.' + extention
        else:
            ext = '.jpg'        
        try:
            urllib.request.urlretrieve(img_src[i], str(file_no).zfill(3) + ext)
            print(img_src[i])
        except Exception:
            continue
        file_no += 1
        # time.sleep(random.uniform(0.1, 0.5))
        print(f'{file_no}번째 이미지 저장')

    driver.close()


if __name__ == '__main__':
    collect_image('코카콜라캔')


