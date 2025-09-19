create view most_populated AS SELECT district,SUM("families"),SUM("households"),SUM("population") as 'populated',SUM("male"),SUM("female") FROM census group by district order by populated DESC;
