# Portfolio Optimization System

This project implements a highly efficient portfolio optimization algorithm designed to closely match or outperform the Smallcase platform in terms of minimum investment and allocation accuracy.

## Strategy: Brute-Force Anchor Optimization

- **Core Idea:** For each stock, the optimizer tries using it as the "anchor" (starting point), assigning it 1, 2, ... shares, and then solves for the minimum number of shares for the other stocks to best match the target weights.
- **Process:**
  1. For each anchor stock, increment its share count and compute the required shares for the rest to maintain target proportions.
  2. For each configuration, calculate the total investment and drift (sum of squared differences between actual and target weights).
  3. Select the allocation with the lowest investment; if tied, choose the one with the lowest drift.
- **Why It Works:**
  - This method exhaustively explores all possible starting points, avoiding local minima and ensuring the most efficient allocation for portfolios with a manageable number of stocks (as in most Smallcase portfolios).
  - The optimizer always returns whole share quantities and respects minimum share constraints.
- **Results:**
  - In direct tests against Smallcase, this optimizer consistently matches or beats Smallcase in both minimum investment and drift, often finding more efficient allocations.

## Mathematical Overview

Given:
- Stock prices: P = {p₁, p₂, ..., pₙ}
- Target weights: W = {w₁, w₂, ..., wₙ}, with ∑wᵢ = 1

For each anchor stock:
1. Assign sharesᵢ = 1, 2, ...
2. Compute total portfolio value V = (sharesᵢ × pᵢ) / wᵢ
3. For each other stock j, compute sharesⱼ = floor((V × wⱼ) / pⱼ), ensuring sharesⱼ ≥ 1
4. Calculate drift: D = ∑(aᵢ - wᵢ)², where aᵢ = (sharesᵢ × pᵢ) / V_actual
5. Track the allocation with the lowest investment and drift

## Features
- Brute-force anchor method for optimal allocation
- Whole-share portfolio optimization
- Drift minimization
- Minimum investment calculation
- Multiple test cases for direct comparison with Smallcase

## Usage
Run the script to see results for all test cases:
```bash
python example.py
```
You can add more test cases by editing `example.py`.

## Customization
- Change stock prices and target weights in `example.py`
- Add or remove test cases as needed

## Notes
- The algorithm is designed for practical, real-world portfolios where only whole shares can be purchased
- Results are based on current stock prices and should be used as a guide, not financial advice 