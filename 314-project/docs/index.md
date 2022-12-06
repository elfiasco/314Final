# Using MLB Pitch Data to Predict Whether a Batter Will Make Contact With The Ball
# By Simon Todreas, Ben Steel, and AJ Finn

## Installation Instructions

## Getting Started Guide

## Examples
![Full Data Head](vscode-remote://codespaces%2Bafinn1-redesigned-trout-74vr7r7r6rj2xv79/workspaces/314Final/314-project/docs/full%20data%20head.png)

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