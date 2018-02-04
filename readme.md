[![Build Status](https://travis-ci.org/JorisJoBo/treedentifier.svg?branch=master)](https://travis-ci.org/JorisJoBo/treedentifier)
[![HitCount](http://hits.dwyl.io/JorisJoBo/treedentifier.svg)](http://hits.dwyl.io/JorisJoBo/treedentifier)

# Treedentifier
Treedentifier allows you to identify trees in your country. The algorithm can learn
what the characteristics of a specific tree species are and detect them when
properly learned. For the development of this algorithm we use LiDAR data of the Netherlands.

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
and a unfiltered LiDAR dataset. We used a modified version of the [Dutch Vegetation Database](https://www.gbif.org/dataset/740df67d-5663-41a2-9d12-33ec33876c47)
as our vegetation dataset and as LiDAR data we used [filtered AHN2 data](http://geodata.nationaalgeoregister.nl/ahn2/atom/ahn2_gefilterd.xml)
and [filtered out AHN2 data](http://geodata.nationaalgeoregister.nl/ahn2/atom/ahn2_uitgefilterd.xml).

### Processing data
To be able to use this data in our algorithm, we need to do some preprocessing first.

#### Preparing the vegetation datasets
The vegetation dataset contains a lot of different plants. Since we are only
interested in trees, we need to remove all non-trees. In the file treespecies,
you can find a list of trees extracted from the Dutch Vegetation Database.

To extract all dominant trees from the vegetation dataset, you can run 'tree_processing.py'.
```
python tree_processing.py
```
Please note that this program looks for the 'joined_db2.csv' file, so you'll have to name your
vegetation dataset like this. This program will create a file called 'dominant_trees.csv' which will be used in a later step.

Now you can run all LAStools you want. We set up a default batch script which will
basically work for everyone. Just run the batch file and you should be fine. You'll need the output file 'ID_growing_forest' of the 'tree_processing.py' step, for the last LAStools step 'LAScanopy'.

When done with LAStools run 'data_processing.py' to combine the dominant trees
and the result matrix of LAScanopy and to remove any unnecessary data..
```
python data_processing.py input_directory output.csv
```
(The 'dominant_trees.csv' file in used by the program above is one of the output files of the earlier executed
'tree_processing.py' step).

Now you're done with the setup. You now should be able to run the algorithms without any problems.

## Machine learning algorithms
In this project we created python algorithms based on two machine learning principles.
You can choose between decision trees and support vector machines. It is recommended using the decision tree algorithm.
During tests decision trees showed better accuracy as well as efficiency (speed) than support vector machines.

### Running the decision tree algorithms
When running the decision tree algorithm, you can take one of the following versions:
- Dependent
- independent

#### Dependent decision tree algorithm
This runs the algorithm on the same forestry data as the training data is originating from.

#### Dependent decision tree algorithm
This runs the algorithm on forest data from other geographic places than the training data is originating from.

### Running the support vector machine algorithms
This algorithm is provided as a Jupyter Notebook ('SVM LiDAR tree classifier.ipynb').
To run this program you'll have to install Jupyter/Ipython Notebook.

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
