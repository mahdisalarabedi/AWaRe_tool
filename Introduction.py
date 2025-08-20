from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env

api_key = os.getenv("OPENAI_API_KEY")

import streamlit as st
st.markdown(
    "<h1 style='direction: rtl; text-align: right;'>معرفی برنامه</h1>",
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style='direction: rtl; text-align: right; font-size:18px;'>
    با سلام و احترام 
    .جهت دریافت توصیه‌های درمان آنتی بیوتیکی داده‌های بالینی و کلینیکی مرتبط را وارد کنید. 
    \n
    .وجه کنید که این برنامه جهت انتخاب بهترین درمان آنتی بیوتیکی در بیماران سرپایی طراحی شده است. 
    \n
   ⚠️⚠️.مدل‌های هوش مصنوعی ممکن است اشتباه کنند⚠️⚠️
    
    </div>
    """,
    unsafe_allow_html=True
)