
from src.netCDF import NetCDF

def test_readVariables():

    o = NetCDF("/Users/tmorales/Documents/wrfout_d01_2000-01-24_12")
    o.netCDF()
    variableInfo = o.get_variable("SWDOWN")
    assert variableInfo is not None


def test_array():

    # I need select four variables with diferent dimension

    o = NetCDF("/Users/tmorales/Documents/wrfout_d01_2000-01-24_12")
    o.netCDF()

    array = o.get_array("SWDOWN")
    assert len(array.shape) == 3


