import speech_recognition as sr
from ai_engine.nlp.scam_detector import detect_scam


def listen_and_detect():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("🎤 Listening...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)

            print("Transcript:", text)

            result = detect_scam(text)

            print("Risk Score:", result["risk_score"])

            if result["is_scam"]:
                print("⚠️ Scam Detected")
            else:
                print("✅ Safe Call")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    listen_and_detect()