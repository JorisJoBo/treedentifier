[![Build Status](https://travis-ci.org/JorisJoBo/treedentifier.svg?branch=master)](https://travis-ci.org/JorisJoBo/treedentifier)
[![HitCount](http://hits.dwyl.io/JorisJoBo/treedentifier.svg)](http://hits.dwyl.io/JorisJoBo/treedentifier)

# Treedentifier
This project will be about an AI solution which will be capable of recognizing
tree species. The solution will learn what the characteristics of a specific species
based on training data that was provided earlier on. We will use LIDAR data of the Netherlands
to train our algorithm.

## Testing
You have to test your code first before pushing. Pushing while failing to do so, may result in failed builds.
For testing you should use [PyCodeStyle](https://github.com/PyCQA/pycodestyle).
To install PyCodeStyle, just execute:
```
pip install -r python-requirements.txt
```
(which will also install all other project required requirements for you)

When done, you can test your code with the following command:
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
