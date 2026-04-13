---
title: H3 Game Theory Session 10
published: 2026-04-10
description: "SMU H3 Game Theory Session 10 Notes"
tags: ["Game Theory", "Economics", "SMU H3"]
category: SMU H3 Notes
draft: false
access: restricted
---
# SMU H3 Map

* Content map: [SMU H3 Game Theory Map](/posts/syllabus/smu-h3-study-map/)

# Screening

## Definition
* Screening is when the uninformed party takes action to learn action to learn information that is relevan to them
* Examples: 
  * Price discrimination by firms
  * Airlines splitting tickets into first class, business class, economy class
  * Telecomm companies offering different mobile phone plans

## Example
### Willingness to pay
| Software Version | Type 1 | Type 2 |
| --- | --- | --- |
| A | 180 | 500 |
| B | 150 | 200 | 

## Setup
* Suppose there are $ 45 $ students in each group (Type 1 / Type 2)
* Marginal costs of producing each unit of the software is (virtually) zero
* There is a fixed cost of developing, but these fixed costs do not affect pricing decisions
* Price decisions are driven by revenue maximisation

## Option 1: Sell only one version
| Software Version | Unit Price | Quantity | Total Revenue |  
| --- | ---  | --- | ---
| A | $150$ | $90$ | $150 \cdot 90 = 13500$ |
| A | $200$ | $45$ | $200 \cdot 45 = 9000$ |
| B | $180$ | $90$ | $180 \cdot 90 = 16200$ |
| B | $500$ | $45$ | $500 \cdot 45 = 22500$ |

## Option 2: (Bad) Screening
* Since consumers care about surplus, i.e.
$$
\text{Surplus} = \text{Willingness} - \text{Price}
$$
* You should NOT set the prices at the willingness to pay
* Consider the following prices,
$$
P_A = 500, \quad P_B = 150
$$

* For type 1 consumers, they will purchase software B since
$$
\begin{aligned}
\text{Surplus}_A &= 180 - 500 = -320 \\
\text{Surplus}_B &= 150 - 150 = 0
\end{aligned}
$$

* For type 2 consumers, they will purchase software B (instead of software A) since
$$
\begin{aligned}
\text{Surplus}_A &= 500 - 500 = 0 \\
\text{Surplus}_B &= 200 - 150 = 50
\end{aligned}
$$

## Option 3: Proper Screening
* Considering the conundrum above, set the price of A such that the surplus derived by type 1 consumers purchasing A is more than purchasing B

* Consider the following prices,
$$
P_A = 449, \quad P_B = 150
$$

* For type 1 consumers, they will purchase software B since
$$
\begin{aligned}
\text{Surplus}_A &= 180 - 449 = -269 \\
\text{Surplus}_B &= 150 - 150 = 0
\end{aligned}
$$

* For type 2 consumers, they will purchase software A since
$$
\begin{aligned}
\text{Surplus}_A &= 500 - 449 = 51 \\
\text{Surplus}_B &= 200 - 150 = 50
\end{aligned}
$$

* Screening success (hooray!)

---

# Auctions 
## Types of Auctions
### Ascending Price
* Increasing price
* Types
  * Price Sealed / Non-Price Sealed
  * First Price Auction / Second Price Auction

### Descending Price
* Decreasing price

## Environment
* Common Value: Take the price provided in the open market
* Private Value: Price setter since value is intrinsic

## Strategic Elements
* Asymmetries of information between seller and bidders,
and among bidders (screening and signalling elements)
* Optimal strategies depend on the type of attitude towards risk, the way values are determined and the type of auction
*  Revenues may or may not change with the type of
auction adopted

# Auctions
## Second Price Sealed Auction 
* Bidding your value is a weakly dominant strategy if your utility depends on the surplus you earn

### Strategy
* If your bid is $ b = v $, your payoff is 
$$
\pi = v - v = 0
$$

* If your bid is $ b < p $, your payoff is
$$
\pi = v - b > 0
$$

## First Price Sealed Auction
* Suppose your value for the object is \$5 and the other bidder's values are \$4, \$3, \$3, \$2, and \$1
* These numbers are common knowledge

### Strategy
* Bidding your value is a weakly dominant strategy
* Thus, bid the second highest price, \$4

## First Price Sealed Auction (Imperfect Information)
* Suppose your value for the object is \$5 and the other bidder's values satisfy $b \in [0, 5]$
* These numbers are not common knowledge

### Strategy
* Assume that you have the highest value for this object
* Estimate the next highest value for the opponent

---

# Continuous Random Variable
## Definition
* Random numbers that belong to a subset of the real numbers
$$
N \sim D, \quad N \in [0, 1]
$$

## Random Variable
* The probability of one outcome is negligible 
$$ 
P(N=k) \rightarrow 0 
$$

* However, the probability that a random outcome is within a range of a certain number is valid

$$
P(N\le 0) = p, \quad p \in [0, 1]
$$

* Call this cumulative density function $ F(x) = P(N \le n)$, we know that
$$
F(0) = 0, \qquad F(1) = 1
$$

* $ F(x) $ is an increasing function of $ x $, which is differentiable 
* $ F'(x) $ has an important role, and deserves its own letter $ f(x) $

$$
f(x) = F'(x) = \lim_{\delta \rightarrow 0} \frac{F(x + \delta) - F(x)}{\delta}
$$

* Thus, the expected value $ E(x) $ is as follows
$$
E(x) = \int_{0}^{1} x \cdot f(x) dx \\
E(x) = \int_{0}^{1} x \cdot dF(x)
$$

## Uniform Distribution
* Each outcome in a certain interval is equally likely
* The uniform distribution for interval $ [0, 1] $ is
$$
F(x) = x \\ 
f(x) = 1 \\ 
E(x) = \int_0^1 x F(x) dx = \frac{1}{2}
$$

* The uniform distribution for interval $ [a, b] $ is
$$
F(x) = \frac{x-a}{b-a} \\ 
f(x) = \frac{1}{b-a} \\ 
E(x) = \int_0^1 x F(x) dx = \frac{a+b}{2}
$$

## General Distribution
* For a general distribution $ F $ in $ [0, 1] $, the formula for the expected value is
$$
E(x) = \int_0^1 x f(x) dx \quad
\begin{cases}
u = x, \quad &du = 1 \\
v = F(x), \quad &dv = f(x)
\end{cases}
$$

$$
E(x) = \bigg( x F(x) \bigg)_0^1 - \int_0^1 F(x) dx
$$

$$
E(x) = 1 - \int_0^1 F(x) dx
$$

---

# Equilibirum in the First-Price Auction

## Setup
* Suppose there are 3 bidders whose object is drawn from the uniform distribution $ v \sim U(0, 1) $
* Bidder with the value $ s $ has the utility as follows:
$$
\pi_x = \begin{cases}
v - p \quad & \text{auction is won} \\
0 \quad & \text{otherwise}
\end{cases}
$$

## Claim 
* The equilibrium bidding function is
$$
b(v) = \frac{2}{3} v
$$
* Show that the words correspond to the math
* The word means $ b(v) $ which is the expected value of the largest of my opponents' $ v_s $ given that they are less than my $ v $
* I am bidder $ 1 $, competitors are bidder $ 2 $ and $ 3 $ 
* I want to compute the probability that the largest of the values between $ v_2 $ and $ v_3 $ is less than or equal to $ x $
$$
\max(v_2, v_3) \le v_1
$$

* This gives the equation for $ F(Y_1) $, where $ Y_1 = \max(v_2, v_3) $

* When is it that $ \max(v_2, v_3) \le x $, when  $ v_2 \le x $ and $ v_3 \le x $

## Illustration
| Case | Constraint 1 | Constraint 2 | Valid? |
| --- | --- | --- | --- |
| 1 | $v_2 < v_3$ | $\{v_2, v_3\} \le x$ | ✓ |
| 2 | $v_2 > v_3$ | $\{v_2, v_3\} \le x$ | ✓ |
| 3 | $v_2 < v_3$ | $v_2 \le x, x \ge v_3$ | ✗ |
| 4 | $v_2 > v_3$ | $v_3 \le x, x \ge v_2$ | ✗ |
| 5 | $v_2 < v_3$ | $\{v_2, v_3\} \ge x$ | ✗ |
| 6 | $v_2 > v_3$ | $\{v_2, v_3\} \ge x$ | ✗ |

## Derivation
* Since we are considering the probabilities for both $ v_2 $ and $ v_3 $ to be less than $ x $, we use the product rule
$$
F(x) \cdot F(x) = F(x)^2
$$

$$
F'(x) = f(x) = 2x
$$

* To compute the expected value under investigation, do

$$
E(x) = \int_0^v \frac{x \cdot f(x)}{v^2} dx = \int_0^v \frac{2x^2}{v^2} dx
$$

$$
E(x) = \frac{2}{v^2} \int_0^v x^2 dx = \frac{2}{v^2}\bigg( \frac{x^3}{3} \bigg)_0^v
$$

$$
E(x) = \frac{2v^3}{3v^2} = \frac{2}{3}v
$$

## Verification
* Perform BEST RESPONSE ANALYSIS
* If bidder 2 and 3 bid according to
$$
b(v_2) = \frac{2}{3} v_2 \quad b(v_3) = \frac{2}{3} v_3 \\
$$
* Then the best bidding function for bidder 1 whose value is $ v_1 $ is 
$$
b(v_1) = \frac{2}{3} v_1
$$

* The expected payoff is
$$
\pi_1 = 
\begin{cases}
(v_1 - b) \quad &\text{if } b \ge \frac{2}{3}v_2 \text{ and } b \ge \frac{2}{3}v_3 \\
0 \quad &\text{otherwise}
\end{cases}
$$

* What is the probability that bidder 1 wins?
$$
P(b \ge \frac{2}{3}v_2 \text{ and } b \ge \frac{2}{3}v_3)
$$

$$
= P(b \ge \frac{2}{3}v_2) \cdot P(b \ge \frac{2}{3}v_3)
$$

$$
= P(v_2 \le \frac{3}{2}b) \cdot P(v_3 \le \frac{3}{2}b)
$$

$$
= F(\frac{3}{2}b) \cdot F(\frac{3}{2}b) = \bigg[F(\frac{3}{2}b)\bigg]^2 = \bigg(\frac{3}{2}b \bigg)^2
$$

$$
P(\text{P1 wins}) = \bigg(\frac{3}{2}b \bigg)^2
$$

$$
E(\pi_1) = (v-b) \cdot P(\text{P1 wins}) + 0 \cdot P(\text{P1 loses})
$$

$$
E(\pi_1) = (v-b) \cdot \bigg(\frac{3}{2}b \bigg)^2
$$

$$
\frac{\partial}{\partial b} E(\pi_1) = \frac{9}{4} \bigg[ 2b(v_1 - b) - b^2 \bigg] = 0
$$

$$
\frac{9}{4} b \bigg[ 2(v_1 - b) - b \bigg] = 0
$$

$$
b \cdot ( 2v_1 - 3b ) = 0
$$

* Does $ b = 0 $ maximise the expected payoff? No.

$$

$$

$$
\therefore b = \frac{2}{3} v_1
$$

---

# All Pay Auction with Common Known Value
## Setup 
* Prize is 1
* $ n $ bidders such that $ n \ge 2 $
* Each bid is cashed but only the largest bidder gets the prize

## Task
* We want to compute the symmetric (each bidder adopts the same mixed strategy) mixed strategy equilibrium

* Let $ F(x) $ be $ P(\text{bid} \le x) $
* Remember that in mixed strategy equilibria, each bidder mixes indepedently of the other bidders
* Let each $ x $ in the mixing bunch belong to the interval $[a, b]$
* Our goal is to find a formula for $ F(x) $ and values for $ a $ and $ b $ 

## Derivation
* We use property 1 of mixed strategy equilibrium: *A player must be indifferent between any two bids in the mixing bunch*

* A player is indifferent between all bids in $ [a, b] $

* We take POV of bidder 1 who bids $ x $ 
$$
E(x) = 1 \cdot P(\text{win}) - x
$$

* Bidder 1 wins when all other bidders bid less than $ x $ 
* Each of them bids less than $ x $ with probability $ F(x) $

* We have $ n-1 $ of the bidders, so we do product rule

$$
P(\text{win}) = F(x)^{n-1}
$$

* The expected value as calculated below must be constant for all values of $ x \in [a, b] $
$$
\therefore E(\pi_1) = F(x)^{n-1} - x = k, \space \forall x \in [a, b]
$$

### Finding $ a $
$$
F(a) = 0 \qquad E(\pi_1)_a = 0 - a = -a
$$

* If $ a > 0 $ and I bid $ 0 $, I lose for sure
* Since $ b \ge 0 $, $ \pi = 0 > -a $ which violates PR2 of mixed strategy
* Thus, $ a $ must be 0

$$
\therefore a = 0
$$

### Finding $ F(x) $
* With $ a = 0 $, $ k = 0 $, meaning the mixed strategy equilibrium is 0

$$
E(\pi_1) = F(x)^{n-1} - x = 0
$$

$$
F(x)^{n-1} = x
$$

$$
F(x) = x^{{\frac{1}{n-1}}}
$$

### Finding $ b $
$$
F(b) = 1
$$

$$
F(b) = b^{\frac{1}{n-1}} = 1
$$

$$
\therefore b = 1
$$

### Conclusion ?
* Mixed strategy involves
$$
x \in [0, 1] \qquad F(x) = x^{\frac{1}{n-1}}
$$

* Note that any bid greater than 1 results in a guaranteed win but negative payoff (which is undesirable)
* PR 2 is satisfied (hooray!)
