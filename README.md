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

- [ ] Day 5 -- [Day 5 Python File](Day_5.py) | [Part 2](Day_5-2.py)
  - Time: Part 1 took about 30 mins. Part 2 is incomplete- I'm overthinking diagonals.
  - Log: Had a silly little bug with enumerating the length of a spliced list (versus starting at the first index of that splice) which took me like 10 mins to find. Oops.

- [ ] Day 6 -- [Day X Python File](Day_6.py) | [Part 2](Day_6-2.py)
  - Time:
  - Log:

- [ ] Day X -- [Day X Python File](Day_X.py) | [Part 2](Day_X-2.py)
  - Time:
  - Log:

...