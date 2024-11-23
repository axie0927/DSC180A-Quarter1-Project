# DSC180A-Quarter1-Project
This repo is my personal contribution to the overall Majorana Neutrino Hunt project. The full repository can be found [here](https://github.com/matthewsegovia/MajoranaNeutrinoHunt.git).

## Description
The goal of our overall project is to develop parameters that will be extracted from the time series data provided to us publicly by the Majorana Demonstrator experiement in order to propose machine learning models that meet the requirements outlined in the Neutrino Physics and Machine Learning (NPML) instructions included in the Majorana Demonstrator data release notes.

## Installation Instructions
How to clone the repository:
``` bash
git clone https://github.com/axie0927/DSC180A-Quarter1-Project.git
``` 

The requriements.txt file lists all the python packages as well as versions needed prior to running the code.

## Features
This repository contains the files for the parameters functions I created for my part of the . The Master.py file in the overall repository combines all the parameters created by each individual member of the project into one file. This file will be used in our Quarter 2 project where we utilize all the parameters created to train our machine learning models.

The parameter-exploration.ipynb file is the jupyter notebook file that I used for the process of creating my parameters. I then extracted my parameter functions into .py files which are pushed to the MajoranaNeutrinoHunt Github repository. The data files are not included in this repository due to the size of the files. 

All data files can be found [here](https://zenodo.org/records/8257027).

The parameters created include:

- **Drift Time** (tdrift50.py): The time taken from the initiation of charge generation to the collection at the detector's point contact at the threshold of 50%.

- **Delayed Charge Recovery** (dcr.py): The rate of area growth in the tail slope region. This is measured by the area above the tail slope to the peak of the rise. 

## Further Reading
[Majorana Demonstrator Data Release Notes](https://arxiv.org/pdf/2308.10856)
