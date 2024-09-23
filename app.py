from flask import Flask, request, jsonify
import spacy, os

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")  # Загрузка модели для английского языка


# Маршрут для обработки запросов
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')  # Получаем сообщение от пользователя
    doc = nlp(user_input)  # Обрабатываем сообщение с помощью spaCy

    response = ""  # Объявляем переменную для ответа

    # Логика для обработки запросов о пакетах и стоимости
    if any(word in user_input.lower() for word in [
        "package", "packages", "pricing", "cost", "price", "rates", "fee", "amount", "$",
        "how much", "what's the price", "what is the price", "how much does it cost",
        "what does it cost", "price range", "pricing details", "service fees",
        "charge", "total cost", "final price", "price breakdown", "what is the fee",
        "cost of services", "cost for session", "what are your rates", "how much for session",
        "how much for photoshoot", "photography rates", "session pricing", "total amount",
        "price for photos", "price for packages", "what's your fee", "what is your fee",
        "session cost", "price of session", "what's the session cost", "what do you charge",
        "cost for package", "fees", "how much for package", "how much do you charge",
        "how much will it be", "cost breakdown", "what's the session price",
        "session fee", "photo session cost", "price for the service", "price inquiry",
        "session inquiry", "cost inquiry", "fees for session", "cost per session",
        "charges", "session charges", "total charges", "price to pay",
        "what do you charge for session", "cost for newborn photography",
        "how much is the session", "total price for session", "cost per package",
        "rates for session", "cost for lifestyle package", "price for mini package",
        "session fee details", "pricing info"
    ]):
        response = ("We offer the following packages:\n"
                    "1. **LIFESTYLE** - $550: A simple 1.5-hour home session without props, focusing on natural, relaxed moments with the newborn and family.\n"
                    "2. **MINI (Newborn Only)** - $790: 2-hour session, wrapped poses for the newborn only, 8 digital images, and 1 prop setup.\n"
                    "3. **STANDARD** - $890: 2-hour session with 2 prop setups, 16 digital images, includes lifestyle photos with parents and siblings.\n"
                    "4. **FULL** - $1190: 2.5-hour session with 3 prop setups, 25 digital images, includes photos of the entire family (up to 6 people).\n"
                    "Would you like more details on any specific package?")
    elif "lifestyle" in user_input.lower():
        response = ("The LIFESTYLE package ($550) includes a 1.5-hour session at your home without props.\n"
                    "This package focuses on natural, relaxed moments with the newborn and family in a cozy home environment.\n"
                    "Would you like more information or to book this package?")
    elif "mini" in user_input.lower():
        response = (
            "The MINI package ($790) is a 2-hour session focused solely on the newborn, with wrapped poses and one prop setup (e.g., basket or blanket).\n"
            "It includes 8 digital images.\n"
            "This package is perfect for capturing the essential moments of your newborn in a minimal setup."
            "Would you like to know more or book this package?")
    elif "standard" in user_input.lower():
        response = ("The STANDARD package ($890) includes a 2-hour session with 2 prop setups and 16 digital images.\n"
                    "This package is ideal for capturing both newborn and lifestyle family photos with parents and siblings.\n"
                    "Would you like more details about this package?")
    elif "full" in user_input.lower():
        response = ("The FULL package ($1190) offers a 2.5-hour session with 3 prop setups and 25 digital images.\n"
                    "It includes photos of the entire family (up to 6 people), making it ideal for larger families who want multiple creative setups.\n"
                    "Would you like to know more or book this package?")
    elif any(
            word in user_input.lower() for word in ["preferences", "setup", "style", "how to choose", "help me choose",
                                                    "which package", "choose package", "recommend", "recommendation",
                                                    "pick package", "suggest package"]):
        response = ("Let's help you choose the right package. Please answer the following questions:\n"
                    "1. Do you prefer simple, creative, or themed setups?\n"
                    "2. Would you like family members to be included in the photos?\n"
                    "3. How much time do you prefer for the session? (1-2 hours or more?)\n"
                    "4. Where would you like the session to be? (In-studio, at home, or outdoor?)\n"
                    "5. Do you have any color preferences or themes for the session?\n"
                    "6. Would you like to use any specific props or accessories for the photoshoot?")
    elif any(word in user_input.lower() for word in ["simple", "creative", "themed", "basic", "minimal", "artistic"]):
        response = (
            "Great! Based on your preference for a simple, creative, or themed setup, I recommend the STANDARD or FULL package.\n"
            "Would you like more details about props and themes?")
    elif any(word in user_input.lower() for word in
             ["family", "siblings", "parents", "children", "group", "whole family"]):
        response = ("Perfect! All our packages, except MINI, include family photos.\n"
                    "The FULL package is best for capturing all family members (up to 6 people).\n"
                    "Would you like to know more about family poses or special themes?")
    elif any(word in user_input.lower() for word in ["studio", "home", "outdoor", "in-studio", "at home", "location"]):
        if "home" in user_input.lower():
            response = (
                "The LIFESTYLE package is perfect for a home session without props, capturing natural, relaxed moments.\n"
                "Would you like more details about this simple and cozy home setup?")
        else:
            response = (
                "We offer in-studio and outdoor sessions. The STANDARD and FULL packages are ideal for these locations, with multiple prop setups.\n"
                "Would you like more details?")
    elif any(word in user_input.lower() for word in ["props", "accessories", "blankets", "baskets", "toys"]):
        response = (
            "For the STANDARD and FULL packages, we can include a variety of props such as blankets, baskets, and themed setups.\n"
            "Would you like to suggest any specific props or themes?")
    elif any(word in user_input.lower() for word in ["colors", "themes", "color scheme", "pastel", "bold", "neutral"]):
        response = ("Color schemes and themes help create a unique session.\n"
                    "Please tell me if you have any specific preferences, such as pastel tones, bold colors, or nature-inspired themes.")

    # Логика для обработки вопросов о бронировании
    elif any(
            word in user_input.lower() for word in ["book", "booking", "how to book", "schedule", "make an appointment",
                                                    "sign up", "reservation", "how to reserve", "arrange session"]):
        response = (
            "To book a photoshoot, you can simply contact us through our website's booking form or send an email.\n"
            "We recommend booking in advance to ensure availability. Would you like a link to our booking page?")
    elif any(
            word in user_input.lower() for word in ["best time", "when", "optimal time", "perfect time", "ideal time"]):
        response = (
            "The best time to book a newborn photoshoot is during your pregnancy, ideally in your second or third trimester.\n"
            "This allows us to schedule the session within the first two weeks after birth, when newborns are easier to photograph.")
    elif any(word in user_input.lower() for word in
             ["why book early", "why book in advance", "early booking", "book early benefits"]):
        response = ("Booking early ensures that you secure your preferred date, as spots fill up quickly.\n"
                    "Early booking also gives us time to discuss your preferences and plan special themes or props for your session.")

    else:
        response = "I'm sorry, I didn't quite catch that. Could you please clarify your preferences or questions?"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

