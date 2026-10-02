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
        "market_indices": "Indian Market Indices & Global Rates (Live Chart)",
        "news_section": "📰 Market-Moving News & Global Macro Updates",
        "refresh": "Data auto-refreshes directly via Live TradingView Feeds."
    },
    "हिंदी": {
        "title": "📈 मार्केट वैली (Market Valley)",
        "subtitle": "आपका अपना द्विभाषी वित्तीय एवं मैक्रो डैशबोर्ड",
        "market_indices": "भारतीय बाजार सूचकांक और लाइव चार्ट्स",
        "news_section": "📰 बाजार को प्रभावित करने वाली खबरें और ग्लोबल मैक्रो अपडेट",
        "refresh": "डेटा सीधे लाइव ट्रेडिंगव्यू फीड्स के माध्यम से अपडेट होता है।"
    }
}

st.title(t[lang]["title"])
st.caption(t[lang]["subtitle"])
st.info(t[lang]["refresh"])
st.markdown("---")

# --- सेक्शन 1: भारतीय बाजार सूचकांक, सोना और क्रिप्टो (TradingView Market Ticker Widget) ---
st.subheader(t[lang]["market_indices"])

# TradingView का लाइव टिकर विजेट (Nifty, Sensex, Gold, Bitcoin सब एक साथ लाइव)
ticker_widget = """
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://tradingview.com" async>
  {
  "symbols": [
    {"proName": "FOREXCOM:SPX2500", "title": "S&P 500"},
    {"proName": "BSE:SENSEX", "title": "SENSEX"},
    {"proName": "NSE:NIFTY", "title": "NIFTY 50"},
    {"proName": "NSE:BANKNIFTY", "title": "NIFTY BANK"},
    {"proName": "TVC:GOLD", "title": "GOLD"},
    {"proName": "BINANCE:BTCUSDT", "title": "BITCOIN"}
  ],
  "colorTheme": "light",
  "isTransparent": false,
  "showSymbolLogo": true,
  "locale": "in"
}
  </script>
</div>
"""
st.components.v1.html(ticker_widget, height=120)

st.markdown("---")

# लाइव एडवांस्ड चार्ट विजेट (Nifty 50 का लाइव ग्राफ देखने के लिए)
chart_widget = """
<div class="tradingview-widget-container" style="height:400px;">
  <div id="tradingview_chart"></div>
  <script type="text/javascript" src="https://tradingview.com"></script>
  <script type="text/javascript">
  new TradingView.widget({
    "autosize": true,
    "symbol": "NSE:NIFTY",
    "interval": "D",
    "timezone": "Asia/Kolkata",
    "theme": "light",
    "style": "1",
    "locale": "in",
    "enable_publishing": false,
    "hide_side_toolbar": false,
    "allow_symbol_change": true,
    "container_id": "tradingview_chart"
  });
  </script>
</div>
"""
st.components.v1.html(chart_widget, height=420)

st.markdown("---")

# --- सेक्शन 2: लाइव न्यूज़ और मैक्रो अपडेट (Investing.com लाइव विजेट) ---
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
