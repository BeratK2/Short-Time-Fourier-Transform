import os 
import librosa
import IPython.display as ipd
import numpy as np
import matplotlib.pyplot as plt

# --- HELPER METHOD TO VISUALIZE SPECTROGRAM ---
def plot_spectrogram(Y, sr, hop_length, y_axis="linear"):
    plt.figure(figsize=(25,10))
    librosa.display.specshow(Y, sr=sr, hop_length=hop_length, x_axis="time", y_axis=y_axis)
    plt.colorbar(format="%+2.f")


# --- PREPROCESS INPUT AUDIO FILE ---
def preprocess(a):
    # --- LOAD AUDIO FILE WITH LIBROSA ---
    loaded_audio, sr = librosa.load(a)

    
    # --- EXTRACT STFT ---
    FRAME_SIZE = 2048 # Typical parameters
    HOP_SIZE = 512 

    S_scale = librosa.stft(loaded_audio, n_fft=FRAME_SIZE, hop_length=HOP_SIZE)
    S_scale.shape # X = frequency, Y = Number of frames (temporal bins)
    type(S_scale[0][0])


    # --- CALCULATE SPECTROGRAM ---
    Y_scale = np.abs(S_scale) ** 2
    Y_scale.shape
    type(Y_scale[0][0])
    

    # --- LOG-AMPLITUDE SPECTROGRAM ---
    Y_log_scale = librosa.power_to_db(Y_scale)
    return plot_spectrogram(Y_log_scale, sr, HOP_SIZE)
    

