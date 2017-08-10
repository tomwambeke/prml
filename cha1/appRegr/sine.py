import pandas as pd
import numpy as np
from message import Message

class Sine(object):
    """ Sample sine function f(x) = sin(2 pi x)

    SET_STD     - set measurement noise
    SET_SPACING - set spacing, random/regular

    TRAINING_DATA
    - create input and target vector: df['x', 't']
    - target includes noise (measurement error)

    SINE_FUNCTION
    - create input and output vector: df['x', 'f']
    - used to draw sine function, no noise
    - created upon initialization
    """

    SEED = 1234567  # random seed
    X_LB = 0.0      # LOWER bound x interval
    X_UB = 1.0      # UPPER bound x interval

    NLARGE = 5001   # decritization number of f(X) - for visualization

    STD_NOISE = None
    SPACING = None

    def __init__(self):
        """ Initializes a sine function object. """
        self.random_state = np.random.RandomState(self.SEED)
        self.df_sine = self._sample_sine(self.NLARGE, regular=True)
        self.df_data = None

    def set_std(self, std):
        """ Set standard deviation measurement error.
        std -- str, standard deviation."""
        # convert to float
        try:
            std = float(std)
        except ValueError:
            raise Message("Select Standard deviation in interval [0, 3].")
        if std < 0 or std > 3:
            raise Message("Select Standard deviation in interval [0, 3].")
        self.STD_NOISE = std

    def set_spacing(self, spacing):
        """ Set option for spacing: regular/random.
        spacing -- str, two options: regular or random."""
        if spacing == 'regular' or spacing == 'random':
            self.SPACING = spacing
        else:
            raise Message("Select Spacing from ['regular','random'].")

    def training_data(self, n_samples):
        """ Obtain training data set by sampling sine function, add noise to
        function values.
        n_samples -- str, number of samples.
        """
        if self.SPACING is None or self.STD_NOISE is None:
            raise Message("STD and/or spacing is missing")
        try:
            n_samples = int(n_samples)
        except ValueError:
            raise Message("Sample N - N must be an integer")
        if self.SPACING == 'regular':
            self.df_data = self._sample_sine(n_samples, regular=True)
        elif self.SPACING == 'random':
            self.df_data = self._sample_sine(n_samples, regular=False)
        self.df_data.rename(columns={'f': 't'}, inplace=True)
        e = self.random_state.normal(loc=0.0, scale=self.STD_NOISE,
                                              size=n_samples)
        self.df_data.loc[:, 't'] = self.df_data.loc[:, 't'] + e

    def _sample_sine(self, n_rows, regular):
        """ Sample sinus function
        args:
        n_rows  -- number of sampling points.
        regular -- bool, sample at regular intervals? If not, points
                   on x axis are chosen at random.
        returns:
        df -- df[x, f(x)], n rows with input and function value.
        """
        if regular is True:
            x = np.linspace(self.X_LB, self.X_UB, n_rows)
        elif regular is False:
            x = self.random_state.uniform(self.X_LB, self.X_UB, n_rows)
        f = np.sin(2*np.pi*x)
        return pd.DataFrame( {'x': x, 'f': f})
