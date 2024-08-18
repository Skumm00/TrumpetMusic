import json
import os

# Extended notechart with more namess
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
    """Fetches and prints the fingering for a given note."""
    if note in chart:
        fingering = chart[note]
        recent_notes.append(note)  # Track the recent note
        if len(recent_notes) > 5:
            recent_notes.pop(0)  # Keep only the last 5 notes
        print(f"The fingering for {note} is {fingering}")
    else:
        print("This note is not in the chart. Please check the note name and try again.")

def listnotes(chart):
    """Lists all notes and their corresponding fingerings."""
    print("Available notes and their fingerings:")
    for note, fingering in chart.items():
        print(f"{note}: {fingering}")

def show_help():
    """Displays the help message."""
    print("Trumpet Note Converter")
    print("You can enter note names to get the corresponding trumpet fingering.")
    print("Examples of valid notes include: C_4, D#_4, LowB_3, etc.")
    print("Type 'list' to see all available notes.")
    print("Type 'recent' to see recent notes.")
    print("Type 'save' to save your custom note chart.")
    print("Type 'load' to load a custom note chart.")
    print("Type 'help' to see this message again.")
    print("Type 'exit' to quit the program.")

def show_recent_notes():
    """Displays the recent notes entered by the user."""
    if recent_notes:
        print("Recent notes:")
        for note in recent_notes:
            print(note)
    else:
        print("No recent notes.")

def save_chart(filename, chart):
    """Saves the current note chart to a file."""
    with open(filename, 'w') as file:
        json.dump(chart, file)
    print(f"Note chart saved to {filename}")

def load_chart(filename):
    """Loads a note chart from a file."""
    global notechart
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            notechart = json.load(file)
        print(f"Note chart loaded from {filename}")
    else:
        print("File not found.")

def note_range():
    """Calculates and displays the note range based on the note chart."""
    notes = list(notechart.keys())
    if notes:
        min_note = min(notes, key=lambda note: notechart[note])
        max_note = max(notes, key=lambda note: notechart[note])
        print(f"Note range from {min_note} to {max_note}")
    else:
        print("Note chart is empty.")

def main():
    """Main function to run the note converter."""
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
        elif note.lower() == "help":
            show_help()
        else:
            getnote(note, notechart)

if __name__ == "__main__":
    main()
