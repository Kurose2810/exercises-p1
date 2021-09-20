import numpy as np

_HEADINGS_='headings'
_DATA_='data'

def create_table(*headings):
    table = {_HEADINGS_: headings, _DATA_: []}
    return table

def append(table, row):
    if len(table[_HEADINGS_]) != len(row): return
    table[_DATA_].append(row)

def headings(table):
    return table[_HEADINGS_]

def data(table):
    return np.array(table[_DATA_])

def sum_col(table, col, dtype=np.float):
    arr = np.array(table[_DATA_])
    return arr[:,col].astype(dtype).sum()

def sum_cols(table):
    arr = np.array(table[_DATA_])
    return arr.sum(axis=0)
