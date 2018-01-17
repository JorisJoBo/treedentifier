[![Build Status](https://travis-ci.org/JorisJoBo/treedentifier.svg?branch=master)](https://travis-ci.org/JorisJoBo/treedentifier)
[![HitCount](http://hits.dwyl.io/JorisJoBo/treedentifier.svg)](http://hits.dwyl.io/JorisJoBo/treedentifier)

# Treedentifier
Treedentifier allows you to identify trees in your country. The algorithm can learn
what the characteristics of a specific tree species are and detect them when
properly learned. For the development of this algorithm we use LIDAR data of the Netherlands.

## Setup
### Software
After cloning the project, please install the required python packages first.
For this project we use Python 3.6. If you don't have python already, you can
download it [here](https://www.python.org/downloads/release/python-364/).
To install the required packages, just execute:
```
pip install -r python-requirements.txt
```

To process the LAZ files in which most LiDAR datasets are formatted, you can
use LAStools. You can download LAStools [here](https://rapidlasso.com/lastools/).
Please note that LAStools is not free. You can use LAStools without paying but it will
distort your data and insert black diagonals in LAScanopy.

### Datasets
After that, you'll need a vegetation dataset of your area, as well as a filtered
and a unfiltered LiDAR dataset. We used the [Dutch Vegetation Database](https://www.gbif.org/dataset/740df67d-5663-41a2-9d12-33ec33876c47)
as our vegetation dataset and as LiDAR data we used [filtered AHN2 data](http://geodata.nationaalgeoregister.nl/ahn2/atom/ahn2_gefilterd.xml)
and [unfiltered AHN2 data](http://geodata.nationaalgeoregister.nl/ahn2/atom/ahn2_uitgefilterd.xml).

### Processing data
To be able to use this data in our algorithm, we need to do some preprocessing first.

#### Preparing the vegetation datasets
The vegetation dataset contains a lot of different plants. Since we are only
interested in trees, we need to remove all non-trees. In the file treespecies,
you can find a list of trees extracted from the Dutch Vegetation Database.

To extract all trees from the vegetation dataset, you can run 'forest-filter.py'.
```
python forest-filter.py
```
Please note that this file looks for the 'joined_db2.csv' file, so you'll have to name your
vegetation dataset like this. This python program will create a new file called
'forest_filter_result.csv' for you. This will contain all trees found in the
vegetation database.

Then, if you want to extract all dominant trees from the dataset, you can run dominant-filter.py.
Which will take the 'forest_filter_result.csv' file created in the previous step and
will generate a new 'dominant_trees.csv' file.
```
python dominant-filter.py
```

After that, you can run 'coordinate-filter.py' to extract the coordinates of the trees.
```
python coordinate-filter.py dominant_trees.csv
```
Please note: it is necessary to provide the 'dominant_trees.csv' file as an argument.

## Contributing
### Testing
You have to test your code first before pushing. Pushing while failing to do so, may result in failed builds.
For testing you should use [PyCodeStyle](https://github.com/PyCQA/pycodestyle).
You can test your code with the following command:
```
pycodestyle --show-source --show-pep8 ./
```
If you want, you can let [autopep8](https://github.com/hhatto/autopep8) fix your issues with the following command:
```
autopep8 --in-place --aggressive --aggressive -r ./
```

## Contributors
The core contributors are:
- Patrick Spaans
- Geerten Rijsdijk
- Thom Visser
- Joris Jonkers Both
