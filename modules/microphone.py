import speech_recognition as sr

# Create a recognizer instance
recognizer = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    # Adjust for ambient noise if necessary
    recognizer.adjust_for_ambient_noise(source)
    print("Listening...")

    # Continuous loop to listen for speech input
    while True:
        try:
            # Listen for speech input from the user
            audio_data = recognizer.listen(source)

            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio_data)

            # Print the recognized text in real-time
            print("You said:", text)

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
