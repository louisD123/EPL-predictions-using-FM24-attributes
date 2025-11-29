
-- capital cl names are annoying
ALTER TABLE matches RENAME COLUMN "Home" TO home;
ALTER TABLE matches RENAME COLUMN "xG" TO xG_home;
ALTER TABLE matches RENAME COLUMN "Score" TO score;
ALTER TABLE matches RENAME COLUMN "xG.1" TO xG_away;
ALTER TABLE matches RENAME COLUMN "Away" TO away;


ALTER TABLE matches
ADD COLUMN home_goals INTEGER,
ADD COLUMN away_goals INTEGER;

UPDATE matches
SET home_goals = split_part(score, '–', 1)::INTEGER,
    away_goals = split_part(score, '–', 2)::INTEGER;

ALTER TABLE matches
DROP COLUMN score;
