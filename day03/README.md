# Day 3: Binary Diagnostic

<sup>
  <a href="https://adventofcode.com/2021/day/3">🔗 Advent of Code 2021: Day 3</a>
</sup><br><br>

There's no explainer for Part 1 since it was pretty straightforward. Part 2 was *much*
more exciting.

## Part 2

In Part 2, we need to calculate oxygen and carbon dioxide ratings based on our puzzle
input. The procedure for calculating either rating generally follows the same algorithm
*but* they differ in ways that are more complex than can comfortably fit in a single expression.

In other words, we can use the same function to calculate the ratings and configure it
differently to handle oxygen vs. carbon dioxide (and vice versa). Imagine something like this:

```python
# Build functions to calculate oxygen rating & carbon dioxide rating
calculate_oxy = build_rating_calculator(lambda most, _: most, default=1)
calculate_co2 = build_rating_calculator(lambda _, least: least, default=0)

# Call functions, passing in puzzle input
oxy = calculate_oxy(inpt)
co2 = calculate_co2(inpt)
```

This calls for a function, `build_rating_calculator`, that takes in

- **`criterion`**, a function that's called with two arguments: the most commonly
  occurring bit, the least commonly occurring bit, and returns a number

- **`default`**, the default criterion to use if there's a tie between the most and least
  commonly occurring bits

...and builds and returns a function that does the actual rating calculation.

```python
def build_rating_calculator(criteria, default):
    def calculate_rating(mtx):
        pass

    return calculate_rating
```

Before tackling `build_rating_calculator` though, I wanted to take the parts involved
with calculating criteria for the rating calculators and break them out into a helper
function:

```python
def calculate_crit(bits, criterion, default):
    most, most_count, least, least_count = chain.from_iterable(
        Counter(bits).most_common()
    )

    return criterion(most, least) if most_count != least_count else default
```

- The first expression is overengineered in the name of aesthetically-pleasing code.
  I wanted something that looked like:

  ```python
  [[most, most_count], [least, least_count]] = Counter(bits).most_common()
  ```

  ...but [structural pattern matching-powered
  destructuring](https://www.python.org/dev/peps/pep-0622/) is only possible in Python
  3.10 and, sadly, I'm on Python 3.9 😳.

  So, as a bit of a hack, I'm using [`chain.from_iterable`](https://docs.python.org/3/library/itertools.html?highlight=chain#itertools.chain.from_iterable) to flatten and unpack values
  from
  [`Counter(bits).most_common()`](https://docs.python.org/3/library/collections.html?highlight=counter#collections.Counter.most_common).
- The returned expression:
  ```python
  criterion(most, least) if most_count != least_count else default
  ```
  ...says to return the result of `criterion` *unless* `most_count` and `least_count` are
  tied, in which case, we should return `default` instead.

With the help of `calculate_crit` and a couple other helper functions I wrote during Part
1, `build_rating_calculator` is relatively easy:

```python
def build_rating_calculator(criterion, default):
    def calculate_rating(mtx):
        candidates = mtx[:]
        i = 0

        while len(candidates) > 1:
            transposed = transpose(candidates)
            bits = transposed[i]
            crit = calculate_crit(bits, criterion, default)

            candidates = list(
                compress(candidates, bits if crit else toggled_bits(bits))
            )
            i += 1

        return candidates[0]

    return calculate_rating
```