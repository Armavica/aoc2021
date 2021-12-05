This repository holds my solutions for the 2021 Advent of Code.

While each day has its own module, some common utility functions live in the
`aoc2021` subdirectory.

To use the makefile:

* `make input` downloads the input of the day and places it into the
  appropriate directory, and displays its 10 first lines.
* `make` runs the program of the day on the input of the day (which
  consists in running `python -m XX XX/input` where XX is the day).
