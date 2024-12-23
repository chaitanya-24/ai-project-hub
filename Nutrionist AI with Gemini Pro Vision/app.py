import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, image):
    # Switch to a supported model
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content([input_prompt, image[0]])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        byte_imgdata = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": byte_imgdata
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file Uploaded")  # Raise an error instead of returning

st.set_page_config(page_title="Nutritionist App")

st.header("Calorie Advisor Nutritionist App🍴")
uploaded_file = st.file_uploader("Choose an Image", type=["png", "jpeg", "jpg"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Fetch Calories")

input_prompt = """
    You are an expert in nutrition where you need to see the food items from the large image
    and calculate the total calories, also provide the details of every food item with calorie 
    intake in the format below:

    1. Item 1 - No. of Calories
    2. Item 2 - No. of Calories
    ----
    ----
    Finally, you can also mention whether the food is healthy or not and also mention the percentage(%) 
    split of carbohydrates, fats, fibers, sugar, and other important nutrients required in our diet.
"""

if submit:
    try:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_data)
        st.header("The Response is⬇️ ")
        st.write(response)
    except FileNotFoundError as e:
        st.error(str(e))  # Display error message in Streamlit app