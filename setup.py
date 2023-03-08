# configuration file for data analysis
path_data = '../../5.raw.cube'
tinit = 0.125 # in ms. This could be found in the data head
freq_center = 1374 # in MHz
Bandwidth = 288 # in MHz
nchan = 96
finit = Bandwidth/nchan # in MHz

# if changing the resolution to reduce space
change_res = True
new_tres = 4 # in ms
#new_fres = # in MHz

# filterbank name
filtname = 'myfilerbank.txt'
