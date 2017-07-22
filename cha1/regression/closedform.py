import numpy as np
from scipy import linalg as sciLinalg
from dataio import DataIO

class ClosedForm(object):
    """ Closed Form solution of regression problem.

    Polynomial Fitting
    y(x, w) = w0 + w1 x^1 + w2 x^2 ... wM x^M    (order M)
    -> compute weights wj

    SOLVE 
    - read input and target vector
    - compute weights of M order polynomial
    - write weights to file


    FUNCTION
    - create input and target vector to draw M order polynomial

    1) create x (length N), loop through bounded interval
    2) compute N time Y(x, w) 
    3) Write to file (option xy)


    YVALUE
    - given x value, return y(x, w)

    """    
    X_LB = 0.0  # Lower Bound 
    X_UB = 1.0  # Upper Bound
    NLARGE = 100001 # decritization number of y(x, w) (vizualization)

    def __init__(self, M):
        """ Initializes ClosedForm object. """
        self.M = M
        self.A = np.empty([self.M+1, self.M+1])
        self.T = np.empty([self.M+1])
        self.W = None
        self.polynomial = None

        self.RMSE_train = None
        self.RMSE_test = None

    def solve(self, file_name, file_out, ln_lambda=None):
        """ Import data, compute weights.

        :param file_name - str, name of data file.
        :param file_out - str, name of the data file to store the weights.
        :param ln_lambda - flaot, regularization constant.

        :output None - weights are computed and exported.
        """ 
        data = DataIO.read_data(file_name)
        x, t, e = data

        self._populate_A(x, ln_lambda)
        self._populate_T(x, t)
        self.W = sciLinalg.solve(self.A, self.T)
        # store polynomial function
        self._polynomial = self._vectorize_polynomial() 

        title = 'weights'
        DataIO.write_data([self.W], file_out, title)    

        # compute Ermse
        y = self._polynomial(x)
        self.RMSE_train = np.sqrt( np.mean( (y-t)**2 ) ) 

    def function(self, file_name):
        x = np.linspace(self.X_LB, self.X_UB, self.NLARGE)
        y = self._polynomial(x)
        title = 'input\tpolynomial'
        DataIO.write_data([x,y], file_name, title)

    def test(self, file_name):
        """ Compute RMSE test data set. """
        data = DataIO.read_data(file_name)
        x, t, e = data
        y = self._polynomial(x)
        self.RMSE_test = np.sqrt( np.mean( (y-t)**2 ) )

    def yvalue(self, x):
        """ return y value, given x value. """
        return self._polynomial(x)

    def _vectorize_polynomial(self):
        """ Return fitted polynomial function.

        :output def - function is returned.
        """
        def polynomial(x):
            y = sum([wj*x**j for j, wj in enumerate(self.W)])
            return y
        return np.vectorize(polynomial)

    def _populate_A(self, x, ln_lambda):
        """ Construct symmetric A matrix. 

        :param x - input vector of length N.
        """
        if ln_lambda is not None:
            l = np.exp(ln_lambda)
        else:
            l = 0

        for i in range(self.M+1):
            for j in range(i, self.M+1):
                Aij = sum([xn**(i+j) for xn in x])
                if i !=j:
                    self.A[i,j] = Aij
                    self.A[j,i] = Aij
                else:
                    self.A[i,i] = Aij + l


    def _populate_T(self, x, t):
        """ Construct vector T.

        :param x - input vector of length N.
        :param t - target vector of length N. 
        """
        for i in range(self.M+1):
            Ti = sum([xn**i*tn for xn, tn in zip(x, t)])
            self.T[i] = Ti