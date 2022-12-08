# 314Final README
**Project Status**: In Progress

**Name**: What Makes the Perfect Fastball?

**Description**: Given MLB pitch data downloaded locally our project will clean it to display only relevant statistics, normalize it by linking it via a pitcher ID to a table with pitcher demographic info obtained from webscraping, and finally include mean aggreagated pitch data in the pithers table. To start cleaning the data we want to remove all irrelevant columns, keeping only 'pitcher', 'batter', 'release_speed', 'release_pos_x', 'release_pos_z', 'pfx_x', 'pfx_z', 'release_spin_rate', 'release_extension', 'spin_axis', and 'description'. The description column will be changed to swinging_strike and values will be set to 1 if swinging_strike was the description, and 0 otherwise. Next, a new column is added containing the total number of pitches thrown during the 2022 season by whichever pitcher the pitch corresponds to. This is done to eliminate players from the table with less than 100 pitches, after removing them the numPitches column is removed. Now, we are ready to web scrape to build our table of pitcher demographic data where each pitcher is an entry as opposed to every pitch as in the other table. From the pitch table we are able to get a unique pitcher ID that will act as a primary key in the pitcher table. Web scraping from mlb.com with the ID will generate various demographic information for the pitcher including, throwing hand, height, weight, age as of July 1 2022. In addition to including this data in the table, aggregated pitch data for each pitcher will also be included. Aggregation was done for 'release_speed', 'release_pos_x', 'release_pos_z', 'pfx_x', 'pfx_z', 'release_spin_rate', 'release_extension', 'spin_axis', 'swinging_strike' by calculating the mean.

**Support**: Large amounts of pitch data is not readily avaliable for download on Baseball Savant and will require concatenating excel files before being used in the project

**Authors**: Simon Todreas, Ben Steel, AJ Finn

