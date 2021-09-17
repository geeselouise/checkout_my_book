# Data Engineering and Analysis of Seattle Public Library Checkouts

Louisa Reilly

## Abstract:
The Checkouts by Title dataset from the Seattle Public Library is a massive dataset. The goal of this project is to engineer an end-to-end data storage, management, and visualization pipeline. SoQL queries via the Socrata API were executed to obtain specific subsets of the data. Spark managed large chunks of data for sampling and processing. All data was saved into a SQL database, and then exploratory data analysis was preformed using Tableau. Some insights gained were how current events, Seattle's culture, and month affect checkout trends. 

## Purpose:
Gain insights into the trends in the types of materials that people checkout, popular authors, and genres. These insights can inform librarians as to which types and how much of checkout items to order. 

## Data: 
The city of Seattle has many openly available public datasets. One of which is [Checkouts by Title](https://data.seattle.gov/Community/Checkouts-by-Title/tmmm-ytt6). This dataset starts with book checkouts in April 2005 to as recent as this month (September). The dataset is updated monthly with ~38.5 million rows of data. There are 11 columns in this dataset. They are as follows:
- UsageClass: lists whether the item was a physical or digital copy
- CheckoutType: the vendoor tool used to checkout the item.
- MaterialType: the type of item checkedout e.g. book, DVD, etc.
- CheckoutYear: 4 digit year of checkout for the re.
- Checkouts: number of times the title was checked out within the month.
- Title: full title and subtitle of the item.
- Creator: the author/ entity that created/ wrote the item.
- Subjects: the subject of the item as it appears in the catalgoue.
- Publisher: the publishing company of the title.
- PublicationYear: year the item was published.

## Algorithms:
- A data pipeline class was created to obtain, manage, store, and analyze the dataset.
    - Load Subset: Socrata SoQL API queries saved in Pandas
    - Save Subset: Take Pandas dataframes and store them in a SQL database or as a CSV file.
    - Update Dataset: combine multiple CSV files into one Pandas dataframe. This enables you to combine multiple API queries into one table.
    - SQL will be used to aggregate and partition the massive dataset
    - Sampling: the datasets were loaded into pyspark via CSV files. Then they were randomly sampled to obtain a small subset of the data for visualizations. There is also a feature for stratified sampling that needs some fine-tuning.
    - Loading into Tableau: SQLAlchemy was used to download tables from the SQL database and upload them into Tableau for visualizations.
    - Visualization and analysis via Tableau: add some annotations and clean-up the visuals for presentations.
    
## Tools:
- SQL database
- Google Cloud Platform
- Spark/Pyspark
- Java Database Connectivity (JDBC) API for Java based programs to access database management systems. 
- Tableau for visualization
- [City of Seattle has a Socrata Open Data API](https://data.seattle.gov/resource/tmmm-ytt6.json) to access the dataset.

## Communication:
- For long-term analysis, a random sample of 10% of the dataset was used.
- For short-term analysis, ~5 years of data (2015 - 2021) to analyze specific trends.
- [Tableau Dashboard](https://public.tableau.com/app/profile/louisa.reilly/viz/chkout_spl_16-20/Dashboard1?publish=yes)
- Tableau Visuals:

![Checkout Material trends for top 3 items](images/items_by_chkout_type.png)
![Checkout Material trends for top 3 items](images/materialstype_overtime_legend.png)

------

![Books that became Movies Checkout Trends](images/books2movies.png)

![Books that became Movies Checkout Trends](images/books2movies_legend.png)

------

![Monthly subject trend with African American as a keyword](images/African_American_subjects.png)

------

![Top 5 total creator checkouts. Many of which are children's books or James Patterson](images/top5_author_total_chkouts.png)

------

![Top 5 average creator checkouts. Many of which are NYT bestseller's](images/top5_author_avg_chkouts.png)