---
title: H3 Game Theory Session 11
published: 2026-04-17
description: "SMU H3 Game Theory Session 11 Notes"
tags: ["Game Theory", "Economics", "SMU H3"]
category: SMU H3 Notes
draft: false
access: restricted
---
# SMU H3 Map

* Content map: [SMU H3 Game Theory Map](/posts/syllabus/smu-h3-study-map/)

---

# Wrapping Up

## Independent Private Values Auctions
* Values are Independent Draws from the Same Distribution

### Second Price Auction
* Same as previous derivations
* Weakly dominant to bid your value $ v $ 

### First Price Auction
* Given your value $ v $, bid the expected value of the largest value among your opponents
* This is assuming your opponents bid less than or equal to $ v $

$$
E[\max(v_2, v_3, ..., v_n) \space | \space v_1 > \max(v_2, v_3, ..., v_n)]
$$

### Random Variables
$$
E[X | x \le v] = \frac{1}{F(v)} \int_a^v x f(x) dx = \frac{1}{F(v)} \int_a^v x dF(x)
$$

## Common and Known Values Auctions
* The prize is worth $ v $ to each bidder

### First Price Auction
* Bidding $ v $ is a dominated strategy
* Bid the biggest number less than $ v $ 

### All Pay Auction
* Everyone pays their bid
* No pure strategy equilibrium
* Mixed  strategy equilibrium exissts

* For $ v = 1 $
$$
F(x) = x^{\frac{1}{n}-1}, \quad \text{s.t. } x \in [0, 1]
$$

---

# War of Attrition (Second-Price All-Pay Auction)

## Definition
* Everyone pays their bid 
* The winner pays the second-highest bid
* It is a contest which the victor is the one that stays in the contest 
* Choosing to remain in the contest is costly for both

## Solution
* Each player mixes their strategy from the interval $ [0, +\infty) $

$$
F_1(x) = 1-e^{-\alpha_2x}, \quad F_2(x) = 1-e^{-\alpha_1x}
$$

* Where $ \alpha_i = \frac{1}{v_i} $
* $ F(x) $ is valid in the range $ [0, 1] $ because as $ x \rightarrow \infty $, $ e^{-\alpha_i x} \rightarrow 0 $

## Setup
* Let $ F_1 $ and $ F_2 $ denote the mixing functions (CDFs) for P1 and P2

### P1 indifference condition
* Bidder 1 bids $ x $, Bidder 2 bids $ y $

#### Case 1
* If P2 bids $ < x $, P1 wins and pays $ y $ 
* Since P1 wins, P1 gets the payoff $ v_1 -y $ 

#### Case 2
* If P2 bids $ > x $, P2 wins and P1 pays $ x $ 
* Since P1 loses, P1 gets the payoff $ -x $ 

$$
E(\pi_1) = \underbrace{\int_0^x (v_1 - y) f_2(y)dy}_{\text{Win Case}} + \underbrace{\vphantom{\int_0^x}(-x)(1-F_2(x))}_{\text{Loss Case}}
$$

#### Applying the indifference condition 
* $ E(\pi_1) $ is a constant function of $ x $

$$
E(\pi_1) = \int_0^x (v_1 - y) f_2(y)dy - x(1-F_2(x))
$$

$$
E(\pi_1) = v_1 \int_0^x f_2(y)dy - \int_0^x y f_2(y)dy - x(1-F_2(x))
$$

$$
E(\pi_1) = v_1 F_2(x) - \int_0^x yf_2(y)dy - x(1-F_2(x))
$$

* To find the equilibrium, take the derivative with respect to $ x $ and set it to zero

$$
\frac{\partial}{\partial x} E(\pi_1) = v_1 f_2(x) - x f_2(x) - \left[(1-F_2(x)) + x(-f_2(x))\right] = 0
$$

$$
v_1 f_2(x) - x f_2(x) - 1 + F_2(x) + x f_2(x) = 0
$$

$$
v_1 f_2(x) = 1-F_2(x)
$$

* Since $ f_2(x) = F_2'(x) $, we can rewrite this as a differential equation

$$
\frac{F_2'(x)}{1-F_2(x)} = \frac{1}{v_1}
$$

* Using the identity

$$
\frac{\partial}{\partial x}\ln(1-F_2(x)) = -\frac{F_2'(x)}{1-F_2(x)}
$$

* We get

$$
\frac{\partial}{\partial x}\ln(1-F_2(x)) = -\frac{1}{v_1} = -\alpha_1
$$

#### Integration and boundary conditions
* Suppose $ F_2(x) $ has the domain $ [a, b] $ such that $ F_2(a) = 0 $

$$
\int_a^x \frac{\partial}{\partial t}\ln(1-F_2(t))dt = \int_a^x -\alpha_1 dt
$$

$$
\ln(1-F_2(x)) - \ln(1-F_2(a)) = -\alpha_1(x-a)
$$

* Since $ F_2(a) = 0 $, $ \ln(1-F_2(a)) = \ln(1) = 0 $

$$
\ln(1-F_2(x)) = -\alpha_1(x-a)
$$

$$
1-F_2(x) = e^{-\alpha_1(x-a)}
$$

$$
F_2(x) = 1-e^{-\alpha_1(x-a)}
$$

#### Finding $ a $ and $ b $
* Upper bound: as $ x \rightarrow \infty $, $ F_2(x) \rightarrow 1 $, so $ b = \infty $
* Lower bound: for P1 to be willing to enter the contest at the minimum bid, the expected payoff at the start must be zero

$$
E(\pi_1) = v_1F_2(a)-\int_0^a yf_2(y)dy-a(1-F_2(a)) = 0
$$

$$
0-\int_0^a yf_2(y)dy-a = 0
$$

* This condition is satisfied when $ a = 0 $

$$
F_2(x) = 1-e^{-\alpha_1 x}
$$

* By the same logic, P1's mixed strategy is

$$
F_1(x) = 1-e^{-\alpha_2 x}
$$

### P2 indifference condition
* The same derivation applies symmetrically, giving $ F_1(x) = 1-e^{-\frac{x}{v_2}} $

## Remarks
* If $ v_1 > v_2 $, then $ F_2(x) < F_1(x) $ for all $ x $
  * The stronger bidder is more likely to bid less
  * The stronger bidder, on average, bids less
  * The stronger bidder wins with probability $ < \frac{1}{2} $
$$
\int_0^\infty xf_1(x)dx < \int_0^\infty xf_2(x)dx
$$
$$
v_2 < v_1
$$ 

$$
P(\text{P1 wins}) = \frac{v_2}{v_1+v_2} = \int_0^\infty f_1(x)F_2(x)dx
$$
  

--- 

# First Price Common Value Auction with Independent Values
## Setup
* $ V = v_1 + v_2 $ is the common value of the prize
* $ v_1, v_2 $ can be any number from 0 to 100 with equal probability, i.e. $ v_1, v_2 \sim U(0, 100) $
* Strategy is a rule that maps any $ v $ from $[0, 1]$ into a non-negative bid $ b(v) $

## Solution
* Equilibrium where both players adopt the same rule $ b(v) $ is 

$$
b(v) = v
$$

## Verify
* Suppose I am P1 with the value $ v_1 $ and thinking of bidding $ b $
* Assume P2 adopts the rule $ b(v_2) = v_2 $ 

* What is my expected payoff? 

| $0 < v_2 < b$ | $b < v_2 < 100$ |
| --- | ---|
| $ \pi > 0 $ | $ \pi < 0 $ |

* $$ \because F(v) = \frac{v_2-0}{100-0} = \frac{v_2}{100}, \quad \therefore f(v_2) = \frac{1}{100} $$

$$
E(\pi) = \int_0^b(v_1+v_2-b)f(v_2)dv_2
$$

$$
E(\pi) = \frac{1}{100} \int_0^b(v_1+v_2-b)dv_2
$$

$$
E(\pi) = \frac{1}{100}\bigg[ v_2(v_1-b) \bigg]^b_0 + \frac{1}{100}\bigg( \frac{v_2^2}{2} \bigg)^b_0
$$

$$
E(\pi) = \frac{1}{200}\bigg[ 2b(v_1 - b) + b^2 \bigg] = \frac{1}{200}\space b( 2v_1 - b )
$$

$$
E(\pi) = -\frac{1}{200}\space b( b - 2v_1 )
$$

* The value of $ b $ that maximises this function is the midpoint between $ b = 0 $ and $ b = 2v_1 $ 
* Thus, the best bid is $ b(v_1) = v_1 $ 

# Second Price Common Value Auction
## Solution 
$$
b(v_1) = 2v_1
$$

## Verify
* Suppose I am P1 with the value $ v_1 $ and thinking of bidding $ b $
* Assume P2 adopts the rule $ b(v_2) = 2v_2 $ 

$$
\pi = v_1 + v_2 - 2v_2
$$

* What is my expected payoff? 

| $0 < v_2 < \frac{b}{2}$ | $\frac{b}{2} < v_2 < 100$ |
| --- | ---|
| $ \pi > 0 $ | $ \pi < 0 $ |

$$
f(v_2) = \frac{1}{100}
$$

$$
E(\pi) = \int_0^\frac{b}{2} (v_1-v_2)f(v_2)dv_2
$$

$$
E(\pi) = \frac{1}{100}\int_0^\frac{b}{2}(v_1-v_2)dv_2
$$

$$
E(\pi) = \frac{1}{100} \bigg[ v_1v_2 - \frac{v_2^2}{2} \bigg]_0^\frac{b}{2}
$$

$$
E(\pi) = \frac{1}{100} \bigg( \frac{v_1b}{2} - \frac{b^2}{8} \bigg)
$$

$$
E(\pi) = \frac{b}{100} \bigg( \frac{v_1}{2} - \frac{b}{8} \bigg)
$$

$$
E(\pi) = \frac{1}{800} \space b( 4v_1 - b )
$$

* The value of $ b $ that maximises this function is the midpoint between $ b = 0 $ and $ b = 4v_1 $ 
* Thus, the best bid is $ b(v_1) = 2v_1 $ 