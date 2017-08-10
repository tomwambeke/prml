import matplotlib
matplotlib.use('TkAgg')

from matplotlib.figure import Figure as pltFigure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg

class Display(object):
    """ Create display object to visualize results.

    SINE_FUNCTION
    - display `unknown` sine function as line (green line)
    - store link to object in LN_SINE

    TRAINING_DATA
    - display sampled noisy training data (blue dots)
    - store link to objects in PT_DATA

    MODEL
    - display trained model (red line)
    - store link to object in LN_MODEL

    """
    BOX = [0.125, 0.125, 0.75, 0.75]

    LIM_X = [-0.1, 1.1]
    LIM_Y = [-1.5, 1.5]
    LN_SINE  = None
    PT_DATA  = None
    LN_MODEL = None

    CLR_BLUE  = "#1445c4"
    CLR_GREEN = "#15cd70"
    CLR_RED   = "#ba1f1f"

    def __init__(self, frame):
        """ Create matplotlib figure and axes object. Create canvas and
        toolbar within tkinter frame. Add matplotlib figure to canvas.
        frame -- a tkinter frame object.
        """
        self.FIG = pltFigure()
        self.AX = self.FIG.add_axes(self.BOX)
        self.AX.set_xlim(self.LIM_X)
        self.AX.set_ylim(self.LIM_Y)
        self.AX.set_xlabel('Input Variable', fontsize=12)
        self.AX.set_ylabel('Target Variable', fontsize=12)

        canvas = FigureCanvasTkAgg(self.FIG, master=frame)
        toolbar = NavigationToolbar2TkAgg(canvas, frame)
        canvas.get_tk_widget().place(relx=0, rely=0,
                                     relwidth=1, relheight=0.9)
        toolbar.place(relx=0.3, rely=0.9, relwidth=0.4, relheight=0.1)

    def sine_function(self, df_sine):
        """ Draw sine function given data from dataframe.
        df_sine -- A pandas dataframe df_sine['x', 'f']
        """
        x, f = df_sine['x'], df_sine['f']
        self.LN_FUNC = self.AX.plot(x, f, linewidth=2,
                                          linestyle='-',
                                          marker='None',
                                          color=self.CLR_GREEN)
        self.FIG.canvas.draw()

    def training_data(self, df_data):
        """ Draw training data set, i.e. noisy samples from sine function.
        df_data -- A pandas dataframe df_data['x', 't']
        """
        if self.PT_DATA is not None:
            self.PT_DATA[0].remove()
        x, t = df_data['x'], df_data['t']
        self.PT_DATA = self.AX.plot(x, t, linestyle='none',
                                          marker='o',
                                          markersize=4,
                                          color=self.CLR_BLUE,
                                          zorder=2)
        self.FIG.canvas.draw()
