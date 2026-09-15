from ai import call_gpt

def main():
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")

    print("Creating your haiku...")

    prompt = f"""
    Write a haiku about {topic} that includes the name {name}.
    The haiku must have exactly three lines:
    - First line: 5 syllables
    - Second line: 7 syllables
    - Third line: 5 syllables

    Return only the three lines of the haiku.
    """

    haiku = call_gpt(prompt)
    print(haiku)

if __name__ == "__main__":
    main()