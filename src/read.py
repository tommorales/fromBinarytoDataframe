
import netCDF4

class Read:

    def __init__(self, fileName):
        self.__fileName = fileName

    def netCDF(self):
        self.file = netCDF4.Dataset(self.__fileName, "r")
        return self.file

    def grib(self):
        pass

    def hdf5(self):
        pass

    def bufr(self):
        pass


def main():
    o = Read("/Users/tmorales/Documents/wrfout_d01_2000-01-24_12")
    print o.netCDF()

if __name__ == "__main__":
    main()