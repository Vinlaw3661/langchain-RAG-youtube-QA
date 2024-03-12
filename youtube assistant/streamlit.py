import streamlit as st
import textwrap
import assistant as assist

st.title("Youtube Assistant")


with st.sidebar:
    with st.form(key='my_form'):

        youtube_url = st.sidebar.text_area(
            label = 'What is the video URL',
            max_chars = 50,
            key = 'video url'
        )

        query = st.sidebar.text_area(
            label = 'Ask me about the video',
            max_chars = 50,
            key = 'query'
        )

        submit_button = st.form_submit_button(label = "Submit")

if query and youtube_url:
    db = assist.vector_db_from_youtube(youtube_url)
    response, docs = assist.get_response_from_query(db=db,query=query)
    st.subheader("Answer")
    st.text(
        textwrap.fill(response,width=80)
    )
    
