@echo off
set outputfolder=LiDAR_data

echo Running LAScanopy... (this may take a while)
mkdir %outputfolder%\canopy

lascanopy -i LiDAR_data\classify\*.laz -names -lor %outputfolder%\ID_growing_forest.csv -p 5 10 25 50 75 90 -min -max -avg -std -ske -kur -qav -c 10 50 -step 1 -o LiDAR_data\canopy\%%~na.csv

PAUSE