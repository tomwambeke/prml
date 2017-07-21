from samplesinus import SampleSinus
from vizualisation import Vizualisation
from closedform import ClosedForm

if __name__ == '__main__':

	sin = SampleSinus()
	sin.target(10)
	sin.sinus_function()

	cf = ClosedForm(M=10)
	cf.solve('sin_N10_xt.dat')
	cf.function()

	viz = Vizualisation()
	viz.target('sin_N10_xt.dat')
	viz.function('sinus.func')
	viz.function('poly_M10.func', 'model')
	viz.show()