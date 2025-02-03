import streamlit as st
import numpy as np
import librosa
import matplotlib.pyplot as plt
from PIL import Image
import rembg as rb
from io import BytesIO

# Set page configuration
st.set_page_config(page_title="Multi-Function App", layout="wide")

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

# Function to generate audio graph
def Audio_graph(signal, sr, start_time, end_time, title, f_ratio=1):
    fs = 44100

    # Load the audio file with the specified time range
    Audio2, sr = librosa.load(signal, offset=start_time, duration=end_time - start_time)

    start_idx = int(start_time * fs)
    end_idx = int(end_time * fs)

    # Extract the time vector and data for the specified time range
    plot_data = Audio2[start_idx:end_idx]
    X = np.fft.fft(plot_data)
    X_mag = np.absolute(X)

    # Frequency plot
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    f = np.linspace(0, sr, len(X_mag))
    f_bins = int(len(X_mag) * f_ratio)

    ax1.plot(f[:f_bins], X_mag[:f_bins])
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_xlim([0, 2100])
    ax1.set_title(title)
    st.pyplot(fig1)  # Display the frequency plot in Streamlit

    # Pitch values plot
    pitches, magnitudes, onset_frames = librosa.pyin(Audio2, sr=sr, fmin=100, fmax=800)

    fig2, ax2 = plt.subplots(figsize=(12, 6))
    ax2.plot(pitches, label='Pitch Values', color='blue')
    ax2.set_xlabel('Time (frames)')
    ax2.set_ylabel('Pitch (Hz)')
    ax2.set_title('Pitch Values Over Time')
    ax2.legend()
    ax2.grid()
    plt.tight_layout()
    st.pyplot(fig2)  # Display the pitch values plot in Streamlit

# Navigation
page = st.sidebar.selectbox("Select a page", ["Background Remover", "Audio Graph Visualization"])

if page == "Background Remover":
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

elif page == "Audio Graph Visualization":
    st.title("Audio Graph Visualization")

    # Upload audio file
    uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

    if uploaded_file is not None:
        # Load the audio file
        audio_path = uploaded_file.name
        with open(audio_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Load the audio file to get its duration
        audio_duration = librosa.get_duration(filename=audio_path)
        st.write(f"Audio Duration: {audio_duration:.2f} seconds")

        # Play the audio file
        st.audio(audio_path)

        # Get user input for start and end time as floats
        start_time = st.number_input("Start Time (seconds)", min_value=0.0, value=0.0, format="%.2f", step=0.1)
        end_time = st.number_input("End Time (seconds)", min_value=0.0, value=min(10.0, audio_duration), format="%.2f", step=0.1)

        # Button to generate the audio graph
        if st.button("Generate Audio Graph"):
            Audio_graph(audio_path, 44100, start_time, end_time, "Audio Graph", f_ratio=0.1)

    # Footer section
    st.markdown(
        """
        <div class="footer">
            <p>Created with ❤️ by Nithish</p>
        </div>
        """,
        unsafe_allow_html=True,
    )