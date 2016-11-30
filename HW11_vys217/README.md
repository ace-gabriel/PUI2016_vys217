# Homework 11

For this homework, I worked with Aaron, Dongjie Fan, Achilles, Priyanshi and helped others as well.

## Assignment 1

I did this by myself. 
In this assignment, I downloaded the Census Tract data from the nyc.gov website. 
Using geopandas and fiona libraries, set up the co-ordinate system.
Created a point geometry for CUSP using shapely
Found the polygon geometry within which CUSP lies and plotted some of the Brooklyn Census tracts and CUSP point on a map

## Assignment 2

Donjhe helped me understanding of the data, i.e the columns from the business-zip data which needs to be used.
Aaron helped me with the interpretation
In this assignment, I have downloaded the business zip data and moved it to PUIdata.
The NYC zipcode data is taken from the geojson file which is uploaded here in github and is present in the same directory as of the notebook
The zip codes and geometry is used from the NYC zip code dataset.
The number of business establishments and zipcode is taken from the 21 zip files for years 1994 to 2014
Then, I have standardized the time-series and clustered it using K-means and Agglomerative Clustering. 
I have visualized the clusters on NYC map and tried to interpret the results