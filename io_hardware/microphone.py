import speech_recognition as sr
from config import is_debug_mode

class MicrophoneModule:
    def __init__(self, microphone_index=0):
        self.microphone_index = microphone_index
        self.isEnabled = True

    def listen(self):
        # Create a recognizer instance
        recognizer = sr.Recognizer()
        if self.isEnabled:
            # Use the default microphone as the audio source
            with sr.Microphone() as source:
                print("Listening...")
                try:
                    # Listen for speech input from the user
                    audio_data = recognizer.listen(source)

                    # Recognize speech using Google Speech Recognition
                    text = recognizer.recognize_google(audio_data)
                    text = f"{text}"
                    text.lower()
                    # Print the recognized text in real-time
                    # if is_debug_mode(): 
                    print("Microphone: ", text)

                    return text

                except sr.UnknownValueError:
                    # Speech not recognized
                    if is_debug_mode(): print("Sorry, could not understand audio")
                    # self.text_to_speech.convert(random.choice(self.cant_understand_audio))

                except sr.RequestError as e:
                    # Unable to access Google Speech Recognition service
                    if is_debug_mode(): print(f"Could not request results from Google Speech Recognition service; {e}")

    def enable(self):
        # Enable text-to-speech
        self.isEnabled = True
        print("Microphone enabled")

    def disable(self):
        # Disable text-to-speech
        self.isEnabled = False
        print("Microphone disabled")