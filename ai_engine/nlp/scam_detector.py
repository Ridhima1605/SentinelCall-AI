scam_keywords = [
    "otp",
    "bank",
    "verify",
    "lottery",
    "prize",
    "urgent",
    "account blocked",
    "send money",
    "credit card",
    "password"
]

def detect_scam(text):

    text = text.lower()
    score = 0

    for word in scam_keywords:
        if word in text:
            score += 10

    risk = min(score, 100)

    return {
        "risk_score": risk,
        "is_scam": risk > 30
    }
