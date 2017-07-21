from matplotlib import pyplot as plt
from dataio import DataIO

class Vizualisation(object):
    """ Vizualise Regression results

    TARGET
    - display input and target points
    - sampled from function including noise

    1) Read Data file: input and target vector 
    2) Display sampled points 

    FUNCTION
    - display function
    1) Read Data file: input and function vector
    2) Display function as line

    """

    FIG_W = 12  # Figure width
    FIG_H = 8  # Figure height

    BOX = [0.1, 0.1, 0.8, 0.8]       # Box axes 1
    XLIM = [-0.1, 1.1]
    YLIM = [-2, 2]

    CLR_DOT   = '#F77F00'
    CLR_FUNC  = '#003049'
    CLR_MODEL = '#D62828'

    def __init__(self):
        self.FIG = plt.figure(figsize=(self.FIG_W, self.FIG_H))
        self.AX1 = self.FIG.add_axes(self.BOX)
        self.AX1.set_xlim(self.XLIM)
        self.AX1.set_ylim(self.YLIM)

        #plt.show()

    def target(self, file_name):
        """ Display sampled points (noisy), read from file the input/target
        pairs and draw the resulting points.

        :param file_name - str, name of the file with the data.
        """
        x, t = DataIO.read_data(file_name)
        self.AX1.plot(x, t,
                      marker='o',
                      markersize=7,
                      linestyle='none',
                      color=self.CLR_DOT,
                      zorder=2)

    def function(self, file_name, clr_option=None):
        """ Display underlying function, read from file input / function value
        pairs. Draw line through the large colleciton of points.

        :param file_name - str, name of the file with the data.
        """
        x, f = DataIO.read_data(file_name)
        if clr_option is None:

            self.AX1.plot(x, f,
                marker='None',
                linestyle='-',
                linewidth=2,
                color=self.CLR_FUNC,
                zorder=3)
        elif clr_option == 'model':

            self.AX1.plot(x, f,
                marker='None',
                linestyle='-',
                linewidth=2,
                color=self.CLR_MODEL,
                zorder=3)



    def show(self):
        """ Show figure on screen. """
        plt.show(self.FIG)