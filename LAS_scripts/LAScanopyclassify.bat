@echo off
set outputfolder=LiDAR_data

echo Running LAScanopy... (this may take a while)
mkdir %outputfolder%\canopy
for %%a in (%outputfolder%\classify\*.laz) do ( 
	echo  - Indexing %%~nxa...
	lascanopy -i LiDAR_data\classify\%%~nxa -lor LiDAR_data\forest_grid_coords.csv -dns -p 5 10 25 50 75 90 -min -max -avg -std -ske -kur -qav -cov -c 0.5 2 4 10 50 -int_min -int_max -int_avg -int_qav -int_std -int_ske -int_kur -int_c 0 128 256 1024 -int_p 25 50 75 -o LiDAR_data\canopy\%%~na.csv
)

PAUSE