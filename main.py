import tkinter as tk

import guiDownloadLyrics as downloader
import guiCreateMarkov as markov
import guiGenerateLine as generate

from config import CHARTS, LYRIC_FONT


class Mumbler(tk.Tk):
    """
    Class which inherits tkinter base class to accomodate potentially several frames
    """

    chosen_chart = []
    label = []

    def __init__(self, *args, **kwargs):
        """
        Create Start Page and show it
        """

        tk.Tk.__init__(self, *args, **kwargs)

        self.chosen_chart = tk.StringVar(self)
        self.chosen_chart.set(CHARTS[0][1])

        container = tk.Frame(self)

        # container.pack(side="top", fill="both", expand=True)
        container.grid(row=0, column=0)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(self, container)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0)
        self.show_frame(StartPage)

    def show_frame(self, controller):
        """
        Function to show a new tkinter frame(window)
        """

        frame = self.frames[controller]
        frame.tkraise()

    def updateMarkov(self):
        """
        Function to run when Update Markov button is pressed.
        Downloads lyrics of chosen genre and updates markovify .json
        """
        downloader.main(self.chosen_chart.get())

    def generateLyric(self):
        """
        Function to run when Generate button is pressed.
        Prints a single line from guiGenerateLine and prints it
        to console and on the GUI itself.
        """

        lyric = generate.main(self.chosen_chart.get())
        self.label['text'] = lyric

    def draw(self):
        """
        Main function of Mumbler, draws menu buttons and pictures
        """

        # Create radiobutton menu for selecting genre
        for (text, chart), i in zip(CHARTS, range(len(CHARTS))):
            b = tk.Radiobutton(self, text=text, variable=self.chosen_chart,
                               value=chart, indicatoron=False)
            b.grid(row=i, column=0, sticky="nsew")

        # Alternative to radiobuttons for dropdown menu
        # menu = tk.OptionMenu(self, self.chosen_chart, *CHARTS)
        # menu.grid(row=0, column=0)

        # Create function buttons to run scripts
        downloadButton = tk.Button(
            self, text="Update Markov", command=self.updateMarkov)
        downloadButton.grid(row=len(CHARTS), column=1,
                            padx=2, pady=2, sticky="sew")

        generateButton = tk.Button(
            self, text="Generate!", command=self.generateLyric)
        generateButton.grid(row=len(CHARTS), column=2,
                            padx=2, pady=2, sticky="sew")

        self.mainloop()


class StartPage(tk.Frame):
    """
    Initial frame of Mumbler app, create more frame classes if you want more windows
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, controller)
        self.winfo_toplevel().title("Mumbler")

        photo_singer = tk.PhotoImage(file="singer.png")
        singer_label = tk.Label(image=photo_singer)
        singer_label.grid(row=len(CHARTS), column=0)
        singer_label.image = photo_singer

        photo_speech = tk.PhotoImage(file="speechbubble.png")
        speech_label = tk.Label(image=photo_speech)
        speech_label.grid(row=0, column=1, rowspan=len(CHARTS), columnspan=2)
        speech_label.image = photo_speech

        parent.label = tk.Label(
            parent, text="", font=LYRIC_FONT, anchor="nw", wraplength="250")
        parent.label.grid(row=0, column=1, rowspan=len(CHARTS) -
                        1, columnspan=2, padx=10, pady=18, sticky="n")


if __name__ == "__main__":
    app = Mumbler()
    app.draw()
