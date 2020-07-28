import pandas as pd
#Data frame
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']},index=['Product A', 'Product B'])
#Series
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')   
#Read CSV
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)   
#shape of csv (rows,columns)    
wine_reviews.shape
#save  DataFrame to disk as a csv file 
animals.to_csv('cows_and_goats.csv')
#use iloc to get first row
first_row = reviews.iloc[0]
#first 10 values from the description column in reviews
first_descriptions = desc.iloc[0:10] #or reviews.description.iloc[:10] or desc.head(10) or reviews.loc[:9, "description"] or 
#using iloc  the first element of the range is included and the last one excluded. 
# So 0:10 will select entries 0,...,9. 
# loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.
#set column equal to index ("title" in case below)
reviews.set_index("title")
#pick certain rows from dataset
sample_reviews = reviews.iloc[[1, 2, 3,5,8],x] 
#where x can be omitted for entire table but would be specific coulumn  if wanted 
#pick certain indices and cols from dataset
indices=[0,1,10,100]
cols=['country','province','region_1','region_2']
df = reviews.loc[indices,cols]
#pick certain columns over cetrain indice range
df = reviews.loc[0:99,["country","variety"]]
#pick reviews of italin wines
italian_wines = reviews.loc[reviews.country =="Italy"]
#or
italian_wines = reviews[reviews.country == 'Italy']
#pick certain countries only and certain reviews only
top_oceania_wines = reviews.loc[(reviews.country=="Australia") & (reviews.points>=95) | (reviews.country=="New Zealand") & (reviews.points>=95)]
#or
top_oceania_wines = reviews.loc[
    (reviews.country.isin(['Australia', 'New Zealand'])) & (reviews.points >= 95)]
#get rid of null values
reviews.loc[reviews.price.notnull()]    
#give index to table backwards
reviews['index_backwards'] = range(len(reviews), 0, -1)
#find median of points
median_points = reviews.points.median()
#get unique list of countries
countries = reviews.country.unique()
#find out how many reviews each country has
reviews_per_country = reviews.country.value_counts()
#price column subtracting mean price
centered_price = reviews.price-reviews.price.mean()
#find best bargain (price vs points)
b = (reviews.points/ reviews.price).idxmax()
bargain_wine  =reviews.loc[b,'title']
#find count of tropical or fruity in description
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

#Create a series star_ratings with the number of stars corresponding to each review in the dataset
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1
star_ratings = reviews.apply(stars, axis='columns')

# Series whose index is the taster_twitter_handle category from the dataset, and whose values count how many reviews each person wrote
reviews_written = reviews.groupby('taster_twitter_handle').size()
#Sort by price.Create a Series whose index is wine prices and whose values is the maximum number of points a wine costing that much was given in a review
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()
#the minimum and maximum prices for each variety of wine.  
#index is the variety category from the dataset. values are the min and max values 
price_extremes=reviews.groupby('variety').price.agg([min, max])
#create df of sorted_varieties containing a copy of the dataframe. 
#varieties are sorted in descending order based on minimum price, then on maximum price
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)
#series where index is reviews, value is avg review score
reviewer_mean_ratings = reviews.groupby('taster_name')['points'].mean()
#a Series whose index is a MultiIndexof {country, variety} pairs
#Sort the values in the Series in descending order based on wine count.
country_variety_counts = reviews.groupby(['country',"variety"]).size().sort_values(ascending=False)

#data type of the points column
dtype = reviews.points.dtype
#Series from entries in the points column, but convert the entries to strings
point_strings = reviews.points.astype("str")
# # of reviews in the dataset missing price
n_missing_prices = pd.isnull(reviews.price).sum()
#Series counting the number of times each value occurs in the region_1 field
#replace missing values with Unknown. Sort in descending order
reviews_per_region = reviews.region_1.fillna("Unknown").value_counts().sort_values(ascending=False)
#change region 1 and region 2 names to region and locale respectively
renamed = reviews.rename(columns={'region_1': 'region','region_2':'locale'})
# change index name to wines
reindexed = reviews.rename_axis("wines", axis='rows')
#combine two datsets with info from either
combined_products = pd.concat([gaming_products,movie_products])
#tables include references to a MeetID, a unique key for each competition included in the database. 
#generate a dataset combining the two tables into one.
powerlifting_combined = powerlifting_meets.set_index('MeetID').join(powerlifting_competitors.set_index("MeetID"))