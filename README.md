# Assumptions

I went through the entire Python course before writing these two lessons. Both build on concepts taught earlier in the course, so the main assumption I made was *where* each lesson slots into the existing course:

- **`enumerate()`** - Chapter 9 (Lists), right after Lesson 19 - Tuples.
- **List Comprehensions** - Chapter 9 (Lists), as the closing lesson (i.e. Lesson 25), after the multi-step list-builders.

<details>
<summary><b>Why <code>enumerate()</code> goes here</b></summary>

<br>

- It's the natural follow-up to Lesson 10 - No-Index Syntax and Lesson 11 - Find an Item. Those teach looping over a list *without* the index. `enumerate()` is the clean answer to "but what if I *do* need the index?", and a better way than `for i in range(len(items))` pattern the course uses in Lesson 9 - Counting and Lesson 12 - Find the Increase.
- Each pass of `enumerate()` hands you an `(index, value)` tuple that you unpack into two variables. Placing it right after Lesson 19 - Tuples means the student has just learned tuple unpacking, so the lesson can lean on it instead of explaining it from scratch.
- I deliberately *didn't* state in the lesson itself that `enumerate()` returns a tuple. Spelling that out would add a layer of detail that makes the lesson longer and a step harder than the course's usual level. And the task was to stay as close to the existing course style as possible.

</details>

<details>
<summary><b>Why List Comprehensions goes here</b></summary>

<br>

- List comprehension is shortcut for the "empty list -> loop -> append" pattern. Users should have written that pattern by hand many times first - which they have by the end of Chapter 9 (Lessons 7, 14, 21, 22, and 24).
- The `if` filter form pairs naturally with the filtering done in  Lesson 14 - Modulo and Lesson 22 - Filter Messages.
</details>

### Some improvements I want to suggest

I went through the entire python course and I found a few things that we can improve while going through the content:

- **Some lessons can be passed without actually doing the exercise**, because they grade the printed output / return value instead of what the code really does:

   - [Chapter 2, Lesson 7 "Basic Variable Types"](https://www.boot.dev/lessons/6f85fe3e-c2a4-42e2-b6ca-6d541170d0b1) - graded on the printed text, so I can just manipulate the string (print `"...is a/an int"`, leave the value a string) and still pass.
   - [Chapter 2, Lesson 8](https://www.boot.dev/lessons/9c216a9b-6467-4526-88f5-02678df98d77) - it says *"Do not hard-code the values into the string"*, yet a hard-coded sentence passes anyway (the lesson even admits it "happens to work").
   - [Chapter 6, Lesson 6](https://www.boot.dev/lessons/fe80bbfc-8725-42cc-807f-74ca1dd9de8b) - it asks for the `-=` operator, but `return current_health - damage` passes just as well.

   **We can fix this by without complicating the lessons** by grading what the code *is/does* rather than what it prints - like we can check the real value/type, and run several different inputs so one hard-coded answer can't match them all. For e.g. I reworked Chapter 2, Lessons 7 as a demo in [`/suggestions`](./suggestions). You'll see the gamed answers now fail.

- What if each course ended with a "final boss"? A set of assignments/quiz questions where an actual character is shown on screen, and every question you solve lands a hit - the more you get right, the more damage it takes, until it finally goes down. I think it would be super cool and fun for users.

- Some lessons in the middle of a course are really about how to use boot.dev itself (like [this](https://www.boot.dev/lessons/e4fac74c-9d67-41ad-a85c-c579cb3ad76f) and [this](https://www.boot.dev/lessons/cbd18c5e-236f-497a-a42e-e83810cc0f04)). I get the "reduce friction to getting started" angle, but tying them to one course means you'd have to repeat them in every course - otherwise someone who starts from a different course never sees them and misses out on these features. It might work better to have them into a short, skippable tutorial that pops up after the X lessons of each course, and track whether a user has already gone through it (a simple flag/cookie) so it's not shown again in their later courses.

- **Some quizzes are too easy because every option except the right one is too obviously wrong**, so you can pick the answer without understanding anything. For example:

   > Why is the variable called `radius` outside the function, but `r` inside?
   > - a) Because programming is needlessly hard and makes me wanna cry sometimes
   > - b) Because only the value of the variable is passed to the function. It is then assigned to a new variable called `r`
   > - c) Because all variables are called `r` inside functions
   > - d) Because all variables are automatically shortened to one letter inside functions

   We should make all four options *real misconceptions* a learner might actually hold, so getting it right means you understood it. And when someone picks a wrong one, have a pop up note explaining why that belief is wrong to steer them back on track.

   Like a better version would be:

   > Why is the variable called `radius` outside the function, but `r` inside?
   > - a) Because only the value of the variable is passed to the function. It is then assigned to a new variable called `r`
   > - b) Because `r` is just a shorter nickname for `radius` - it's the same variable.
   > - c) Because a function can't reuse a name from outside, so it needs a new one.
   > - d) Because the value is copied into `r` and `radius` is then deleted.

- When I was on a free tier account - the "Ask Boots" feature and the "Interview With Boots" feature fails with wrong error message. It gave me - `Unable to contact the Claude API... it should be back soon!`  - I was really confused about it - It should let me know that this is a paid feature.

Here are the Screenshots:

[!CH3 L2](./static/CH3-L2.png)
[!CH3 L8](./static/CH3-L8.png)

- Some assignments have a lot of variables that we need to copy from the text area to the terminal area. (eg. [Chapter 3, Lesson 16](https://www.boot.dev/lessons/7d07216c-d599-40c2-976e-b87027dd5f12)) - We should provide a feature to just double click on a variable name and it should copy it (instead of that painful `ctrl + shift + c` or `ctrl + c`), or even just single click - This is a feature implemented in [kodekloud](https://kodekloud.com/) (another platform I have used a lot) and its really helpful.

- I think we can also add executable code snippets, e.g. [Chapter 8, Lesson 6](https://www.boot.dev/lessons/f5ae3654-8363-436d-9858-51ac376251b6) - instead of this quiz question which I think is useless - not helping with anything. we could have had a code snippet of wrong indentation and one with correct indentation and asked the user to run both of them to learn what the error would look like.

It doesnt have to be code snippets , it could be snippets of logic. it will come in handy for lessons like [Logical Operators](https://www.boot.dev/lessons/a4a6409a-b55a-4e6f-ba0e-a995fbe7a3d8).

- The quiz in [this lesson](https://www.boot.dev/lessons/151c87c8-0a37-422b-945c-c0f886a1b7ee) doesn't really test anything - it just asks whether AND/OR/NOT are logical or bitwise operators. It would be stronger to actually check understanding: one question on what logical operators are, one on what bitwise operators are, and maybe a third on what AND/OR/NOT each do. The runnable-snippets idea would also fit perfectly here - it could replace the static examples in the lesson.

- [Chapter 7, Lesson 7](https://www.boot.dev/lessons/47ed07e2-2096-4b92-aea2-54f18df458cb) and [Chapter 7, Lesson 8](https://www.boot.dev/lessons/6e61347c-ff5e-453b-a35f-680e2775c0e3) share the same name and overlap heavily - Lesson 7 is basically repeated in Lesson 8. They should be merged into a single lesson.

- [This lesson](https://www.boot.dev/lessons/08ef99ed-f4b0-427d-bfcc-e6737e8dc141) and [this one](https://www.boot.dev/lessons/f0ea6348-63d8-4bda-bd7a-b82b2226d2b7) are quizzes even though they're set up as assignments - their type should be corrected. (The lessons right next to them are fine.)

- The first two lessons in the "Loops" chapter ([Lesson 1](https://www.boot.dev/lessons/81ebc973-32c2-40d3-92a0-97c594bff0ba) and [Lesson 2](https://www.boot.dev/lessons/a84740d3-9146-40c9-ae67-54486d171f60)) are almost identical - the "Whitespace Matters in Python!" section and the assignment repeat across both. They could be merged into a single lesson.

- Chapter 4 "Scope" only talks about global scope, it should have some quiz or a small assignment on showing the difference in global scope vs local scope.

- why not just move to the next lesson if one is complete - like have a 3 sec countdown that we are moving to next lesson if we dont want the user to immediately jump to next lesson, the user can cancel the countdown by pressing a key or clicking somewhere. I had to manually do `ctrl + .` during my speed run - I would prefer it happening automatically. 