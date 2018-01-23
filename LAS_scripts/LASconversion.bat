@echo off
set filelist=26gn1 32fz2 33az1 33az2 32hn2 33cn1 33cn2 32hz2 33cz1 33cz2 28cn1 28cn2 28cz2
set outputfolder=LiDAR_data2

if not exist %outputfolder% (
	echo LiDAR_data folder doesn't exist yet. Creating...
	mkdir %outputfolder%
)

echo Stage 1: running LASmerge... (this may take a while)
for %%a in (%filelist%) do (
	if exist g%%a.laz (
		if exist u%%a.laz (
			echo  - Merging %%a...
			lasmerge -i g%%a.laz u%%a.laz -o %outputfolder%\%%a.laz
		)
	)
)

echo Stage 2: running LASindex... (this may take a while)
for %%a in (%outputfolder%\*.laz) do (
	echo  - Indexing %%a...
	lasindex -i %%a
)

echo Stage 3: running Tiling (this may take a while)
mkdir %outputfolder%\tiling
for %%a in (%outputfolder%\*.laz) do (
	echo  - Running on %%~na...
	lastile -i %%a -o %outputfolder%\tiling\%%~na
)

echo Stage 4: running LASground_new (this may take a while)
mkdir %outputfolder%\ground
for %%a in (%outputfolder%\tiling\*.las) do (
	echo  - Running on %%~nxa...
	lasground_new -i %outputfolder%\tiling\%%~nxa -o %outputfolder%\ground\%%~na.laz -ignore_class 7
)

echo Stage 5: running LASheight (this may take a while)
mkdir %outputfolder%\height
for %%a in (%outputfolder%\ground\*.laz) do (
	echo  - Running on %%~nxa...
	lasheight -i %outputfolder%\ground\%%~nxa -o %outputfolder%\height\%%~na.laz
)

echo Conversion finished
PAUSE
