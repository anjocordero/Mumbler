import tkinter as tk

import guiDownloadLyrics as downloader
import guiCreateMarkov as markov
import guiGenerateLine as generate

#LARGE_FONT = ("Verdana", 12)


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

        frame.grid(row=0, column=0)

        self.show_frame(StartPage)

    def show_frame(self, controller):

        frame = self.frames[controller]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, controller)
        self.winfo_toplevel().title("Mumbler")

        #label = tk.Label(self, text="Mumbler", font=LARGE_FONT)
        # label.grid(row=0, column=0)#.pack()


def main():

    app = Mumbler()

    CHARTS = [
        ("Hot 100", "hot100"),
        ("Pop", "pop"),
        ("Rock", "rock"),
        ("Latin", "latin"),
        ("Hip-hop", "hiphop"),
        ("Alternative", "alternative"),
        ("EDM", "edm")
    ]

    chosen_chart = tk.StringVar(app)
    chosen_chart.set("pop") # not CHARTS[0] because hot100 functionality is out of date

    i = 0

    for text, chart in CHARTS:
        b = tk.Radiobutton(app, text=text, variable=chosen_chart, value=chart, indicatoron=True)
        b.grid(row=i, column=0, sticky="w")
        i += 1

    # menu = tk.OptionMenu(app, chosen_chart, *CHARTS)
    # menu.grid(row=0, column=0)

    downloadButton = tk.Button(app, text="Download", command=lambda: downloader.main(chosen_chart.get()))
    downloadButton.grid(row=len(CHARTS), column=1, padx=2, pady=2, sticky="ew")

    markovButton = tk.Button(app, text="Create Markov", command=lambda: markov.main(chosen_chart.get()))
    markovButton.grid(row=len(CHARTS), column=2, pady=2)

    generateButton = tk.Button(app, text="Generate!", command=lambda: generate.main(chosen_chart.get()))
    generateButton.grid(row=len(CHARTS), column=3, padx=2, pady=2)

    app.mainloop()


if __name__ == "__main__":
    main()