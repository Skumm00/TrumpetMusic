#Music Converter that converts note names to the fingerings used on a trumpet
#Useful for not knowing what a note name is 

#the notechart

notechart = {
  "B",2,
  "C",0,
  "C#",123,
  "Db",123,
  "D",13,
  "D#",23,
  "Eb",2300,
  "F",1,
  "F#",200,
  "Gb",20,
  "G",0,
  "G#",230,
  "Ab",230,
  "A",12,
  "A#",1,
  "Bb",10,
  "HighB",2,
  "HighC",0,
  
}

print(notechart[1])
def getnote(note,chart):
  print("Here!")
  if note in chart:
    print(chart[note])
  else:
    print("This note is not in the chart")
def main():
  while True:
    note = input("Enter a note: ")
    if note == "exit":
      break
    getnote(note,notechart)

main()