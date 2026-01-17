---
title: H3 Game Theory Session 1
published: 2026-01-09
description: "SMU H3 Game Theory Session 1 Notes"
tags: ["Game Theory", "Economics"]
category: Notes
draft: false
---
# What is Game Theory?

## Definition
- Study of strategy and information, which influences decision-making
- Maximising utility given the information in a particular environment
- Takes into account the actions of other players

---

# What Makes Up a Game?

## Players
- Agents playing against each other in the game

## Strategies
- The options that the players have
- The potential actions players can employ

## Information Structure
- The sequence of moves

## Payoffs
- Rewards or potential outcomes
- Shaped by the strategies of players

---

# Types of Games

## By Sequence
- **Simultaneous**: Players do not know what others choose
- **Sequential**: Players take turns and know the outcomes of the others’ choices

## By Payoff
- **Zero-Sum**: Winner and loser
- **Non-Zero-Sum**: Players can jointly do better

## By Information
- **Complete Information**: Players have information about all parts of the game
- **Incomplete Information**: Players do not have information about all parts of the game

---

# Assumptions

## Rationality of Players
- Maximise personal utility
- Capable of figuring out how
- Does not exclude altruistic behaviours
- Does not exclude different payoffs
- Ability to figure out the best plan of action works against experienced players

## Common Knowledge
- Players are aware of how the game works
- Players know that other players are rational

---

# Equilibrium
- Each player is doing their best given what the other is doing
- It is a stable situation or outcome
- No player has an incentive to switch to a different outcome

---

# 21 Flags Game

## Details
- Sequentially make choices
- Perfect information

## Rules
- There are 21 flags
- Each turn, a player can take 1, 2, or 3 flags
- The goal is to be the one to take the last flag

## Strategy
- Use backward induction
- Set the game indicator as the number of flags left
- Draw up a table:

| No. of Flags Left | Optimal Choice |
|------------------|----------------|
| 1, 2, 3          | (Win) Take all |
| 4                | (Lose) Any choice |
| 5                | Take 1 |
| 6                | Take 2 |
| 7                | Take 3 |
| 8                | (Lose) Any choice |

---

# Beauty Contest Game

## Details
- Simultaneous choices
- Perfect information

## Rules
- Pick a random number
- All numbers are averaged
- The person with the number closest to **half of the average** wins

## Strategy
- In the first round, the average of random numbers will likely be 50
- Half of the average is 25
- Iteratively, the game state evolves as:
  - 25 → 12.5 → 6.25 → 3.125 → … → 0
- If everyone chooses 0, the outcome is also 0
