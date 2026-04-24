#!/usr/bin/env python3
"""Instagram Caption Generator — a CLI tool for generating engaging captions."""

import random
import sys

# ---------------------------------------------------------------------------
# Caption Data Store
# ---------------------------------------------------------------------------
# Each topic maps to a dict of moods, each mood holding a list of captions.
# Captions use a mix of English and Hinglish for high engagement.

CAPTIONS = {
    "travel": {
        "motivational": [
            "Ek hi life hai... explore it fully 🌍✈️",
            "The world is a book, and those who don't travel read only one page 📖",
            "Duniya dekho, khud ko samjho 🌏",
            "Collect moments, not things 🗺️",
            "Zindagi mein ek baar toh yeh jagah dekhni chahiye 🏔️",
        ],
        "funny": [
            "I need 6 months of vacation, twice a year 🏖️😂",
            "Calories don't count when you're on vacation 🍕✈️",
            "Paisa aata hai jaata hai, travel memories forever rehti hain 😜",
            "My wallet is crying but my soul is happy 💸😅",
            "Out of office. Out of budget. Out of my mind 🤪",
        ],
        "aesthetic": [
            "Lost in places that feel like home 🗺️",
            "Passport full, heart fuller ❤️",
            "Wandering where the WiFi is weak 🌿",
            "Sunsets and silhouettes ✨",
            "Between the pages of a map 🌅",
        ],
    },
    "adventure": {
        "motivational": [
            "Fear is temporary, memories are forever 🪂",
            "Risk liya hai... regret nahi karenge 💪",
            "Life begins at the end of your comfort zone 🔥",
            "Push your limits, surprise yourself 🚀",
            "Darr ke aage jeet hai 🏆",
        ],
        "funny": [
            "I don't need therapy, I need adventure 🧗😂",
            "My survival skills: Google Maps and snacks 🗺️🍫",
            "Adventure is just bad planning with a good attitude 😜",
            "Bungee jumping kiya, ab EMI bhi jump kar rahi hai 💸😅",
            "Went outside once. Graphics were amazing 🌄😂",
        ],
        "aesthetic": [
            "Living life one jump at a time 🔥",
            "Wild heart, free soul 🦅",
            "Chasing horizons 🌄",
            "Into the wild unknown 🌲",
            "Altitude over attitude 🏔️",
        ],
    },
    "selflove": {
        "motivational": [
            "Be your own kind of beautiful ✨",
            "Confidence is the best outfit 💯",
            "You are enough, always have been 💖",
            "Apni value khud pehchano, duniya baad mein pehchanegi 🌟",
            "Self-love is not selfish, it's necessary 🫶",
        ],
        "funny": [
            "Main character energy 🎬",
            "I'm not lazy, I'm on energy-saving mode 😴😂",
            "Mirror says: 'Aaj toh mast lag rahe ho' 🪞😎",
            "Too glam to give a damn 💅",
            "I don't need your approval, I have mine 😏",
        ],
        "aesthetic": [
            "Bloom where you are planted 🌸",
            "Soft heart, strong mind 🤍",
            "Healing is not linear, but it's beautiful 🌿",
            "Glow different ✨",
            "Becoming the person I needed 🦋",
        ],
    },
    "fitness": {
        "motivational": [
            "No pain, no gain — simple hai 💪🔥",
            "Your body can stand almost anything. Train your mind 🧠",
            "Excuses don't burn calories 🏋️",
            "Aaj ka workout, kal ka confidence 💯",
            "Stronger than yesterday, weaker than tomorrow 📈",
        ],
        "funny": [
            "I work out because I really like food 🍔😂",
            "Gym jaana hai but bed bhi toh pyaara hai 🛏️😴",
            "Leg day? More like can't-walk-tomorrow day 🦵😅",
            "Running late counts as cardio, right? 🏃💨",
            "Protein shake tastes like regret and ambition 🥤😜",
        ],
        "aesthetic": [
            "Sweat is just fat crying 💧",
            "Iron therapy 🏋️",
            "Built, not bought 🔨",
            "Discipline over motivation 🖤",
            "Grind in silence, let results make the noise 🤫",
        ],
    },
    "food": {
        "motivational": [
            "Good food = Good mood 🍽️✨",
            "Life is too short for bad food 🍕",
            "Cooking is love made visible ❤️‍🔥",
            "Khaana khao, khush raho 😋",
            "Every meal is a chance to nourish yourself 🥗",
        ],
        "funny": [
            "I'm on a seafood diet — I see food, I eat it 🦐😂",
            "Diet starts Monday... every Monday 📅😜",
            "Biryani fixes everything 🍚🤤",
            "My relationship with food is the only stable one 💀😅",
            "Calories? I don't know her 🍩😏",
        ],
        "aesthetic": [
            "Eat well, travel often 🌮✈️",
            "A table full of love 🕯️🍷",
            "Flavours that tell stories 🍜",
            "Simple ingredients, soulful food 🫕",
            "Plated with love 🍽️🤍",
        ],
    },
    "fashion": {
        "motivational": [
            "Dress how you want to be addressed 👔✨",
            "Style is a way to say who you are without speaking 🗣️",
            "Fashion fades, style is eternal — YSL 💎",
            "Apna style, apni pehchaan 🔥",
            "Wear confidence, it never goes out of style 💯",
        ],
        "funny": [
            "Life isn't perfect but your outfit can be 👗😂",
            "Shopping is my cardio 🛍️🏃",
            "I dress up even for grocery runs 🛒💅",
            "Outfit repeat? I don't know what that means 😜",
            "Kapde kam pad gaye, budget nahi 💸😅",
        ],
        "aesthetic": [
            "Elegance is an attitude 🖤",
            "Less is more 🤍",
            "Monochrome mood 🖤🤍",
            "Details make the difference ✨",
            "Styled by mood 🌙",
        ],
    },
    "nature": {
        "motivational": [
            "In every walk with nature, one receives far more than they seek 🌿",
            "Nature does not hurry, yet everything is accomplished 🍃",
            "Prakriti se seekho — patience aur beauty dono milegi 🌻",
            "Look deep into nature, and you will understand everything 🌊",
            "The earth has music for those who listen 🎶🌍",
        ],
        "funny": [
            "I'm an outdoor person — I like outdoor dining 🍽️😂",
            "Nature called, I didn't pick up... then it texted 📱🌲",
            "Went for a hike, came back a different person (a tired one) 🥾😅",
            "Trees are the best — they never judge 🌳😜",
            "Vitamin N: Nature 🏞️💚",
        ],
        "aesthetic": [
            "Earth tones and golden hours 🌾",
            "Where flowers bloom, so does hope 🌸",
            "Breathing in the wild 🌬️🌲",
            "Rooted in nature 🌿",
            "Sky above, earth below, peace within 🌅",
        ],
    },
    "love": {
        "motivational": [
            "Love is not finding someone to live with, it's finding someone you can't live without 💕",
            "Pyaar mein logic mat lagao, bas feel karo ❤️",
            "The best thing to hold onto in life is each other 🤝",
            "Love deeply, live fully 💖",
            "Two hearts, one beautiful journey 🛤️❤️",
        ],
        "funny": [
            "We go together like biryani and raita 🍚😂",
            "Love is sharing your food... and that's a big deal 🍕❤️",
            "Relationship status: committed to WiFi 📶😜",
            "You're the cheese to my pizza 🧀🍕",
            "Tum meri wali ho... EMI mein 💸😅",
        ],
        "aesthetic": [
            "Written in the stars ✨💫",
            "Tangled up in you 🤍",
            "Quiet love, loud hearts 🫀",
            "Forever starts now 🌙",
            "You are my favourite notification 📱💕",
        ],
    },
}

# ---------------------------------------------------------------------------
# Hashtag Data Store
# ---------------------------------------------------------------------------

HASHTAGS = {
    "travel": [
        "#travel", "#wanderlust", "#travelgram", "#instatravel", "#explore",
        "#travelphotography", "#adventure", "#traveltheworld", "#vacation",
        "#globetrotter", "#travelblogger", "#roamtheplanet",
    ],
    "adventure": [
        "#adventure", "#adventuretime", "#outdoors", "#explore", "#adrenaline",
        "#thrillseeker", "#adventurelife", "#extremesports", "#getoutside",
        "#liveadventurously", "#neverstopexploring", "#wildandfree",
    ],
    "selflove": [
        "#selflove", "#selfcare", "#loveyourself", "#positivevibes", "#confidence",
        "#mentalhealth", "#glowup", "#beyourself", "#innerpeace",
        "#selfworth", "#mindfulness", "#healingjourney",
    ],
    "fitness": [
        "#fitness", "#gym", "#workout", "#fitnessmotivation", "#fit",
        "#bodybuilding", "#training", "#health", "#fitfam",
        "#gymlife", "#exercise", "#strongnotskinny",
    ],
    "food": [
        "#food", "#foodie", "#foodporn", "#instafood", "#yummy",
        "#foodphotography", "#delicious", "#homemade", "#foodlover",
        "#foodstagram", "#cooking", "#tasty",
    ],
    "fashion": [
        "#fashion", "#style", "#ootd", "#fashionblogger", "#instafashion",
        "#streetstyle", "#fashionista", "#outfitoftheday", "#lookbook",
        "#fashionstyle", "#trendy", "#whatiwore",
    ],
    "nature": [
        "#nature", "#naturephotography", "#landscape", "#naturelovers",
        "#outdoors", "#earth", "#wildlife", "#sunset", "#mountains",
        "#forest", "#green", "#mothernature",
    ],
    "love": [
        "#love", "#couplegoals", "#relationship", "#romance", "#lovestory",
        "#together", "#soulmate", "#forever", "#instalove",
        "#lovequotes", "#truelove", "#hearttoheart",
    ],
}

# ---------------------------------------------------------------------------
# Core Functions
# ---------------------------------------------------------------------------

def get_available_topics() -> list[str]:
    """Return a sorted list of all available caption topics."""
    return sorted(CAPTIONS.keys())


def get_available_moods(topic: str) -> list[str]:
    """Return a sorted list of moods available for a given topic."""
    topic = topic.lower().strip()
    if topic not in CAPTIONS:
        return []
    return sorted(CAPTIONS[topic].keys())


def generate_caption(topic: str, mood: str | None = None) -> str:
    """Generate a single random caption for the given topic and optional mood.

    Args:
        topic: The caption topic (e.g. 'travel', 'fitness').
        mood:  Optional mood filter (e.g. 'funny', 'motivational', 'aesthetic').
               If None, picks from all moods for that topic.

    Returns:
        A caption string.

    Raises:
        ValueError: If the topic (or mood) is not found.
    """
    topic = topic.lower().strip()
    if topic not in CAPTIONS:
        raise ValueError(
            f"Topic '{topic}' not found. Available topics: {', '.join(get_available_topics())}"
        )

    if mood is not None:
        mood = mood.lower().strip()
        if mood not in CAPTIONS[topic]:
            raise ValueError(
                f"Mood '{mood}' not found for topic '{topic}'. "
                f"Available moods: {', '.join(get_available_moods(topic))}"
            )
        pool = CAPTIONS[topic][mood]
    else:
        # Combine all moods
        pool = [cap for mood_caps in CAPTIONS[topic].values() for cap in mood_caps]

    return random.choice(pool)


def generate_captions(topic: str, mood: str | None = None, count: int = 3) -> list[str]:
    """Generate multiple unique captions (up to available pool size).

    Args:
        topic: The caption topic.
        mood:  Optional mood filter.
        count: Number of captions to return.

    Returns:
        A list of caption strings.
    """
    topic = topic.lower().strip()
    if topic not in CAPTIONS:
        raise ValueError(
            f"Topic '{topic}' not found. Available topics: {', '.join(get_available_topics())}"
        )

    if mood is not None:
        mood = mood.lower().strip()
        if mood not in CAPTIONS[topic]:
            raise ValueError(
                f"Mood '{mood}' not found for topic '{topic}'. "
                f"Available moods: {', '.join(get_available_moods(topic))}"
            )
        pool = list(CAPTIONS[topic][mood])
    else:
        pool = [cap for mood_caps in CAPTIONS[topic].values() for cap in mood_caps]

    count = min(count, len(pool))
    return random.sample(pool, count)


def generate_hashtags(topic: str, count: int = 5) -> list[str]:
    """Return a random selection of hashtags for the given topic.

    Args:
        topic: The caption topic.
        count: Number of hashtags to return.

    Returns:
        A list of hashtag strings.
    """
    topic = topic.lower().strip()
    if topic not in HASHTAGS:
        return []
    pool = HASHTAGS[topic]
    count = min(count, len(pool))
    return random.sample(pool, count)


def format_post(caption: str, hashtags: list[str]) -> str:
    """Combine a caption and hashtags into a ready-to-copy Instagram post."""
    return f"{caption}\n\n{'  '.join(hashtags)}"


# ---------------------------------------------------------------------------
# Interactive CLI
# ---------------------------------------------------------------------------

def _print_menu(items: list[str], label: str) -> None:
    """Pretty-print a numbered menu."""
    print(f"\n📋  Available {label}:")
    for i, item in enumerate(items, 1):
        print(f"   {i}. {item}")


def cli() -> None:
    """Run the interactive command-line interface."""
    print("=" * 50)
    print("  ✨  Instagram Caption Generator  ✨")
    print("=" * 50)

    # --- Topic selection ---
    topics = get_available_topics()
    _print_menu(topics, "Topics")
    topic_input = input("\nEnter a topic name or number: ").strip()

    # Allow selection by number
    if topic_input.isdigit():
        idx = int(topic_input) - 1
        if 0 <= idx < len(topics):
            topic = topics[idx]
        else:
            print("❌  Invalid number. Exiting.")
            sys.exit(1)
    else:
        topic = topic_input.lower()

    if topic not in CAPTIONS:
        print(f"❌  Topic '{topic}' not found. More topics coming soon 🚀")
        sys.exit(1)

    # --- Mood selection ---
    moods = get_available_moods(topic)
    _print_menu(moods, "Moods")
    print(f"   {len(moods) + 1}. all (mix of everything)")
    mood_input = input("\nEnter a mood name or number (or press Enter for all): ").strip()

    mood = None
    if mood_input:
        if mood_input.isdigit():
            idx = int(mood_input) - 1
            if 0 <= idx < len(moods):
                mood = moods[idx]
            # else keep mood = None (all)
        else:
            mood = mood_input.lower() if mood_input.lower() in moods else None

    # --- Count selection ---
    count_input = input("\nHow many captions? (default 3): ").strip()
    count = int(count_input) if count_input.isdigit() and int(count_input) > 0 else 3

    # --- Generate ---
    try:
        captions = generate_captions(topic, mood=mood, count=count)
    except ValueError as e:
        print(f"❌  {e}")
        sys.exit(1)

    hashtags = generate_hashtags(topic, count=5)

    print("\n" + "=" * 50)
    print(f"  📝  Captions for #{topic}" + (f" ({mood})" if mood else ""))
    print("=" * 50)
    for i, cap in enumerate(captions, 1):
        print(f"\n  {i}. {cap}")

    if hashtags:
        print(f"\n  🏷️  Suggested Hashtags:\n  {'  '.join(hashtags)}")

    # --- Ready-to-copy post ---
    print("\n" + "-" * 50)
    print("  📋  Ready-to-copy post (caption #1 + hashtags):")
    print("-" * 50)
    print(f"\n{format_post(captions[0], hashtags)}\n")


if __name__ == "__main__":
    cli()
