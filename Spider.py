import multiprocessing
import logging
import httpx
import json
import re
import os



logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('scrape.log')
    ]
)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}



def scrape_page(url):
    logging.info('scraping %s...', url)
    
    try:
        response = httpx.get(url=url, headers=headers, timeout=None)
        if response.status_code == 200:
            return response.text
        else:
            logging.error('get inavilid status code %s while scraping %s', response.status_code, url)
    except httpx.RequestError:
        logging.exception('error occurred while scraping %s', url)



def scrape_and_save_details(url):
    dir = 'details'
    if not os.path.exists(dir):
        os.makedirs(dir)

    html = scrape_page(url)
    get_and_save_details(html, dir, '')



def get_urls(html):
    urls = []

    raw_results = re.findall('famed-song-2.*?href="(.*?)"', html, re.S)
    for result in raw_results:
        url = 'https://mzh.moegirl.org.cn' + result
        urls.append(url)

    logging.info('get detail url %s', len(urls))
    return urls



def get_basic_information(html):
    results = []
    
    raw_results = re.findall('famed-song-2">.*?niconico</a>', html, re.S)
    for result in raw_results:
        
        title = re.search('曲目.*?href="(.*?)".*?>(.*?)<', result)
        name = title.group(2)
        name_url = 'https://mzh.moegirl.org.cn' + title.group(1)
        
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
    dir = 'basic'
    if not os.path.exists(dir):
        os.makedirs(dir)

    path = dir+'/Basic_info.json'
    with open(path,'w',encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=2)



def get_and_save_details(html, dir, num):
    logging.info('scrape %s...', num)
    
    #处理标题
    title = re.search('.*?<body class="mediawiki.*?page-(.*?) rootpage', html, re.S)
    if title:
        title = title.group(1)

    #处理歌曲信息
    info = re.search('<table class="moe-infobox.*?</table>', html, re.S)
    if info:
        info = info.group()
        #删除脚本部分
        info_removed = re.search('.*\n(<tr>.*?<script>.*?</tr>)', info, re.S)
        if info_removed:
            info_removed = info_removed.group(1)
            info = info.replace(info_removed, '', 1)
        #补全链接
        info = re.sub('href="/', 'href="https://mzh.moegirl.org.cn/', info)
        logging.info('success get info')

    #处理歌词
    lyrics = re.search('歌词</span>\n*</h[23]>.*?(<div class="Lyrics Lyrics-.*?<div style="clear:both">\n*</div>\n*</div>)', html, re.S)
    if not lyrics:
        lyrics = re.search('歌词</span>\n*</h[23]>.*?(<div class="poem">.*?</p>\n*</div>)', html, re.S)
        if not lyrics:
            lyrics = re.search('歌词</span>\n*</h[23]>(.*?)<h[23]>', html, re.S)
            if not lyrics:
                lyrics = re.search('歌词</span>\n*</h[23]>(.*?)<div style="clear: both;', html, re.S)
    if title == '七色的黑塔利亚动画':#特殊1
        lyrics = re.search('歌词</span>\n*</h[23]>(.*?)<h[23]>', html, re.S)
    if lyrics:
        #补全链接
        lyrics = re.sub('href="/', 'href="https://mzh.moegirl.org.cn/', lyrics.group(1))
        logging.info('success get lyrics')
    if title == '甩葱歌':#特殊2
        lyrics = re.search('(<div style="color:#39C5BB">.*?</div>\n*</div>).*?</h3>.*?(<div class="poem">.*?</div>)', html, re.S)
        lyrics = lyrics.group(1)+'\n'+lyrics.group(2)


    #存入文件
    if title:
        path = '%s/%s_%s.html' % (dir, num, title)
        with open(path,'w',encoding='utf-8') as file:
            if info:
                file.write(info+'\n\n\n')
            if lyrics:
                file.write(lyrics)



if __name__ =='__main__':
    url = 'https://mzh.moegirl.org.cn/VOCALOID%E4%BC%A0%E8%AF%B4%E6%9B%B2'

    #爬取基本信息
    html = scrape_page(url)
    results = get_basic_information(html)

    save_basic_information(results)

    #爬取详细信息
    
    #多进程方式(被网站ban了)
    # pool = multiprocessing.Pool()
    # urls = get_urls(html)
    # pool.map(scrape_and_save_details, urls)
    # pool.close()
    # pool.join()
    
    #单进程方式
    urls = get_urls(html)
    dir = 'details'
    if not os.path.exists(dir):
        os.makedirs(dir)
    num = 1
    for url in urls:
        if num >= 1 and num <= 1:
            html = scrape_page(url)
            get_and_save_details(html, dir, num)
        num += 1
