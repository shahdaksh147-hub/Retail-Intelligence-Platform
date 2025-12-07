
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import LSTM, Dense

def build_lstm():
    model = Sequential([
        LSTM(64, activation='tanh', return_sequences=False),
        Dense(32, activation='relu'),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

if __name__ == "__main__":
    print("LSTM Forecasting Model Ready")
