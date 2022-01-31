def __init__(self, master, gui):
        super().__init__(master, text="output: Tremolo")
        self.gui = gui
        self.input_waveform = tk.StringVar()
        self.input_waveform.set("<off>")
        self.input_rate = tk.DoubleVar()
        self.input_depth = tk.DoubleVar()
        self.input_rate.set(5)
        self.input_depth.set(80)
        row = 0
        tk.Label(self, text="waveform").grid(row=row, column=0)
        values = ["<off>", "sine", "triangle", "sawtooth", "square"]
        menu = tk.OptionMenu(self, self.input_waveform, *values)
        menu["width"] = 10
        menu.grid(row=row, column=1)
        row += 1
        tk.Label(self, text="rate").grid(row=row, column=0, sticky=tk.E)
        tk.Scale(self, orient=tk.HORIZONTAL, variable=self.input_rate, from_=0.0, to=10.0, resolution=.1,
                 width=10, length=100).grid(row=row, column=1)
        row += 1
        tk.Label(self, text="depth").grid(row=row, column=0, sticky=tk.E)
        tk.Scale(self, orient=tk.HORIZONTAL, variable=self.input_depth, from_=0.0, to=1.0, resolution=.02,
                 width=10, length=100).grid(row=row, column=1) 