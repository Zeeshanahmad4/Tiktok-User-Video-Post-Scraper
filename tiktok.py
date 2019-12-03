from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import csv
import urllib.request



driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.set_page_load_timeout(100)
username = input("Enter username : ") 
url = 'https://www.tiktok.com/@{}?langCountry=en'.format(username)
driver.get(url)
sleep(3)
i = 0
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while(match == False):
    lastCount = lenOfPage
    sleep(5)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match = True

links = []
main1 = driver.find_element_by_css_selector("#__APP_ROOT__ > div._global_container > div > div._base_layout_content > div > div > div._video_feed_container")
videodad = main1.find_elements_by_class_name("_video_feed_item")
print (len(videodad))
z= 0
y = 1
for alpha in videodad:
    try:
        z += y
        alpha.click()
        sleep(1)
        src = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[1]/a/video").get_attribute("src")
        driver.find_element_by_xpath("/html/body/div[3]/div/img").click()
        sleep(5)
        print(src)
        print(100*"-")
        print("downloading")
        urllib.request.urlretrieve(src, {}.mp4'.format(z)) 
        print("done")
    except:
        pass
