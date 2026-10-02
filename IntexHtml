import streamlit as st
import yfinance as yf
import pandas as pd

# 1. पेज का लेआउट और नाम सेट करना (Market Valley)
st.set_page_config(page_title="Market Valley - Financial Dashboard", layout="wide", page_icon="📈")

# 2. भाषा का चयन (Language Toggle)
lang = st.sidebar.radio("🌐 Select Language / भाषा चुनें", ["English", "हिंदी"])

# 3. अनुवाद डिक्शनरी (Translation Dictionary)
t = {
    "English": {
        "title": "📈 Market Valley",
        "subtitle": "Your Ultimate Bilingual Financial & Macro Dashboard",
        "market_indices": "Indian Market Indices",
        "commodities_crypto": "Gold & Crypto Market",
        "news_section": "📰 Market-Moving News & Global Macro Updates",
        "price": "Price",
        "change": "Change",
        "refresh": "Data auto-refreshes every 60 seconds."
    },
    "हिंदी": {
        "title": "📈 मार्केट वैली (Market Valley)",
        "subtitle": "आपका अपना द्विभाषी वित्तीय एवं मैक्रो डैशबोर्ड",
        "market_indices": "भारतीय बाजार सूचकांक (Indices)",
        "commodities_crypto": "सोना और क्रिप्टो बाजार",
        "news_section": "📰 बाजार को प्रभावित करने वाली खबरें और ग्लोबल मैक्रो अपडेट",
        "price": "कीमत",
        "change": "बदलाव",
        "refresh": "डेटा हर 60 सेकंड में स्वचालित रूप से अपडेट होता है।"
    }
}

st.title(t[lang]["title"])
st.caption(t[lang]["subtitle"])
st.info(t[lang]["refresh"])
st.markdown("---")

# 4. लाइव मार्केट डेटा खींचने का फ़ंक्शन (Yahoo Finance)
@st.cache_data(ttl=60)
def get_market_data(ticker):
    try:
        data = yf.Ticker(ticker)
        hist = data.history(period="2d")
        if len(hist) >= 2:
            price = hist['Close'].iloc[-1]
            prev_price = hist['Close'].iloc[-2]
            change = price - prev_price
            pct_change = (change / prev_price) * 100
            return round(price, 2), round(pct_change, 2)
    except Exception:
        return "N/A", "N/A"

# --- सेक्शन 1: भारतीय बाजार सूचकांक (Nifty, Sensex, Bank Nifty) ---
st.subheader(t[lang]["market_indices"])
col1, col2, col3 = st.columns(3)

# निफ्टी 50
nifty_p, nifty_c = get_market_data("^NSEI")
col1.metric("NIFTY 50", f"₹{nifty_p:,}" if isinstance(nifty_p, (int, float)) else "N/A", f"{nifty_c}%" if isinstance(nifty_c, (int, float)) else "N/A")

# सेंसेक्स
sensex_p, sensex_c = get_market_data("^BSESN")
col2.metric("SENSEX", f"₹{sensex_p:,}" if isinstance(sensex_p, (int, float)) else "N/A", f"{sensex_c}%" if isinstance(sensex_c, (int, float)) else "N/A")

# निफ्टी बैंक
bank_p, bank_c = get_market_data("^NSEBANK")
col3.metric("NIFTY BANK", f"₹{bank_p:,}" if isinstance(bank_p, (int, float)) else "N/A", f"{bank_c}%" if isinstance(bank_c, (int, float)) else "N/A")

st.markdown("---")

# --- सेक्शन 2: सोना और क्रिप्टो बाजार ---
st.subheader(t[lang]["commodities_crypto"])
col4, col5, col6 = st.columns(3)

# सोना (Gold Futures)
gold_p, gold_c = get_market_data("GC=F")
col4.metric("GOLD (USD/Ounce)", f"${gold_p:,}" if isinstance(gold_p, (int, float)) else "N/A", f"{gold_c}%" if isinstance(gold_c, (int, float)) else "N/A")

# बिटकॉइन
btc_p, btc_c = get_market_data("BTC-USD")
col5.metric("BITCOIN (USD)", f"${btc_p:,}" if isinstance(btc_p, (int, float)) else "N/A", f"{btc_c}%" if isinstance(btc_c, (int, float)) else "N/A")

# इथेरियम
eth_p, eth_c = get_market_data("ETH-USD")
col6.metric("ETHEREUM (USD)", f"${eth_p:,}" if isinstance(eth_p, (int, float)) else "N/A", f"{eth_c}%" if isinstance(eth_c, (int, float)) else "N/A")

st.markdown("---")

# --- सेक्शन 3: लाइव न्यूज़ और मैक्रो अपडेट (Investing.com लाइव विजेट) ---
st.subheader(t[lang]["news_section"])

# बिना किसी API Key के लाइव न्यूज़ दिखाने के लिए HTML/JS विजेट
news_widget = """
<iframe src="https://forexprostools.com?echo_mode=dark&categories=7,1,2,3,9,10&importance=1,2,3&features=datepicker,timezone&countries=14,5&calType=week&timeZone=23&lang=1" 
width="100%" height="500" frameborder="0" allowtransparency="true" marginwidth="0" marginheight="0"></iframe>
"""
st.components.v1.html(news_widget, height=520, scrolling=True)

# पादलेख (Footer)
st.markdown("---")
st.caption("© 2026 Market Valley | Developed for Indian Retail Investors")
