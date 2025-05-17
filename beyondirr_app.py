import streamlit as st
import pandas as pd
from portfolio_optimizer import PortfolioOptimizer

st.set_page_config(page_title="BeyondIRR - Portfolio Optimizer", layout="wide")

st.title("BeyondIRR - Portfolio Optimizer (Smallcase Style)")

st.markdown("""
Enter your stocks, prices, and target weights.  
Get the minimum investment and optimal allocation instantly!
""")

# --- Stock input table ---
st.subheader("Add & Organize Stocks")

if "stocks" not in st.session_state:
    st.session_state.stocks = [
        {"Stock": "State Bank of India", "Price": 792.25, "Weight": 0.03},
        {"Stock": "Bank of Baroda Ltd", "Price": 237.12, "Weight": 0.0334},
        {"Stock": "Maharashtra Scooters Ltd", "Price": 12557.00, "Weight": 0.8365},
        {"Stock": "Dixon Technologies (India) Ltd", "Price": 16539.00, "Weight": 0.10},
    ]

df = pd.DataFrame(st.session_state.stocks)
edited_df = st.experimental_data_editor(df, num_rows="dynamic", use_container_width=True)

# --- Validate weights ---
total_weight = edited_df["Weight"].sum()
if abs(total_weight - 1.0) > 0.01:
    st.warning(f"Total weight is {total_weight:.4f}. Please ensure weights sum to 1.0.")

# --- Run optimizer ---
if st.button("Optimize Portfolio") and abs(total_weight - 1.0) <= 0.01:
    stock_values = dict(zip(edited_df["Stock"], edited_df["Price"]))
    target_weights = dict(zip(edited_df["Stock"], edited_df["Weight"]))
    optimizer = PortfolioOptimizer(stock_values, target_weights)
    min_investment = optimizer.calculate_min_investment()
    allocation = optimizer.get_portfolio_allocation()
    metrics = optimizer.get_drift_metrics()

    st.success(f"Minimum Investment Needed: ₹{min_investment:,.2f}")
    st.dataframe(allocation, use_container_width=True)
    st.write("**Drift Metrics:**")
    st.json(metrics)
    st.download_button("Download Allocation as CSV", allocation.to_csv(index=False), "allocation.csv")

st.markdown("---")
st.caption("Made with ❤️ by BeyondIRR")
