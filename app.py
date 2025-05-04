import streamlit as st
from utils import load_data, get_top_k_recommendations

st.set_page_config(page_title="SHL Assessment Recommender")
st.title("GenAI SHL Assessment Recommendation System")

st.write("Enter a job description or natural language query:")

query = st.text_area("Job Description / Query")

if 'data' not in st.session_state:
    st.session_state.data = load_data()

if st.button("Get Recommendations") and query:
    results = get_top_k_recommendations(query, st.session_state.data)
    
    st.subheader("Top Recommended SHL Assessments")
    for _, row in results.iterrows():
        st.markdown(f"### [{row['Name']}]({row['URL']})")
        st.markdown(f"- **Remote Testing Support**: {row['Remote Support']}")
        st.markdown(f"- **Adaptive Support**: {row['Adaptive Support']}")
        st.markdown(f"- **Duration**: {row['Duration']}")
        st.markdown(f"- **Test Type**: {row['Test Type']}")
        st.markdown(f"- **Similarity Score**: {round(row['similarity'], 2)}")
        st.markdown("---")
