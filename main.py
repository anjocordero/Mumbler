import tkinter as tk

import guiDownloadLyrics as downloader
import guiCreateMarkov as markov
import guiGenerateLine as generate

# LARGE_FONT = ("Verdana", 12)


class Mumbler(tk.Tk):
    """
    Class which inherits tkinter base class to accomodate several potential frames
    """

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

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

        frame = self.frames[controller]
        frame.tkraise()


class StartPage(tk.Frame):
    """
    Initial frame of Mumbler app, create more frame classes if you want more windows
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, controller)
        self.winfo_toplevel().title("Mumbler")

        # label = tk.Label(self, text="Mumbler", font=LARGE_FONT)
        # label.grid(row=0, column=0)#.pack()


def main():

    app = Mumbler()

    CHARTS = [
        # (Text to appear on button, billboard.com url)
        ("Hot 100", "hot100"),
        ("Pop", "pop"),
        ("Rock", "rock"),
        ("Latin", "latin"),
        ("Hip-hop", "hiphop"),
        ("Alternative", "alternative"),
        ("EDM", "edm")
    ]

    chosen_chart = tk.StringVar(app)
    # default to pop because hot100 functionality is currently out of date
    chosen_chart.set("pop")

    # Create radiobutton menu for selecting genre
    for (text, chart), i in zip(CHARTS, range(len(CHARTS))):
        b = tk.Radiobutton(app, text=text, variable=chosen_chart,
                           value=chart, indicatoron=True)
        b.grid(row=i, column=0, sticky="w")

    # menu = tk.OptionMenu(app, chosen_chart, *CHARTS)
    # menu.grid(row=0, column=0)

    downloadButton = tk.Button(
        app, text="Download", command=lambda: downloader.main(chosen_chart.get()))
    downloadButton.grid(row=len(CHARTS), column=1, padx=2, pady=2, sticky="ew")

    markovButton = tk.Button(app, text="Create Markov",
                             command=lambda: markov.main(chosen_chart.get()))
    markovButton.grid(row=len(CHARTS), column=2, pady=2)

    generateButton = tk.Button(
        app, text="Generate!", command=lambda: generate.main(chosen_chart.get()))
    generateButton.grid(row=len(CHARTS), column=3, padx=2, pady=2)

    app.mainloop()


if __name__ == "__main__":
    main()