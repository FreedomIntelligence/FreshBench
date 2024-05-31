from src.BBC.wr import wr_bbc as wr_bbc
from src.Wiki.wr import wr_wiki as wr_wiki
from src.wattpad.rq import rq_wattpad as rq_wattpad
from src.arxiv.rq import rq_arxiv as rq_arxiv 
from src.arxiv.rq_year import rq_arxiv as rq_arxiv_year# this is used to crawl a special year's arxiv

from src.Yahoo.wr import wr_Yahoo as wr_Yahoo
from src.reddit.praw import praw_reddit as praw_reddit
from src.quora.wr import wr_quora as wr_quora
from src.github.rq import rq_github as rq_github

# from src.checkFile.check_crawl import check_crawl
#TODO what do the check file done?
# from src.checkFile.check_crawl import test_check_files_exist

import os
import datetime
import logging
import time
import json
logging.basicConfig(level=logging.INFO,filename='./app.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.info("start up")



doday=datetime.datetime.now().strftime("%Y-%m-%d")

# os.mkdir(f"/data/{doday}",exist_ok=True)
os.makedirs(f"./data/{doday}", exist_ok=True)

# crawl_list=[rq_github,wr_wiki,wr_quora,rq_arxiv,praw_reddit,wr_bbc,rq_wattpad,wr_Yahoo,]#,
crawl_list=[praw_reddit,]#,rq_github,wr_wiki,wr_quora,wr_Yahoo#wr_bbc,rq_wattpad
# crawl_list=[rq_github,wr_wiki,wr_quora,praw_reddit,rq_wattpad,wr_Yahoo,]#,rq_arxiv,wr_bbc
# crawl_list=[praw_reddit,rq_wattpad,]#,rq_github,wr_wiki,wr_quorawr_Yahoo#wr_bbc
# crawl_list=[wr_bbc,wr_quora, wr_Yahoo]
# crawl_list=[wr_Yahoo]
# crawl_list=[rq_github]
# crawl_list=[wr_quora]
crawl_list=[rq_wattpad]
# crawl_list=[wr_wiki]
# crawl_list=[praw_reddit]
crawl_list=[rq_github,wr_wiki,wr_quora,praw_reddit,rq_wattpad,wr_Yahoo,]#,wr_bbc,rq_arxiv
crawl_list=[wr_wiki,praw_reddit,rq_wattpad,wr_Yahoo,]#,wr_bbc,rq_arxiv,wr_quora
crawl_list=[wr_Yahoo]
crawl_list=[wr_quora]

# 更高频率: reddit检查是否时间不对,quora是否后续报错是为什么,watpadd怎么办,Yahoo需要每天爬吗,watpadd更新似乎不够快,一天一次,然后bbc的修改一下,看看到什么程度会稳定,
# 测试bbc

for crawler in crawl_list:
    print(f"start to crawl {crawler.__name__}")
    config={}
    st_time=time.time()
    save_path_base=f'./data/{doday}/{crawler.__name__}/'
    #check exist:
    if not os.path.exists(save_path_base):
        os.makedirs(save_path_base, exist_ok=True)
        
    config['save_path']=f"{save_path_base}{crawler.__name__}.jsonl"
    config['save_folder_pdf_arxiv']=f"./data/{doday}/{crawler.__name__}_pdfs"
    config["topic_quora"]=['Technology','Mathematics','Health','Movies','what','how','why',]#'where','when','who','which','he','she'
    config['headless']=False
    


    try:
        crawler(config)
        logging.info(f"crawler {crawler.__name__} done, time_used:{round(time.time()-st_time,2)}")
    #     #read file and get how many lines
    #     with open (config['save_path'],'r') as f:
    #         lines=f.readlines()
    #         logger.info(f"crawler {crawler.__name__} done, total lines:{len(lines)}")
            
    #         for line in lines:
    #             data = json.loads(line.strip())
                
    #             # 检查text_blocks是否存在并且长度是否超过300
    #             num_10,num_300,num_5000=0
    #             if 'text_blocks' in data and len(data['text_blocks']) > 10:
    #                 num_10+=1
    #                 if len(data['text_blocks']) > 300:
    #                     num_300+=1
    #                 if len(data['text_blocks']) > 5000:
    #                     num_5000+=1
    #             logger.info(f'num_10:{num_10},num_300:{num_300},num_5000:{num_5000}')
    #             if num_10<50:
    #                 logger.error(f'num_10:{num_10} is less than 50, please check crawler {crawler.__name__}')


    except Exception as e:
        import traceback
        print(f"                crawler {crawler.__name__} failed, time_used:{round(time.time()-st_time,2)}, error:{e},trackback:{traceback.format_exc()}")
        logging.error(f"                crawler {crawler.__name__} failed, time_used:{round(time.time()-st_time,2)}, error:{e},trackback:{traceback.format_exc()}")

# test_check_files_exist(directory=os.path.join('data','doday'))