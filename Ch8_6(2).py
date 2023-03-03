# 爬蟲程式範例：輸入網址與網頁標示, 解析網頁並顯示訊息
# 例外處理
try:
    # 引入相關套件
    import requests
    from bs4 import BeautifulSoup
    # 輸入網址, 解析網頁
    url = input('請輸入網址...')
    str_html = requests.get(url)
    x=BeautifulSoup(str_html.text,"html.parser")
    # 輸入第1層標示
    mark_up_1 = input('請輸入標示1...')
    x = x.select(mark_up_1)
    # 輸入第2層標示
    mark_up_2 = input('請輸入標示2...') 
    for item in x:
        result = item.select(mark_up_2)[0].text.strip()
        ''' []裏的數字可以更改，會擷取出不同的內容，
        由於網頁上資料多寡不一，數字若超過串列個數的範圍，
        程式會執行except例外'''
        print(result)   # 顯示第2層標示裏的文字
    print('\n程式完成 ......')    
except IndexError:
    ''' 若資料擷取完畢或沒有相對應的標示，則顯示「沒有資料了」，
    以避免程式出現錯誤訊息'''
    print('\n沒有資料了......')
