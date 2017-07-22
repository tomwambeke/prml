from modelselection import ModelSelection
from regularization import Regularization

if __name__ == '__main__':

    model_selection = True
    regularization = True

    if model_selection:

        ms = ModelSelection(Ntraining=10,
                            Ntest=100,
                            Mmax=9)

        ms = ModelSelection(Ntraining=15,
                            Ntest=100,
                            Mmax=9)

        ms = ModelSelection(Ntraining=100,
                            Ntest=100,
                            Mmax=9)

    if regularization: 

        reg = Regularization(Ntraining=10,
                             Ntest=100,
                             M=9)