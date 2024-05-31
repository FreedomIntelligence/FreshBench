# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     # browser = playwright.chromium.launch(headless=False)
#     # browser = playwright.chromium.launch(headless=True)
#     browser = playwright.chromium.launch(headless=config['headless'])
    
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://demo.playwright.dev/todomvc/")
#     page.goto("https://demo.playwright.dev/todomvc/#/")
#     page.get_by_placeholder("What needs to be done?").click()
#     page.get_by_role("heading", name="todos").click()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)

# # get_by_role("link", name="real TodoMVC app.")





# # this failed to handle the page.goto("https://demo.playwright.dev/todomvc/") correctly, for it is not a static page
# import requests
# from bs4 import BeautifulSoup
# import re
# import pdb


# def extract_content_from_url(url):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',}
#     # {
#     # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
#     # }
    
#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()
#     except requests.HTTPError as http_err:
#         return f"HTTP error occurred: {http_err}"
#     except Exception as err:
#         return f"An error occurred: {err}"

#     soup = BeautifulSoup(response.text, 'html')
#     soup2 = BeautifulSoup(response.text, 'html.parser')
#     pdb.set_trace()
#     print("text_blocks:",text_blocks)

#     selector = 'section[data-component="text-block"]'
#     soup.find_all(selector)
#     select_dic={"data-component":"text-block"}
#     # script id="__NEXT_DATA__"
#     # soup.find_all('script', id="__NEXT_DATA__")
#     soup.find_all('section',select_dic)

# #  soup.find('script', id="__NEXT_DATA__").text     
# #      data=json.loads(    soup.find('script', id="__NEXT_DATA__").text)  
# # (Pdb) data['props']['pageProps']['page']
#     # {'class': 
#     # Extract and return the inner text of each element, joined by newlines
#     return "\n".join([element.get_text(strip=True) for element in elements if element.get_text(strip=True)])


    
    
#     main_content = soup.find('main')
#     content_list = []

#     if main_content:
        
#         pattern = re.compile(r'(text-block|subheadline-block)')

#         content_divs = main_content.find_all('div', attrs={'data-component': pattern})

#         for div in content_divs:
#             content = ' '.join(div.stripped_strings)
#             content_list.append(content)
    
#     joined_string = '\n'.join(content_list)

#     return joined_string
# extract_content_from_url('https://www.bbc.com/news/technology-67556607')

# import plotly.graph_objects as go
# import pandas as pd

# # 示例数据：每个模型的日期和分数，以及关键日期
# data = {
#     "Model A": {
#         "dates": pd.date_range(start="2022-01-01", end="2022-01-10"),
#         "scores": [1, 3, 2, 5, 7, 8, 10, 9, 12, 11],
#         "key_date": pd.Timestamp("2022-01-06")
#     },
#     "Model B": {
#         "dates": pd.date_range(start="2022-01-01", end="2022-01-10"),
#         "scores": [2, 2, 4, 6, 5, 9, 7, 10, 13, 12],
#         "key_date": pd.Timestamp("2022-01-05")
#     }
# }

# # 创建图表
# fig = go.Figure()

# for model, info in data.items():
#     dates = info["dates"]
#     scores = info["scores"]
#     key_date = info["key_date"]

#     # 在关键日期之前使用虚线
#     fig.add_trace(go.Scatter(x=dates[dates < key_date], y=scores[:len(dates[dates < key_date])],
#                              mode='lines', name=f'{model} Before', line=dict(dash='dash')))

#     # 在关键日期及之后使用实线
#     fig.add_trace(go.Scatter(x=dates[dates >= key_date], y=scores[len(dates[dates < key_date])-1:],
#                              mode='lines', name=f'{model} After', line=dict(dash='solid')))

# # 添加图表标题和坐标轴标签
# fig.update_layout(title='Model Scores Before and After Key Dates',
#                   xaxis_title='Date',
#                   yaxis_title='Score',
#                   xaxis=dict(showline=True, showgrid=True),
#                   yaxis=dict(showline=True, showgrid=True))

# # 显示图表
# fig.show()
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# 示例数据：两个模型的日期和分数，以及各自的关键日期
models_data = {
    "Model A": {
        "dates": ["2022-01-01", "2022-01-03", "2022-01-05", "2022-01-07", "2022-01-09"],
        "scores": [1, 3, 5, 27, 9],
        "key_date": "2022-01-05",
    },
    "Model B": {
        "dates": ["2022-01-02", "2022-01-04", "2022-01-06", "2022-01-08", "2022-01-10"],
        "scores": [12, 4, 46, 8, 10],
        "key_date": "2022-01-06",
    }
}

fig = go.Figure()
colors='''aliceblue, antiquewhite, aqua, aquamarine, azure,
            beige, bisque, black, blanchedalmond, blue,
            blueviolet, brown, burlywood, cadetblue,
            chartreuse, chocolate, coral, cornflowerblue,
            cornsilk, crimson, cyan, darkblue, darkcyan,
            darkgoldenrod, darkgray, darkgrey, darkgreen,
            darkkhaki, darkmagenta, darkolivegreen, darkorange,
            darkorchid, darkred, darksalmon, darkseagreen,
            darkslateblue, darkslategray, darkslategrey,
            darkturquoise, darkviolet, deeppink, deepskyblue,
            dimgray, dimgrey, dodgerblue, firebrick,
            floralwhite, forestgreen, fuchsia, gainsboro,
            ghostwhite, gold, goldenrod, gray, grey, green,
            greenyellow, honeydew, hotpink, indianred, indigo,
            ivory, khaki, lavender, lavenderblush, lawngreen,
            lemonchiffon, lightblue, lightcoral, lightcyan,
            lightgoldenrodyellow, lightgray, lightgrey,
            lightgreen, lightpink, lightsalmon, lightseagreen,
            lightskyblue, lightslategray, lightslategrey,
            lightsteelblue, lightyellow, lime, limegreen,
            linen, magenta, maroon, mediumaquamarine,
            mediumblue, mediumorchid, mediumpurple,
            mediumseagreen, mediumslateblue, mediumspringgreen,
            mediumturquoise, mediumvioletred, midnightblue,
            mintcream, mistyrose, moccasin, navajowhite, navy,
            oldlace, olive, olivedrab, orange, orangered,
            orchid, palegoldenrod, palegreen, paleturquoise,
            palevioletred, papayawhip, peachpuff, peru, pink,
            plum, powderblue, purple, red, rosybrown,
            royalblue, rebeccapurple, saddlebrown, salmon,
            sandybrown, seagreen, seashell, sienna, silver,
            skyblue, slateblue, slategray, slategrey, snow,
            springgreen, steelblue, tan, teal, thistle, tomato,
            turquoise, violet, wheat, white, whitesmoke,
            yellow, yellow-green'''.replace('\n',' ').split(', ')
for idx,(model_name, model_info) in enumerate(models_data.items()):
    # 转换日期为pandas的日期类型
    dates = pd.to_datetime(model_info['dates'])
    scores = model_info['scores']
    key_date = pd.to_datetime(model_info['key_date'])
    color=colors[idx%len(colors)]
    
    # 创建完整的日期范围以确保连续性
    full_dates = pd.date_range(start=dates.min(), end=dates.max())
    
    # 创建DataFrame以方便处理
    df = pd.DataFrame({'Date': dates, 'Score': scores})
    df.set_index('Date', inplace=True)
    
    # 对缺失的日期进行线性插值
    df_full = df.reindex(full_dates).interpolate()
    
    # 拆分为关键日期前后两部分
    before_key_date = df_full.loc[df_full.index <= key_date]
    after_key_date = df_full.loc[df_full.index >= key_date]
    
    # 添加关键日期之前的数据（虚线）
    fig.add_trace(go.Scatter(x=before_key_date.index, y=before_key_date['Score'],
                             mode='lines', name=f'{model_name} Before', line=dict(dash='solid',color=color)))
    
    # 添加关键日期之后的数据（实线）
    fig.add_trace(go.Scatter(x=after_key_date.index, y=after_key_date['Score'],
                             mode='lines', name=f'{model_name} After', line=dict(dash='dash',color=color)))

# 添加图表标题和坐标轴标签
fig.update_layout(title='Smoothed Model Scores Before and After Key Dates',
                  xaxis_title='Date',
                  yaxis_title='Score',
                  xaxis=dict(showline=True, showgrid=True),
                  yaxis=dict(showline=True, showgrid=True))

fig.show()
