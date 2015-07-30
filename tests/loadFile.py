
from src.read import Read

def test_loadNetCDF():

    o = Read("/Users/tmorales/Documents/wrfout_d01_2000-01-24_12")
    file = o.netCDF()
    assert file == None
