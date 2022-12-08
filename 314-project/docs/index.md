# Using MLB Pitch Data to Predict Whether a Batter Will Make Contact With The Ball
# By Simon Todreas, Ben Steel, and AJ Finn

## README
Project Status: In Progress

Name: What Makes the Perfect Fastball?

Description: Given MLB pitch data downloaded locally our project will clean it to display only relevant statistics, normalize it by linking it via a pitcher ID to a table with pitcher demographic info obtained from webscraping, and finally include mean aggreagated pitch data in the pithers table. To start cleaning the data we want to remove all irrelevant columns, keeping only 'pitcher', 'batter', 'release_speed', 'release_pos_x', 'release_pos_z', 'pfx_x', 'pfx_z', 'release_spin_rate', 'release_extension', 'spin_axis', and 'description'. The description column will be changed to swinging_strike and values will be set to 1 if swinging_strike was the description, and 0 otherwise. Next, a new column is added containing the total number of pitches thrown during the 2022 season by whichever pitcher the pitch corresponds to. This is done to eliminate players from the table with less than 100 pitches, after removing them the numPitches column is removed. Now, we are ready to web scrape to build our table of pitcher demographic data where each pitcher is an entry as opposed to every pitch as in the other table. From the pitch table we are able to get a unique pitcher ID that will act as a primary key in the pitcher table. Web scraping from mlb.com with the ID will generate various demographic information for the pitcher including, throwing hand, height, weight, age as of July 1 2022. In addition to including this data in the table, aggregated pitch data for each pitcher will also be included. Aggregation was done for 'release_speed', 'release_pos_x', 'release_pos_z', 'pfx_x', 'pfx_z', 'release_spin_rate', 'release_extension', 'spin_axis', 'swinging_strike' by calculating the mean.

Support: Large amounts of pitch data is not readily avaliable for download on Baseball Savant and will require concatenating excel files before being used in the project

Authors: Simon Todreas, Ben Steel, AJ Finn

## Installation Instructions

## Getting Started Guide

## Examples
![Full Data Head](full%20data%20head.png)

## BDD-Style Feature Documentation
Data Normalization

As a user exploring and analyzing the data, I want two linked tables to separately examine pitcher specific information and individual pitch characteristics.
As a user analyzing the pitch data, I may be curious about the effect that age, for example, has on pitch movement to see if it is predictive of pitch success. However it would be expensive and repetitive to have age listed for every pitch, so we will include pitcher specific information in a separate table from the pitch information. These tables will be linked by a pitcher ID so users can join them and use all information should they please.


Data Aggregation

As a user analyzing the pitch data, I want statistical information aggregated by taking averages on a pitcher by pitcher basis. This will allow the user to compare the pitchers directly for each statistic of interest, providing further insight into what statistics have the most effect on whether the ball is hit or not. Aggregating the data will make it easier to identify statistics that have the most influence on whether the ball is hit or not.

Web Scraping

As a user analyzing the data I want to have access to as many possibly helpful variables as possible. I also don’t want to have to spend too much time combining various datasets or searching for my variables through other sources. I may not only want to look at a pitcher’s detailed spin rates, velocities, or similar stats but instead I want to see more general data such as height or weight that isn’t included in the baseball savant database. To deal with this we can use web scraping to collect the general data for each pitcher found in the baseball savant database through their biographies on mlb.com. This gives me easy access to data that without web scraping techniques I would not have. 


## API Documentation
`biographicalinfo`


## Contributing Guide
N/A