# Checkout this book from the Seattle Public Library

Louisa Reilly

## Design: 
The Checkouts by Title dataset from the Seattle Public Library is a massive dataset. The goal of this project is to engineer an end-to-end data storage and processing pipeline. The pipeline will store the dataset as a SQL database which will update monthly. At the end of the pipeline, the dataset will be visualized using an interactive Tableau dashboard. This project has potential for use by librarians in determining what forms of media the library should invest in and how many copies are necessary for each item to meet checkout demands.

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
- SQL will be used to aggregate and partition the massive dataset
- Cleaning could be done using RegEx

## Tools:
- SQL database
- Google Cloud Platform to handle
- Spark since the dataset is so large.
- Tableau for visualization
- [City of Seattle has a Socrata Open Data API](https://data.seattle.gov/resource/tmmm-ytt6.json) to access the dataset.