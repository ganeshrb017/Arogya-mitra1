from langdetect import detect

def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"

def validate_response(response):
    blacklist = ["miracle cure", "instant cure"]

    for word in blacklist:
        if word in response.lower():
            return "Please consult a certified doctor."

    return response