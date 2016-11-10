hive>
CREATE TABLE $InputTableName 
(
ID String,
Content String
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t';

hive>
CREATE TABLE $OutTableName 
(
ID String,
Content String,
Tokens String
)

hive>
add FILE nltk_scoring.py;
add FILE english.pickle; #Adding file to DistributedCache
INSERT OVERWRITE TABLE $OutTableName
SELECT
        TRANSFORM (id, content)
    USING 'PYTHONPATH nltk_scoring.py'
    AS (id string, content string, tokens string )
FROM $InputTablename;
