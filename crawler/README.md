# 自動爬取券商分點資料

## 圖形驗證碼辨識
考量從頭訓練模型不太實際 直接使用陽春版[第三方套件](https://github.com/sml2h3/ddddocr)  
缺點：證交所使用的驗證碼對套件來說太複雜 有時候辨識會失敗

## 網路爬蟲
用selenium比較快  
但需要先下載和自己chrome版本相同的[chromedriver](https://chromedriver.chromium.org/downloads) 
會自動把成交價量的csv檔下載到同一個資料夾

## To-Do List
1. 資料前處理
