import speech_recognition as sr

class MicrophoneModule:
    def __init__(self, microphone_index=0):
        self.microphone_index = microphone_index

    def listen(self):
        # Create a recognizer instance
        recognizer = sr.Recognizer()

        # Use the default microphone as the audio source
        with sr.Microphone() as source:
            print("Listening...")

            try:
                # Listen for speech input from the user
                audio_data = recognizer.listen(source)

                # Recognize speech using Google Speech Recognition
                text = recognizer.recognize_google(audio_data)

                # Print the recognized text in real-time
                print("You said:", text)
                return text.lower()

            except sr.UnknownValueError:
                # Speech not recognized
                print("Sorry, could not understand audio")

            except sr.RequestError as e:
                # Unable to access Google Speech Recognition service
                print(
                    "Could not request results from Google Speech Recognition service; {0}".format(
                        e
                    )
                )
