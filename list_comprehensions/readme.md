# List Comprehensions

By now you've written this pattern multiple times: create an empty list, loop over some data, and append a new value on each pass.

```python
damage_rolls = [10, 25, 50, 75]
doubled = []
for roll in damage_rolls:
    doubled.append(roll * 2)
print(doubled)
# Prints: [20, 50, 100, 150]
```

Python has a compact shortcut for this pattern, called *list comprehension*. The same code collapses into a single line:

```python
damage_rolls = [10, 25, 50, 75]
doubled = [roll * 2 for roll in damage_rolls]
print(doubled)
# Prints: [20, 50, 100, 150]
```

The shape of a list comprehension is:

```python
[expression for item in iterable]
```

The `expression` is what each new element will be. Read our example as: "give me `roll * 2` (expression), for each `roll` in `damage_rolls`."

## Adding a Condition

You can also add an `if` to the end to keep *only* the items you care about:

```python
[expression for item in iterable if condition]
```

For example, to keep only the rolls that landed above `20`:

```python
damage_rolls = [10, 25, 50, 75]
big_hits = [roll for roll in damage_rolls if roll > 20]
print(big_hits)
# Prints: [25, 50, 75]
```

Only the items where `condition` is `True` make it into the new list.

## Don't Overdo It

Comprehensions are powerful, but they aren't always the right call. If a comprehension gets so long or so deeply nested that it's hard to read at a glance, a plain `for` loop is the better choice. Clean code beats clever code.

## Assignment

In Fantasy Quest, a critical hit lands for *double* damage. The combat system rolls a damage number for every attack, and any roll of `50` or higher counts as a critical hit.

Complete the `get_critical_hits` function. It takes a list of damage rolls (integers) and returns a *new* list containing the final damage of each critical hit, with every critical roll doubled.

Here's an example of how your `get_critical_hits` function should work when called:

```python
damage_rolls = [12, 75, 40, 100, 9]
crits = get_critical_hits(damage_rolls)
print(crits)
# [150, 200]
```

Use a single list comprehension with an `if` condition to build the list.
