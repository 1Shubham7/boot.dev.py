# Enumerate

Remember the clean "no-index" syntax for looping over a list?

```python
items = ["sword", "shield", "potion"]
for item in items:
    print(item)
```

It's elegant, but it throws away the index. Sometimes you need *both* the index and the value at the same time. You could reach back for the clunky `range(len(items))` approach:

```python
items = ["sword", "shield", "potion"]
for index in range(len(items)):
    print(f"{index}: {items[index]}")
# Prints:
# 0: sword
# 1: shield
# 2: potion
```

That works, but Python gives us something cleaner: the built-in `enumerate()` function.

```python
items = ["sword", "shield", "potion"]
for index, item in enumerate(items):
    print(f"{index}: {item}")
# Prints:
# 0: sword
# 1: shield
# 2: potion
```

On each pass through the loop, `enumerate()` hands you the index *and* the value together.

## Choosing Where to Start

The index starts at `0` by default, just like list indexes. Pass a second argument to start counting somewhere else:

```python
heroes = ["Aria", "Bjorn", "Cassius"]
for place, hero in enumerate(heroes, start=1):
    print(f"{place}: {hero}")
# Prints:
# 1: Aria
# 2: Bjorn
# 3: Cassius
```

Notice that `start` only changes the *number* `enumerate()` counts out - it doesn't skip any items. We still loop over the whole list beginning with the very first hero (`Aria`); she's just labeled `1` instead of `0`. The `start` value is a counter, not a starting index into the list.

## Assignment

Players want to see a nicely numbered quest log in their Fantasy Quest journal.

Complete the `get_quest_log` function. It takes a list of quest names (strings) and returns a *new* list of strings, where each quest is numbered starting at `1`.

Here's an example of how your `get_quest_log` function should work when called:

```python
quests = ["Slay the dragon", "Find the lost amulet", "Rescue the merchant"]
log = get_quest_log(quests)
print(log)
# ['1. Slay the dragon', '2. Find the lost amulet', '3. Rescue the merchant']
```

Use `enumerate()` with a `start` value so you don't have to keep track of the number yourself.
