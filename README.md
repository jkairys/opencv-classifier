## Synopsis

A framework for training image classifiers based on the sharkshadows image library. At the time of writing this library consists of approximately 2,000 cropped images, each contain an object or class of object that could be expected at the beach. The framework allows you to generate a cascade image classifier using the OpenCV framework.

## Requirements
You will need:
* A local copy of the sharkshadows image library (cropped images are all that is required, you don't need originals)
* OpenCV version 3
* Python3

## Motivation

OpenCV appears to be a very capable platform, but the documentation is a bit... sparse / inconsistent. Perhaps I'm slow, but it has taken me about a month to get something working. Using this framework you should be up and running in minutes (plus training time, so let's say _days_).

## Code Example

To generate a classifier, clone this repository:

Then just run the script:
./bin/run.py --images=/opt/sharkshadows/img/samples/ --keyword=shark


## Installation

Just clone the repository and you're ready to go:
git clone repo-url train-classifier
cd train-classifier

## License

MIT
