# Extended notechart with more specific names
notechart = {
    "B_4": 2,  #B in 4th ocatvave
    "C_4": 0,  #C In 4th octave
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
    "LowB_3": 2,  #B in third octave
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
    "MiddleB_4": 2,  #Middle B in 4th octave
    "MiddleC_4": 0
}

def getnote(note, chart):
    #Fetches and prints the fingering for a given note
    if note in chart:
        print(f"The fingering for {note} is {chart[note]}")
    else:
        print("This note is not in the chart. Please check the note name and try again.")

def listnotes(chart):
    #Lists all notes and their corresponding fingerings
    print("Available notes and their fingerings:")
    for note, fingering in chart.items():
        print(f"{note}: {fingering}")

def show_help():
    """Displays the help message."""
    print("Trumpet Note Converter")
    print("You can enter note names to get the corresponding trumpet fingering.")
    print("Examples of valid notes include: C_4, D#_4, LowB_3, etc.")
    print("Type 'list' to see all available notes.")
    print("Type 'help' to see this message again.")
    print("Type 'exit' to quit the program.")

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
        elif note.lower() == "help":
            show_help()
        else:
            getnote(note, notechart)

if __name__ == "__main__":
    main()
