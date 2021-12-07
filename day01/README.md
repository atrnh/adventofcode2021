# Day 1: Sonar Sweep

<small>
  <a href="https://adventofcode.com/2021/day/1">🔗 Advent of Code 2021: Day 1</a>
</small><br><br>

This isn't my first Advent of Code. I'm already familiar with the way these challenges are
generally structured. Each challenge has two parts but...!

*...you don't get to see Part 2 until you've solved Part 1.*

*This* is what I come to Advent of Code for &mdash; Part 2 is always a twist that'll
test the engineering choices you made in Part 1.

## Part 1

**The gist of Part 1:** given a list of measurements and count the number of times they
increase between one measurement and the next.

For example:

###### Here's the example list

<pre>
<del>199</del>
<b>200 ⌃</b>
<b>208 ⌃</b>
<b>210 ⌃</b>
<del>200 ⌄</del>
<b>207 ⌃</b>
<b>240 ⌃</b>
<b>269 ⌃</b>
<del>260 ⌄</del>
<b>263 ⌃</b>
</pre>

...this list gives us `7` increases.

### My solution

Whenever I approach the first part of any Advent of Code challenge, I try to anticipate
what might come next in Part 2...

Since we're doing *something* to one number and the
proceeding number, I guessed that the *something* might change.

If you've already solved this one, you'll know that I guessed wrong (this is exactly why
Advent of Code is fun though), but here's what I did:

```python
def do_with_next(iterable, func):
    results = []

    prev = None
    for el in iterable:
        if prev is not None:
            results.append(func(prev, el))

        prev = el

    return results
```

Then, we can count depth increases like so:

```python
def count_depth_incr(depths):
    increases = [
        1 if is_increased else 0
        for is_increased in do_with_next(depths, lambda x, y: x < y)
    ]
    return sum(increases)
```

## Part 2

**The twist in Part 2** wasn't to perform some other procedure on a number and its proceeding
number like I'd guessed; instead, it was to **take a rolling sum of measurements, 3
measurements at a time** and *then* count the depth increases.

So, as I mentioned earlier, I never got to take advantage of my (overengineered)
`do_with_next` function but I *was* able to save myself from writing a ton of new code by
borrowing from example code in the Python docs!

### My solution

I wanted to implement the *rolling sum* part of this challenge with
[`collections.deque`](https://docs.python.org/3/library/collections.html#deque-objects).
This is where skimming through documentation can really pay off &mdash; right below the
list of all `deque` methods, there's a little section called [`deque`
Recipes](https://docs.python.org/3/library/collections.html#deque-recipes) and in that
section, you'll find this example function called `moving_average`:

```python
def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n
```

This is almost exactly what I need (even down to the default width of the window being
`n=3`). With one small modification to `yield s` instead of `s / n`...

```python
def moving_sum(iterable, n=3):
    it = iter(iterable)
    d = deque(itertools.islice(it, n - 1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s
```

...we can count depth increases after taking a rolling sum of depths like so:

```python
def count_rolling_depth_incr(depths):
    rolling_depths = moving_sum(depths)
    return count_depth_incr(rolling_depths)
```