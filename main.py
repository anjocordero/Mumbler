import tkinter as tk

import guiDownloadLyrics as downloader
import guiCreateMarkov as markov
import guiGenerateLine as generate

LARGE_FONT = ("Verdana", 12)


class Mumbler(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)

        #container.pack(side="top", fill="both", expand=True)
        container.grid(row=0, column=0)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(self, container)

        self.frames[StartPage] = frame

        # frame.pack()
        frame.grid(row=0, column=0)

        self.show_frame(StartPage)

    def show_frame(self, controller):

        frame = self.frames[controller]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, controller)

        #label = tk.Label(self, text="Mumbler", font=LARGE_FONT)
        # label.grid(row=0, column=0)#.pack()


def main():

    app = Mumbler()

    CHARTS = [
        "hot100",
        "pop",
        "rock",
        "latin",
        "hiphop",
        "alternative",
        "edm"
    ]

    chosen_chart = tk.StringVar(app)
    chosen_chart.set(CHARTS[1]) # not CHARTS[0] because hot100 functionality is out of date

    menu = tk.OptionMenu(app, chosen_chart, *CHARTS)
    menu.grid(row=0, column=0)

    downloadButton = tk.Button(app, text="Download", command=lambda: downloader.main(chosen_chart.get()))
    downloadButton.grid(row=2, column=0)

    markovButton = tk.Button(app, text="Create Markov", command=lambda: markov.main(chosen_chart.get()))
    markovButton.grid(row=2, column=1)

    generateButton = tk.Button(app, text="Generate!", command=lambda: generate.main(chosen_chart.get()))
    generateButton.grid(row=2, column=2)

    app.mainloop()


if __name__ == "__main__":
    main()