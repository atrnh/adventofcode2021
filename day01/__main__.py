import sys

from . import count_depth_incr, count_rolling_depth_incr

if __name__ == "__main__":
    depths = [int(line) for line in sys.stdin.readlines()]

    # Part 1
    print(count_depth_incr(depths))

    # Part 2
    print(count_rolling_depth_incr(depths))
