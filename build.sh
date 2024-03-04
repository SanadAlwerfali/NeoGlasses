#!/bin/bash

packages=(
    "opencv-python"
    "Pillow"
    "pynput"
    "numpy"
    "pytesseract"
    "pyttsx3"
    "SpeechRecognition"
)

for package in "${packages[@]}"; do
    echo "Installing $package..."
    pip3 install $package
done

echo "Installation complete."
