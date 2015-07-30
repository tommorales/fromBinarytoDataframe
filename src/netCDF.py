
import netCDF4

from src.read import Read

class NetCDF(Read):

    def __init__(self, fileName):
        Read.__init__(self, fileName)

    def get_variable(self, variable):
        return self.file.variables[variable]

    def get_array(self, variable, timeStep=None, level=None, lon=None, lat=None):

        arrayDimension= len(self.file.variables[variable].shape)
        if arrayDimension == 1: return self.file.variables[variable][:]
        if arrayDimension == 2: return self.file.variables[variable][:,:]
        if arrayDimension == 3: return self.file.variables[variable][:,:,:]
        if arrayDimension == 4: return self.variables[variable][:,:,:,:]

    def get_slide(self, timeStep=None, level=None, lon=None, lat=None):
        pass





def main():
    o = NetCDF("/Users/tmorales/Documents/wrfout_d01_2000-01-24_12")
    o.netCDF()
    print o.get_variable("SWDOWN")

    print o.get_array("SWDOWN")

if __name__ == "__main__":
    main()