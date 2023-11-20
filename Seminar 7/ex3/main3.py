from trei.statistics import Statistics
from trei.auto import Auto
from trei.tests import test_count_color

def main():
    s = Statistics()
    auto= [ Auto('m1', 'm2', 10000,'red'),
            Auto('m1','m2', 1000, 'blue'),
            ]
    color = 'red'
    print(f' red autos= {s.count_color(auto,color)}')

    print(f' avg year= {s.avg_year(auto, 'm1')}')

test_count_color()
main()
