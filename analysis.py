# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb

data = pd.read_csv("steam-200k.csv")

# %% [markdown]
# ### Question 1 : How many unique users are in the dataset? ###

# %%
unique_users = data["UserID"].nunique()
unique_users

# %% [markdown]
# ### Question 2: What is the total number of games listed in the dataset? ###

# %%
total_games = data["Game"].nunique()
total_games

# %% [markdown]
# ### Question 3: Find the game with the average playtime per user and determine its average playtime. ###

# %%
avgTimePerGame = data[data["Behavior"] == "play"].groupby("Game")["Hours"].mean()
sortData = avgTimePerGame.sort_values(ascending=False)
sortData.head()

# %% [markdown]
# ### Question 4: Which game has the highest variability in playtime among users? ###

# %%
stdPlayTime = data[data["Behavior"] == "play"].groupby("Game")["Hours"].std().sort_values(ascending=False)
stdPlayTime.head()

# %% [markdown]
# ### Question 5: Find top 5 users in terms of total playtime and the game ###

# %%
totalPlayTime = data[data["Behavior"] == "play"].groupby("UserID")["Hours"].sum()
sortedData = totalPlayTime.sort_values(ascending=False).head(5)

res = {}
for user_id in sortedData.index:
    user_games = data[(data["UserID"] == user_id) & (data["Behavior"] == "play")]
    most_played_game = user_games.sort_values(by="Hours", ascending=False).iloc[0]["Game"]
    res[user_id] = most_played_game

res

# %% [markdown]
# ### Question 6: Top 10 most popular games ###

# %%
topTenGames = data[data["Behavior"] == "play"].groupby("Game")["UserID"].nunique().sort_values(ascending=False).head(10)
topTenGames

# %% [markdown]
# ### Question 7: Create a chart and show hows the top 10 most popular games. ###

# %%
sb.set(style = "whitegrid")
plt.figure(figsize = (5,4))
sb.barplot(x = topTenGames.values, y = topTenGames.index, palette="viridis")
plt.title('Top 10 Most Popular Games by Unique Users')
plt.show()


# %% [markdown]
# ### Question 8: Percentage of top 10 games purchase

# %%
purchases = data[data["Behavior"] == "purchase"].groupby("Game")["UserID"].nunique().sort_values(ascending=False).head(10)

plt.figure(figsize=(5,4))
plt.pie(purchases, labels=purchases.index, autopct='%1.1f%%')
plt.axis('equal')
plt.show()


