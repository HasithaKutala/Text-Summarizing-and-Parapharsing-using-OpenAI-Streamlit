# Text summarizing and paraphrasing using OpenAI and Streamlit 

**1. Setting up **

Install and import all the required libraries 
import openai 
imnport streamlit as st 

Streamlit is a popular Python library used for building interactive web applications

**2. Set the GPT-3 API key **

To use the OpenAI API, you will need to obtain an API key by signing up for a free account on the OpenAI website and creating a new API key. You can then use the API key in your code by setting it as the value of the openai.api_key variable. 
The key should be private so we use package from streamlit called "st.secrets" which provides a way to securely store and access sensitive information, such as API keys, in Streamlit applications.
- First create a file in the same folder with name "secrets.toml" this allows you to separate your sensitive data from your code and keep it protected. This store values such as API keys, passwords, or any other confidential information needed by your Streamlit application. In the secrets.toml file write pass and give the api key as value to it pass= " sk- ".
- Now in the main app.py file write this to access the api key from secrets.toml.
openai.api_key=st.secrets['pass']. 

- Temperature is the parameter which controls the randomness of the generated text. The low temperature will give you more focused output and the high temperature will give more random and more imaginative output.

**3.Enter the text**

- Now we will create text area for user to enter Streamlit’s text_area function

- If you want you can add radio buttons to user to choose the desried option so we can use streamlit st.radio function. 

**4. Generating the summary and paraphrasing **


First we start with checking the length of the article, if its length is greater than 100 then we will add button to click which will generate the summary. We use streamlit button function and info function to see the generated summary.

we will use OpenAI Completion API to generate a summary and paraphrasing of the article. The Completion class is an AI-powered text completion model that can generate text based on a prompt provided by the user. The create() method of the Completion class is called with several parameters: Model, prompt, max_tokens, temperature.

The create() method returns a response object that contains the generated text as well as other metadata about the request. The response object is stored in the response variable for use later in the code.

-summary = response_summary["choices"][0]["text"] is used to extract the generated summary from the response received from the OpenAI language model.

- If you want to download the result we can use the streamlit download_button function to get summarised and paraphrased outputs.

**5. Word count**

when the user generates the summary then the model gives us the word count of the input text and the summarised text. 
-len(article_text.split()) gives you the count of words in the input: article_text string by splitting it into substrings based on whitespace and counting the number of resulting elements in the list.
-len(summary.split()) gives us the word count of summarized text:
-Then it can be displayed using st.info()
