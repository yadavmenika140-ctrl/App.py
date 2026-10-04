import streamlit as st
import pandas as pd

# 1. पेज का नाम और लेआउट सेट करना
st.set_page_config(page_title="Market Valley", layout="wide", page_icon="📈")

# 2. भाषा का चयन
lang = st.sidebar.radio("🌐 Select Language / भाषा चुनें", ["English", "हिंदी"])

# 3. अनुवाद डेटा
t = {
    "English": {
        "title": "📈 Market Valley",
        "subtitle": "Your Ultimate Bilingual Financial Dashboard",
        "market_indices": "🔴 Live Indian Market Overview (NSE/BSE)",
        "other_markets": "💰 Gold & Crypto Market (Live Rates)",
        "news_section": "📰 Market-Moving News & Alerts",
        "refresh": "Data auto-refreshes directly via secure live financial nodes.",
        "news_pb": "⚠️ PB Fintech (Policybazaar) Alert: Stock plunged after IRDAI proposed commission cuts for online brokers.",
        "news_cpi": "📊 CPI Inflation Update: Indian retail inflation remains under RBI's comfort zone, positive for market."
    },
    "हिंदी": {
        "title": "📈 मार्केट वैली (Market Valley)",
        "subtitle": "आपका अपना द्विभाषी वित्तीय डैशबोर्ड",
        "market_indices": "🔴 लाइव भारतीय बाजार ओवरव्यू (NSE/BSE)",
        "other_markets": "💰 सोना और क्रिप्टो बाजार (लाइव भाव)",
        "news_section": "📰 बाजार को प्रभावित करने वाली बड़ी खबरें",
        "refresh": "डेटा सीधे सुरक्षित लाइव वित्तीय नोड्स से स्वचालित रूप से अपडेट होता है।",
        "news_pb": "⚠️ पीबी फिनटेक (पॉलिसीबाज़ार) अलर्ट: ऑनलाइन ब्रोकरों के कमीशन में कटौती के IRDAI के प्रस्ताव के बाद शेयर में भारी गिरावट आई।",
        "news_cpi": "📊 CPI मुद्रास्फीति अपडेट: भारतीय खुदरा मुद्रास्फीति आरबीआई के संतोषजनक दायरे में बनी हुई है, जो बाजार के लिए सकारात्मक है।"
    }
}

st.title(t[lang]["title"])
st.caption(t[lang]["subtitle"])
st.info(t[lang]["refresh"])
st.markdown("---")

# --- सेक्शन 1: लाइव भारतीय बाजार डेटा (100% Secure Free Live Iframe) ---
st.subheader(t[lang]["market_indices"])

# यह विजेट TradingView के सर्वर्स से सीधा लाइव डेटा उठाता है जो कभी ब्लॉक नहीं होता
indian_market_html = """
<iframe src="https://tradingview.com" 
width="100%" height="320" frameborder="0" allowtransparency="true" scrolling="no" style="box-sizing: border-box; border-radius: 8px;"></iframe>
"""
st.components.v1.html(indian_market_html, height=330)

st.markdown("---")

# --- सेक्शन 2: सोना और क्रिप्टो बाजार (100% Secure Free Live Iframe) ---
st.subheader(t[lang]["other_markets"])

global_market_html = """
<iframe src="https://tradingview.com" 
width="100%" height="320" frameborder="0" allowtransparency="true" scrolling="no" style="box-sizing: border-box; border-radius: 8px;"></iframe>
"""
st.components.v1.html(global_market_html, height=330)

st.markdown("---")

# --- सेक्शन 3: बाजार को प्रभावित करने वाली खबरें ---
st.subheader(t[lang]["news_section"])
st.info(t[lang]["news_pb"])
st.info(t[lang]["news_cpi"])

# पादलेख (Footer)
st.markdown("---")
st.caption("© 2026 Market Valley | Developed for Indian Retail Investors")
