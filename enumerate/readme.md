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
for i in range(len(items)):
    print(f"{i}: {items[i]}")
# Prints:
# 0: sword
# 1: shield
# 2: potion
```

That works, but Python gives us something cleaner: the built-in `enumerate()` function.

```python
items = ["sword", "shield", "potion"]
for i, item in enumerate(items):
    print(f"{i}: {item}")
# Prints:
# 0: sword
# 1: shield
# 2: potion
```

On each pass through the loop, `enumerate()` hands you the index *and* the value together, so you never have to index back into the list yourself.

## Starting at a Different Number

By default the index starts at `0`, just like normal list indexes. If you'd rather start counting somewhere else, pass a `start` value as the second argument:

```python
players = ["Aria", "Bjorn", "Cassius"]
for rank, player in enumerate(players, start=1):
    print(f"{rank}. {player}")
# Prints:
# 1. Aria
# 2. Bjorn
# 3. Cassius
```

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
