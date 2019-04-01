# comet_tools [![Build status](https://travis-ci.com/umd-lhcb/comet_tools.svg?branch=master)](https://travis-ci.com/umd-lhcb)
A collection of COMET tools for various LHCb UT upgrade testings.


## `GbtxMemAnalyzer.py`
Analyze the elink signal transmission quality by analyze parsed elink tables.


## `GbtxMemParser.py`
Python library capable of parsing through exported memory files provided by the MiniDAQ. Each line in the memory file corresponds to the state of the GBTX's 7 elinks. This parser saves every single line and matches the states to their correct elink identifier using python dictionaries, then returns a neat list of these dictionaries to be used by **GbtxMemAnalyzer**. Each elink has a state that consists of a two-digit hexadecimal number. Written by Jorge Ramirez with oversight provided by Yipeng Sun.  


## `CsvGen.py`
Generate csv instruction sets to program COMET. For more technical details,
refer to the script source code. Prototyped by Raymond Su.
