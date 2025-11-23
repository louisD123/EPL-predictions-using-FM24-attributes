
-- capital cl names are annoying
ALTER TABLE matches RENAME COLUMN "Home" TO home;
ALTER TABLE matches RENAME COLUMN "xG" TO xG_home;
ALTER TABLE matches RENAME COLUMN "Score" TO score;
ALTER TABLE matches RENAME COLUMN "xG.1" TO xG_away;
ALTER TABLE matches RENAME COLUMN "Away" TO away;
