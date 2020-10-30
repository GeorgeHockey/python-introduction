#!/usr/bin/env python
# coding: utf-8

#%%
# # Series and DataFrames
# 
# This lesson covers:
# 
# * Constructing pandas Series and DataFrames 
# 
# <a id="stock-data"></a>
# ## Data
# September 2018 prices (adjusted closing prices) for the S&P 500 EFT (SPY),
# Apple (AAPL) and Google (GOOG) are listed below:
# 
# 
# 
# | Date   | SPY Price | AAPL Price | GOOG Price | 
# |:-------|----------:|-----------:|-----------:| 
# | Sept4  | 289.81    | 228.36     | 1197.00    | 
# | Sept5  | 289.03    | 226.87     | 1186.48    |
# | Sept6  | 288.16    | 223.10     | 1171.44    | 
# | Sept7  | 287.60    | 221.30     | 1164.83    | 
# | Sept10 | 288.10    | 218.33     | 1164.64    | 
# | Sept11 | 289.05    | 223.85     | 1177.36    | 
# | Sept12 | 289.12    | 221.07     | 1162.82    | 
# | Sept13 | 290.83    | 226.41     | 1175.33    | 
# | Sept14 | 290.88    | 223.84     | 1172.53    | 
# | Sept17 | 289.34    | 217.88     | 1156.05    | 
# | Sept18 | 290.91    | 218.24     | 1161.22    | 
# | Sept19 | 291.44    | 216.64     | 1158.78    | 
# 
# **Prices in Sember
#  

#%%

#%%
# ## Problem: Input a pandas Series
# 
# Create vectors for each of the days in the [Table](#stock-data) named `sep_xx`
# where `xx` is the numeric date. For example,  
# ```python
# import pandas as pd
# 
# sep_04 = pd.Series([289.81,228.36,1197.00], index=["SPY","AAPL","GOOG"]);
# ```
# 
# Using the ticker names as the `index` of each series

#%%
import pandas as pd
tickers = ["SPY","AAPL","GOOG"]
sep_04 = pd.Series([289.81, 228.36, 1197.00], index = tickers)
sep_05 = pd.Series([289.03, 226.87, 1186.48  ], index = tickers)
sep_06 = pd.Series([288.16 ,223.10 ,1171.44], index = tickers)
sep_07 = pd.Series([287.60, 221.30, 1164.83], index = tickers)
sep_10 = pd.Series([288.10, 218.33, 1164.64], index = tickers)
sep_11 = pd.Series([289.05, 223.85 ,1177.36], index = tickers)
sep_12 = pd.Series([289.12, 221.07 ,1162.82], index = tickers)
sep_13 = pd.Series([290.83, 226.41, 1175.33], index = tickers)
sep_14 = pd.Series([290.88, 223.84, 1172.53], index = tickers)
sep_17 = pd.Series([289.34 ,217.88, 1156.05], index = tickers)
sep_18 = pd.Series([290.91 ,218.24,1161.22], index = tickers)
sep_19 = pd.Series([291.44, 216.64, 1158.78], index = tickers)







#%%
# ## Problem: Create a Vector of Dates
# 
# Use the pandas function `pd.to_datetime` to convert a list of string dates to
# a pandas `DateTimeIndex`, which can be used to set dates in other arrays.
# 
# For example, the first two dates are
# ```python
# import pandas as pd
# 
# dates_2 = pd.to_datetime(["4-9-2018","5-9-2018"])
# print(dates_2)
# ```
# which produces
# 
# ```
# DatetimeIndex(["2018-04-09", "2018-05-09"], dtype="datetime64[ns]", freq=None)
# ```
# 
# Create a vector containing all of the dates in the table.

#%%
dates = pd.to_datetime(["2018-09-04", "2018-09-05", "2018-09-06", "2018-09-07", "2018-09-10", "2018-09-11", "2018-09-12", "2018-09-13", "2018-09-14", "2018-09-17", "2018-09-18", "2018-09-19"])
print(dates)

#%%
# ## Problem: Input a Series with Dates
# 
# Create vectors for each of the ticker symbols in [Table](#stock-data) named
# spy, aapl and goog, respectively. Use the variable `dates` that you created
# in the previous step as the index. 
# 
# For example
# 
# ```python
# goog = pd.Series([1197.00,1186.48,1171.44,...], index=dates)
# ```
# 
# Set the `name` of each series as the series" ticker.

#%%
goog = pd.Series([1197.00,1186.48, 1171.44, 1164.83, 1164.64, 1177.36, 1162.82, 1175.33, 1172.53, 1156.05, 1161.22,1158.78], index = dates, name = "GOOG")
spy = pd.Series([289.81, 289.03, 288.16, 287.60, 288.10, 289.05, 289.12, 290.83, 290.88, 289.34, 290.91, 291.44], index = dates, name = "SPY")
aapl = pd.Series([228.36, 226.87, 223.10, 221.30, 218.33, 223.85, 221.07, 226.41, 223.84, 217.88, 218.24, 216.64], index = dates, name = "AAPL")


print(goog, spy, aapl)

#%%
# ## Problem: Create a DataFrame
# 
# Create a DataFrame named `prices` containing [Table](#stock-data). Set the
# column names equal to the ticker and set the index to `dates`.
# 
# ```python
# prices = pd.DataFrame([[289.81, 228.36, 1197.00], [289.03, 226.87, 1186.48]],
#                       columns = ["SPY", "AAPL", "GOOG"],index=dates_2)
# ```

#%%

prices = pd.DataFrame([[289.81, 228.36, 1197.00],[289.03, 226.87, 1186.48],[288.16 ,223.10 ,1171.44],[287.60, 221.30, 1164.83],[288.10, 218.33, 1164.64],[289.05, 223.85 ,1177.36],[289.12, 221.07 ,1162.82],[290.83, 226.41, 1175.33],[290.88, 223.84, 1172.53],[289.34 ,217.88, 1156.05],[290.91 ,218.24,1161.22],[291.44, 216.64, 1158.78]], columns = ([tickers]), index = dates )

#%%
# Save the price data
# 
# This block saves prices to a HDF file for use in later lessons. The
# function used to save the data is covered in a later lesson.
# 
# This function uses some sophisticated features of Python. Do not
# worry if it is unclear at this point.

#%%
# Setup: Save prices, goog and sep_04 into a single file for use in other lessons

# Only run if prices has been defined
if "prices" in globals():
    import pandas as pd
    dates = pd.Series(dates)
    variables = ["sep_04", "sep_05", "sep_06", "sep_07", "sep_10", "sep_11",
                 "sep_12", "sep_13", "sep_14", "sep_17", "sep_18", "sep_19",
                 "spy", "goog", "aapl", "prices", "dates"]
    with pd.HDFStore("data/dataframes.h5", mode="w") as h5:
        for var in variables:
            h5.put(var, globals()[var])


#%%
# ## Exercises
# 
# ### Exercise: Creating DataFrames
# 
# Turn the table below into a DataFrame where the index is set as the index and
# the column names are used in the `DataFrame`.
# 
# | index | Firm         | Profit    |  
# |:------|:-------------|----------:| 
# | A     | Alcoa        | 3,428     |
# | B     | Berkshire    | 67,421    |
# | C     | Coca Cola    | 197.4     |
# | D     | Dannon       | -342.1    |

#%%

profits = pd.DataFrame([["A", "Alcoa", 3428], ["B", "Berkshire", 67421],["C", "Coca Cola", 197.4],["D", "Dannon"   , -342.1] ], columns = (["Index", "Firm", "Profits"]), index = (["A", "B", "C", "D"]))
