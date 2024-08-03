from datetime import datetime
import random
import os.path
import os
import time


current_path = os.path.abspath(__name__) #取得目前檔案路徑
directory_name = os.path.dirname(current_path) #取得目前資料夾路行
data_path = os.path.join(directory_name,'data') #目前資料夾路徑加上data目錄
print(data_path)
if not os.path.isdir(data_path):
    print("沒有data的目錄,手動建立目錄")
    os.mkdir(data_path)
else:
    print("目錄已經建立")

log_path = os.path.join(data_path,'iot.log')
if not os.path.isfile(log_path):
    print("沒有iot.log檔,建立新檔")
    with open(log_path,mode='w',encoding='utf-8',newline='') as file:
        file.write('時間,濕度,溫度\n')
    
else:
    print("已經有log檔")

Hum = str(random.randint(330,820) /10)
Tem = str(random.randint(0,100))
print("Humidity:",Hum,"\n","Tempture:",Tem)
localtime = time.localtime()
result = time.strftime("%Y-%m-%d %I:%M:%S %p",localtime)
#now_str = now.strftime("%Y-%m-%d %I:%M:%S %p")
#with open(log_path,mode='w',encoding='utf-8',newline='') as file:
#        file.write(now_str + ',67.9,28.5\n')
with open(log_path,mode='w',encoding='utf-8',newline='') as file:
        file.write(result + ',' + Hum + ',' + Tem + "\n")
