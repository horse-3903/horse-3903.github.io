---
title: H3 Game Theory Session 3
published: 2026-01-23
description: "SMU H3 Game Theory Session 3 Notes"
tags: ["Game Theory", "Economics"]
category: Notes
draft: false
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
* Is the following claim true: 

<p style="text-align: center;"><i>"For the beauty contest, is the choice of 100 dominated by 99, 99 dominated by 98, 98 dominated by 97, 97 dominated by 96 and so on?"</i></p>

## Take-Home Problem 2
### Show that bidding at $ b \ge V $ is a dominated strategy

### Show that any bid $ (b, b + 0.1) $ where $ \pi_2 > 0, b \ge 100 $ is also a Nash Equilibrium

### What if the winner is the highest bidder but pays the lower bid? (Second-Price Sealed Problem)
* There is a weakly dominant strategy: Bidders bid their $ V $

#### Using $ V_2 = 250 $, show that $ b_2 = 250 $ is weakly dominant


$$
\text{let } x \text{ be a value s.t. } x > 250
$$

| P2 \ P1 | $ b_1 < 250 $ | $ b_1 = 250 $ | $ 250 < b_1 < x $ | $ b_1 > x $ | $ b_1 = x $ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $ b_2 = 250 $ | $ \pi_2 = 250 - b_1 $ | $ \pi_2 = 0 $ | $ \pi_2 = - $ | $ \pi_2 = 0 $ |
| $ b_2 = x $ | $ \pi_2 = $ | $ \pi_2 = $ | $ \pi_2 = $ |  $ \pi_2 = $ |

* Therefore, $ b_2 = V_2 $ is never worse but sometimmes better than $ b_2 = x $


### Notice how much the seller earns in both cases
* First-Price Auction:
  * Nash Equilbrium Strategy: $(100, 250)$
