from modelselection import ModelSelection
from regularization import Regularization

if __name__ == '__main__':

    model_selection = False
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
                             M=9, descr='A')

        list_lnl = [-40, -37.5, -35, -32.5, -30, -27.5, -25, -22.5, -20]
        reg = Regularization(Ntraining=10,
                             Ntest=100, 
                             M=9, descr='B', 
                             list_lnl=list_lnl, display=True)