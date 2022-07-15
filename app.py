#!/usr/bin/env python
# coding: utf-8

# ### <font color="Orange">**【 チャットボット作成 】**</font>
# ####  **テーマ：自然言語処理**
# ##### サブテーマ：streamlitを使用したチャットボットの作成

# #### 参考URL
# https://axross-recipe.com/recipes/348#chapter-35585

# In[8]:


import streamlit as st
import requests


# In[9]:


# A3RT APIのキー
apikey = "DZZSyQ7nm8sviABhGS4vBHBcfjAKDNjh"
chat_logs = []


# In[10]:


# Streamlitで多用する文法。title関数の引数に与えた文字列がWebアプリのタイトルとして表示される
# subheader関数でヘッダーにテキストを表示。text_input関数でテキスト入力ウィンドウを設置される（引数の文字列は説明文として表示）。


# In[11]:


st.title("Chatbot with streamlit")
st.subheader("メッセージを入力してから送信をタップしてください")
message = st.text_input("メッセージ")


# In[12]:


# チャットボットAPIを呼び出すsend_pya3rt関数を記載
# APIキーとWebアプリ上で受け取るテキストをパラメーターとしてAPIに送信し、レスポンスとして返答文を受け取る処理
def send_pya3rt(endpoint, apikey, text, callback):
    params = {'apikey': apikey,
              'query': text,
              }
    if callback is not None:
        params['callback'] = callback

    response = requests.post(endpoint, params)

    return response.json()


# In[13]:


# Webアプリの仕様としては、メッセージ送信ボタンを選択するとAPIが呼び出されてチャットボットの返信が表示される形
# ボタンが選択された時に呼び出される関数（generate_response）を定義
# ①send_pya3rt関数で入力されたテキストとAPIキーを送信し、レスポンスをJson形式で受け取る
# ②返信文を取り出し、送信文と返信文をchat_logsリストに追加してwrite関数でWebアプリ画面に表示
def generate_response():
    ans_json = send_pya3rt('https://api.a3rt.recruit.co.jp/talk/v1/smalltalk',
                       apikey, message, None)
    ans = ans_json['results'][0]['reply']
    chat_logs.append('you: ' + message)
    chat_logs.append('AI: ' + ans)
    for chat_log in chat_logs:
        st.write(chat_log)


# In[14]:


# 最後にテキスト送信ボタンをbutton関数で設置
# if文の条件式にすることでボタンが選択された際にsend_pya3rt関数が実行
if st.button("送信"):
    generate_response()


# In[ ]:




