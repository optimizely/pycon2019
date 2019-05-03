# Modern Solvers: Problems well-defined are problems solved

Speaker: Raymond Hettinger
PyCon Description: https://us.pycon.org/2019/schedule/presentation/149/
Slides: 



## Can we use our machines to make ourselves smarter

> "It is a human mind amplified by the instantaneous relays possible in a computer" -  Lt Cmdr Spock in "The Ultimate Computer"

Raymond Hettinger: "It was not a good episode, but that stuck with me forever."


## Problems well defined are problems solved

> It's easier to make rules than to find a way to solve them.  Put a description of a problem into a solution finder.

- depth-first search, 
- then SAT solvers and how to access them from the Python world
- reinforcement learning 
- Temporal Logic with TLA and Z3
- Generic MCTS with CNN (convolutional neural networks) and Reinforcement Learning

Keep in mind the generic solutions outclassed the custom solutions over time.


## What to keep in  mind as we explore

- The examples are fun toy problems at the periphery of human capability, stretch your imagination to solve even harder problems with the same tooling


##  Depth First Search and Breadth First Search

Both easy to implement with `collections.deque()`

- prepend to queue or appended to queue for dfs or bfs respectively.

## Generic Puzzle Solver

Raymond built one a long time ago

- Subclass the solver and add extra information, 
    1. initial position, 
    1. rule to generate all possible moves for the next position, 
    1. are  we  at  the goal
- combinatorial explosion - exploit symmetry sometimes 
    - e.g. tic-tac-toe - teach computer that starting game with  top left corner is isomorphic to  lower left corner 

## Jug Filling Problem

3 jugs, 8, 5, 3 liters: find a sequence leaving four liters in the ?largest? jug

Use raymond's solver on the jug filler, get a shortest path solution

What if we have 10-20-30 jugs? Isomorphic to knapsack problem, exceeds human capability and eventually our computational power.


## Sliding Block Puzzle

"Never met anyone who could solve the puzzle except me. I wrote a computer program in basic."

> It is combinatorial with only one little exit door halfway through the graph. The second graph has only one exit door and many routes back to the first graph. Total puzzle is about 80 moves.

- Goal defined as a compiled regular expression, about 15-year-old code for Raymond (probably including translation from basic and basic code).

- Raymond runs this in Python 3.80


## SAT Solvers

Satisfiability Problems. Propositional Logic Formulas can be solved with this.  Write it in symbolic form.

If you would like to use this tool, use Raymond's slides to reacquire the necessary knowledge to write the logic in the necessary form.

If at least one row on the right side of the SAT table is true, then the problem is Satisfiable.

10 variables, 2^10,  20 variables, 2^20. With 1000 variabales, there are more states than molecules in the universe.

"Are there little problems inside we can exploit for real world problems?" - now we can solve some problems with over 10^6 variables

### Why do we care?

- see slides


## Python `pycosat` for SAT solving

Need to rewrite expression "Conjunctive Normal Form (CNF)" - a product of sums and Rs.

Negative case as -1, positive case as +1, then the next case a s -1,+2 or something. See slides

### Raymond wrote a tool to translate phrases we can understand into this format

Kind of difficult to start in Conjunctive Normal Form. We typically start in disjunctive normal form.

#### Raymond wrote a function from_dnf to go from  DNF->CNF

Also lets not use P, Q, R, lets just good python naming.

#### Raymond's Convenience Functions too

- some_of()
- one_of()
- none_of()

## Write a sudoku solver, it's interesting

Raymond: "I reject my earlier Sudoku solver. It is not as good as this. For a really tough sudoku, like 100x100 which your solvers would fail on, I just need to describe the problem and hand it to a Solver."


## Einstein puzzle

- None of the legends about this are true
- since there are a lot of uniques/sets, use one_of()
- there's a bijection
- Goal: "Who keeps the fish?"
- How do we solve it manually? I am profoundly UNINTERESTED in that at this point. - Raymond
- Interesting thing is how we describe the puzzle 
- always write helper functions that use from_dnf() as output, you can give humanistic problem statements to get to output
- picosat will be super fast to start using if you use my library... otherwise it will take a few days to get started
- Conda has to make decisions about conflicts and their dependencies. They use picosat as a sat solver for this problem.


## Pattern Recognition and reinforcement learning

See the link because he is going pretty fast and it's all there. I'll take any verbal notes.

Reinforcemnt Learning: Randomly try strategies. If they work, choose them more often.

- Getting my son to eat broccoli
- Rock Paper Scissors
  - unwinnable game but what if you can anticipate a particular opponent? this game is interesting with repeat play.
  - this thing will figure you out, no one will beat it (but i guess you could tie it with coin flips)
-  multi armed bandit approach scales and scales to more interesting games


## SMT and Model Checkers

Next step up for tree searchers and sat solvers:

- Satisfiability Modulo Theories (SMT) Problems
- State more complex than just truth tables
- Temporal Logic
- Searching a Graph instead of a tree


### Dining Philosophers

We need 10 chopsticks but they only have 5.

Interesting thing as that most peoples' solution sounds right but is always wrong. 

In education - shows how hard it is to create correct multithreaded code.

- Very easy to do unconstrained model.
- State space is 3^5, but we are interested in number of paths through the state tree...

One working strategy, keep a queue of who eats next,  and request to  eat if you  want to eat. When it becomes available, acquire left, acquire right, and eat, then release both.
 

#### Relationship to multithreaded code

How many of you have complex multithreaded code that is correct and that can prove that it is correct with a test suite?


#### Temporal Operators

Predicate P is always eventually true.


#### TLA+ Model Checker

See notes

There is a link to a nice writeup

#### Microsoft Z3

Z3py library gives you access to Z3 through the link in Raymond's talk


## AlphaZero

Learn to play most complex games, e.g. chess, with nothing except the rules.

Reinforcement learning - beat him game after game after game, my son is smart and will eventually beat me. This is how I learned chess from my father.

AlphaZero will let us compress 6 years of reinforcement learning into 6 hours.

Give AlphaZero rules for chess, then rules for shogi, then rules for Go.  In each case after 6-8 hours, AlphaZero learned to beat the best humans and computer programs in the world.  NOT CUSTOM FOR CHESS.

SO MANY DRAWS IN CHESS - against StockFish. Totally destroys it at about 1/3 wins, 2/3 draws, ?no? losses.

See Raymond's link to alphazero preprint on deepmind.

AlphaZero is NOT open source. Leela Chess is.  Python is not fast enough, C is not fast enough, can we do better? CUDA code on GPU.


## Monte Carlo Tree Search

See presentation content from Raymond.


## The future

> Difficult to predict the future is, always in motion." - Yoda

### Does this end badly?

- Kasparov - Deep Thinking: where Artificial Intelligence ends and human creativity begins
  - Does not think it will end badly


