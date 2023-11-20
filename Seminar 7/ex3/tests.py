from statistics import Statistics
from auto import Auto

def test_count_color():
    s = Statistics()
    autos = [ Auto('m1', 'm2', 1000, 'red'),
              Auto('m1', 'm2', 1000, 'blue'),
              Auto('m1', 'm2', 1000, 'red')
            ]
