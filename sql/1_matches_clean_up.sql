


-- clean up and dropping the unimportant colmns
CREATE TABLE matches_clean AS
SELECT 
    "Home",
    "xG",
    "Score",
    "xG.1",
    "Away"
FROM matches
WHERE "Wk" ~ '^[0-9]+$';


DROP TABLE matches;


ALTER TABLE matches_clean RENAME TO matches;