# script to create the filterbank file
import setup
import numpy as np
import matplotlib.pyplot as plt

# load ascii file with loadtxt
def get_filterbank():

    Frequency, Time, Amplitude = np.loadtxt(setup.path_data, unpack = True)

    # create filterbank directly by reshaping amplitude
    # the data is organized by frequency (need to reshape according to nchan)
    nbin = int(np.max(Time)) + 1 # number of time bin, it starts with 0
    if setup.change_res:
        # reshape according to new integration time
        newtbin = int(setup.new_tres/setup.tinit) # how many points to average
        newbin = int(nbin/newtbin) # new bin
        fcube = np.reshape(Amplitude,newshape=(setup.nchan,newbin,newtbin))
        fcube = np.mean(fcube,axis=2)

    else:
        fcube = np.reshape(Amplitude,newshape=(setup.nchan,nbin))

    return fcube 
