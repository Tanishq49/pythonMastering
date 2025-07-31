from deep_translator import GoogleTranslator
import requests

# Step 1: Translate Hindi → English
hindi_word = input("Enter a Hindi word: ")
english_word = GoogleTranslator(source='hi', target='en').translate(hindi_word)

print(f"\n🔁 Translated: {hindi_word} → {english_word}")

# Step 2: Get English definition
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{english_word}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"\n📚 Definitions for '{english_word}':")
    for meaning in data[0]['meanings']:
        part_of_speech = meaning['partOfSpeech']
        for definition in meaning['definitions']:
            print(f"\n→ ({part_of_speech}) {definition['definition']}")
            if 'example' in definition:
                print(f"   Example: {definition['example']}")
else:
    print("❌ No definition found.")
