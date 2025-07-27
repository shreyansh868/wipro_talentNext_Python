"""Your friend has sent you a text file containing n lines. He sent a secret message with it, 
which tells you the place and time where you have to go and meet him.
He challenges you to find it out without seeing the content of the file. He has given hints to find it. 
Let's surprise him by breaking the challenge with our python code."""

#Code

from collections import Counter
import os

sample_content = """Meet me at Park tomorrow
Let's have a walk in Park
Park is calm and quiet
Don't forget to bring snacks
Arrive at the Park before noon
See you soon at the Park
Bring some water to the Park
Stay safe and be on time
Park has beautiful trees
Don't be late to the Park
"""

filename = "secret.txt"

with open(filename, 'w') as f:
    f.write(sample_content)

def find_secret_message(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    line_count = len(lines)
    hour = line_count % 12
    if hour == 0:
        hour = 12
    time_period = "AM" if line_count <= 12 else "PM"
    meeting_time = f"{hour} {time_period}"

    words = []
    for line in lines:
        words.extend(line.strip().split())

    word_counts = Counter(words)
    most_common_word, _ = word_counts.most_common(1)[0]
    meeting_place = f"{most_common_word} Street"

    # Print final output
    print("\n📍 Secret Meeting Details")
    print("Meeting Time  :", meeting_time)
    print("Meeting Place :", meeting_place)

# Step 3: Run the function
if os.path.exists(filename):
    find_secret_message(filename)
else:
    print("❌ secret.txt not found.")
