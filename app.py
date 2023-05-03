import streamlit as st
from utils import summarize, generate_image

st.title("Text to Summary to Image")
st.header("This is a sample web app that summarizes text and generates and image of the summary")

text = st.text_area("Enter your URL below", "https://www.theverge.com/23702900/hyundai-ioniq-6-review-ev-specs-photos-price")

if st.button("Summarize and Generate Image"):
    if not text:
        st.error("Please Input a text in the text box")
    else:
        with st.spinner("Summarizing...."):
            summary = summarize(text)
        with st.spinner("Generating Image....."):
            image = generate_image(summary)
        st.info(f"Summary: {summary}")
        st.image(image)
