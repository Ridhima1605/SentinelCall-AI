from ai_engine.speech.speech_to_text import convert_audio_to_text
from ai_engine.nlp.scam_detector import detect_scam

def analyze_call(audio_file):

    text = convert_audio_to_text(audio_file)

    prediction,prob = detect_scam(text)

    return {
        "call_text": text,
        "scam_prediction": int(prediction),
        "fraud_probability": float(prob)
    }