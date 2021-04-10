i
# PY_20210401_109021490yuyao
當req = requests.get("URL")

200→有資料可以抓

404→錯誤(nopage)


<img height=200 width=5000 src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ca50e69d-ac8d-4257-a98a-b38349df319f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210410T063558Z&X-Amz-Expires=86400&X-Amz-Signature=a9f8e4c399c14b2db95c48daaaffd1ee63a83aa85227e1c448f498518add992c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22"></img>

lxml→以前網站之格式

王老師 BIG5 重點=顯示錯誤字串，將他轉為空白

如何把資料寫到檔案去:利用open(檔案名，寫入模式，編碼)丟給變數

<img height=200 width=500 src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5ee8470b-fe92-4efb-9c92-a6f85054e581/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210410T063706Z&X-Amz-Expires=86400&X-Amz-Signature=c87667527c5023e7eca1a9e366ec664fc067420beddbc8b3ab076509ef1f5567&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22"></img>
這次的網址有規則→{0}可替換掉

file 指的是 html的檔名(.....html)  用"/"切開 —>

WHY [-1]—>索引值可以是負→從後面數出來

也就是urlList[len(urlList)-1]

<img height=200 width=500 src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ca50e69d-ac8d-4257-a98a-b38349df319f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210410T063558Z&X-Amz-Expires=86400&X-Amz-Signature=a9f8e4c399c14b2db95c48daaaffd1ee63a83aa85227e1c448f498518add992c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22"></img>
<br>
<br>

<img height=200 width=500 src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5ee8470b-fe92-4efb-9c92-a6f85054e581/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210410T063706Z&X-Amz-Expires=86400&X-Amz-Signature=c87667527c5023e7eca1a9e366ec664fc067420beddbc8b3ab076509ef1f5567&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22"></img>

<br>
<br>


# 完整函式

<img height=200 width=500  src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ffbf3921-0aa5-4304-90fc-a45dc2915ac9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210410T065150Z&X-Amz-Expires=86400&X-Amz-Signature=9c239c67c1b4c20ff1a4e3b3e955f1006f8ab198ec92d7cf58a3476f898592e4&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22"></img>
<br>
<br>
<br>


<img height=200 width=500 src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ce568d0d-5496-4c47-bbcf-9aec66f2fde7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210410T065515Z&X-Amz-Expires=86400&X-Amz-Signature=d055ffdf8320062a312c713dc1edb9bb8e321393fe592636b980f1d5ad3e5855&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22"></img>
<br>
<br>
<br>


<img height=200 width=500 src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/edd306d6-c744-4453-a252-16d1ca510dca/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210410T065638Z&X-Amz-Expires=86400&X-Amz-Signature=fd913a8fa5d2d3519bddb242e54cbdd086d3577ff78e12d9b9ea7368f0561a7c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22"></img>
<br>
<br>
<br>

<img height=200 width=500 src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/268254df-9cb9-4286-8273-66e90bce1f13/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210410T065752Z&X-Amz-Expires=86400&X-Amz-Signature=2aee551f51a0b96d6b50147dbad4026d7bc94320cc3a4902ff1ed2e9f8a94cdb&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22"></img>