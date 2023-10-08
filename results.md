```sql
SELECT * FROM population_by_country_2020 LIMIT 5
```

```response from database
[Row(Country (or dependency)='China', Population (2020)=1440297825, Yearly Change='0.39 %', Net Change=5540090, Density (P/Km²)=153, Land Area (Km²)=9388211, Migrants (net)=-348399.0, Fert. Rate='1.7', Med. Age='38', Urban Pop %='61 %', World Share='18.47 %'), Row(Country (or dependency)='India', Population (2020)=1382345085, Yearly Change='0.99 %', Net Change=13586631, Density (P/Km²)=464, Land Area (Km²)=2973190, Migrants (net)=-532687.0, Fert. Rate='2.2', Med. Age='28', Urban Pop %='35 %', World Share='17.70 %'), Row(Country (or dependency)='United States', Population (2020)=331341050, Yearly Change='0.59 %', Net Change=1937734, Density (P/Km²)=36, Land Area (Km²)=9147420, Migrants (net)=954806.0, Fert. Rate='1.8', Med. Age='38', Urban Pop %='83 %', World Share='4.25 %'), Row(Country (or dependency)='Indonesia', Population (2020)=274021604, Yearly Change='1.07 %', Net Change=2898047, Density (P/Km²)=151, Land Area (Km²)=1811570, Migrants (net)=-98955.0, Fert. Rate='2.3', Med. Age='30', Urban Pop %='56 %', World Share='3.51 %'), Row(Country (or dependency)='Pakistan', Population (2020)=221612785, Yearly Change='2.00 %', Net Change=4327022, Density (P/Km²)=287, Land Area (Km²)=770880, Migrants (net)=-233379.0, Fert. Rate='3.6', Med. Age='23', Urban Pop %='35 %', World Share='2.83 %')]
```

```sql


SELECT * FROM population_by_country_2020 WHERE "Country (or dependency)" = 'United States'
```

```response from database
[]
```

