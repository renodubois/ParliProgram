from tkinter import *
from tkinter import ttk

'''
    populateMembersList:
    Desc: Opens a file dialog to find a text file, then uses the contents of the
    file to put members in the members list.
    Returns: listvariable containing the names of the members from the text file
    Error handling: will give error message and abort if the file is corrupt
'''
def populateMembersList(*args):
    pass

'''
    addToSpeakersList:
    Desc: Takes a member from the list box, removes it from there, and adds it
    to the speaker's listbox.
    Returns: none
'''
def addToSpeakersList(*args):
    pass

'''
    removeFromSpeakersList:
    Desc: Removes a member from the speaker's listbox, and adds them back to the
    members listbox.
    Returns: none
'''
def removeFromSpeakersList(*args):
    pass

# Initilize the Tk framework, give our window a name
root = Tk()
root.title("ParliProgram")
# Make our mainframe for the window:
mainframe = ttk.Frame(root)
mainframe.grid(column = 0, row = 0, sticky = (N, S, E, W))
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)
# Some test values, so the list can be debugged w/o the file opening being
# implemented just yet. TODO: Remove when deploying
testValues = ('Reno', 'John', 'Dan', 'Brian', 'Kelly', 'Hunter', 'Mario', 'Zargham')
stringTestValues = StringVar(value = testValues)

# Listbox of current members at the meeting, empty by default
memberList = Listbox(mainframe, listvariable = stringTestValues, height = 5)
# Listbox for the speaker's list, empty by default
currentSpeakers = StringVar()
speakersList = Listbox(mainframe, listvariable = currentSpeakers, height = 5)
# Button to open up a list of members. Currently will accept only .txt files
openFile = ttk.Button(mainframe, text = 'Load members', command = populateMembersList)
# Arrow button to take from members list to speaker's list.
addToSpeaker = ttk.Button(mainframe, text = '->', command = addToSpeakersList)
# Arrow button to take from speaker's list to members list.
removeFromSpeaker = ttk.Button(mainframe, text = '<-', command = removeFromSpeakersList)
# Grid the above widgets
memberList.grid(column = 0, row = 0, rowspan = 6, sticky = (N, S, E, W))
speakersList.grid(column = 6, row = 0, rowspan = 6, sticky = (N, S, E, W))
openFile.grid(column = 10, row = 1)
addToSpeaker.grid(column = 5, row = 1)
removeFromSpeaker.grid(column = 5, row = 3)
# Start the window loop
root.mainloop()
