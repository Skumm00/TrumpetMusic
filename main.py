import json
import os
import logging
from difflib import get_close_matches

# Setup logging
logging.basicConfig(filename='music_converter.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Extended notechart with more names
notechart = {
    "B_4": 2,  # B in 4th octave
    "C_4": 0,  # C in 4th octave
    "C#_4": 123,
    "Db_4": 123,
    "D_4": 13,
    "D#_4": 23,
    "Eb_4": 2300,
    "F_4": 1,
    "F#_4": 200,
    "Gb_4": 20,
    "G_4": 0,
    "G#_4": 230,
    "Ab_4": 230,
    "A_4": 12,
    "A#_4": 1,
    "Bb_4": 10,
    "HighB_4": 2,
    "HighC_4": 0,
    "LowB_3": 2,  # B in 3rd octave
    "LowC_3": 0,
    "LowC#_3": 123,
    "LowDb_3": 123,
    "LowD_3": 13,
    "LowD#_3": 23,
    "LowEb_3": 2300,
    "LowF_3": 1,
    "LowF#_3": 200,
    "LowGb_3": 20,
    "LowG_3": 0,
    "LowG#_3": 230,
    "LowAb_3": 230,
    "LowA_3": 12,
    "LowA#_3": 1,
    "LowBb_3": 10,
    "MiddleB_4": 2,  # Middle B in 4th octave
    "MiddleC_4": 0
}

# Global variable to keep track of recent notes
recent_notes = []

def getnote(note, chart):
    # Fetches and prints the fingering for a given note.
    note = note.strip()
    if note in chart:
        fingering = chart[note]
        recent_notes.append(note)
        if len(recent_notes) > 5:
            recent_notes.pop(0)
        print(f"The fingering for {note} is {fingering}")
    else:
        # Fuzzy matching for similar note names
        similar_notes = get_close_matches(note, chart.keys())
        if similar_notes:
            print(f"Note not found. Did you mean: {', '.join(similar_notes)}?")
        else:
            print("This note is not in the chart. Please check the note name and try again.")
        logging.warning(f"Note not found: {note}")

def listnotes(chart):
    # Lists all notes and their corresponding fingerings.
    print("Available notes and their fingerings:")
    for note, fingering in chart.items():
        print(f"{note}: {fingering}")

def show_help():
    # Displays the help message.
    print("Trumpet Note Converter")
    print("You can enter note names to get the corresponding trumpet fingering.")
    print("Examples of valid notes include: C_4, D#_4, LowB_3, etc.")
    print("Type 'list' to see all available notes.")
    print("Type 'recent' to see recent notes.")
    print("Type 'save' to save your custom note chart.")
    print("Type 'load' to load a custom note chart.")
    print("Type 'note_range' to see the note range.")
    print("Type 'frequency' to calculate the frequency of a note.")
    print("Type 'profile' to manage user profiles.")
    print("Type 'help' to see this message again.")
    print("Type 'exit' to quit the program.")

def show_recent_notes():
    # Displays the recent notes entered by the user.
    if recent_notes:
        print("Recent notes:")
        for note in recent_notes:
            print(note)
    else:
        print("No recent notes.")

def save_chart(filename, chart):
    # Saves the current note chart to a file.
    with open(filename, 'w') as file:
        json.dump(chart, file)
    print(f"Note chart saved to {filename}")

def load_chart(filename):
    # Loads a note chart from a file.
    global notechart
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            notechart = json.load(file)
        print(f"Note chart loaded from {filename}")
    else:
        print("File not found.")
        logging.error(f"File not found: {filename}")

def note_range():
    # Calculates and displays the note range based on the note chart.
    notes = list(notechart.keys())
    if notes:
        min_note = min(notes, key=lambda note: notechart[note])
        max_note = max(notes, key=lambda note: notechart[note])
        print(f"Note range from {min_note} to {max_note}")
    else:
        print("Note chart is empty.")

def calculate_frequency(note):
    # Calculates and displays the frequency of a given note.
    # A simplified frequency calculation for demonstration purposes
    # Real-world calculations require more precise formulas and context
    base_freq = 440  # Frequency of A4
    # Simple formula assuming equal temperament scale and octave adjustments
    # Note: This is an approximation
    try:
        octave = int(note.split('_')[1])
        # Simple formula: base_freq * 2^((n - 49) / 12), where n is the note index in the scale
        note_index = list(notechart.keys()).index(note) % 12
        note_freq = base_freq * 2 ** ((octave - 4 + note_index) / 12)
        print(f"The frequency of {note} is approximately {note_freq:.2f} Hz")
    except ValueError:
        print("Invalid note format.")
        logging.error(f"Invalid note format: {note}")

def manage_profiles():
    # Manages user profiles for storing preferences.
    profiles_file = 'profiles.json'
    if os.path.exists(profiles_file):
        with open(profiles_file, 'r') as file:
            profiles = json.load(file)
    else:
        profiles = {}

    print("Profile Management:")
    action = input("Type 'create' to create a new profile or 'list' to list existing profiles: ").strip().lower()

    if action == 'create':
        profile_name = input("Enter the profile name: ").strip()
        profiles[profile_name] = notechart
        with open(profiles_file, 'w') as file:
            json.dump(profiles, file)
        print(f"Profile '{profile_name}' created.")
    elif action == 'list':
        print("Existing profiles:")
        for profile in profiles.keys():
            print(profile)
    else:
        print("Invalid action.")
        logging.warning(f"Invalid action in profile management: {action}")

def main():
    # Main function to run the note converter.
    show_help()
    while True:
        note = input("Enter a note (or type 'help' for assistance): ").strip()
        if note.lower() == "exit":
            print("Exiting the program. Have a great day!")
            break
        elif note.lower() == "list":
            listnotes(notechart)
        elif note.lower() == "recent":
            show_recent_notes()
        elif note.lower() == "save":
            filename = input("Enter the filename to save the note chart: ").strip()
            save_chart(filename, notechart)
        elif note.lower() == "load":
            filename = input("Enter the filename to load the note chart: ").strip()
            load_chart(filename)
        elif note.lower() == "note_range":
            note_range()
        elif note.lower() == "frequency":
            note_name = input("Enter the note name to calculate the frequency: ").strip()
            calculate_frequency(note_name)
        elif note.lower() == "profile":
            manage_profiles()
        elif note.lower() == "help":
            show_help()
        else:
            getnote(note, notechart)

if __name__ == "__main__":
    main()
