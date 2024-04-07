from selenium import webdriver 
from bs4 import BeautifulSoup as bs
import time
import csv


start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome()
browser.get(start_url)
time.sleep(10)
browser.find_element("xpath","//*[@id='primary_column']/footer/div/div/div/nav/span[2]/a").click()

def scrap():
    headers = ["Proper name",'Distance',"Mass","Radius"]
    planet_data = []

    for i in range(0,220):
        soup = bs(browser.page_source,"html.parser")
        for ultag in soup.find_all("ul",attrs={'class','exoplanet'}):
            li_tags = ultag.find_all('li')
            temp_list = []
            for index,li_tag in enumerate(li_tags):
                if index == 0: 
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element("xpath","//*[@id='primary_column']/footer/div/div/div/nav/span[2]/a").click()
    with open("scrapper_2.csv","w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(planet_data)

scrap()