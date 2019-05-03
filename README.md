# GV Code Challenge

## Installation Instructions
This program utilizes Python (3.4) and one of its' standard libraries 'sys'. 

If you don't already have Python installed, you can head [here](https://www.python.org/downloads/release/python-340/) and download the current version, which is the only dependency for this project.

#

## How to run
Now that you have the correct Python version installed, it's time to run the program.

The simplest way to execute this program is at the command line
```
python3.4 main.py <test file>.txt
```

The most important thing here, is that the input file is provided or else the program will exit with nothing to show. I have a test file included so you can examine the format and use it to test on your own.

#

## Input File Formatting
My program is designed to take a `.txt` file as the input set, which is structured as comma separated value ranges.

For example, if the user watched from timestamp 1000 to 4000, and timestamp 5500 to 6350, the file would be structured like:

```
1000-4000, 5500-6350
```

And the UVT ('unique view time') would be 3850.

## Testing
Currently, the program tests itself by running the input through an alternate algorithm and checking the results against itself. The alternate algorithm is much less efficient but functions to generate identical output, so it is adequate for testing smaller sets currently.
