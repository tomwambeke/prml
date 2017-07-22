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

    def __init__(self, Ntraining, Ntest, M, list_lnl=None):
        """ Create test and training data set. 

        :param Ntraining - int, number of data points in training dataset.
        :param Ntest - int, number of data points in test dataset.
        :param M - int, order of the polynomial. 
        """

        FOLDER = 'reg_N{0}_M{1}'.format(Ntraining, M)
        self.train = self.FRMT_TRAIN.format(FOLDER)
        self.test = self.FRMT_TEST.format(FOLDER)        

        sin = SampleSinus()
        sin.target(Ntraining, self.train)
        sin.target(Ntest, self.test, xdistr='random')
        SIN_FUNC = '{0}//sinus.func'.format(FOLDER)
        sin.function( SIN_FUNC )

        # lnl = ln( lambda )
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





