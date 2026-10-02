import streamlit as st
import requests
import urllib.request
import json

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
        "refresh": "Data auto-refreshes every 60 seconds."
    },
    "हिंदी": {
        "title": "📈 मार्केट वैली (Market Valley)",
        "subtitle": "आपका अपना द्विभाषी वित्तीय एवं मैक्रो डैशबोर्ड",
        "market_indices": "भारतीय बाजार सूचकांक (Indices)",
        "commodities_crypto": "सोना और क्रिप्टो बाजार",
        "news_section": "📰 बाजार को प्रभावित करने वाली खबरें और ग्लोबल मैक्रो अपडेट",
        "refresh": "डेटा हर 60 सेकंड में स्वचालित रूप से अपडेट होता है।"
    }
}

st.title(t[lang]["title"])
st.caption(t[lang]["subtitle"])
st.info(t[lang]["refresh"])
st.markdown("---")

# 4. बिना ब्लॉक होने वाली लाइव मार्केट डेटा ट्रिक (Alternative Free API Method)
@st.cache_data(ttl=60)
def get_alternative_data(symbol_type):
    # यह मुफ़्त और बिना चाबी (Key) के चलने वाला डेटा सोर्स है जो सर्वर्स पर ब्लॉक नहीं होता
    try:
        if symbol_type == "nifty":
            url = "https://yahoo.com^NSEI?range=2d&interval=1d"
        elif symbol_type == "sensex":
            url = "https://yahoo.com^BSESN?range=2d&interval=1d"
        elif symbol_type == "banknifty":
            url = "https://yahoo.com^NSEBANK?range=2d&interval=1d"
        elif symbol_type == "gold":
            url = "https://yahoo.comGC=F?range=2d&interval=1d"
        elif symbol_type == "btc":
            url = "https://yahoo.comBTC-USD?range=2d&interval=1d"
        elif symbol_type == "eth":
            url = "https://yahoo.comETH-USD?range=2d&interval=1d"
        
        # ब्राउज़र जैसा हेडर सेट करना ताकि ब्लॉक न हो
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        
        result = data['chart']['result'][0]
        price = result['meta']['regularMarketPrice']
        prev_price = result['meta']['previousClose']
        
        change = price - prev_price
        pct_change = (change / prev_price) * 100
        return round(price, 2), round(pct_change, 2)
    except:
        return "Loading..", 0.0

# --- सेक्शन 1: भारतीय बाजार सूचकांक (Nifty, Sensex, Bank Nifty) ---
st.subheader(t[lang]["market_indices"])
col1, col2, col3 = st.columns(3)

# निफ्टी 50
nifty_p, nifty_c = get_alternative_data("nifty")
col1.metric("NIFTY 50", f"₹{nifty_p}" if nifty_p != "Loading.." else "Loading..", f"{nifty_c}%")

# सेंसेक्स
sensex_p, sensex_c = get_alternative_data("sensex")
col2.metric("SENSEX", f"₹{sensex_p}" if sensex_p != "Loading.." else "Loading..", f"{sensex_c}%")

# निफ्टी बैंक
bank_p, bank_c = get_alternative_data("banknifty")
col3.metric("NIFTY BANK", f"₹{bank_p}" if bank_p != "Loading.." else "Loading..", f"{bank_c}%")

st.markdown("---")

# --- सेक्शन 2: सोना और क्रिप्टो बाजार ---
st.subheader(t[lang]["commodities_crypto"])
col4, col5, col6 = st.columns(3)

# सोना (Gold Futures)
gold_p, gold_c = get_alternative_data("gold")
col4.metric("GOLD (USD/Ounce)", f"${gold_p}" if gold_p != "Loading.." else "Loading..", f"{gold_c}%")

# बिटकॉइन
btc_p, btc_c = get_alternative_data("btc")
col5.metric("BITCOIN (USD)", f"${btc_p}" if btc_p != "Loading.." else "Loading..", f"{btc_c}%")

# इथेरियम
eth_p, eth_c = get_alternative_data("eth")
col6.metric("ETHEREUM (USD)", f"${eth_p}" if eth_p != "Loading.." else "Loading..", f"{eth_c}%")

st.markdown("---")

# --- सेक्शन 3: लाइव न्यूज़ और मैक्रो अपडेट (Investing.com लाइव विजेट) ---
st.subheader(t[lang]["news_section"])

# लाइव न्यूज़ दिखाने के लिए विश्वसनीय HTML/JS विजेट
news_widget = """
<iframe src="https://forexprostools.com?echo_mode=dark&categories=7,1,2,3,9,10&importance=1,2,3&features=datepicker,timezone&countries=14,5&calType=week&timeZone=23&lang=1" 
width="100%" height="500" frameborder="0" allowtransparency="true" marginwidth="0" marginheight="0"></iframe>
"""
st.components.v1.html(news_widget, height=520, scrolling=True)

# पादलेख (Footer)
st.markdown("---")
st.caption("© 2026 Market Valley | Developed for Indian Retail Investors")
