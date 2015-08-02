
import os
import urllib
from subprocess import call

from src.netCDF import NetCDF

# download file
URL= "http://www2.mmm.ucar.edu/wrf/TUTORIAL_DATA/JAN00/wrfout_d01_2000-01-24_12.gz"
FILE= "wrfout_d01_2000-01-24_12.gz"

# esta mal -----------------------------------------------------------
if os.path.exists(FILE) == False:
    try:
        urllib.urlretrieve(URL, FILE)
        print "File downloaded .."
        try:
            f = open(FILE, "r")
            call(["gunzip", FILE], stdout=f)
        except Exception, e:
            print "I can not descompress the file: {0}".fomat(FILE)
        finally:
            f.close()
    except Exception, e:
        print "I can not download the file"
# ----------------------------------------------------------------------






def test_readVariables():

    o = NetCDF("/Users/tmorales/Documents/wrfout_d01_2000-01-24_12")
    o.netCDF()
    variableInfo = o.get_variable("SWDOWN")
    assert variableInfo is not None


def test_array():

    # I need select four variables with diferent dimension

    o = NetCDF("/Users/tmorales/Documents/wrfout_d01_2000-01-24_12")
    o.netCDF()

    array = o.get_array("ZS")
    assert len(array.shape) == 2

    array = o.get_array("SWDOWN")
    assert len(array.shape) == 3

    array = o.get_array("V")
    assert len(array.shape) == 4


