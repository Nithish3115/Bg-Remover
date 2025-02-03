import streamlit as st
import numpy as np
import librosa
import matplotlib.pyplot as plt

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

# Streamlit app
st.markdown(
    """
    <style>
    .reportview-container {
        background: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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

    # Get user input for start and end time as integers
   # Get user input for start and end time as floats
    start_time = st.number_input("Start Time (seconds)", min_value=0.0, value=0.0, format="%.2f", step=0.1)
    end_time = st.number_input("End Time (seconds)", min_value=0.0, value=min(10.0, audio_duration), format="%.2f", step=0.1)
    # Button to generate the audio graph
    if st.button("Generate Audio Graph"):
        Audio_graph(audio_path, 44100, start_time, end_time, "Audio Graph", f_ratio=0.1)