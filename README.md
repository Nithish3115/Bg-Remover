# Streamlit Background Remover and Audio Visualizer

## Overview

This Streamlit application provides two main functionalities:

1. **Background Remover**: Effortlessly remove backgrounds from images using the `rembg` library.
2. **Audio Visualizer**: Visualize audio files using `librosa`, including displaying the audio waveform, pitch values, and the Fast Fourier Transform (FFT) of the audio signal.

## Features

- **Image Background Removal**: 
  - Upload an image, and the app will remove its background, allowing you to download the processed image.
  - The background removal process uses advanced algorithms to isolate the subject of the image.

- **Audio Visualization**: 
  - Upload an audio file to visualize:
    - The audio waveform, which represents the amplitude of the audio signal over time.
    - The pitch values over time, showing how the pitch of the audio changes.
    - The frequency spectrum using FFT, which provides insight into the frequency components of the audio signal.

## Requirements

To run this application, you need to have the following Python packages installed:

- `streamlit`: A framework for building web applications in Python.
- `rembg`: A library for removing backgrounds from images.
- `librosa`: A library for analyzing and visualizing audio signals.
- `numpy`: A library for numerical computations in Python.
- `matplotlib`: A plotting library for creating static, animated, and interactive visualizations in Python.
- `Pillow`: A library for image processing in Python.

You can install the required packages using pip:

```bash
pip install streamlit rembg librosa numpy matplotlib Pillow
```
## Usage

### 1.Background Remover

Navigate to the Background Remover Section: On the main page, select the Background Remover functionality.

Upload an Image: Click on the file uploader to upload an image file (supported formats: JPG, PNG, JPEG).

View Processed Images: The app will process the image and display both the original and the background-removed image side by side.

Download the Processed Image: Click the download button to save the background-removed image to your local machine.

### 2.Audio Visualizer
Navigate to the Audio Visualizer Section: On the main page, select the Audio Visualizer functionality.

Upload an Audio File: Click on the file uploader to upload an audio file (supported formats: WAV, MP3).

View Audio Duration: The app will display the duration of the audio file and allow you to play the audio.

Specify Time Range: Use the number input fields to specify the start and end times for the audio visualization.

Generate Audio Graph: Click the button to generate the audio graph, which includes:

The audio waveform.The pitch values over time.

The FFT of the audio signal, showing the frequency components.
