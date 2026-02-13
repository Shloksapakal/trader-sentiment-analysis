# trader-sentiment-analysis
Trader Performance vs Market Sentiment Analysis
Objective
The objective of this project was to analyze how Bitcoin market sentiment (Fear & Greed Index) relates to trader behavior and performance on Hyperliquid. The goal was to identify measurable patterns and propose sentiment-aware trading strategies based on data.
Dataset Overview
Two datasets were used:
Bitcoin Market Sentiment (Fear/Greed Index)
Date
Sentiment classification (Extreme Fear → Extreme Greed)
Hyperliquid Historical Trader Data
Account
Timestamp IST
Closed PnL
Size USD
Trade ID
Side
Other trade-related fields
The datasets were aligned at the daily level using normalized timestamps.
Part A – Data Preparation
Steps performed:
Converted timestamps to datetime format
Normalized dates for daily alignment
Merged trader data with sentiment classification
Created a win indicator (1 if Closed PnL > 0, else 0)
Computed daily performance and behavioral metrics
Key metrics generated:
Daily PnL (total & average)
Win rate
PnL volatility
Average trade size
Trade frequency
Long/Short distribution
Total trades analyzed: 88,467
Total traders: 16
Part B – Performance Analysis
Performance Across Sentiment Regimes
The results show that trader performance varies meaningfully across sentiment conditions.
Extreme Greed shows the highest average PnL (~67.9) and highest win rate (~46%).
Extreme Fear shows the lowest win rate (~37%) and highest volatility.
Fear regimes trigger high activity but not the strongest performance.
This suggests that strong bullish momentum environments provide more consistent profitability, while extreme fear introduces instability and higher risk.
Behavioral Analysis
Behavioral patterns shift noticeably with sentiment:
The largest average trade size (~$7,816) occurs during Fear regimes.
Trade frequency is highest during Fear periods.
During Greed and Extreme Greed, SELL trades slightly exceed BUY trades, suggesting mild contrarian behavior.
Overall, traders increase activity and exposure during volatile Fear periods, even though performance consistency is higher during Extreme Greed.
Actionable Strategy Recommendations
Based on the findings, the following sentiment-aware rules are proposed:
1. Risk Reduction During Extreme Fear
Reduce position size by 30–40% and avoid increasing trade frequency during Extreme Fear regimes due to high volatility and low win rate.
2. Momentum Participation During Extreme Greed
Increase trade participation during Extreme Greed regimes while maintaining moderate position size to capture trend persistence.
3. Control Overtrading During Fear
Implement a daily trade cap during Fear conditions to reduce reactive, volatility-driven overtrading.
These adjustments allow dynamic risk scaling instead of using uniform exposure across all market conditions.
Bonus – Predictive Modeling
A logistic regression model was built to predict daily trader profitability (profitable vs non-profitable) using:
Sentiment regime
Average trade size
Trade count
Win rate
Model Accuracy: 93.8%
This indicates that sentiment combined with trader behavior provides strong predictive signal for daily profitability classification. Further validation with time-series splits would be required for production-level deployment.
Bonus – Trader Clustering
KMeans clustering (3 clusters) was applied to segment traders into behavioral archetypes based on:
Average PnL
Volatility
Trade size
Trade frequency
Win rate
The clustering revealed:
Aggressive high-exposure traders
Conservative lower-performance traders
Balanced moderate-risk traders
This suggests that sentiment-based adjustments could be applied differently across trader types rather than uniformly.
Bonus – Streamlit Dashboard
A lightweight Streamlit dashboard was created to allow interactive exploration of:
Sentiment-based performance
PnL distribution
Trade behavior
To run locally:
streamlit run app.py
Conclusion
The analysis demonstrates that market sentiment significantly influences trader behavior and performance.
Fear regimes increase activity and exposure but do not provide the highest risk-adjusted returns. Extreme Greed environments show stronger consistency and profitability.
Incorporating sentiment-aware risk controls and trader segmentation can improve strategy robustness compared to static trading approaches.
Repository Structure
Trader_Sentiment_Analysis.ipynb
cleaned_merged_data.csv
app.py
requirements.txt
README.md
