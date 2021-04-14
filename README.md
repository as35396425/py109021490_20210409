
# PY_20210401_109021490yuyao
當req = requests.get("URL")

200→有資料可以抓

404→錯誤(nopage)



lxml→以前網站之格式

王老師 BIG5 重點=顯示錯誤字串，將他轉為空白

如何把資料寫到檔案去:利用open(檔案名，寫入模式，編碼)丟給變數


這次的網址有規則→{0}可替換掉

file 指的是 html的檔名(.....html)  用"/"切開 —>

WHY [-1]—>索引值可以是負→從後面數出來

也就是urlList[len(urlList)-1]


# 產生亂數休息秒數 : 3~8
    s=random.random()*5+3   #隨機生成3~8秒  原本為0~1 故 *5+3
        print("休息"+str(s)+"秒")
        time.sleep(s)#生成休息秒數

# 函式 web scraping bot
    <h1>當中最主要的函式 呼叫此式 連接其他函式(get_word parse_html get_resource </h1>
    def web_scraping_bot(urls):
        eng_words=[]
        for url in urls:    
            file = url.split("/")[-1]  #此地方用給予索引值[-1]-->抓最後一個
            print("catching:",file,"web data...")
            r=get_resource(url) #從此函式抓到裝成人類的url
            if r.status_code==requests.codes.ok:#若有回應
                soup=parse_html(r.text) # r.text(已經做完header encoding)放進湯-->當中為lxml
                words = get_word(soup,file)#抓東西進去
                eng_words=eng_words + words   #把抓到的加起來
                time.sleep(5)       
            else:
                print("HTTP request error!!")
    return eng_words

# 函式general URL
    def generate_urls(url,start_page,end_page): #此函式用於生成迴圈頁數之網址(有規律性、頁數...)
    urls=[]                                     #存網址的list
    for page in range (start_page,end_page):  #for 迴圈 -->跑頁數(開始 結束)
        urls.append(url.format(page))  #替換大括號中數字
    return urls 

# 函式get_resource
    def get_resource(url):#假裝是人類
    headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    } #從network 當中 看他的request --> preview 可找到User-Agent
    res=requests.get(url, headers=headers) #傳回url並且headers是上面
    res.encoding="utf8"
    return res
# 函式get_word
    def get_word(soup,file):
    words=[]    
    count = 0
    for wordlist_table in soup.find_all(class_="table-responsive"):#find_all要的東西 並存入變數
       
        for word_entry in wordlist_table.find_all("table"): #並且在剛剛的變數 在抓 像是抓完一層在抓更裡面
            for word_entry_1 in word_entry.find_all("tbody"):
                for word_entry_2 in word_entry_1.find_all("tr"):
                    for word_entry_3 in word_entry_2.find_all("td"):
                            count+=1   #計數
                            print(word_entry_3)
                            new_word=[]
                            new_word.append(file)       #剛剛切下來的檔名   
                            new_word.append(str(count)) #設定的次數
                            new_word.append(word_entry_3.text.replace("\n",""))
                                                        #從迴圈看 抓的是td
                            words.append(new_word) #將剛剛的東西全部存入words
    return words
# 函式 parse_html    
    def parse_html(html_str):
        return BeautifulSoup(html_str,"lxml") 就是以lxml為格式

# 函式存檔用
    def save_to_csv(words,file): 
    with open(file,"w+",newline="",encoding="utf-8")as fp: #進入enter 並且執行完exit
        writer = csv.writer(fp)
        for word in words:
            writer.writerow(word)
-------------------------------------------------------------------------------------------
    open(檔名,模式) newline 換行
    encoding 寫入編碼 
    寫入模式有:
    r讀取
    w寫入--->如檔案存在,會先刪掉,就是會覆蓋原先內容
    a寫入--->如檔案存在，從最後方追加
    x寫入--->.........,送出例外通知
    b:二進位模式
    t:文字模式
    +為了更新用 讀取以及寫入
    r+讀取且從第一行開頭寫入 有文字會覆蓋掉
    w+ 可讀取的w
    a+ 可讀取的a