from dotenv import load_dotenv
load_dotenv()

# app.py
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import streamlit as st

# OpenAI APIキーを環境変数から取得
openai_api_key = os.getenv("OPENAI_API_KEY")

# LangChainでLLM（ChatGPT）を使う準備
llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0,
    openai_api_key=openai_api_key
)
def ask_expert(input_text, expert_type):
    # 専門家ごとのシステムメッセージを定義
    if expert_type == "健康":
        system_message = SystemMessage(
            content="あなたは優秀な健康の専門家としてユーザーの健康に関する質問に丁寧に答えてください。"
        )
    elif expert_type == "旅行":
        system_message = SystemMessage(
            content="あなたは旅行プランナーの専門家としてユーザーの旅行に関する相談に優しく答えてください。"
        )
    else:
        system_message = SystemMessage(
            content="あなたは親切な一般アドバイザーとしてユーザーに役立つ回答をしてください。"
        )

    # ユーザーの質問をHumanMessageにする
    user_message = HumanMessage(content=input_text)

    # LLMに問い合わせて回答を得る
    response = llm([system_message, user_message])

    return response.content

# アプリのタイトルと説明
st.title("専門家AIチャットアプリ")
st.write("以下のフォームに質問を入力し、専門家の種類を選んで送信してください。AIが専門家として回答します。")

# 専門家の選択（ラジオボタン）
expert_type = st.radio("専門家の種類を選んでください：", ("健康", "旅行"))

# ユーザーの入力
user_input = st.text_input("質問を入力してください")

# 送信ボタン
if st.button("送信"):
    if user_input:
        #定義した関数を呼び出し
        response = ask_expert(user_input, expert_type)

        st.divider()

        st.success("回答：")   
        st.write(response)
    else:
        st.warning("質問を入力してください。")

