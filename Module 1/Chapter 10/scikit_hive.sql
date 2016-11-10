CREATE TABLE $InputTableName (
ID String,
Content String
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t';CREATE TABLE $InputTableName (
ID String,
Content String
)
ROW FORMAT DELIMITED

hive>CREATE TABLE $OutTableName (
ID String,
Content String,
predict String,
predict_score double
)
hive>
add FILE vectorizer.pkl;
add FILE classifier.pkl;

hive>
add FILE classification.py;
INSERT OVERWRITE TABLE $OutTableName
SELECT
    TRANSFORM (id, content)
    USING '/opt/anaconda/python2.7/bin/python2.7 classification.py'
    AS (id string, scorestringscore string )
FROM $Tablename;