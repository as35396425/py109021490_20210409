import requests
import time  
import csv
from bs4 import BeautifulSoup
URL="https://www.majortests.com/word-lists/word-list-0{}.html"


def generate_urls(url,start_page,end_page): #此函式用於生成迴圈頁數之網址(有規律性、頁數...)
    urls=[]                                     #存網址的list
    for page in range (start_page,end_page):  #for 迴圈 -->跑頁數
        urls.append(url.format(page))  #替換大括號中數字
    return urls 


def get_resource(url):#假裝是人類
    headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    } #從network 當中 看他的request --> preview 可找到User-Agent
    return requests.get(url, headers=headers) #傳回url並且headers是上面
    
def parse_html(html_str):
    return BeautifulSoup(html_str,"lxml")

def get_word(soup,file):
    words=[]    
    count = 0
    for wordlist_table in soup.find_all(class_="wordlist"):#find_all要的東西 並存入變數
        count+=1   #計數
        for word_entry in wordlist_table.find_all("tr"): #並且在剛剛的變數 在抓 像是抓完一層在抓更裡面
            new_word=[]
            new_word.append(file)  #剛剛切下來的檔名   
            new_word.append(str(count))#設定的次數
            new_word.append(word_entry.th.text)#tr底下的th
            new_word.append(word_entry.td.text)#底下的td
            words.append(new_word) #將剛剛的東西全部存入words
    return words

def web_scraping_bot(urls):
    eng_words=[]
    for url in urls:    
        file = url.split("/")[-1]  #此地方用給予索引值[-1]-->抓最後一個
        print("catching:",file,"web data...")
        r=get_resource(url) #從此函式抓到裝成人類的url
        if r.status_code==requests.codes.ok:#若有回應
            soup=parse_html(r.text) #r.text放進湯-->當中為lxml
            words = get_word(soup,file)#抓東西進去
            eng_words=eng_words + words   #把抓到的加起來
            time.sleep(5)       
        else:
            print("HTTP request error!!")
    return eng_words

def save_to_csv(words,file):
    with open(file,"w+",newline="",encoding="utf-8")as fp: #進入enter 並且執行完exit
        writer = csv.writer(fp)
        for word in words:
            writer.writerow(word)


if __name__ == '__main__':   #__name__==__main__ ??
    urlx=generate_urls(URL,1,3)  #變數為生成頁數之url
    eng_words = web_scraping_bot(urlx)
    for item in eng_words:
        print(item)
    save_to_csv(eng_words, "engWordList 1 .csv")
'''  
        s=random.random()*5+3   #隨機生成3~8秒  原本為0~1 故 *5+3
        print("休息"+str(s)+"秒")
        time.sleep(s)#生成休息秒數
'''
