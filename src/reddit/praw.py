

import pdb


def praw_reddit(config=None):
    import datetime
    import json
    if  config is None:
        config={}
        config['save_path']='.data/reddit_data.jsonl'
    import praw
    print(f'start')


    reddit = praw.Reddit(
        client_id="deImkPevl0FGZWg9UiY7Vw",
        client_secret="OjVaUP0TdBWUHEZmmDd9GWSzNH_1fA",
        user_agent="RedditCrawler by u/ShadoWJackson",
    )

    subreddit = reddit.subreddit("all")
    print(f'get subreddit')


    posts = subreddit.new(limit=1000) 
    # print(f'len(posts):{len(posts)}')

    count=0
    all=0
    with open(config['save_path'], "a",encoding='utf-8') as f:
        for post in posts:
            all+=1
            print(post.url)
            # pdb.set_trace()
            if 1:#not  '/www.reddit.com/r/'  in post.url:
                    # f.write(f"Title: {post.title}\n")
                    # f.write(f"Content: {post.selftext}\n")
                    # f.write(f"Link: {post.url}\n\n")
                if len(post.selftext)>50:
                    entry = {"date": datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"), "error": False, "url": post.url,'text_blocks':post.selftext}
                    count+=1
                    json.dump(entry, f, ensure_ascii=False)
                    f.write("\n")
            # else:
                # print(f"{post.url} not a reddit link")
    print(f"praw_reddit done, get {all} posts, {count} posts saved")