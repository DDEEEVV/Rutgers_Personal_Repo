# Financial_Planning.hw

## My work can be found by clicking here: [DAVIT_CUEDARI_Financial_Planner_HW](financial-planner.ipynb)

![Financial Planner](MC_simulation_results/financial-planner.png)

This homework consist in working with APIs and running several Monte Carlo simulations. The results will help to calculate the expected portfolio returns given a specific initial investment amount.

## Background

Using the skills that I have learned during this first month in the FinTech BootCamp, especially on APIs as part of technical solution I have created two financial analysis tools:

The first tool consists on building a personal financial planner that will allow users to have clear visualization of their savings that they have invested in: Stocks, Bonds and Cryptocurrencies and make sure that they have enough money as an emergency fund!

The second tool will be a retirement planning tool that will use the Alpaca API to fetch historical closing prices for a retirement portfolio composed of stocks and bonds, then run Monte Carlo simulations to project the portfolio performance at 30 years. 

I have used the Monte Carlo data to calculate the expected portfolio returns given a specific initial investment amount and the results will be different based on the initial investment, years of projection which will determine the minimum and the maximum outcome of that investment projection.
__________________________________________________________________________________
I really enjoyed working on this homework and I have learned a lot from it. Thanks to my amazing instructor and the Rutgers Institution for providing all the tools for me to learn!
__________________________________________________________________________________


Here is a time line of my work:

First I have to import libraries and dependencies, the ones that are new on this work are: *load_dotenv, alpaca_trade_api, json and MCSimulation*

Using the url provided I am able to find the current price from the crypto market and by multiplying it by the amount I find the value of the crypto portfolio:
![current crypto wallet balance](MC_simulation_results/value_of_1.2BTC_5.3ETH.png)

Next I have to create two other variables for the current amount of shares for Bonds and Stocks:
Using ALPACA API get_bars  I am able to extract data and use them to run my analysis:

*Important note here: for my ALPACA_API_KEY I am not using the .env so I am not creating a gitignore file. I have used the zshrc file to store and hide my api keys in my local environment so they won't get exposed online.*

Running all the code I am able to get the current price and the current value by multiplying amount with price:


![AGG and SPY close prices](MC_simulation_results/closing_prices.png)
![the current value of shares](MC_simulation_results/value_of_shares.png)

# Saving Health Analysis

For a monthly income provided and crypto portfolio and stock/bonds portfolio we have to set an ideal emergency fund:

![savings pie chart](MC_simulation_results/piechart.png)

The emergency fund has to be created based on the 3 times the monthly income,
and the analysis consist on the total amount of savings that should not exceed the total amount saved in stocks, bonds and cryptos.
Validating health through a conditional statements we get this result:

![validating saving health](MC_simulation_results/validating_saving_health.png)

## *The second tool - Retirement Planning*

I started with setting up tickers and the start and the end dates of the historical data to be extracted with alpaca.get_bars and use it ti create a stock data frame.
I used that data frame to run 500 Monte Carlo Simulations with weights: 40% in AGG and 60% in SPY for 30 years.
The results using this fascinating tool are amazingly generated in 1 minute:

![simulation outcomes](MC_simulation_results/simulation_1.png)
![probability distribution outcome](MC_simulation_results/distribution_1.png)

>### *There is a 95% chance that an initial investment of $20,000 in the portfolio over the next 30 years will end within in the range of $86,660.26 and $1,146,726.14*


*Increasing the initial investment by 50%:*
>### *There is a 95% chance that an initial investment of $30,000.0 in the portfolio over the next 30 years will end within in the range of $129,990.39 and $1,720,089.21*





### Five Years Retirement Option

![simulation outcomes](MC_simulation_results/early_retirement_5years_simulation.png)
![probability distribution outcome](MC_simulation_results/early_retirement_5years_distribution.png)

>### *There is a 95% chance that an initial investment of $60,000 in the portfolio over the next 5 years will end within in the range of $54,643.5 and $144,425.04*


### Ten Years Retirement Option

![simulation outcomes](MC_simulation_results/early_retirement_10years_simulation.png)
![probability distribution outcome](MC_simulation_results/early_retirement_10years_distribution.png)

>### *There is a 95% chance that an initial investment of $60,000 in the portfolio over the next 10 years will end within in the range of $72,877.37 and $311,493.28*