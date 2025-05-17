import numpy as np
import pandas as pd
from itertools import permutations
import yfinance as yf
from datetime import datetime

class PortfolioOptimizer:
    def __init__(self, stock_values, target_weights):
        """
        Initialize the portfolio optimizer
        
        Parameters:
        -----------
        stock_values : dict
            Dictionary of stock values (e.g., {'AAPL': 211.45, 'MSFT': 453.13})
        target_weights : dict
            Dictionary of target weights for each symbol (e.g., {'AAPL': 0.3, 'MSFT': 0.7})
        """
        self.stock_values = stock_values
        self.target_weights = target_weights
        self.symbols = list(stock_values.keys())
        self.optimal_shares = None
        self.best_allocation = None
        self.best_metrics = None
        
    def calculate_min_investment(self):
        best_investment = float('inf')
        best_drift = float('inf')
        best_shares = None
        best_allocation = None
        best_metrics = None
        # Try each stock as the anchor (start with 1 share)
        for anchor in self.symbols:
            min_shares = {}
            shares = 1
            while shares < 1000:  # Reasonable upper bound to avoid infinite loop
                # Calculate total value needed for anchor
                current_value = shares * self.stock_values[anchor]
                total_value = current_value / self.target_weights[anchor]
                valid = True
                for other_symbol in self.symbols:
                    if other_symbol != anchor:
                        other_shares = int(np.floor((total_value * self.target_weights[other_symbol]) / self.stock_values[other_symbol]))
                        if other_shares < 1:
                            valid = False
                            break
                        min_shares[other_symbol] = other_shares
                if valid:
                    min_shares[anchor] = shares
                    # Calculate total investment
                    total_investment = sum(min_shares[s] * self.stock_values[s] for s in self.symbols)
                    # Calculate actual weights
                    actual_weights = {s: (min_shares[s] * self.stock_values[s]) / total_investment for s in self.symbols}
                    # Calculate drift
                    drift = sum((actual_weights[s] - self.target_weights[s]) ** 2 for s in self.symbols)
                    # If this is the best so far, save it
                    if (total_investment < best_investment) or (np.isclose(total_investment, best_investment) and drift < best_drift):
                        best_investment = total_investment
                        best_drift = drift
                        best_shares = min_shares.copy()
                        best_allocation = self._make_allocation(min_shares, total_investment)
                        best_metrics = self._make_metrics(actual_weights, drift, total_investment)
                    break
                shares += 1
        self.optimal_shares = best_shares
        self.best_allocation = best_allocation
        self.best_metrics = best_metrics
        return best_investment
    
    def _make_allocation(self, shares_dict, total_value):
        allocation = []
        for symbol in self.symbols:
            shares = shares_dict[symbol]
            price = self.stock_values[symbol]
            value = shares * price
            allocation.append({
                'Symbol': symbol,
                'Shares': shares,
                'Price': price,
                'Value': value,
                'Target Weight': self.target_weights.get(symbol, 0),
                'Actual Weight': value / total_value if total_value > 0 else 0
            })
        # Calculate final weights
        for item in allocation:
            item['Actual Weight'] = item['Value'] / total_value
        return pd.DataFrame(allocation)
    
    def _make_metrics(self, actual_weights, drift, total_investment):
        max_drift = max(abs(actual_weights[s] - self.target_weights[s]) for s in self.symbols)
        return {
            'Total Drift': drift,
            'Maximum Weight Deviation': max_drift,
            'Total Investment': total_investment
        }
    
    def get_portfolio_allocation(self):
        if self.best_allocation is None:
            self.calculate_min_investment()
        return self.best_allocation
    
    def get_drift_metrics(self):
        if self.best_metrics is None:
            self.calculate_min_investment()
        return self.best_metrics 