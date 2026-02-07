---
title: H3 Game Theory Session 3
published: 2026-01-23
description: "SMU H3 Game Theory Session 3 Notes"
tags: ["Game Theory", "Economics", "SMU H3"]
category: Notes
draft: false
---

# SMU H3 Map

* Content map: [SMU H3 Game Theory Map](/posts/syllabus/smu-h3-study-map/)

---


# Golden Balls
## Players
* 2 players
* Both players have the same strategies (options)

## Information Structure
* Simultaneous Game
* Both players decide on their strategy and make it known to the other player at the same time

## Strategy
* 2 Players can choose to either **split** or **steal**
* $ \{split, steal\} $

## Outcomes
* If the players choose to *split*, both players get half the prize each
* If one player chooses to *steal* and the other player chooses to *split*, the player who chooses to *steal* receives all of the prize
* If both players choose to *steal*, both players get nothing

## Payoffs
### Summary
$ \text{let } p \text{ be the total prize available to both players} $
$$ 
(split, split) \rightarrow (\frac{p}{2}, \frac{p}{2}) \quad

(split, steal) \rightarrow (0, p)
$$

$$
(steal, split) \rightarrow (p, 0) \quad

(steal, steal) \rightarrow (0, 0)
$$

### Payoff Matrix
| P1 \ P2 |  Split   |  Steal |
| --- | --- | --- |
| Split | $\frac p 2, \frac p 2$ | $0, p$ |
| Steal | $p, 0$ | $0, 0$ |

#### Outcomes
* When the other player chooses **split**, choosing **steal** is better than split
* When the other player chooses **steal**, choosing **steal** is as equally good/bad as **split**

#### Conclusions
* Steal is **never worse**, but **sometimes better** than split
* Steal is a **weakly <u>dominant</u> strategy**
* Split is a **weakly  <u>dominated</u> strategy**

# Black or Red

## Instructions
* You will be asked to choose between red or black. 
* Your earnings are determined by the colour that you choose and by the colour chosen by the person matched with you. 
  * If you each play red, you will each earn 2 participation points. 
  * If you each play black, you will each earn 3 participation points. 
  * If you play black and the other person plays red, then you earn zero and the other person earns 5 participation points. 
  * If you play red and the other person plays black, you earn 5  participations points, and the other person earns zero.

## Players
* 2 players
* Both players have the same strategies (options)

## Information Structure
* Simultaneous Game
* Both players decide on their strategy and make it known to the other player at the same time


## Strategy
* 2 players can choose to either **red** or **black**


## Payoff Matrix

| P2 \ P1         |  Red   | Black  | Payoff (P2) |
| --- | --- | --- | --- |
| **Red**         |  2, 2  |  5, 0  |    2 / 5    |
| **Black**       |  0, 5  |  3, 3  |    0 / 3    |
| **Payoff (P1)** |  2 / 5 |  0 / 3 |     --      |

---

# Dominant and Dominated Strategy
## Dominant Strategy
* A strategy that does better than all other strategies no matter the other player's actions
* This means the strategy is **independent** of what the other player(s) perform
* A rational player will **always choose a dominant strategy**

## Justification for Dominant Strategy
* Given **common knowledge**, since the player knows that the other player will play a dominant strategy, the current player will change their strategy to outperform him
* In many cases, this would be to not play a dominanted strategy, and play a **dominant strategy**

## Existence of Dominated Strategies
* In many games, there might not be a **dominant strategy**
* However, there exists **dominated strategy** which consistently performs worse than other possible strategy

## Implications of Dominated Strategies
* We can delete dominated strategies from the game
* If new dominated strategies arise from this, we can delete them too

## Iterative Deletion of Dominated Strategies

### Initial Payoff
| P1 \ P2 | **X** | **Y** | **W** | **Z** |
| :---: | :---: | :---: | :---: | :---: |
| **A** | 4, 5 | 5, 4 | 0, 3 | 6, 2 |
| **B** | 3, 4 | 4, 3 | 5, 2 | 0, 0 |
| **C** | 2, 4 | 3, 3 | 4, 2 | 2, 1 |
| **D** | 1, 0 | 2, 2 | 3, 0 | 1, 4 |

### Iteration
* From the original case, **D** is dominated by **C**

| P1 \ P2 | **X** | **Y** | **W** | **Z** |
| :---: | :---: | :---: | :---: | :---: |
| **A** | 4, 5 | 5, 4 | 0, 3 | 6, 2 |
| **B** | 3, 4 | 4, 3 | 5, 2 | 0, 0 |
| **C** | 2, 4 | 3, 3 | 4, 2 | 2, 1 |

* **Z** is dominated by **W**

| P1 \ P2 | **X** | **Y** | **W** |
| :---: | :---: | :---: | :---: |
| **A** | 4, 5 | 5, 4 | 0, 3 |
| **B** | 3, 4 | 4, 3 | 5, 2 |
| **C** | 2, 4 | 3, 3 | 4, 2 |

* **W** is dominated by **Y**

| P1 \ P2 | **X** | **Y** |
| :---: | :---: | :---: |
| **A** | 4, 5 | 5, 4 |
| **B** | 3, 4 | 4, 3 |
| **C** | 2, 4 | 3, 3 |

* **C** is dominated by **B**

| P1 \ P2 | **X** | **Y** |
| :---: | :---: | :---: |
| **A** | 4, 5 | 5, 4 |
| **B** | 3, 4 | 4, 3 |

* **Y** is dominated by **X**

| P1 \ P2 | **X** |
| :---: | :---: |
| **A** | 4, 5 |
| **B** | 3, 4 |

* **B** is dominated by **A**

| P1 \ P2 | **X** |
| :---: | :---: |
| **A** | 4, 5 |

* It can be concluded that the optimal strategy is for P1 to select **A**, P2 to select **X**
* This is unconditionally the best option for both players

---

# Nash Equilibria
## Definition
* Nash equilibria refers to the state which is the **best response** given the **response of other players**
* In a Nash equilibrium state, **no player can benefit by changing their strategy alone**, meaning that each player’s strategy is the **best response** to others’ strategies

## Methods of Analysis
### (1) Best Response Analysis
* Iterate through every possible strategy
* Identify the best response of both players given the choice made by the opposing player
* Record these responses in the payoff matrix
* If both payoffs are recorded, this strategy is a **Nash equilibrium**

### (2) Guess and Verify
* Give a random strategy for both players
* Identify whether this is an equilibria using best response
* If this is not the best response to either (or both), this is not a **Nash equilibrium**

## Notes
* Nash Equilibrium is a pair of <u>**strategies**</u>, NOT payoffs
* A dominant strategy is the Nash Equilibrium

## Best Response

### Initial State

| P1 \ P2 | L | C | R |
| :---: | :---: | :---: | :---: |
| **T** | -2, 1 | -1, 2 | 2, 0 |
| **M** | 2, 2 | -2, 0 | 1, -1 |
| **B** | 1, 4 | -3, 6 | 0, 8 |

### Conditional Strategy

#### Player 1
* If P2 chooses L, the best strategy for P1 is M for a payoff of 2
* If P2 chooses C, the best strategy for P1 is T for a payoff of -1
* If P2 chooses R, the best strategy for P1 is T for a payoff of 2

#### Player 2
* If P1 chooses T, the best strategy for P2 is C for a payoff of 2
* If P1 chooses M, the best strategy for P2 is L for a payoff of 2
* If P1 chooses B, the best strategy for P2 is B for a payoff of 8

| P1 \ P2 | L | C | R |
| :---: | :---: | :---: | :---: |
| **T** | -2, 1 | **-1**, **2** | **2**, 0 |
| **M** | **2**, **2** | -2, 0 | 1, -1 |
| **B** | 1, 4 | -3, 6 | 0, **8** |

#### Analysis
* For $(T, C)$ and $(M, L)$: this is the **best strategy** for P2 given what P1 does AND for P1 given what P2 does
* Neither player has an incentive to change their strategy given what the other player does

---

# First-Price Sealed Bid Auction

## Terminology
* Bidders: $ P_1, P_2 $
* Bids: $ b_1, b_2 $
* Willingness to Pay: $ V_1, V_2 $

## Players
* 2 Bidders, P1 and P2
* $ V_1 = 100 $ is the willingness to pay for the object by P1
* $ V_2 = 250 $ is the willingness to pay for the object by P2

## Information Structure
* Players **simultaneously** submit bids in the form of $0, 0.1, 0.2, ...$
* Both players know their own and each others' willingness to pay
* The **highest bidder wins the object** and pays their bid, the **lower bidders do not get the object** and do not pay
* In case of a tie, a winner is **selected at random**

## Payoffs
* Payoffs are represented by the consumer surplus derived form consuming the object

$$
\pi_1
\begin{cases}
V_1 - b_1 \quad \text{if} \quad b_1 > b_2 \\
0 \quad \text{if} \quad b_1 < b_2 \\
\frac{V_1 - b_1}{2} \quad \text{if} \quad b_1 = b_2
\end{cases}
$$

$$
\pi_2
\begin{cases}
V_2 - b_2 \quad \text{if} \quad b_2 > b_1 \\
0 \quad \text{if} \quad b_2 < b_1 \\
\frac{V_2 - b_2}{2} \quad \text{if} \quad b_2 = b_1
\end{cases}
$$

## Guess and Verify
### Guess #1
* $(100, 100.1)$ 

### Outcome #1
* P2 Wins
* $\pi_1 = 0$
* $\pi_2 = 250 - 100.1 = 149.9$

### Verify #1

* P1 can choose three options:
  * $ b_1 < 100 $: P2 still wins, so $ \pi_1 = 0 $ 
  * $ b_1 = b_2 = 100.1 $: 50/50 chance of winning, so $ \pi_1 = \frac{100 - 100.1}{2} < 0 $
  * $ b_1 > 100.1 $: P1 wins, so $ \pi_1 = 100 - b_1 < 0 \quad (\because b_1 > 100.1)$

* P2 can choose three options:
  * $ b_2 < 100 $: P1 wins, so $ \pi_2 = 0 $ 
  * $ b_2 = b_1 = 100 $: 50/50 chance of winning, so $ \pi_1 = \frac{250 - 100}{2} = 75 < 149.9 $
  * $ b_2 > 100.1 $: P1 wins, so $ \pi_2 = 250 - b_2 < 149.9 \quad (\because b_2 > 100.1)$

* $(100, 100.1)$ is a Nash Equilibrium

### Guess #2
* $(99.9, 100)$ 

### Outcome #2
* P2 Wins
* $\pi_1 = 0.01$
* $\pi_2 = 250 - 100 = 150$

### Verify #2

* P1 can choose three options:
  * $ b_1 < 99.9 $: P2 still wins, so $ \pi_1 = 0 $ 
  * $ b_1 = b_2 = 100 $: 50/50 chance of winning, so $ \pi_1 = \frac{100 - 100}{2} = 0 $
  * $ b_1 > 100 $: P1 wins, so $ \pi_1 = 100 - b_1 < 0 $

* P2 can choose three options:
  * $ b_2 < 99.9 $: P1 wins, so $ \pi_2 = 0 $ 
  * $ b_2 = b_1 = 99.9 $: 50/50 chance of winning, so $ \pi_1 = \frac{250 - 99.9}{2} = 75.05 < 149.9 $
  * $ b_2 > 100 $: P2 wins, so $ \pi_2 = 250 - b_2 < 150 $

* $(99.9, 100)$ is a Nash Equilibrium

---

# Take-Home Problems

## Take-Home Problem 1

### <p style="text-align: centre;"><i>"For the beauty contest, is the choice of 100 dominated by 99, 99 dominated by 98, 98 dominated by 97, 97 dominated by 96 and so on?"</i></p>

### Guess and Verify
$$ \text{for simplicity, let there be 2 players in the game} $$

$$ \text{let } c_1 \text{ and } c_2 \text{ be the numbers chosen by P1 and P2 respectively} $$

$$ \text{let } m \text{ be the mean of } c_1 \text{ and } c_2 $$

$$
m = \frac{c_1 + c_2}{2}
$$

$$ \text{let } d_1 \text{ and } d_2 \text{ be the difference between } m \text{ and } c_1 \text{ and } c_2 \text{ respectively} $$

$$
d_1 = \bigg| c_1 - \frac{m}{2} \bigg| \\
d_2 = \bigg| c_2 - \frac{m}{2} \bigg|
$$

* Winning conditions are as follows:
$$
\text{winner}
\begin{cases}
\text{tie} \quad \text{if } c_1 = c_2 \text{ or } d_1 = d_2 \\
P1 \quad \text{if } d_1 < d_2 \\
P2 \quad \text{otherwise}
\end{cases}
$$

| P1 \ P2 | $ c_2 = 100 $ | $ c_2 = 99 $ | $ c_2 = 98 $ | ... | $ c_2 = 33 $ |
| :-: | :-: | :-: | :-: | :-: | :-: | 
| $ c_1 = 100 $ | $ d_1 = d_2 = 0 $| $ d_1 = 50.25 \\ > \\ d_2 = 49.25 $| $ d_1 = 50.5 \\ > \\ d_2 = 48.5 $ | $ ... $ | $ d_1 = 66.75 \\ > \\ d_2 = 0.25 $ |

* $ c_1 = 100 $ is dominated by $ c_1 \in \{0, 1, 2, ..., 99\}$ 
* Since you are comparing $ c_1 $ and $ c_2 $ with $ \frac{m}{2} $, any $ c \text{ s.t. } c = max(c_1, c_2) $ is a dominated strategy
* Choosing a lower number where $ c > \frac{m}{2} $ will decrease the distance of $ c $ from $ \frac{m}{2} $

### Macroscopic Perspective
* If players in the beauty contest chose numbers at random, the mean $ m = \frac{1}{n} \sum^{n}_{i=0} c_i = 50 $, with the target $ \frac{m}{2} = 50 $
* This means all strategies where $ c > 50 $ are strictly dominated
* Repeating this process:
  * Means will be $ m = 25, 12.5, 7.25, 3.625, 1.8125, ... $
  * Targets will be $ 12.5, 7.25, 3.625, 1.8125, 0.90625, ... $
* At every step, $ c > m $ are strictly dominated
* Since the sequence of $ m $ converges at $ 0 $, all strategies where $ c > 0 $ are dominated
* Thus, the strategy $ c = 0 $ is weakly dominant and is a Nash equilibrium

## Take-Home Problem 2
### For the First-Price Sealed Problem, show that bidding at $ b \ge V $ is a dominated strategy
$$ \text{let } V_1 = 100, V_2 = 250 $$
$$
\text{suppose } b_1 = 100.1: 
$$

$$ b_1 = 100.1
\begin{cases}
b_2 < 100.1: \pi_1 = -0.1 < 0 \\
b_2 = 100.1: \pi_1 = -0.05 < 0 \\
b_2 > 100.1: \pi_1 = 0
\end{cases}
$$

* It can be concluded that $ \pi \le 0 $ for $ b >  $
* This holds true for $ b \ge V $

### For the First-Price Sealed Problem, show that any bid $ (b, b + 0.1) $ where $ 100 \le b < 250 $ is also a Nash Equilibrium

$$ \text{let } V_1 = 100, V_2 = 250 $$

$$
\pi_2 = 250 - (b + 0.1) \\
\therefore \pi_2 \in [0, 149.9]
$$

| $ b_1 \le 100 $ | $ 100 < b_1 < b $ | $ b_1 = b + 0.1 $ | $ b_1 > b + 0.1 $ |
| :---: | :---: | :---: | :---: |
| $ \pi_1 = 0 $ | $ \pi_1 = 0 $ | $ \pi_1 = \frac{-0.1}{2} = -0.05  $ | $ \pi_1 = 100 - b_1 < 0 $ | 

* P1 has **no incentive to change his strategy** as the $ \pi_1 = 0 $, and all other choices result in either the same or worse payoffs
* P2 has **no incentive to change his strategy** as $ \pi_2 = 250 - b $ is the maximum payoff given the bid of $ (b, b + 0.1) $

### For the Second-Price Sealed Problem, using $ V_2 = 250 $, show that $ b_2 = 250 $ is weakly dominant

$$ \text{let } V_1 = 100, V_2 = 250 $$


* Player 2's payoff can be represented as:

$$
\pi_2 
\begin{cases}
250 - b_1 \quad \text{if } b_2 > b_1 \\
0 \quad \text{if } b_2 < b_1 \\
\frac{250 - b_1}{2} \quad \text{if } b_2 = b_1
\end{cases}
$$

* To guess and verify, we do the following:

$$
\text{let } x \text{ be a value s.t. } x > 250
$$

| P2 \ P1 | $ b_1 < 250 $ | $ b_1 = 250 $ | $ 250 < b_1 < x $ | $ b_1 = x $ | $ b_1 > x $ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $ b_2 = 250 $ | $ \pi_2 = 250 - b_1 > 0 $ | $ \pi_2 = \frac{250}{2} = 125 $ | $ \pi_2 = 0 $ | $ \pi_2 = 0 $ | $ \pi_2 = 0 $ |
| $ b_2 = x $ | $ \pi_2 = 250 - b_1 $ | $ \pi_2 = 0 $ | $ \pi_2 = 250 - b_1 < 0 $ |  $ \pi_2 = \frac{250 - x}{2} < 0 $ | $ \pi_2 = 0 $ | 

* Therefore, $ b_2 = V_2 $ is never worse but sometimes better than $ b_2 = x $


### Notice how much the seller earns in both cases
$$ \text{let } V_1 = 100, V_2 = 250 $$

* **First-Price Sealed Auction**: Nash Equilbrium Strategy is $(99.9, 100)$
* **Second-Price Sealed Auction**: Nash Equilibrium Strategy is $ (100, 250) $
* In both cases, the seller receives $ 100 $
