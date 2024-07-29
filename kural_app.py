# Author: K. Mariya Arul Raj

import streamlit as st
import os
import openai
from PIL import Image
import streamlit as st

os.environ['OPENAI_API_KEY'] = 'sk-proj-fFmAYI14aLwtbzTWLUjqT3BlbkFJBTwdT5wH2KxOqZtwMq56'

# image = "Thiruvalluvar.jpeg"
# st.image(image=image)

bottom_image = "Thiruvalluvar.jpeg"
if bottom_image is not None:
    image = Image.open(bottom_image)
    new_image = image.resize((125, 125))
    with st.columns(3)[1]:
        st.header("")
        st.image(new_image)

# st.title("Welcome to Thamizh koorum Nal Uzhagam!")
st.title("Welcome to தமிழ் கூறும் நல்லுலகம்!")

input_text = st.text_input("Enter a word")

st.write("The word you entered is: " + input_text)

def get_response(text):
    response = openai.chat.completions.create(
        model='gpt-4o-2024-05-13',
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


