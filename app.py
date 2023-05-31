
#install dependencies 
import streamlit as st 
import pandas as pd
import numpy as np
import openai 

#Enter your secret key 

openai.api_key=st.secrets['pass']

st.title("Text Summarizing and Parapharsing using OpenAI + Streamlit ")

article_text=st.text_area("Enter or Paste your text to summarize")

output_size = st.radio ( label = "summary Length", 
                        options= ["Short", "Medium", "Long"],
                        )
temp=st.slider("Temperature- controls the randomness of text",0.0,1.0,0.5)

if output_size == "Short":
    out_token = 50
elif output_size == "Medium":
    out_token = 128
else:
    out_token = 516

if len(article_text)>100:

    #To summarize the text
    if st.button("Generate Summary"):
        response_summary=openai.Completion.create(
            engine="text-davinci-003",
            prompt="Please summarize the article for me in a few sentences : "+ article_text,
            max_tokens = 516,
            temperature= temp
        )
        summary= response_summary["choices"][0]["text"]
        st.info(summary)
        

        #To get word count of input text
        input_word_count= len(article_text.split())
        st.info(f"Word count of input text: {input_word_count}")

        #To get the word count of summmarized text

        summary_word_count =len(summary.split())
        st.info(f"Word count of generated summary :{summary_word_count}")

        st.download_button("Download Result",summary)

        
else:
        st.warning(" The sentence is not too long enough")
        
text=st.text_area("Enter or Paste your text to Paraphrase")

output=st.radio ( label = "synonyms", 
                        options= ["Fewer changes-more accurate", "More changes-Less accurate"],
                        )
#To Paraphrase the text
if st.button("Generate Paraphrase"):
    response_paraphrase = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Can you rephrase the artcile while preserving the main idea of the artcile : "+ article_text,
        max_tokens = 100,
        temperature= temp
    )
    paraphrase= response_paraphrase["choices"][0]["text"]
    st.info(f"Paraphrase: {paraphrase}")
    st.download_button("Download Result",paraphrase)

