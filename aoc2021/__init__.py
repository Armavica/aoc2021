import numpy as np
import fileinput as fi

def lines(template="s"):
    """
    Read all lines of input, either stdin or files on sys.argv[1:], and convert
    them according to the template ("s" for string, "i" for integer and "f" for
    float).

    # Returns
    List of parsed lines
    """
    fcts = {"s": str, "i": int, "f": float}
    l = [[fcts[t](x) for t, x in zip(template, line.rstrip().split())]
         for line in fi.input()]
    # If only one field per line, simplify the output
    if len(template) == 1:
        l = [x[0] for x in l]
    # If only numerical data, return a numpy array
    if "s" not in template:
        l = np.array(l)
    return l

