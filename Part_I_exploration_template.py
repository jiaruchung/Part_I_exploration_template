import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'tmdb_5000_credits.csv'
df = pd.read_csv(file_path)

# Display the first few rows to understand its structure
df.head()

# Identifying columns that are relevant for analysis
# Selecting only the columns that contain essential information for movies: 'movie_id', 'title', 'cast', and 'crew'
df_cleaned = df[['movie_id', 'title', 'cast', 'crew']]



df_cleaned.head()

# Identify the problematic entries in the 'movie_id' column
invalid_movie_ids = df_cleaned[~df_cleaned['movie_id'].str.isdigit()]

# Display the problematic entries
invalid_movie_ids

# Convert 'movie_id' to string to handle all values, including NaNs and floats
df_cleaned['movie_id'] = df_cleaned['movie_id'].astype(str)

# Identify the problematic entries in the 'movie_id' column
invalid_movie_ids = df_cleaned[~df_cleaned['movie_id'].str.isdigit()]

# Display the problematic entries
invalid_movie_ids


# Univariate Exploration 1: Distribution of 'movie_id'
plt.figure(figsize=(10, 5))
plt.hist(df_cleaned['movie_id'].astype(int), bins=50, edgecolor='k')
plt.title('Distribution of Movie IDs')
plt.xlabel('Movie ID')
plt.ylabel('Frequency')
plt.show()

# Univariate Exploration 2: Count of Movies by Title Length
df_cleaned['title_length'] = df_cleaned['title'].apply(len)
plt.figure(figsize=(10, 5))
plt.hist(df_cleaned['title_length'], bins=30, edgecolor='k')
plt.title('Distribution of Movie Title Lengths')
plt.xlabel('Title Length')
plt.ylabel('Frequency')
plt.show()

# Univariate Exploration 3: Number of Cast Members per Movie
df_cleaned['cast_count'] = df_cleaned['cast'].apply(lambda x: len(eval(x)) if pd.notnull(x) else 0)
plt.figure(figsize=(10, 5))
plt.hist(df_cleaned['cast_count'], bins=30, edgecolor='k')
plt.title('Distribution of Number of Cast Members per Movie')
plt.xlabel('Number of Cast Members')
plt.ylabel('Frequency')
plt.show()

# Univariate Exploration 4: Number of Crew Members per Movie
df_cleaned['crew_count'] = df_cleaned['crew'].apply(lambda x: len(eval(x)) if pd.notnull(x) else 0)
plt.figure(figsize=(10, 5))
plt.hist(df_cleaned['crew_count'], bins=30, edgecolor='k')
plt.title('Distribution of Number of Crew Members per Movie')
plt.xlabel('Number of Crew Members')
plt.ylabel('Frequency')
plt.show()