import logging
import httpx
import json
import re

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('scrape.log')
    ]
)

def scrape_page(url, headers):
    logging.info('scraping %s...', url)
    
    try:
        response = httpx.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            logging.error('get inavilid status code %s while scraping %s', response.status_code, url)
    except httpx.RequestError:
        logging.exception('error occurred while scraping %s', url)
        
def get_basic_information(text):
    results = []
    
    raw_results = re.findall('famed-song-2">.*?niconico</a>', text, re.S)
    for result in raw_results:
        
        title = re.search('曲目.*?href="(.*?)".*?>(.*?)<', result)
        name = title.group(2)
        name_url = '(https://mzh.moegirl.org.cn' + title.group(1)
        
        # P主无wiki链接
        P = re.search('P主</b>：(.*?)<', result)
        if P.group(1) == '':
            # P主有wiki链接
            P = re.search('P主</b>：<.*?>(.*?)<', result)
        if P.group(1) == '':
            # P主如有wiki链接
            P = re.search('P主</b>：<.*?><.*?>(.*?)<', result)
        producer = P.group(1)

        time = re.search('投稿.*?：(.*?)<.*?达成.*?：(.*?)<.*?所用.*?：(.*?)<', result)
        submission_time = time.group(1)
        achieve_time = time.group(2)
        time_cost = time.group(3)
            
        result = {
            'name': name,
            'name_url': name_url,
            'producer': producer,
            'submission_time': submission_time,
            'achieve_time': achieve_time,
            'time_cost': time_cost
        }
        results.append(result)

    return results
    
    
    
def save_basic_information(results):
    path = 'Basic_info.json'
    with open(path,'w',encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=2)



url = 'https://mzh.moegirl.org.cn/VOCALOID%E4%BC%A0%E8%AF%B4%E6%9B%B2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

text = scrape_page(url, headers)
results = get_basic_information(text)

save_basic_information(results)

# 正则表达式
# 歌曲详情界面链接:
#   famed-song-2.*?href="(.*?)"