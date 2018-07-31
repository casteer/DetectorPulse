# DetectorPulse

Python code which plots a simplified pulse and noise as an example pulse from a photomultiplier tube.

It can be used to study the effect of pulse pile-up on the observed signal shape by adding in additional pulses (some are given but commented out) and the effect of better or worse timing resolution on the signal shape. 

This could also be used as the basis to examine how often a given pulse discrimination threshold would produce a logical pulse and the spread in trigger times (time-walk). This part hasn't been written (feel free to have a go - if you do, please let me know)

In order to create the plot, use the command _python DetectorPulse.py_ within a terminal. It has been tested under Ubuntu 18.04. 

This python code requires a number of libraries that can be found at the start of the DetectorPulse.py file when they are imported. 

Hope you find it interesting and/or useful!
