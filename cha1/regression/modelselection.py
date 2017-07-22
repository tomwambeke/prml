from samplesinus import SampleSinus
from vizualisation import Vizualisation
from closedform import ClosedForm
from matplotlib import pyplot as plt

class ModelSelection(object):
    """ 
    Fit different order polynomials to the training data.
    Evaluate model performance using a test data set.

    """

    FIG_W = 6  # Figure width
    FIG_H = 4  # Figure height

    BOX = [0.1, 0.1, 0.8, 0.8]       # Box axes 1
    YLIM = [0, 1]

    CLR_TRAIN  = '#003049'
    CLR_TEST = '#D62828'

    FRMT_TRAIN = '{0}//tranining_xte.dat'
    FRMT_TEST = '{0}//test_xte.dat'

    def __init__(self, Ntraining, Ntest, Mmax):
        """ Create test and training data set. Fit differt polynomials.

        :param Ntraining - int, number of data points in training dataset.
        :param Ntest - int, number of data points in test dataset.
        :param Mmax - int, maximum number for polynomial order.
        """
        
        # Create Training Data, Test Data and Function Definition
        FOLDER = 'model_N{0}'.format(Ntraining)
        self.train = self.FRMT_TRAIN.format(FOLDER)
        self.test = self.FRMT_TEST.format(FOLDER)        

        sin = SampleSinus()
        sin.target(Ntraining, self.train)
        sin.target(Ntest, self.test, xdistr='random')
        SIN_FUNC = '{0}//sinus.func'.format(FOLDER)
        sin.function( SIN_FUNC )

        self.Ms = []
        self.RMSEs_train = []
        self.RMSEs_test = []

        self.Mmax= Mmax
        for m in range(self.Mmax+1):

            model = '{0}//poly_M{1}.func'.format(FOLDER, m)
            fig_name = '{0}//poly_M{1}.png'.format(FOLDER, m)
            weights_name = '{0}/weights_M{1}.dat'.format(FOLDER, m)

            cs = ClosedForm(m)
            cs.solve(self.train, weights_name)
            cs.test(self.test)
            cs.function(model)

            viz = Vizualisation()
            viz.target(self.train)
            viz.function( SIN_FUNC )
            viz.function(model, clr_option='model')
            viz.to_file( fig_name )

            self.Ms.append(m)
            self.RMSEs_train.append( cs.RMSE_train )
            self.RMSEs_test.append( cs.RMSE_test )

        file_out = '{0}//model_selection.png'.format( FOLDER )
        self._display_errors(file_out)

    def _display_errors(self, file_out):
        """ Display training and test errors. """

        self.FIG = plt.figure(figsize=(self.FIG_W, self.FIG_H))
        self.AX1 = self.FIG.add_axes(self.BOX)
        self.AX1.set_xlim([-1, self.Mmax+1])
        self.AX1.set_ylim(self.YLIM)

        self.AX1.plot(self.Ms, self.RMSEs_train, 
                      marker='o',
                      linestyle='-',
                      linewidth=2,
                      color=self.CLR_TRAIN)
        self.AX1.plot(self.Ms, self.RMSEs_test, 
                      marker='o',
                      linestyle='-',
                      linewidth=2,
                      color=self.CLR_TEST)

        self.FIG.savefig(file_out)
