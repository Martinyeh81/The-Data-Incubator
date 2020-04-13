# Predict the price of Renfe AVE ticket

## Description
Our problem is to predict the price of Renfe AVE ticket, which is regression. In fact, the ticket of train is basically influenced by distance and time, but perhaps there are other reasons which affect the price of ticket. Moreover, there are no particle rules which compute the price. Thus, we want to understand how company predict the price of tickets. Furthermore, there are some problems in the dataset.

## Data

This is the data of 5 rows.

||insert_date|origin|destination|start_date|end_date|train_type|price|train_class|fare|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|0|2019-04-11 21:49:46|MADRID|BARCELONA|2019-04-18 05:50:00|2019-04-18 08:55:00|AVE|68.95|Preferente|Promo|
|1|2019-04-11 21:49:46|MADRID|BARCELONA|2019-04-18 06:30:00|2019-04-18 09:20:00|AVE|75.40|Turista|Promo|
|2|2019-04-11 21:49:46|MADRID|BARCELONA|2019-04-18 07:00:00|2019-04-18 09:30:00|AVE|106.75|Turista|Plus	Promo|
|3|2019-04-11 21:49:46|MADRID|BARCELONA|2019-04-18 07:30:00|2019-04-18 10:40:00|AVE|90.50|Turista|Plus	Promo|
|4|2019-04-11 21:49:46|MADRID|BARCELONA|2019-04-18 08:00:00|2019-04-18 10:30:00|AVE|88.95|Turista|Promo|

1. insert_date: date and time when the price was collected and written in the database, scrapping time (UTC)
2. origin: origin city
3. destination: destination city
4. start_date: train departure time (European Central Time)
5. end_date: train arrival time (European Central Time)
6. train_type: train service name
7. price: price (euros)
8. train_class: ticket class, tourist, business, etc.
9. fare: ticket fare, round trip, etc.

## Problem

There are some problems in the dataset. 
1. Time series: inser_date, start_date and end_date are time series. 
2. Categorical: origin, destination, train type, train_class and fare.
3. Missing data: price, train_class and fare. 
4. The dataset which is too big is 7644664 rows x 52 columns. 

## Preprocessing
### Large Data

### Time Series

### Cate


