# Assumptions

I went through the entire Python course before writing these two lessons. Both build on concepts taught earlier in the course, so the main assumption I made was *where* each lesson slots into the existing course:

- **`enumerate()`** - **Chapter 9 (Lists)**, right after **Lesson 19 - Tuples**.
- **List Comprehensions** - **Chapter 9 (Lists)**, as the closing lesson (i.e. **Lesson 25**), after the multi-step list-builders.

<details>
<summary><b>Why <code>enumerate()</code> goes here</b></summary>

<br>

- It's the natural follow-up to **Lesson 10 - No-Index Syntax** and **Lesson 11 - Find an Item**. Those teach looping over a list *without* the index. `enumerate()` is the clean answer to "but what if I *do* need the index?", and a better way than `for i in range(len(items))` pattern the course uses in **Lesson 9 - Counting** and **Lesson 12 - Find the Increase**.
- Each pass of `enumerate()` hands you an `(index, value)` **tuple** that you unpack into two variables. Placing it right after **Lesson 19 - Tuples** means the student has just learned tuple unpacking, so the lesson can lean on it instead of explaining it from scratch.
- I deliberately *didn't* state in the lesson itself that `enumerate()` returns a tuple. Spelling that out would add a layer of detail that makes the lesson longer and a step harder than the course's usual level. And the task was to stay as close to the existing course style as possible.

</details>

<details>
<summary><b>Why List Comprehensions goes here</b></summary>

<br>

- List comprehension is shortcut for the **empty list -> loop -> append** pattern. Users should have written that pattern by hand many times first - which they have by the end of Chapter 9 (Lessons 7, 14, 21, 22, and 24).
- The `if` filter form pairs naturally with the filtering done in  **Lesson 14 - Modulo** and **Lesson 22 - Filter Messages**.
</details>
