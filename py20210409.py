import requests
import time  
import csv
from bs4 import BeautifulSoup
URL="https://www.majortests.com/word-lists/word-list-0{}.html"


def generate_urls(url,start_page,end_page):
    urls=[]#存網址的list
    for page in range (start_page,end_page):  #for 迴圈 -->跑頁數
        urls.append(url.format(page))  #替換大括號中數字
    return urls 


def get_resource(url):
    headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    } #從network 當中 看他的request --> preview 可找到User-Agent
    return requests.get(url, headers=headers)
    
def parse_html(html_str):
    return BeautifulSoup(html_str,"lxml")

def get_word(soup,file):
    words=[]    
    count = 0
    for wordlist_table in soup.find_all(class_="wordlist"):
        count+=1
        for word_entry in wordlist_table.find_all("tr"):
            new_word=[]
            new_word.append(file)  #剛剛切下來的檔名
            new_word.append(str(count))#設定的次數
            new_word.append(word_entry.th.text)#tr底下的th
            new_word.append(word_entry.td.text)#底下的td
            words.append(new_word)
    return words

def web_scraping_bot(urls):
    eng_words=[]
    for url in urls:    
        file = url.split("/")[-1]  #此地方用給予索引值[-1]-->抓最後一個
        print("catching:",file,"web data...")
        r=get_resource(url)
        if r.status_code==requests.codes.ok:
            soup=parse_html(r.text)
            words = get_word(soup,file)
            eng_words=eng_words + words   
            time.sleep(5)       
        else:
            print("HTTP request error!!")
    return eng_words

def save_to_csv(words,file):
    with open(file,"w+",newline="",encoding="utf-8")as fp:
        writer = csv.writer(fp)
        for word in words:
            writer.writerow(word)


if __name__ == '__main__':   #__name__==__main__ ??
    urlx=generate_urls(URL,1,3)
    eng_words = web_scraping_bot(urlx)
    for item in eng_words:
        print(item)
    save_to_csv(eng_words, "engWordList 1 .csv")
'''  
        s=random.random()*5+3   #隨機生成3~8秒  原本為0~1 故 *5+3
        print("休息"+str(s)+"秒")
        time.sleep(s)#生成休息秒數
'''
