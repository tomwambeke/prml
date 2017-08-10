import tkinter as tk
from sine import Sine
from display import Display
from message import Message

class App(object):
    """ The regression application.

    The application accepts input from the command line and visualizes
    results in a display window.

    noise   E   -- set standard deviation representing measurement noise.
    spacing O   -- select spacing option (regular/random)
    sample  N   -- sample N points on the sine function.
    """

    def __init__(self, root):
        """ Initializes the sine and standard display object and setup a loop
        to continuously process the user input provided via the command line.
        """
        # construct two frames
        frame1 = tk.Frame(root)
        frame1.place(relx=0, rely=0, relheight=1, relwidth=0.75)
        frame2 = tk.Frame(root)
        frame2.place(relx=0.75, rely=0, relheight=1, relwidth=0.25)

        self.sine = Sine()
        self.display = Display(frame1)
        # Place scrollbar
        s = tk.Scrollbar(frame2)
        s.place(relx=0.95, rely=0, relwidth=0.05, relheight=0.5)
        # Place text box to display previous commands
        self.hist = tk.Text(frame2)
        self.hist.config(yscrollcommand=s.set)
        self.hist.place(relx=0, rely=0, relwidth=0.95, relheight=0.5)
        # entry box to display new commands
        self.cmd_var = tk.StringVar()
        cmd = tk.Entry(frame2, textvariable=self.cmd_var)
        cmd.bind('<Return>', self._execute_command)
        cmd.place(relx=0, rely=0.5, relwidth=1, relheight=0.2)
        # text box to display output messages
        self.out_var = tk.StringVar()
        out = tk.Entry(frame2, textvariable=self.out_var)
        out.place(relx=0, rely=0.7, relwidth=1, relheight=0.3)

        self.display.sine_function(self.sine.df_sine)
        self.root = root

    def _execute_command(self, event):
        """ Interpret command line arguments.
        args:
        command -- str, input string provided via command line.
        """
        command = self.cmd_var.get()
        self.cmd_var.set('')
        if 'quit' in command:
             self.root.quit()
        # interpret command
        try:
            if 'noise' in command:
                self.sine.set_std(command.split()[1])
            elif 'spacing' in command:
                self.sine.set_spacing(command.split()[1])
            elif 'sample' in command:
                self.sine.training_data(command.split()[1])
                self.display.training_data(self.sine.df_data)
        except Message as m:
            self.out_var.set(m.message)

        hist = self.hist.insert(tk.END, command + '\n')

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Regression Application')
    root.geometry("1000x600")
    app = App(root)
    root.mainloop()
