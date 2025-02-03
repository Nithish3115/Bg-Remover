import rembg as rb
from PIL import Image
import streamlit as st
from io import BytesIO

# Set page configuration
st.set_page_config(page_title="Background Remover", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* General Page Styling */
    body {
        background-color: #e6eef5;
        font-family: Arial, sans-serif;
    }
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Header Styling */
    h1 {
        color: #004d80;
        font-size: 3em;
        text-align: center;
    }
    h2 {
        color: #004d80;
        font-size: 1.5em;
        margin-bottom: 10px;
    }
    .sidebar h2 {
        color: #004d80;
    }

    /* Sidebar Styling */
    .sidebar {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    .sidebar-content {
        text-align: center;
    }
    .sidebar-content a {
        text-decoration: none;
        color: #4a90e2;
        font-weight: bold;
    }
    
    /* Image Columns Styling */
    .stImage {
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.15);
    }

    /* Download Button Styling */
    .stDownloadButton {
        background-color: #004d80;
        color: #ffffff;
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold;
    }
    .stDownloadButton:hover {
        background-color: #00375d;
        color: #ffffff;
    }

    /* Footer Styling */
    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 14px;
        color: #888888;
    }
    .footer p {
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.title("🎨 Background Remover")
st.markdown("<h2 style='text-align: center;'>Remove backgrounds from your images effortlessly!</h2>", unsafe_allow_html=True)

# Sidebar content
with st.sidebar:
    st.markdown("<div class='sidebar-content'>", unsafe_allow_html=True)
    st.write("### About the Developer")
    st.write("Nithish")
    st.caption("Follow me here ↓")
    st.write("[LinkedIn](https://www.linkedin.com/in/nithish-s-53a9a5292/)", unsafe_allow_html=True)
    st.write("[GitHub](https://github.com/Nithish3115/)", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# File uploader
img_inp = st.file_uploader("Upload your image here", type=["jpg", "png", "jpeg"], accept_multiple_files=False)

# Function to convert image to downloadable format
def downloadable(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

# Main content
if img_inp is not None:
    image = Image.open(img_inp)
    fixed = rb.remove(image)
    downloadable_image = downloadable(fixed)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("📥 Your Uploaded Image")
        st.image(image, use_column_width=True)
        
    with col2:
        st.header("📤 Background Removed Image")
        st.image(downloadable_image, use_column_width=True)

    st.download_button("⬇️ Download Background Removed Image", downloadable_image, key="download_button", file_name="bgremoved.png")

# Footer section
st.markdown(
    """
    <div class="footer">
        <p>Created with ❤️ by Nithish</p>
    </div>
    """,
    unsafe_allow_html=True,
)