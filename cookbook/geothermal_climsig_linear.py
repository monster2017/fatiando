"""
Geothermal: Forward and inverse modeling of a linear change in temperature
measured in a well
"""
import numpy
from fatiando import utils
from fatiando.geothermal import climsig
from fatiando.vis import mpl

# Generating synthetic data
amp = 5.43
age = 78.2
# along a well at these depths
zp = numpy.arange(0, 100, 1)
temp, error = utils.contaminate(climsig.linear(amp, age, zp), 0.02,
    percent=True, return_stddev=True)

# Preparing for the inversion
data = climsig.SingleChange(temp, zp, mode='linear')
estimate = data.fit(initial=[1, 1])
est_amp, est_age = estimate

print "Linear change in temperature"
print "  true:      amp=%.3f age=%.3f" % (amp, age)
print "  estimated: amp=%.3f age=%.3f" % (est_amp, est_age)

mpl.figure(figsize=(4,5))
mpl.title("Residual well temperature")
mpl.plot(temp, zp, 'ok', label='Observed')
mpl.plot(data.predicted(estimate), zp, '--r', linewidth=3, label='Predicted')
mpl.legend(loc='lower right', numpoints=1)
mpl.xlabel("Temperature (C)")
mpl.ylabel("Z (m)")
mpl.ylim(100, 0)
mpl.show()
