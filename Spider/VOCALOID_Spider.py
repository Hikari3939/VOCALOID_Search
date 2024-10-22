import logging
import httpx
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



url = 'https://mzh.moegirl.org.cn/VOCALOID%E4%BC%A0%E8%AF%B4%E6%9B%B2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

results = re.findall('famed-song-2">.*?niconico</a>', scrape_page(url, headers), re.S)

path = 'E:\Study\Computer\Projects\Only_Software\Self\VOCALOID_Search\VOCALOID.txt'
with open(path,'w',encoding='utf-8') as file:
    for result in results:
        
        title = re.search('曲目.*?href="(.*?)".*?>(.*?)<', result)
        file.write('曲目:' + title.group(2) + '\n')
        # file.write('(https://mzh.moegirl.org.cn' + title.group(1) +')\n')
        
        # P主无wiki链接
        P = re.search('P主</b>：(.*?)<', result)
        if P.group(1) == '':
            # P主有wiki链接
            P = re.search('P主</b>：<.*?>(.*?)<', result)
        if P.group(1) == '':
            # P主如有wiki链接
            P = re.search('P主</b>：<.*?><.*?>(.*?)<', result)
        file.write('P主:' + P.group(1) +'\n')
  
        time = re.search('投稿.*?：(.*?)<.*?达成.*?：(.*?)<.*?所用.*?：(.*?)<', result)
        file.write('投稿时间:' + time.group(1) +'\n')
        file.write('达成时间:' + time.group(2) +'\n')
        file.write('所用时间:' + time.group(3) +'\n\n')

# 正则表达式
# 歌曲详情界面链接:
#   famed-song-2.*?href="(.*?)"