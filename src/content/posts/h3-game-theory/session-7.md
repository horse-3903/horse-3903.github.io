---
title: H3 Game Theory Session 7
published: 2026-03-06
description: "SMU H3 Game Theory Session 7 Notes"
tags: ["Game Theory", "Economics", "SMU H3"]
category: SMU H3 Notes
draft: false
access: restricted
---
# SMU H3 Map

* Content map: [SMU H3 Game Theory Map](/posts/syllabus/smu-h3-study-map/)

---

# Mixed Strategy Recap
|         |   | $r$ | $s$ | $1-r-s$ | 
|---------|---|------|------|------|
|         |   |  A   |  B   |  C   |
| $p$     | A | 1, 1 | 1, 0 | 0, 0 |
| $q$     | B | 0, 1 | 2, 2 | 1, 0 |
| $1-p-q$ | C | 0, 0 | 0, 1 | 3, 3 |

## Step 1

* Write and solve the two inequalities of which $A$ gives the biggest expected payoff for P1 in terms of P2's probabilities

* Write and solve the two inequalities of which $B$ gives the biggest expected payoff for P1 in terms of P2's probabilities

* Write and solve the two inequalities of which $C$ gives the biggest expected payoff for P1 in terms of P2's probabilities

## Step 2
* Repeat for expected payoff for P2 in terms of P1's probabilities

## Step 3
* Solve for inequalities and draw the best response graph

### Fully Mixed Equilibria
* At the point where all three inequalities meet, it represents the probabilities where the player is indifferent to all three choices (i.e. payoffs are the same)
* This represents the fully-mixed Nash equilibrium

### Partially Mixed Equilibria
* Along the line of intersection of two regions, it represents the probabilities where the player is indifferent to both choices (i.e. payoffs are the same)
* At the same time, the player is worse off from choosing the last option not in the bag
* This represents the partially-mixed Nash equilibrium

---

# Repeated Games
## Conditions
* Game has an uncertain end, and it is possible to infinitely repeat the game
* You must care about the future impact and not be myopic

## Definitions
* A **repeated game** is a supergame where the same game ("stage game") is played for a certain number of rounds in succession, $ T $
  * $ T $ can be finite (finitely repeated game), or
  * $ T $ can be infinite (infinitely repeated game)

* The **payoffs** are the sum of payoffs earned a each round

* The **information** is such that the players know the outcome of each game at each round

* The **strategies** of the game can be represented as the following:
  * Let the history of the game be the outcomes from round $ 1 $ to round $ t $ be $ h_t $
  * The strategy is a rule mapping **any** history $ h_t $ into a choice of the base game
  * Strategies are a complete descripton of the choies that the player will make, so they must prescribe an aciton  at each round for any possible history

## Finite Game
### Example 
* Prisoners' Dilemma repeated twice ($ t=2 $)
* Since the first round has 4 possible outcomes, the strategy for a player must tell what choice to make at:
  * **Round 1**: ($C$ or $D$) 
  * **Round 2**: choice to make in any of the 4 possible outcomes ($CC$, $CD$, $DC$, $DD$)

### Strategies
#### Grim-Trigger:
* Start with $C$
* As soon as one player chooses $D$, play $D$ forever
$$
\{C, (C, D, D, D)\}
$$

#### Tit-for-Tat
* Start with $C$
* Mimic the other opponents' choice the previous round $ t-1 $  

$$
\{C, (C, D, C, D)\}
$$

#### Unconditional Cooperator
* Always play $C$

$$
\{C, (C, C, C, C)\}
$$

#### Unconditional Defector
* Always play $D$

$$
\{D, (D, D, D, D)\}
$$

### Constricting the Sub-game Perfect Equilibrium
* For a two-round prisoner dilemma
* Starting at round 2, since it is the last round, there is a dominant strategy for each player ($D$), the equilibrium is $\{D, D\}$ regardless of subgame
* Move the payoffs from the subgames of round 2 to attain the following payoff matrix

|   | C | D |
|---|---|---|
| C | $a+4, a+4$ | $a-2, a+6$ | 
| D |  $a+6, a-2$ | $2a, 2a$  | 

* Since players are incentivised to defect when choosing $ \{C, C\} $, or $ \{C, D\} $ or $ \{D, C\} $
* The best response for either player is $ D $, meaning that the Nash equilibrium is $ \{D, D\} $
* **Unconditional defection** is the subgame perfect equilibrium


## Infinite Game
### Think
* **Observation 1:**
    * Since there is no end, backward induction is not feasible
    * However, you can create recursive systems which allow for effective calculation
* **Observation 2:**
    * You cannot look at payoffs in the same way since comparing infinite payoffs with infinite payoffs does not make sense
    * There is a decay which comes with time since we value completing things now than latter

### Example 1
* Players are impatient, so \$1 today is worth more than \$1 later
* Suppose you deposit $ D $
  * After 1 year you have $ D + \gamma D = D(1 + \gamma)$
  * After 2 years you have $ D(1 + \gamma) + \gamma D(1 + \gamma) = D(1 + \gamma)^2$
  * After 3 years you have $ D(1 + \gamma)^2 + \gamma D(1 + \gamma)^2 = D(1 + \gamma)^3 $

### Example 2
* If you want to return $ P $ some time from now
* The present value of $ \$ P $ one year can be represented as
$$
x_1 = \frac{P}{1+\gamma}
$$

* The present value of $ \$ P $ two years can be represented as
$$
x_2 = \frac{P}{(1+\gamma)^2}
$$

* The present value of $ \$ P $ $t$ years can be represented as
$$
x_t = \frac{P}{(1+\gamma)^t}
$$

* Let $\delta = \frac{1}{1+\gamma}$, we have that
$$
x_1 = \delta P, \quad x_2 = \delta^2 P, ...\space, \space x_t = \delta^t P
$$

### Application to Game Theory
* Suppose the sequence of payoffs for P1 is 
$$
\pi_1, \pi_2, \pi_3, ...
$$

* The payoff in the repeated game will be 
$$
\pi = \pi_1 + \delta \pi_2 + \delta^2 \pi_3 + ...
$$
* We consider round $ 1 $ as today, and we discount future payoffs on the basis of how far they are from round 1

### Another Example 3
* If players always cooperate, P1 earns 4 in each round
$$
\pi = 4 + 4\delta + 4\delta^2 + ... + 4\delta^t \\
\pi = 4(1 + \delta + \delta^2 + ... + \delta^t) \\
\pi = 4 \sum_{t}^{\infty}\delta^t = \frac{4}{1-\delta} \\
$$

### Best Response strategy
* Let us call the infinitely repeated game $ \mathcal G $
* Let $ \sigma $ denote a strategy for $ \mathcal G $, where $(\sigma, \sigma)$ is a subgame perfect equilibrium **if and only if** no player can gain by deviating just once at every subgame
* Deviating will bring the game into another subgame state

#### Example
* Grim-trigger is a subgame perfect equilibrium if $ \delta $ is large enough
* This means players are not too impatient or myopic

* With grim-trigger, we have two possible families of subgames
  1. At least one player chose $ D $ 
  2. No $ D $ chosen so far

* If history 1, play $ C $ for one round
* If history 2, play $ D $

* In history 1, if players stck to grim-trigger, P1 earns (moving forward)
$$
V(C_1 C) = 4 + 4 \delta + 4 \delta^2 + ... \\
V(C_1 C) = 4 + \delta(4 + 4\delta + ...) \\
V(C_1 C) = 4 + \delta V(C_1 C) \\
(1 - \delta) V(C_1 C) = 4 \\
V(C_1 C) = \frac{4}{1 - \delta}
$$

* In history 2, if players stick to grim-trigger, P1 earns (moving forward)
$$

$$