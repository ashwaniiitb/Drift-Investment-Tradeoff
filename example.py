from portfolio_optimizer import PortfolioOptimizer

def run_case(case_name, stock_values, target_weights):
    print(f"\n=== {case_name} ===")
    optimizer = PortfolioOptimizer(
        stock_values=stock_values,
        target_weights=target_weights
    )
    min_investment = optimizer.calculate_min_investment()
    print(f"Minimum Investment Needed: ₹{min_investment:,.2f}")
    allocation = optimizer.get_portfolio_allocation()
    print("Optimized Portfolio Allocation:")
    print(allocation.to_string(index=False))
    metrics = optimizer.get_drift_metrics()
    print("Drift Metrics:")
    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")


def main():
    # --- Image 1: 4-stock Smallcase example ---
    stock_values_1 = {
        'State Bank of India': 792.25,
        'Bank of Baroda Ltd': 237.12,
        'Maharashtra Scooters Ltd': 12557.00,
        'Dixon Technologies (India) Ltd': 16539.00
    }
    target_weights_1 = {
        'State Bank of India': 0.03,
        'Bank of Baroda Ltd': 0.0334,
        'Maharashtra Scooters Ltd': 0.8365,
        'Dixon Technologies (India) Ltd': 0.10
    }

    # --- Image 2: 6-stock Smallcase example ---
    stock_values_2 = {
        'Indian Overseas Bank': 37.88,
        'Canara Bank Ltd': 107.54,
        'State Bank of India': 792.10,
        'Bank of Baroda Ltd': 236.40,
        'Maharashtra Scooters Ltd': 12572.00,
        'Dixon Technologies (India) Ltd': 16540.00
    }
    target_weights_2 = {
        'Indian Overseas Bank': 0.0771,
        'Canara Bank Ltd': 0.2599,
        'State Bank of India': 0.03,
        'Bank of Baroda Ltd': 0.0205,
        'Maharashtra Scooters Ltd': 0.5125,
        'Dixon Technologies (India) Ltd': 0.10
    }

    # --- Image 3: 7-stock Smallcase example ---
    stock_values_3 = {
        'Indian Bank': 593.95,
        'Bank of India Ltd': 114.25,
        'Indian Overseas Bank': 37.86,
        'Canara Bank Ltd': 107.52,
        'State Bank of India': 791.80,
        'Bank of Baroda Ltd': 236.47,
        'Maharashtra Scooters Ltd': 12572.00
    }
    target_weights_3 = {
        'Indian Bank': 0.1287,
        'Bank of India Ltd': 0.0493,
        'Indian Overseas Bank': 0.0771,
        'Canara Bank Ltd': 0.2699,
        'State Bank of India': 0.06,
        'Bank of Baroda Ltd': 0.0159,
        'Maharashtra Scooters Ltd': 0.3991
    }

    # --- Image 4: 8-stock Smallcase example ---
    stock_values_4 = {
        'Indian Bank': 593.95,
        'Bank of India Ltd': 114.25,
        'Indian Overseas Bank': 37.86,
        'Canara Bank Ltd': 107.52,
        'State Bank of India': 791.80,
        'Bank of Baroda Ltd': 236.47,
        'Maharashtra Scooters Ltd': 12572.00,
        'Dixon Technologies (India) Ltd': 16531.00
    }
    target_weights_4 = {
        'Indian Bank': 0.1287,
        'Bank of India Ltd': 0.0493,
        'Indian Overseas Bank': 0.0771,
        'Canara Bank Ltd': 0.2699,
        'State Bank of India': 0.06,
        'Bank of Baroda Ltd': 0.0121,
        'Maharashtra Scooters Ltd': 0.3029,
        'Dixon Technologies (India) Ltd': 0.10
    }

    run_case("Image 1: 4-stock Smallcase", stock_values_1, target_weights_1)
    run_case("Image 2: 6-stock Smallcase", stock_values_2, target_weights_2)
    run_case("Image 3: 7-stock Smallcase", stock_values_3, target_weights_3)
    run_case("Image 4: 8-stock Smallcase", stock_values_4, target_weights_4)

if __name__ == "__main__":
    main() 