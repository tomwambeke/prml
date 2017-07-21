import numpy as np

class SampleSinus(object):
    """ Sample sinus function f(x) = sin(2 pi x)

    
    RANDOM NOISY
    - create input and target vector
    - noise (measurement error)

    1) Draw N times x from Uniform(0, 1)
    2) Compute N times f(x) = sin( 2 pi x)
    3) Draw N times e from N(0, 0.3)
    4) Add e to f(x)
    5) Write to file (option xt)


    SINUS FUNCTION
    - create input and target vector
    - to draw sinus function
    - no noise

    1) create x (length N), loop through bounded interval
    2) compue N times f(x) = sin( 2 pi x)
    3) Write to file (option xt)


    INPUT VECTOR
    - create input vector (no target vector)
    1) Draw N times x from Uniform(0, 1)
    2) Write to file (option x)

    """

    SEED = 9001 # random seed

    X_LBU = 0.0  # Lower Bound Uniform distribution
    X_UBU = 1.0  # Upper Bound Uniform distribution
    STD_NOISE = 0.3 # standard deviation normal error distribution

    FILEFRMT = 'sin_{0}_{1}.dat'  # File name format, replace {0} with N,
        # replace {1} with sampling option, either x or xt.

    NLARGE = 10001 # decritization number of f(x) (vizualization)

    def __init__(self, seed=None):
        """ Initialize SampleSinus object. """
        
        # Check if random seed is provided
        if seed is None:
            seed = self.SEED
        # construct random state object
        self.random_state = np.random.RandomState(seed)

    def target(self, N, file_name=None):
        """ Execute sampling operation (see class description)

        :param N - int, number of data points.
        :param file_name - str, name of the output file.

        :output None - write data to file.
        """
        if file_name is None:
            file_name = self.FILEFRMT.format(N, 'xt')

        x = self.random_state.uniform(self.X_LBU, self.X_UBU, N)
        y = np.sin(2*np.pi*x)
        e = self.random_state.normal(loc=0.0, scale=self.STD_NOISE, size=N)
        t = y + e
        title = 'input - target'
        self._write_data(x, file_name, title, t)

    def sinus_function(self, file_name=None):
        if file_name is None:
            file_name = self.FILEFRMT.format(self.NLARGE, 'xsin')

        x = np.linspace(self.X_LBU, self.X_UBU, self.NLARGE)
        f = np.sin(2*np.pi*x)
        title = 'input - sinus function'
        self._write_data(x, file_name, title, f)

    def input(self, N, file_name=None):
        if file_name is None:
            file_name = self.FILEFRMT.format(N, 'x')

        x = self.random_state.uniform(self.X_LBU, self.X_UBU, N)
        title = 'input'
        self._write_data(x, file_name, title)

    def _write_data(self, x, file_name, title, y=None):
        """ Write data point to file.

        :param x - np array of length N, sampled input variables.
        :param t - np array of length N, sampled target variables.
        :param file_name - str, name of output file.        
        """
        with open(file_name, 'w') as f:
            f.write(title +' \n')

            if y is not None:
                line = '{0:.5f}\t{1:.5f}\n'
                for (xi, yi) in zip(x, y):
                    f.write( line.format(xi, yi) )
            else:
                line = '{0:.5f}\n'
                for xi in x:
                    f.write( line.format(xi) )

if __name__ == '__main__':
    print('Running ... Sample Sinus')

    sin = SampleSinus()
    sin.target(10)
    sin.sinus_function()
    sin.input(10)
