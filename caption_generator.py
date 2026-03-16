import random

captions = {
    "travel": [
        "Ek hi life hai... explore it fully 🌍✈️",
        "Lost in places that feel like home 🗺️",
        "Passport full, heart fuller ❤️"
    ],
    "adventure": [
        "Fear is temporary, memories are forever 🪂",
        "Living life one jump at a time 🔥",
        "Risk liya hai... regret nahi karenge 💪"
    ],
    "selflove": [
        "Be your own kind of beautiful ✨",
        "Confidence is the best outfit 💯",
        "Main character energy 🎬"
    ]
}

topic = input("Enter topic: ").lower()

if topic in captions:
    print(random.choice(captions[topic]))
else:
    print("More captions coming soon 🚀")
