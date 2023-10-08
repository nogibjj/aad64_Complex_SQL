# aad64_Complex_SQL
Complex SQL Query for a MySQL Database

[![CI](https://github.com/nogibjj/aad64_Complex_SQL/actions/workflows/actions.yml/badge.svg)](https://github.com/nogibjj/aad64_Complex_SQL/actions/workflows/actions.yml)

## Objective and Steps:
* This assignment was deesigned to carry out complex SQL queries, such as, join and sort.
* For the same, I used Databricks to create an SQL warehouse with two different databases. Both datasets were imported from Kaggle (please check the [data folder](https://github.com/nogibjj/aad64_SQL_Start/edit/main/data) to take a look at the csv files):
+ Population by Country (2020) database.
+ Meat Consumption by Country (2020) database.
* After this, I created functions designed to establish a connection between my project and Databricks in my [data.py](https://github.com/nogibjj/aad64_SQL_Start/edit/main/mylib/data.py) file.
* To then query the databases which I could then communicate with after the connection, queries were written up in the [data.sql](https://github.com/nogibjj/aad64_SQL_Start/edit/main/data.sql) file.
* Lastly, to bring it all together, the queries were copied and their outputs were directly rendered to the [results.md](https://github.com/nogibjj/aad64_SQL_Start/edit/main/results.md) markdown.
* The functions were called in [main.py](https://github.com/nogibjj/aad64_SQL_Start/edit/main/main.py) and the connection was tested in the [test_main.py](https://github.com/nogibjj/aad64_SQL_Start/edit/main/test_main.py) file.

## SQL Operations:
For this project, the following SQL operations were carried out:
* `SELECT` query to see the first five rows of the databases.
* `WHERE` to have a specific selection of a row in the database.
* `ORDER` to sort the databases in __descending__ order of specific columns.
* `GROUP BY` to group rows with the same values into summary rows.
* `JOIN` to join the two selected databases on one column (which are the same values for each, here, Country). 

As indicated in the status badge, this project passed all workflow steps. 
