import streamlit as st

# 1. पेज का नाम और लेआउट
st.set_page_config(page_title="Market Valley", layout="wide", page_icon="📈")

# 2. भाषा का चयन
lang = st.sidebar.radio("🌐 Select Language / भाषा चुनें", ["English", "हिंदी"])

# 3. अनुवाद डेटा
t = {
    "English": {
        "title": "📈 Market Valley",
        "subtitle": "Your Ultimate Bilingual Financial Dashboard",
        "market_indices": "🔴 Live Market Indices (NSE/BSE)",
        "other_markets": "💰 Gold & Crypto Market",
        "news_section": "📰 Market-Moving News & Alerts",
        "table_name": "Market",
        "table_price": "Price",
        "table_change": "Status",
        "news_pb": "⚠️ PB Fintech (Policybazaar) Alert: Stock plunged after IRDAI proposed commission cuts for online brokers.",
        "news_cpi": "📊 CPI Inflation Update: Indian retail inflation remains under RBI's comfort zone, positive for market.",
        "news_rbi": "🏦 RBI Policy News: Experts expect no rate cut in the upcoming meeting due to global cues.",
        "news_global": "🌍 Global Market: US Markets ended in green, providing a positive handover for Nifty & Sensex.",
        "demat_text": "🔥 Start Investing Today! Open a Free Demat Account with Top Brokers."
    },
    "हिंदी": {
        "title": "📈 मार्केट वैली (Market Valley)",
        "subtitle": "आपका अपना द्विभाषी वित्तीय डैशबोर्ड",
        "market_indices": "🔴 भारतीय बाजार सूचकांक (NSE/BSE)",
        "other_markets": "💰 सोना और क्रिप्टो बाजार",
        "news_section": "📰 बाजार को प्रभावित करने वाली बड़ी खबरें",
        "table_name": "बाजार",
        "table_price": "अनुमानित कीमत",
        "table_change": "स्थिति",
        "news_pb": "⚠️ पीबी फिनटेक (पॉलिसीबाज़ार) अलर्ट: ऑनलाइन ब्रोकरों के कमीशन में कटौती के IRDAI के प्रस्ताव के बाद शेयर में भारी गिरावट आई।",
        "news_cpi": "📊 CPI मुद्रास्फीति अपडेट: भारतीय खुदरा मुद्रास्फीति आरबीआई के संतोषजनक दायरे में बनी हुई है, जो बाजार के लिए सकारात्मक है।",
        "news_rbi": "🏦 RBI पॉलिसी समाचार: वैश्विक संकेतों के कारण विशेषज्ञों को आगामी बैठक में ब्याज दरों में कटौती की उम्मीद नहीं है।",
        "news_global": "🌍 ग्लोबल मार्केट: अमेरिकी बाजार बढ़त के साथ बंद हुए, जिससे निफ्टी और सेंसेक्स के लिए सकारात्मक संकेत हैं।",
        "demat_text": "🔥 आज ही निवेश शुरू करें! भारत के टॉप ब्रोकर्स के साथ मुफ़्त में डीमैट अकाउंट खोलें।"
    }
}

st.title(t[lang]["title"])
st.caption(t[lang]["subtitle"])
st.markdown("---")

# --- सेक्शन 1: भारतीय बाजार सूचकांक ---
st.subheader(t[lang]["market_indices"])

# सुंदर और साफ टेबल डेटा
market_data = {
    t[lang]["table_name"]: ["NIFTY 50", "SENSEX", "NIFTY BANK"],
    t[lang]["table_price"]: ["24,150.00", "79,200.00", "51,500.00"],
    t[lang]["table_change"]: ["🟢 +0.85%", "🟢 +0.72%", "🔴 -0.30%"]
}
st.table(market_data)

st.markdown("---")

# --- सेक्शन 2: सोना और क्रिप्टो बाजार ---
st.subheader(t[lang]["other_markets"])

other_data = {
    t[lang]["table_name"]: ["GOLD (10g / 24K)", "BITCOIN (BTC)", "ETHEREUM (ETH)"],
    t[lang]["table_price"]: ["₹75,800", "$64,200", "$2,650"],
    t[lang]["table_change"]: ["🟢 +1.20%", "🟢 +2.50%", "🔴 -0.95%"]
}
st.table(other_data)

st.markdown("---")

# --- सेक्शन 3: ब्रांड का पहला पैसा कमाने वाला बटन (Demat Account Button) ---
st.success(t[lang]["demat_text"])
st.button("👉 Open Free Demat Account (मुफ़्त खाता खोलें)")

st.markdown("---")

# --- सेक्शन 4: बाजार को प्रभावित करने वाली खबरें (PB Fintech, CPI, RBI) ---
st.subheader(t[lang]["news_section"])

st.info(t[lang]["news_pb"])
st.info(t[lang]["news_cpi"])
st.info(t[lang]["news_rbi"])
st.info(t[lang]["news_global"])

# पादलेख (Footer)
st.markdown("---")
st.caption("© 2026 Market Valley | Developed for Indian Retail Investors")
