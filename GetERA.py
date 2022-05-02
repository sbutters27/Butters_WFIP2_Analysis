#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:19:02 2021

@author: nbodini
"""

#!/usr/bin/env python
import cdsapi

# NOTE: This doesn't work while on NREL's VPN
c = cdsapi.Client()
c.retrieve('reanalysis-era5-complete', { # Requests follow MARS syntax
                                         # Keywords 'expver' and 'class' can be dropped. They are obsolete
                                         # since their values are imposed by 'reanalysis-era5-complete'
    'date'    : '2016-01-01/to/2017-04-01', # The hyphens can be omitted
    'levelist': '127/128/129/130/131/132/133/134/135/136/137', # 1 is top level, 137 the lowest model level in ERA5. Use '/' to separate values.
    'levtype' : 'ml',                    # model level
    'param'   : '131/132/135',           # Variebles needed. Full information at https://apps.ecmwf.int/codes/grib/param-db/
    'stream'  : 'oper',                  # Denotes ERA5. Ensemble members are selected by 'enda'
    'time'    : '00/to/23/by/1',         # You can drop :00:00 and use MARS short-hand notation, instead of '00/06/12/18'
    'type'    : 'an',
    'area'    : '46/-121/45/-118',         # North, West, South, East. Default: global
    'grid'    : '1.0/1.0',               # Latitude/longitude. Default: spherical harmonics or reduced Gaussian grid
    'format'  : 'netcdf',                # Output needs to be regular lat-lon, so only works in combination with 'grid'!
}, 'ERA5-ml-uvw-subarea.nc')     # Output file. Adapt as you wish.