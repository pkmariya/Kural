# Author: K. Mariya Arul Raj

import streamlit as st
import os
import openai

os.environ['OPENAI_API_KEY'] = 'sk-proj-fFmAYI14aLwtbzTWLUjqT3BlbkFJBTwdT5wH2KxOqZtwMq56'

st.title("Welcome to Thamizh koorum Nal Uzhagam!")

input_text = st.text_input("Enter a word")

st.write("The word you entered is: " + input_text)

def get_response(text):
    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are my Thirukural Guru!"},
            {"role": "user", "content": f"For this word {text}. What is the associated Kural?"}
        ],
        temperature=0.7,
        max_tokens=256,
        top_p=1.0
    )

    return response.choices[0].message.content.strip()

if st.button("Get a Kural for my Word"):
    result = get_response(input_text)
    # st.subheader(f"The associated Kural for the Word {input_text} is: ".format(input_text))
    st.write(result)


