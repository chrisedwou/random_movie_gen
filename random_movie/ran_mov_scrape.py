from bs4 import BeautifulSoup
import requests
import sys
import chromedriver_binary
import time
import random
import pandas
from selenium import webdriver

SCROLL_PAUSE_TIME = 3

def scrape(url):
    driver = webdriver.Chrome()
    driver.get(url)

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
        time.sleep(SCROLL_PAUSE_TIME)
    
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        
    html = driver.page_source
    movies = BeautifulSoup(html,'lxml')
    driver.quit()
    
    match = movies.find_all('a', class_='av-beard-title-link')
    all_titles = []
    
    for title in match:
        all_titles.append(title.text)
        
    return all_titles


horror_movies = scrape('https://www.amazon.com/gp/video/search/ref=atv_hm_hom_1_c_sjczfj_8_smr?queryToken=eyJ0eXBlIjoicXVlcnkiLCJuYXYiOnRydWUsInBpIjoiZGVmYXVsdCIsInNlYyI6ImNlbnRlciIsInN0eXBlIjoic2VhcmNoIiwicXJ5Ijoibm9kZT0yODU4Nzc4MDExJmZpZWxkLXdheXNfdG9fd2F0Y2g9MTIwMDc4NjUwMTEmcF9uX2VudGl0eV90eXBlPTE0MDY5MTg0MDExJmFkdWx0LXByb2R1Y3Q9MCZiYm49Mjg1ODc3ODAxMSZmaWVsZC10aGVtZV9icm93c2UtYmluPTI2NTAzNzEwMTEmZmllbGQtaXNfcHJpbWVfYmVuZWZpdD0xJnNlYXJjaC1hbGlhcz1pbnN0YW50LXZpZGVvJnFzLWF2X3JlcXVlc3RfdHlwZT00JnFzLWlzLXByaW1lLWN1c3RvbWVyPTIiLCJydCI6IlNKY1pGanNtciIsInR4dCI6IkhvcnJvciBtb3ZpZXMiLCJvZmZzZXQiOjAsInN5cyI6WyJDTVNfVDEiXSwibnBzaSI6MCwib3JlcSI6IjZlMTdhOWZjLWZiMDMtNDlmMi04YmYyLWU0ZTRkNGZkMDk0YjowIiwic3RyaWQiOiIxOjFOT1dDNUVIQzVONjEjI01aUVdHWkxVTVZTRUdZTFNONTJYR1pMTSJ9&pageId=default&queryPageType=browse&ie=UTF8')
sci_fi_movies = scrape('https://www.amazon.com/gp/video/search/ref=atv_hm_hom_c_vqt8w2_21_smr?queryToken=eyJ0eXBlIjoicXVlcnkiLCJuYXYiOnRydWUsInBpIjoiZGVmYXVsdCIsInNlYyI6ImNlbnRlciIsInN0eXBlIjoic2VhcmNoIiwicXJ5Ijoibm9kZT0yODU4Nzc4MDExJmZpZWxkLXdheXNfdG9fd2F0Y2g9MTIwMDc4NjUwMTEmcF9uX2VudGl0eV90eXBlPTE0MDY5MTg0MDExJmFkdWx0LXByb2R1Y3Q9MCZiYm49Mjg1ODc3ODAxMSZmaWVsZC10aGVtZV9icm93c2UtYmluPTI2NTAzNzYwMTEmZmllbGQtaXNfcHJpbWVfYmVuZWZpdD0xJnNlYXJjaC1hbGlhcz1pbnN0YW50LXZpZGVvJnFzLWF2X3JlcXVlc3RfdHlwZT00JnFzLWlzLXByaW1lLWN1c3RvbWVyPTIiLCJydCI6IlZRdDhXMnNtciIsInR4dCI6IlNjaWVuY2UgZmljdGlvbiBtb3ZpZXMiLCJvZmZzZXQiOjAsInN5cyI6WyJDTVNfVDEiXSwibnBzaSI6MCwib3JlcSI6IjI1M2YwOTZkLWMwNmEtNGZjOS05YzY5LTQxNzJjMzdhNzEwMzowIiwic3RyaWQiOiIxOjEyQUFEUDJYQUlPSUVYIyNNWlFXR1pMVU1WU0VHWUxTTjUyWEdaTE0ifQ%3D%3D&pageId=default&queryPageType=browse&ie=UTF8')
action_movies = scrape("https://www.amazon.com/gp/video/search/ref=atv_hm_hom_c_hmzhzc_19_smr?queryToken=eyJ0eXBlIjoicXVlcnkiLCJuYXYiOnRydWUsInBpIjoiZGVmYXVsdCIsInNlYyI6ImNlbnRlciIsInN0eXBlIjoic2VhcmNoIiwicXJ5Ijoibm9kZT0yODU4Nzc4MDExJmZpZWxkLXdheXNfdG9fd2F0Y2g9MTIwMDc4NjUwMTEmcF9uX2VudGl0eV90eXBlPTE0MDY5MTg0MDExJmFkdWx0LXByb2R1Y3Q9MCZiYm49Mjg1ODc3ODAxMSZmaWVsZC10aGVtZV9icm93c2UtYmluPTI2NTAzNjMwMTEmZmllbGQtaXNfcHJpbWVfYmVuZWZpdD0xJnNlYXJjaC1hbGlhcz1pbnN0YW50LXZpZGVvJnFzLWF2X3JlcXVlc3RfdHlwZT00JnFzLWlzLXByaW1lLWN1c3RvbWVyPTIiLCJydCI6IkhtWkh6Q3NtciIsInR4dCI6IkFjdGlvbiBhbmQgYWR2ZW50dXJlIG1vdmllcyIsIm9mZnNldCI6MCwic3lzIjpbIkNNU19UMSJdLCJucHNpIjowLCJvcmVxIjoiZDBiNGFkZGItZTI4Ni00MTQ0LThjZTAtMGEwNDA3NzBkZWYyOjAiLCJzdHJpZCI6IjE6MVpMMVJWUUNLV0FHRyMjTVpRV0daTFVNVlNFR1lMU041MlhHWkxNIn0%3D&pageId=default&queryPageType=browse&ie=UTF8")

all_movies = horror_movies + sci_fi_movies + horror_movies

df = pandas.DataFrame(data={"col1":all_movies})
df.to_csv("./all_movies.csv2",sep=',',index=False)

df_h = pandas.DataFrame(data={"col1":horror_movies})
df_s = pandas.DataFrame(data={"col1":sci_fi_movies})
df_a = pandas.DataFrame(data={"col1":action_movies})

df_h.to_csv("./horror_movies2.csv",sep=',',index=False)
df_s.to_csv("./sci_fi_movies2.csv",sep=',',index=False)
df_a.to_csv("./action_movies2.csv",sep=',',index=False)
