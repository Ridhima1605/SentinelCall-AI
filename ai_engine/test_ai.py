from ai_engine.nlp.scam_detector import detect_scam

text = "Send OTP now to unblock your bank account"

prediction, prob = detect_scam(text)

print("Prediction:", prediction)
print("Fraud Probability:", prob)