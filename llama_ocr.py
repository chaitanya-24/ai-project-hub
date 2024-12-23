import streamlit as st
from groq import Groq
import base64
from PIL import Image
import os 
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

# Function to encode the image
def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

# Initialize Groq client
client = Groq(api_key=groq_api_key)

# Page configuration
st.set_page_config(
    page_title="Llama OCR",
    page_icon="🦙"
)

# Title and description in main area
st.title("🦙 Llama OCR")

# Create a container for the upload message and delete button
col1, col2 = st.columns([3, 1])  # Adjust column sizes as needed

st.markdown('<p style="margin-top: -20px;">Extract structured text from images using Llama 3.2 Vision!</p>', unsafe_allow_html=True)
st.markdown("---")

with col2:
    if st.button("Clear🗑️"):
        extracted_content = ""
        # st.success("Data deleted.")

# Sidebar for image upload
st.sidebar.header("Upload Image")
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Variable to store extracted content
extracted_content = ""

if uploaded_file is not None:
    # Display the uploaded image in the sidebar
    st.sidebar.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

    # Add an "Extract" button in the sidebar
    if st.sidebar.button("Extract Text 🔍", type="primary"):
        # Encode the uploaded image
        base64_image = encode_image(uploaded_file)

        # Prepare the chat completion request
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text", 
                            "text": """Please analyze the text contained within the provided image. Your task is to extract all readable content and present it in a structured Markdown format. The output should be clear, concise, and well-organized, ensuring that it is easy to read and understand. 

                                        **Instructions:**
                                        1. **Extract All Text:** Identify and extract all text elements from the image, including headings, paragraphs, bullet points, and any other relevant textual information.
                                        2. **Organize Content:** Structure the extracted text logically. Use appropriate Markdown formatting such as:
                                        - **Headings** for main topics
                                        - **Subheadings** for subtopics
                                        - **Bullet points** or **numbered lists** for enumerations
                                        - **Code blocks** where applicable, especially for technical content or specific data formats.
                                        3. **Maintain Original Formatting:** If the image contains any specific formatting (like bold or italic text), try to reflect this in the Markdown output where possible.
                                        4. **Ignore Non-Text Elements:** Focus solely on textual content; do not include descriptions of images or graphics that do not contain relevant text.
                            """
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                            },
                        },
                    ],
                }
            ],
            model="llama-3.2-11b-vision-preview",
        )

        # Get the response and store it in extracted_content
        extracted_content = chat_completion.choices[0].message.content

# Center display of extracted content if available
if extracted_content:
    st.subheader("Analysis Result:")
    st.markdown(extracted_content)
