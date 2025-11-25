from Shortcuts.parse import *
from collections import Counter
from collections import deque
import numpy as np
import re
import networkx as nx
import sys
import heapq
from math import *
import itertools as it
from copy import deepcopy

abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def printTotal(totals):
    print(f"Part 1: {totals[0]}")
    print(f"Part 2: {totals[1]}")