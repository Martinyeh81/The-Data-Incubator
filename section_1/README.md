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
1. Time series: inser_date, start_date and end_date 
2. Categorical: origin, destination, train type, train_class and fare.
3. Missing data: price, train_class and fare. 
4. The dataset which is too big is 7644664 rows x 52 columns. 

||Columns type|Number of missing data|
|---|---|---|
|insert_date|datetime64[ns]|0|
|origin|object|0|
|destination|object|0|
|start_date|datetime64[ns]|0|
|end_date|datetime64[ns]|0|
|train_type|object|0|
|price|float64|573121|
|train_class|object|26690|
|fare|object|26690|

## Preprocessing
### Number of Data
  We use train_test_split from scikit- learn to decrease the sample because the dataset is too large, so we use 10% of dataset to be trained. Moreover, we split datasets again, which Training set is 90% of dataset and testing data is 10% of dataset.
### Time Series
  1. We divid the feature of insert_date to the features of month, day, hour, minute and second. We don’t need the feature of year because all features of year are the same.

|Insert_date minimum date time|Insert_date maximum date time|
|---|---|
|2019-04-11 21:49:46|2019-05-09 21:19:16|

|Insert_date|Insert_month|Insert_day|Insert_hour|Insert_min|Insert_sec|
|---|---|---|---|---|---|
|2019-04-11 21:49:46|04|11|21|49|46|

  2. The features of start_date and end_date are time series, so we change the datetime to hour, which we calculate between start_date and end_date to represent the features of start_date and end_date because all of people spent less than one day taking the train.

|start_date|end_date|start_end_hour|
|---|---|---|
|2019-04-18 05:50:00|2019-04-18 08:55:00|3.083333|
  
### Categorical
  1. RandomForest: Directly convert into code
  2. Linear regression: one hot encoding
### Missing data
  We drop the data which has empty value because there are at least 7000000x52 data in the dataset, which doesn’t affect the result a lot. Moreover, for the price part, we fill the mean of price.
### Feature selection
##### Ridge
![Ridge_coef](https://github.com/Martinyeh81/The-Data-Incubator/blob/master/section_1/Image/LR_Ridge_coef.png)
##### Lasso
![Lasso_coef](https://github.com/Martinyeh81/The-Data-Incubator/blob/master/section_1/Image/LR_Lasso_coef.png)
##### Random Forest
![Random_coef](https://github.com/Martinyeh81/The-Data-Incubator/blob/master/section_1/Image/Random_coef.png)

## Result
1000 samples
### Linear Regression with Ridge
![Ridge_result](https://github.com/Martinyeh81/The-Data-Incubator/blob/master/section_1/Image/LR_Ridge_result.png)
![Ridge_curve](https://github.com/Martinyeh81/The-Data-Incubator/blob/master/section_1/Image/LR_Ridge_curve.png)
### Linear Regression with Lasso
![Lasso_result](https://github.com/Martinyeh81/The-Data-Incubator/blob/master/section_1/Image/LR_Lasso_result.png)
![Lasso_curve](https://github.com/Martinyeh81/The-Data-Incubator/blob/master/section_1/Image/LR_Lasso_curve.png)
### Random Forest Regression
![Random_result](https://github.com/Martinyeh81/The-Data-Incubator/blob/master/section_1/Image/Random_result.png)
![Random_curve](https://github.com/Martinyeh81/The-Data-Incubator/blob/master/section_1/Image/Random_curve.png)
### Comparation
||LR with Ridge|LR with Lasso|Random Forest|
| --- | --- | --- | --- |
|MSE|129.67215|129.68961|90.71796|
|R square|0.78991|0.78988|0.85302|

## Conclusions
1. The data doesn't complete yet, especially the linear regression because we can increase the degree to compute the best result. However, we need enough time and good computer to run the data.
2. Also for the Random Forest, we only try 10 and 100 trees. there are other parameter we can try.

