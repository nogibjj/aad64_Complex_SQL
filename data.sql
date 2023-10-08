SELECT * FROM population_by_country_2020 LIMIT 5;

SELECT * FROM population_by_country_2020 WHERE country = 'United States';

GROUP BY Country (or dependency) ORDER BY Population (2020) DESC LIMIT 10;

SELECT * FROM meat_consumption WHERE Country = 'United States';

GROUP BY Country ORDER BY Meat consumption DESC LIMIT 10;

JOIN population_by_country_2020 ON population_by_country_2020.Country = meat_consumption.Country;

SELECT p.Country, p.Population_2020, p.Yearly_Change, m.Meat_consumption
FROM population_by_country_2020 p
JOIN meat_consumption m ON p.Country = m.Country
ORDER BY m.Meat_consumption DESC;
