import tkinter as tk

import guiDownloadLyrics as downloader
import guiCreateMarkov as markov
import guiGenerateLine as generate

from config import CHARTS, LYRIC_FONT, ImageFolder


class Mumbler(tk.Tk):
    """
    Class which inherits tkinter base class to accomodate potentially several
    frames
    """

    def __init__(self, *args, **kwargs):
        """
        Create Start Page and show it
        """
        # Call tkinter init function since this inherits it
        tk.Tk.__init__(self, *args, **kwargs)

        # Comment out to allow resizing window
        self.resizable(False, False)

        # Setup for button menu
        self.chosen_chart = tk.StringVar(self)
        self.chosen_chart.set(CHARTS[0][1])

        # Create container for window
        container = tk.Frame(self)
        container.grid(row=0, column=0)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create list of possible windows
        self.frames = {}

        # Initialize start page (currently only page)
        frame = StartPage(self, container)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0)
        self.show_frame(StartPage)



    def show_frame(self, container):
        """
        Function to show a new tkinter frame(window)
        """

        frame = self.frames[container]
        frame.tkraise()


class StartPage(tk.Frame):
    """
    Initial frame of Mumbler app, create more frame classes if you want more
    windows
    """

    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent, container)
        self.parent = parent
        self.winfo_toplevel().title("Mumbler")

        photo_singer = tk.PhotoImage(file=ImageFolder + "/singer.png")
        singer_label = tk.Label(self, image=photo_singer, width=102, height=128)
        singer_label.grid(row=len(CHARTS), column=0)
        singer_label.image = photo_singer

        photo_speech = tk.PhotoImage(file=ImageFolder + "/speechbubble.png")
        speech_label = tk.Label(self, image=photo_speech, width=300, height=200)
        speech_label.grid(row=0, column=1, rowspan=len(CHARTS), columnspan=2)
        speech_label.image = photo_speech

        self.label = tk.Label(
            self, text="Welcome to Mumbler!", font=LYRIC_FONT, anchor="nw",
            wraplength=250, height=5)
        self.label.grid(row=0, column=1, rowspan=len(CHARTS), 
            columnspan=2, padx=10, pady=20, sticky="n")

        ### Draw buttons/menu

        # Create radiobutton menu for selecting genre
        for (text, chart), i in zip(CHARTS, range(len(CHARTS))):
            b = tk.Radiobutton(self, text=text, variable=parent.chosen_chart,
                               value=chart, indicatoron=False)
            b.grid(row=i, column=0, sticky="nsew")

        """
        # Alternative to radiobuttons for dropdown menu
        menu = tk.OptionMenu(self, self.chosen_chart, *CHARTS)
        menu.grid(row=0, column=0)
        """

        # Create function buttons to run scripts
        downloadButton = tk.Button(
            self, text="Update Markov", command=self.updateMarkov)
        downloadButton.grid(row=len(CHARTS), column=1,
                            padx=2, pady=2, sticky="sew")

        generateButton = tk.Button(
            self, text="Generate Line!", command=self.generateLyric)
        generateButton.grid(row=len(CHARTS), column=2,
                            padx=2, pady=2, sticky="sew")

    def updateMarkov(self):
        """
        Function to run when Update Markov button is pressed.
        Downloads lyrics of chosen genre and updates markovify .json
        """
        self.label['text'] = "Updating " + str(self.parent.chosen_chart.get()) + \
        " chart. Please wait!"
        self.update()
        downloader.main(self.parent.chosen_chart.get())
        self.label['text'] = "Update complete!"
        self.update()

    def generateLyric(self):
        """
        Function to run when Generate button is pressed.
        Prints a single line from guiGenerateLine and prints it
        to console and on the GUI itself.
        """

        self.label['text'] = generate.main(self.parent.chosen_chart.get())
        self.update()

if __name__ == "__main__":
    app = Mumbler()
    app.mainloop()
