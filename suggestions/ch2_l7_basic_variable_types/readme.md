# Basic Variable Types

Python has a few basic data types you'll use constantly:

- **String** (`str`) - text, wrapped in quotes: `"Gandalf"`
- **Integer** (`int`) - a whole number, no quotes: `42`
- **Float** (`float`) - a number with a decimal part: `72.5`
- **Boolean** (`bool`) - either `True` or `False`

The quotes are what matter most here. `"100"` is a *string* (text that happens to look like a number), while `100` is an *integer* you can do math with. In the same way, `"True"` is a string, but `True` is a boolean.

```python
health = 100        # int
name = "Gandalf"    # str
mana = 72.5         # float
has_magic = True    # bool
```

## Assignment

A Fantasy Quest character's stats were set up with the wrong types - a couple of values are stored as strings by mistake.

Fix the two variables so each holds the correct type:

- `player_health` should be an `int` with the value `100`
- `player_has_magic` should be a `bool` with the value `True`

Don't wrap the values in quotes. The tests check the *real type* of each variable, not how it looks when printed - so printing the right words won't pass; the variable itself has to be the correct type.
