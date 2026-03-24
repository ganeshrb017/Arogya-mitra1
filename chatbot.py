from transformers import pipeline
from app.utils import detect_language, validate_response
from app.llm import get_health_response

classifier = pipeline("zero-shot-classification")

labels = ["symptoms", "treatment", "prevention", "emergency"]

def classify_intent(text):
    result = classifier(text, labels)
    return result['labels'][0]

def chatbot_pipeline(user_input):
    lang = detect_language(user_input)

    intent = classify_intent(user_input)

    response = get_health_response(user_input)

    response = validate_response(response)

    return {
        "intent": intent,
        "response": response,
        "language": lang
    }