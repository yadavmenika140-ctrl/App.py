import streamlit as st

# 1. पेज का लेआउट और नाम सेट करना (Market Valley)
st.set_page_config(page_title="Market Valley - Financial Dashboard", layout="wide", page_icon="📈")

# 2. भाषा का चयन (Language Toggle)
lang = st.sidebar.radio("🌐 Select Language / भाषा चुनें", ["English", "हिंदी"])

# 3. अनुवाद डिक्शनरी (Translation Dictionary)
t = {
    "English": {
        "title": "📈 Market Valley",
        "subtitle": "Your Ultimate Bilingual Financial & Macro Dashboard",
        "market_indices": "🔴 Live Market Overview & Prices",
        "news_section": "📰 Market-Moving News & Global Macro Updates",
        "refresh": "Data auto-refreshes directly via secure live feeds."
    },
    "हिंदी": {
        "title": "📈 मार्केट वैली (Market Valley)",
        "subtitle": "आपका अपना द्विभाषी वित्तीय एवं मैक्रो डैशबोर्ड",
        "market_indices": "🔴 लाइव मार्केट ओवरव्यू और कीमतें",
        "news_section": "📰 बाजार को प्रभावित करने वाली खबरें और ग्लोबल मैक्रो अपडेट",
        "refresh": "डेटा सीधे सुरक्षित लाइव फीड्स के माध्यम से अपडेट होता है।"
    }
}

st.title(t[lang]["title"])
st.caption(t[lang]["subtitle"])
st.info(t[lang]["refresh"])
st.markdown("---")

# --- सेक्शन 1: लाइव मार्केट डेटा (Hassle-Free HTML Market Overview Widget) ---
st.subheader(t[lang]["market_indices"])

# यह विजेट पूरी तरह से HTML पर चलता है और मोबाइल ब्राउज़र्स पर 100% काम करता है
market_overview_html = """
<iframe src="https://tradingview.com" 
width="100%" height="450" frameborder="0" allowtransparency="true" scrolling="no" style="box-sizing: border-box; border-radius: 8px;"></iframe>
"""
st.components.v1.html(market_overview_html, height=460)

st.markdown("---")

# --- सेक्शन 2: लाइव न्यूज़ और मैक्रो अपडेट (Investing.com लाइव विजेट) ---
st.subheader(t[lang]["news_section"])

# लाइव न्यूज़ दिखाने के लिए मोबाइल-फ्रेंडली फ्रेम
news_widget = """
<iframe src="https://forexprostools.com?echo_mode=dark&categories=7,1,2,3,9,10&importance=1,2,3&features=datepicker,timezone&countries=14,5&calType=week&timeZone=23&lang=1" 
width="100%" height="450" frameborder="0" allowtransparency="true" marginwidth="0" marginheight="0" style="border-radius: 8px;"></iframe>
"""
st.components.v1.html(news_widget, height=470, scrolling=True)

# पादलेख (Footer)
st.markdown("---")
st.caption("© 2026 Market Valley | Developed for Indian Retail Investors")
