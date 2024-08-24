import streamlit as st
import redis
from dotenv import load_dotenv
import os
import json
import pandas as pd
from streamlit_autorefresh import st_autorefresh

#load_dotenv()
#redis_conn = redis.Redis(host=os.environ['REDIS_HOST'], port=6379, password=os.environ['REDIS_PASSWORD'])
#redis_conn.lrange('myraspberry/led',-5,-1)#抓最後的前五筆資料
#st.write(bytes_list)#讀面上面資料

load_dotenv()
st_autorefresh()
#redis_conn = redis.Redis(host=os.environ['REDIS_HOST'], port=6379, password=os.environ['REDIS_PASSWORD'])
redis_conn = redis.Redis.from_url(url=os.environ['RENDER_REDIS_INTERNAL'])
bytes_list = redis_conn.lrange('myraspberry/led',-5,-1)#抓最後的前五筆資料
#str_list = [bytes_str.decode('utf-8') for bytes_str in bytes_list]
str_list = [bytes_str.decode('utf-8') for bytes_str in reversed(bytes_list)]
dict_list = [json.loads(string) for string in str_list]
#st.write(str_list)#讀面上面資料
st.write(dict_list)
df1 = pd.DataFrame(dict_list)

st.title("traning classroom")
st.header("sensor:blue[cool] :sunglasses:")
st.dataframe(df1,
            hide_index=True,
            column_config={
                "status":st.column_config.CheckboxColumn(label='button_status',width = 'small'),
                "date":st.column_config.DatetimeColumn(label='Time',width='medium')
             })
