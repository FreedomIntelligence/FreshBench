# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.bbc.com/news")
#     page.get_by_role("link", name="A volcano spews lava and").click()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)

import time
import requests
from bs4 import BeautifulSoup
from tqdm.notebook import tqdm
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
import re
import os

from playwright.sync_api import sync_playwright
import json
#import datetime



def generate_dates_m_d_Y_compatible(start_date, end_date):
    start = datetime.strptime(start_date, "%m/%d/%Y")
    end = datetime.strptime(end_date, "%m/%d/%Y")
    step = timedelta(days=1)
    
    date_list = []
    while start <= end:
        date_str = f"{start.month}/{start.day}/{start.year}"
        date_list.append(date_str)
        start += step
    
    return date_list


def get_search_results(url, retries=5, sleep_time=5):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
     }
    
    for attempt in range(retries):
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print(response)
            soup = BeautifulSoup(response.text, 'html.parser')
            search_results = soup.find_all('a')
            
            links = [link['href'] for link in search_results if link.has_attr('href')]
            links = [x for x in links if 'https://www.bbc.com/news/' in x]
            links = [x for x in links if '/live/' not in x]
            links = [x.replace('/url?q=', '') for x in links]
            links = [x.split('&')[0] for x in links]
            links = [x for x in links if x[-1].isdigit()]
            
            return links
        else:
            print(f'Response status code {response.status_code}. Retrying in {sleep_time} seconds...')
            time.sleep(sleep_time)
    
    print("Failed to retrieve data after multiple attempts.")
    return []




def extract_text(page, selector):
    elements = page.query_selector_all(selector)
    # print(page.content())
    return "\n".join([element.inner_text() for element in elements if element.inner_text().strip()])

def run(playwright,config):
    # browser = playwright.chromium.launch(headless=False)
    # browser = playwright.chromium.launch(headless=True)
    
    browser = playwright.chromium.launch(headless=config['headless'])
    
    context = browser.new_context()
    
    # 打开 BBC 新闻主页
    page = context.new_page()
    # page.goto("https://www.bbc.com/news",timeout=60000)

    # # 获取所有新闻链接
    # news_links = page.query_selector_all("a[data-testid='internal-link']")
    # urls = [link.get_attribute("href") for link in news_links if link.get_attribute("href")]
    # print('urls:',urls)

    

    url = 'https://www.google.com/search?q=news+site:bbc.com/news&tbs=cdr:1,cd_min:<DATE>,cd_max:<DATE>&tbm=nws&start=<START>'
    max_page_num = 50
    sleep_time = 1.0

    # start_date = "1/25/2024"
    # end_date = "2/3/2024"
    start_date = config['start_date']
    #"11/20/2023"
    end_date = config['end_date']
    #"12/10/2023"

    dates = generate_dates_m_d_Y_compatible(start_date, end_date)

    url_list = []
    for date in dates:
        for start in [str(x * 10) for x in range(max_page_num)]:
            request_url = url.replace('<START>', start).replace('<DATE>', date)
            search_links = get_search_results(request_url)
            url_list += search_links
            print('-' * 100)
            print(f'date:{date} start:{start} total:{len(set(url_list))}')
            for link in search_links:
                print(link)
            if len(search_links) == 0:
                break
            time.sleep(sleep_time)

    #urls=['https://www.bbc.com/news/world-middle-east-67589259',
  #'https://www.bbc.com/news/world-us-canada-67571551',]
    print(url_list)
    urls=url_list

    # 遍历链接并提取信息
    for url in urls:#[20:26]
        # endswith a number:
        if not url[-1].isdigit():
            print("not endswith a number skip",url)
            continue
        #full_url=f"https://www.bbc.com{url}"
        full_url=url
        print("url:",full_url)
        page.goto(full_url)
        text_blocks=None
        url='https://www.bbc.com/news/world-europe-62030919'

        # 提取页面标题和文本
        # title = page.query_selector("h1")  # 假设标题总是在 h1 标签中
        # content = page.query_selector("article")  # 假设主要内容在 article 标签中
        try:
            # page.wait_for_selector("section[data-component='text-block']")  # 等待元素加载
            text_blocks = extract_text(page, "section[data-component='text-block']")#, ul[class=]
            print("text_blocks:",text_blocks)

            # element=page.locator("section[data-component='text-block']")
            # text_blocks = element.inner_text()
            error=False


        except Exception as e:  
            print(e)
            print("can not find text_blocks")
            error=True


        entry = {"date": datetime.now().strftime("%Y-%m-%d-%H-%M"), "error": error, "url": full_url,'text_blocks':text_blocks}
        with open(config['save_path'], "a", encoding="utf-8") as file:
            # for entry in data:
            json.dump(entry, file, ensure_ascii=False)
            file.write("\n")
        exit()

        print("\n----------\n")

    # 关闭浏览器
    context.close()
    browser.close()

def wr_bbc(config=None):
    if  config is None:
        config={}
        config['save_path']='./BBC_data.jsonl'
        config['headless']=False
        config['start_date']="1/1/2024"
        config['end_date']="1/5/2024"

    with sync_playwright() as playwright:
        run(playwright,config)


if __name__ =='__main__':
    # print('run default')

    # wr_bbc()
    # print('run finished')

    # save in the ./../../data/{yyyy-mm-dd}/wr_bbc/wr_bbc.jsonl
    # and give me the date ,every time shift 2 months
    # for date in ["1/1/2023","3/1/2023","5/1/2023","7/1/2023","9/1/2023","11/1/2023"]:
    #     # yyyy-mm-dd
    #     date_start=date.

    #     date_end=#add 3days

    #     wr_bbc({'save_path':f'./../../data/{date}/wr_bbc/wr_bbc.jsonl','start_date':date_start,'end_date':date_end,'headless':False})
    #     print('run finished')
    #     time.sleep(10)
    import logging
    import traceback

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',filename='./app.log', filemode='a')
    




    date_format = "%m/%d/%Y"  # Define the date format

    dates = [
            "1/2/2023", "3/2/2023", "5/2/2023", "7/2/2023", "9/2/2023", "11/2/2023",
             "1/2/2022", "3/2/2022", "5/2/2022", "7/2/2022", 
             "9/2/2022", "11/2/2022",]

    for date_str in dates:
        logging.info(f'run for period: {date_str}')
        time_start=time.time()
        try:
            # Convert string to datetime object
            date_start = datetime.strptime(date_str, date_format)
            # Add 3 days to the start date to get the end date
            date_end = date_start + timedelta(days=3)
            date_end_str_mdy = date_end.strftime('%m/%d/%Y')

            # Convert datetime objects back to string in the format yyyy-mm-dd for the save path
            date_start_str = date_start.strftime('%Y-%m-%d')
            date_end_str = date_end.strftime('%Y-%m-%d')

            # Define the save path with the correct format and dates
            save_folder=f'./../../data/{date_start_str}/wr_bbc/'
            if not os.path.exists(save_folder):
                os.makedirs(save_folder)
                print(f'Folder created: {save_folder}')
            save_path = save_folder+f'wr_bbc.jsonl'
            
            # Run your function with the calculated start and end dates
            wr_bbc({'save_path': save_path, 'start_date': date_str, 'end_date': date_end_str_mdy, 'headless': False})
            print('run finished for period:', date_start_str, 'to', date_end_str)
        except:
            logging.error(f'Error running for period: {date_str}')
            logging.error(traceback.format_exc())
        time_end=time.time()
        logging.info(f'run for period: {date_str} time cost:{time_end-time_start}')
            # Sleep for 10 seconds before proceeding to the next date
        time.sleep(10)