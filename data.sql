SELECT * FROM population_by_country_2020 LIMIT 5;

SELECT * FROM population_by_country_2020 WHERE `Country (or dependency)` = 'United States';

SELECT `Country (or dependency)`, SUM(`Population (2020)`) AS `Total Population`
FROM population_by_country_2020
GROUP BY `Country (or dependency)`
ORDER BY `Total Population` DESC
LIMIT 10;

SELECT * FROM meat_consumption LIMIT 5;

SELECT `Country`, SUM(`Meat consumption`) AS `Total Meat Consumption`
FROM meat_consumption
GROUP BY `Country`
ORDER BY `Total Meat Consumption` DESC
LIMIT 10;

SELECT p.`Country (or dependency)`, p.`Population (2020)`, m.`Meat consumption`
FROM population_by_country_2020 p
JOIN meat_consumption m ON p.`Country (or dependency)` = m.`Country`
ORDER BY m.`Meat consumption` DESC;
