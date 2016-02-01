"""
Zonal mean process
"""

from pywps.Process import WPSProcess

class ZonalMean(WPSProcess):
    """This process calculates zonal mean in netcdf file"""
    def __init__(self):
        WPSProcess.__init__(
            self,
            identifier = "zonal_mean",
            title = "Zonal Mean",
            version = "0.4",
            abstract="zonal mean in NetCDF File.",
            statusSupported=True,
            storeSupported=True
            )

        self.dataset = self.addComplexInput(
            identifier="dataset",
            title="Dataset (NetCDF)",
            minOccurs=1,
            maxOccurs=100,
            maxmegabites=5000,
            formats=[{"mimeType":"application/x-netcdf"}],
            )

        self.output = self.addComplexOutput(
            identifier="output",
            title="Output",
            abstract="Output",
            formats=[{"mimeType":"text/plain"}],
            asReference=True,
            )

    def execute(self):
        self.status.set("starting zonal mean ...", 0)

        nc_files = self.getInputValues(identifier='dataset')

        # the Scientific Python netCDF 3 interface
        # http://dirac.cnrs-orleans.fr/ScientificPython/
        #from Scientific.IO.NetCDF import NetCDFFile as Dataset
        from netCDF4 import Dataset
        # the 'classic' version of the netCDF4 python interface
        # http://code.google.com/p/netcdf4-python/
        #from netCDF4_classic import Dataset
        from numpy import arange, dtype # array module from http://numpy.scipy.org
        from numpy.testing import assert_array_equal, assert_array_almost_equal
        """
        einfachstes Beispiel fuer Einlesen einer netcdf-Datei und Berechnung von zonalen Mitteln
        vorher test auf richtigkeit der Einheiten und Achsen
        """
        nlats = 6; nlons = 12
        # open netCDF file for reading
        ncfile = Dataset(nc_files[0],'r') 
        # expected latitudes and longitudes of grid
        lats_check = 25.0 + 5.0*arange(nlats,dtype='float32')
        lons_check = -125.0 + 5.0*arange(nlons,dtype='float32')
        # expected data.
        #press_check = 900. + 6.0*arange(0.,nlats*nlons,dtype='float32') # 1d array
        #press_check.shape = (nlats,nlons) # reshape to 2d array
        #temp_check = 9. + 0.25*arange(nlats*nlons,dtype='float32') # 1d array
        #temp_check.shape = (nlats,nlons) # reshape to 2d array
        # get pressure and temperature variables.
        temp = ncfile.variables['temperature']
        press = ncfile.variables['pressure']
        # check units attributes.
        try:
            assert(temp.units == 'celsius')
        except:
            raise AttributeError('temperature units attribute not what was expected')
        try:
            assert(press.units == 'hPa')
        except:
            raise AttributeError('pressure units attribute not what was expected')
        # check data
        #print ("press=",press[:])
        #print ("press_check=",press_check)
        #try:
        #    assert_array_almost_equal(press[:],press_check)
        #except:
        #    raise ValueError('pressure data not what was expected')
        #try:
        #    assert_array_almost_equal(temp[:],temp_check)
        #except:
        #    raise ValueError('temperature data not what was expected')
        # get coordinate variables.
        lats = ncfile.variables['latitude']
        lons = ncfile.variables['longitude']
        # check units attributes.
        try:
            assert(lats.units == 'degrees_north')
        except:
            raise AttributeError('latitude units attribute not what was expected')
        try:
            assert(lons.units == 'degrees_east')
        except:
            raise AttributeError('longitude units attribute not what was expected')
        # check data
        try:
            assert_array_almost_equal(lats[:],lats_check)
        except:
            raise ValueError('latitude data not what was expected')
        try:
            assert_array_almost_equal(lons[:],lons_check)
        except:
            raise ValueError('longitude data not what was expected')
        

        outfile = 'out.txt'
        with open(outfile, 'w') as fp:
            fp.write('*** SUCCESS reading example file testfile.nc!\n')
            fp.write("mean zonal pressure %s hPa" % ( sum(press[:])/6. ) )

        # close the file.
        ncfile.close()

        self.output.setValue( outfile )

        self.status.set("done", 100)



