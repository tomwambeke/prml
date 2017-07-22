from samplesinus import SampleSinus
from vizualisation import Vizualisation
from closedform import ClosedForm
from matplotlib import pyplot as plt
import numpy as np

class Regularization(object):
    """
    Fit high order polynomials to training data. Vary regularization constant,
    evaluate difference in performance.

    """

    FIG_W = 6  # Figure width
    FIG_H = 4  # Figure height

    BOX = [0.1, 0.1, 0.8, 0.8]       # Box axes 1
    YLIM = [0, 1]

    CLR_TRAIN  = '#003049'
    CLR_TEST = '#D62828'

    FRMT_TRAIN = '{0}//tranining_xte.dat'
    FRMT_TEST = '{0}//test_xte.dat'

    def __init__(self, Ntraining, Ntest, M, descr,
                       list_lnl=None, display=False):
        """ Create test and training data set. 

        :param Ntraining - int, number of data points in training dataset.
        :param Ntest - int, number of data points in test dataset.
        :param M - int, order of the polynomial. 
        """

        FOLDER = 'reg_N{0}_M{1}_{2}'.format(Ntraining, M, descr)
        self.train = self.FRMT_TRAIN.format(FOLDER)
        self.test = self.FRMT_TEST.format(FOLDER)        

        sin = SampleSinus()
        sin.target(Ntraining, self.train)
        sin.target(Ntest, self.test, xdistr='evenly')
        SIN_FUNC = '{0}//sinus.func'.format(FOLDER)
        sin.function( SIN_FUNC )

        self.RMSEs_train = []
        self.RMSEs_test  = []

        # lnl = ln( lambda )
        if list_lnl is None:
            list_lnl = [-np.inf, -18, 0]
        
        for lnl in list_lnl:
            model = '{0}//poly_L{1}.func'.format(FOLDER, lnl)
            fig_name = '{0}//poly_L{1}.png'.format(FOLDER, lnl)
            weights_name = '{0}/weights_L{1}.dat'.format(FOLDER, lnl)

            cs = ClosedForm(M)
            cs.solve(self.train, weights_name, lnl)
            cs.test(self.test)
            cs.function(model)

            viz = Vizualisation()
            viz.target(self.train)
            viz.function( SIN_FUNC )
            viz.function(model, clr_option='model')
            viz.to_file( fig_name )

            self.RMSEs_train.append( cs.RMSE_train )
            self.RMSEs_test.append( cs.RMSE_test )

        if display is True:
            file_out = '{0}//regularization.png'.format( FOLDER )
            self._display_errors( file_out, list_lnl )

    
    def _display_errors(self, file_out, list_lnl):
        """ Display training and test errors. """

        self.FIG = plt.figure(figsize=(self.FIG_W, self.FIG_H))
        self.AX1 = self.FIG.add_axes(self.BOX)
        self.AX1.set_xlim([list_lnl[0]-2, list_lnl[-1]+2])
        self.AX1.set_ylim(self.YLIM)

        self.AX1.plot(list_lnl, self.RMSEs_train, 
                      marker='o',
                      linestyle='-',
                      linewidth=2,
                      color=self.CLR_TRAIN)
        self.AX1.plot(list_lnl, self.RMSEs_test, 
                      marker='o',
                      linestyle='-',
                      linewidth=2,
                      color=self.CLR_TEST)

        self.FIG.savefig(file_out)