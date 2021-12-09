# Advent of Code 2021 - Mark Bacon

Advent of Code submissions for 2021. They've started off pretty easy so I feel pretty good about getting them done.

## Information

At least until the 17th or 18th, these solutions won't be very creative. Once my final papers wrap up, I look forward to [livestreaming these on my YouTube Channel](https://www.youtube.com/markbacon78) as a part of a series I'll be starting called "Leetcode Livestreams" (but I'll probably need to think of a different name). A nice, creative way to kick things off!

Make sure to try challenges on your own before you do this. I'll start commenting the code when it gets unreadable. If you want comments or explanations, reach out to me on [Twitter at @Mobkinz78](http://www.twitter.com/Mobkinz78) and I'll add those! It might not be as readable for beginners as I realize.

Lastly, I chose Python because it's a quick language and I'm looking to get very good at it for interview questions in the inevitable future. Thanks for stopping by!

## 目次 Table of Contents

- [x] Day 1 -- [Day 1 Python File](Day_1.py) | [Part 2](Day_1-2.py)
  - Time: 6 minutes
  - Log: Very straightforward. Just iterating through lines and adding up the respective numbers. I believe I had to add 1 before submitting the response due to an issue with the last index I wasn't feeling like fixing.

- [x] Day 2 -- [Day 2 Python File](Day_2.py) | [Part 2](Day_2-2.py)
  - Time: 9 minutes
  - Log: That shouldn't have taken me that long. Nonetheless, I would like to revisit this one to see if there's a more brief solution, but honestly I think this might just be as concise as it gets for efficient yet readable code (but with Python... you never know what secrets lay hidden beneath).

- [x] Day 3 -- [Day 3 Python File](Day_3.py) | [Part 2](Day_3-2.py)
  - Time: 13 minutes for part 1, 24 for part 2
  - Log: Part 1 was easy... part 2 took a lot of parsing in my head to figure out what it was eveng asking me haha. When you read the example case, it's really not that bad. Part two took a little more debugging, and I realized I had to count the bits for the updated lists (versus keeping the count of all the numbers). You could definitely combine the two loops I have here into one when you get both ratings, and would definitely be more optimal as a result, but for now I'll leave it as-is.

- [x] Day 4 -- [Day 4 Python File](Day_4.py) | [Part 2](Day_4-2.py)
  - Time: 36 minutes for part 1
  - Log: Everything just had a lot of moving parts but ended up getting part 1 first try. I thought part 2 was going to be really easy but you need to find out how to get the last winning board without constantly editing the boards... and I took a break at that point. Ended up coming back and the solution was trivial. Save all of the winning boards and when a board wins, just pop it from the dictionary.

- [x] Day 5 -- [Day 5 Python File](Day_5.py) | [Part 2](Day_5-2.py)
  - Time: Part 1 took about 30 mins. And finally on day 7... he figured out diagonal lines.
  - Log: Had a silly little bug with enumerating the length of a spliced list (versus starting at the first index of that splice) which took me like 10 mins to find. Oops. Did the long way for diagonal line comparisons since the shortcut didn't seem to be working out for me. I'll leave as-is for now, maybe revisit to make shorter. But alas... I've got two days to catch up on!

- [x] Day 6 -- [Day X Python File](Day_6.py) | [Part 2](Day_6-2.py)
  - Time: 21 minutes for part 1, part 2 was like 5 mins after I realized the non-recursive solution.
  - Log: Getting the 'formula' for part 1 took me a second, as I had to add an extra day and extra age based on the fact I decremented before the logic, but otherwise the recursive solution on each fish is what worked for me. Seeing as part 2 is taking... ages... to run for the test cases, we'll do something more straightforward based on days, not fish in the input. Still takes a while, but it's shorter. Shoutout to @esilverm for the hint on optimizing it more.

- [x] Day 7 -- [Day 7 Python File](Day_7.py) | [Part 2](Day_7-2.py)
  - Time: 6 minutes for part 1. About 13 for part 2, did it in a class oops.
  - Log: I just figured that I could find the median... and then that worked. You'll see why it took me 6 minutes if you look at the code. This... doesn't work for part 2. I just brute forced part 2 but I do want to come back to see the 'proper' way of doing this because it took a while haha.

- [ ] Day 8 -- [Day 8 Python File](Day_8.py) | [Part 2](Day_8-2.py)
  - Time:
  - Log:

- [x] Day 9 -- [Day 9 Python File](Day_9.py) | [Part 2](Day_9-2.py)
  - Time: 13 minutes for part 1
  - Log: Day 1 (part 1) was super easy. Will be cool to see if there's some graph approach to this versus all those conditionals I wrote. Part 2 is similar, and I smell a graph solution being required. Part 2 took me about an hour, and about 40 of those minutes were spent messing with recursion. Then I more or less recalled BFS! Proud of myself, lol.

- [ ] Day X -- [Day X Python File](Day_X.py) | [Part 2](Day_X-2.py)
  - Time:
  - Log:

...
