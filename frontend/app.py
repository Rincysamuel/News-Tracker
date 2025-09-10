import streamlit as st
import httpx

st.set_page_config(page_title="Global News Topic Tracker", layout="wide")
st.title("📈 Global News Topic Tracker")

if st.button("🔄 Refresh Topics"):
    st.rerun()

with st.spinner("Fetching topic summaries..."):
    try:
        response = httpx.get("http://127.0.0.1:8000/topics", timeout=60.0)
        data = response.json()
        st.subheader("📰 Summary")
        st.write(data["summary"])

        st.subheader("🧾 Raw Headlines")
        for article in data["articles"]:
            st.markdown(f"- [{article['title']}]({article['link']})")

    except Exception as e:
        st.error(f"Error fetching summaries: {e}")
