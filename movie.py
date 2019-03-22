# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from itertools import count
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from twitterscraper import query_tweets
from twitterscraper.main import JSONEncoder
import json
import csv
import datetime as dt
import re


#년도별 url 넘겨주기
def crawling_start():

    driver = webdriver.PhantomJS()
    url_home = 'https://movie.naver.com/movie/sdb/browsing/bmovie.nhn'

    # for year in range(2016,2017):
    #     url = url_home + '?open=%s' %str(year)
    #     movie_address(driver, url)
    #     # driver.save_screenshot('movie-1.png')

    movie_aud(driver, '13시간')



# def movie_address(driver, url):
#     naver = 'https://movie.naver.com'
#     driver.get(url)
#     html = driver.page_source
#     bs = BeautifulSoup(html, 'html.parser')
#
#     movie_ul = bs.select('#old_content > ul[class=directory_list] > li')
#     for movie_li in movie_ul:
#         each_movie = naver + movie_li.select_one('a')['href']
#         movie_crawling(driver, each_movie)
#
#
#
# def movie_crawling(driver, url):
#
#     time.sleep(2)
#     driver.get(url)
#     html_each = driver.page_source
#     bs = BeautifulSoup(html_each, 'html.parser')
#
#     #제목
#     title_sel = bs.select_one('#content > div.article > div.mv_info_area > div.mv_info > h3[class=h_movie] > a')
#     title = title_sel.text
#     print(title_sel.text)
#
#     #개봉연도월일
#     year_sel = bs.select('#content > div.article > div.mv_info_area > div.mv_info > dl > dd > p > span > a')
#     year_str = year_sel[len(year_sel)-2]
#     month_str = year_sel[len(year_sel)-1]
#     year_mv = (int)(year_str.text)
#     date_mv = (int)(month_str.text[4]+month_str.text[5])
#     month_mv = (int)(month_str.text[1]+month_str.text[2])
#     print(year_mv, month_mv, date_mv)
#
#     year_4 =year_mv
#     month_4 = month_mv-1
#     date_4 = date_mv
#     year_1 =year_mv
#     month_1 = month_mv-1
#     date_1 = date_mv
#
#     if month_mv == 1:
#         year_4 = year_mv-1
#         month_4 = 12
#         date_4 = date_mv
#     else:
#          year_4 = year_mv
#          month_4 = month_mv-1
#          date_4 = date_mv
#
#     if date_mv <= 7 and month_mv == 1:
#         year_1 = year_mv-1
#         month_1 = 12
#         date_1 = 26
#     elif date_mv <= 7:
#         year1 = year_mv
#         month_1 = month_mv-1
#         date_1 = 26
#     else:
#         year_1 = year_mv
#         month_1 = month_mv
#         date_1 = date_mv-7
#
#
#     #actors의 0번째는 감독이름, 나머지 주연배우들
#     actor_sel = bs.select('#content > div.article > div.section_group.section_group_frst > div > div > ul > li > a.tx_people')
#     actors = []
#     for ac in actor_sel:
#         actors.append(ac.text)
#     print(actors)
#
#     cnt_tweet = 0
#     for tweet in  query_tweets(title, limit=10000, begindate=dt.date(year_4,month_4,date_4), enddate=dt.date(year_1,month_1,date_1), poolsize=10, lang=''):
#         cnt_tweet += 1
#     print(cnt_tweet)

def movie_aud(driver, title):
    daum_basic_url = 'https://movie.daum.net'
    daum_url = 'https://movie.daum.net/main/new#slide-1-0'
    driver.get(daum_url)
    html = driver.page_source
    bs = bs = BeautifulSoup(html, 'html.parser')

    research_sel = driver.find_element_by_name('searchText')
    research_sel.send_keys((str)(title))
    form = driver.find_element_by_css_selector("button.ico_searchbar[type=submit]")
    form.submit()

    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')
    a_mv = bs.select_one('#contents_result > li > a.link_join')

    movie_url = daum_basic_url + a_mv['href']
    driver.get(movie_url)
    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')
    driver.save_screenshot('note-2.png')
    audience_sel = bs.select_one('#totalAudience')
    print(audience_sel.text)


if __name__ == '__main__':

    print('영화 info 크롤링 시작')
    crawling_start()
    print('영화 info 크롤링 종료')
