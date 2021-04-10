import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()


req = requests.get("https://csie.asia.edu.tw/project/semester-103",verify=False)#verify=False :忽略http安全證書的驗證
req.encoding="utf8"   #以utf8讀取
if req.status_code== 200:


    #print(req.text)
    soup=BeautifulSoup(req.text,"lxml")#抓資料時要看哪個是標的物(EX:ul=沒有序列 li="list item" ol="oder list" class="")

    result1=soup.select("div.table-responsive p")   #select 可以鎖定 <div class=table-responsive >      <p>      </div>
     
    fp=open("Homework.txt","w",encoding="utf8")  #open (檔名，寫入模式，寫入編碼)
    for val in result1:
        text2=val.text.replace("\n","")
        print(text2)
        fp.write(text2+"\n")  #寫資料到記憶體 記得要關才會寫成檔案()<span style='mso-tab-count:1'>

    fp.close()
else:
    print("no page")


