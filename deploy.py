import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lead Scraper Results", layout="wide")

st.title("📊 Lead Scraper Results")
st.write("This app displays and lets you download scraped leads from LinkedIn.")

uploaded_file = st.file_uploader("Upload your leads CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Make LinkedIn URLs clickable
    df['LinkedIn URL'] = df['LinkedIn URL'].apply(lambda x: f"<a href='{x}' target='_blank'>🔗 Profile</a>")
    
    # Show leads with hyperlinks
    st.markdown("### 🔍 Uploaded Leads with Links")
    st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)

    # Lead scoring
    def score_lead(row):
        score = 0
        keywords = ['Google', 'AI', 'ML', 'Data', 'Senior', 'Principal', 'Lead','Manager']
        for kw in keywords:
            if kw.lower() in row['Name/Title'].lower() or kw.lower() in str(row['Snippet']).lower():
                score += 2
        return score

    df['Lead Score'] = df.apply(score_lead, axis=1)
    df = df.sort_values(by='Lead Score', ascending=False)

    # Show lead scores
    st.subheader("📈 Scored Leads")
    st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)

    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Scored Leads CSV",
        data=csv,
        file_name='scored_leads.csv',
        mime='text/csv'
    )
else:
    st.warning("Upload a leads.csv file to begin.")
