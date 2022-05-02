# Butters_WFIP2_Analysis

Sean Butters
sean.butters@colorado.edu
Last Updated: May 2, 2022

This is my research code comparing lidar observations from 3 sites at the WFIP2 project against model products ERA-5, MERRA-2, and WTK-LED (WRF). 

There is a directory for each site. Inside each folder is the following:
-A WTK file provided by collaborator Nicola Bodini of NREL (SiteNameWRF)
-A MERRA-2 file extracted from renewables.ninja (SiteNameMERRA2)
-An ERA-5 file extacted from the Copernicus CDS (SiteNameERA)
-A folder containing raw lidar files (SiteNameLidarFiles)
-A notebook used to process raw lidar data files (SiteNameLidarProcessing.ipynb)
-A file containing processed hourly lidar data for comparison to model products (SiteNameLidarInterpolated Hourly)
-The overall analysis notebook which reads in the aforementioned files and analyzes the data (SiteAbbreviation_Analysis.ipynb)
