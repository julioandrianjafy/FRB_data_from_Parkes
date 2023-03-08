import numpy as np
import filterbank
import setup
#import matplotlib.pyplot as plt

# create a general filterbank class (independent to setup)
# we can use this in other projects
class fcube_class():

        # initialize parameters
        def __init__(self, data, bw, fres, fhigh, tres):

            self.data = data
            self.bw = bw
            self.fres = fres
            self.fhigh = fhigh
            self.tres = tres

        # get freq values for all channels
        def freq_val(self):

            freqar = np.arange(len(self.data)) # assuming that first dim is frequency
            freqval = self.fhigh - freqar*self.fres
            return freqval

        # Time delay with respect to a reference frequency
        def time_delay(self, DM, f):

            # convert to Ghz
            lo = f*1e-3
            hi = self.fhigh*1e-3

            # calculate delay
            dt = 4.15*(lo**(-2) - hi**(-2))*DM

            return np.int0(np.around(dt/self.tres))

        # dedisperse the filterbank
        def dedisperse(self,DM):

            # calculate time delay for all frequencies
            delays = self.time_delay(DM,self.freq_val())

            newframe = []
            for i in range(len(delays)):
                newframe.append(np.roll(self.data[i],-delays[i]))
            return newframe



#testcube = filterbank.get_filterbank()
#mycube = fcube_class(testcube,setup.Bandwidth,setup.finit,1518,setup.new_tres)
#nf = mycube.dedisperse(790)

#plt.imshow(nf)
#plt.show()
