


CREATE TABLE team_averages AS
SELECT
    "Club",
    AVG("Cor") AS cor_avg,
    AVG("Cro") AS cro_avg,
    AVG("Dri") AS dri_avg,
    AVG("Fin") AS fin_avg,
    AVG("Fir") AS fir_avg,
    AVG("Fre") AS fre_avg,
    AVG("Hea") AS hea_avg,
    AVG("Lon") AS lon_avg,
    AVG("L Th") AS l_th_avg,
    AVG("Pas") AS pas_avg,
    AVG("Pen") AS pen_avg,
    AVG("Tck") AS tck_avg,
    AVG("Tec") AS tec_avg,
    AVG("Agg") AS agg_avg,
    AVG("Ant") AS ant_avg,
    AVG("Bra") AS bra_avg,
    AVG("Cmp") AS cmp_avg,
    AVG("Cnt") AS cnt_avg,
    AVG("Dec") AS dec_avg,
    AVG("Det") AS det_avg,
    AVG("Fla") AS fla_avg,
    AVG("Ldr") AS ldr_avg,
    AVG("OtB") AS otb_avg,
    AVG("Pos") AS pos_avg,
    AVG("Tea") AS tea_avg,
    AVG("Vis") AS vis_avg,
    AVG("Wor") AS wor_avg,
    AVG("Acc") AS acc_avg,
    AVG("Agi") AS agi_avg,
    AVG("Bal") AS bal_avg,
    AVG("Jum") AS jum_avg,
    AVG("Pac") AS pac_avg,
    AVG("Nat") AS nat_avg,
    AVG("Sta") AS sta_avg,
    AVG("Str") AS str_avg
FROM players
GROUP BY "Club";


UPDATE team_averages
SET "Club" = CASE "Club"
    WHEN 'City' THEN 'Manchester City'
    WHEN 'United' THEN 'Manchester Utd'
    WHEN 'Ipswich' THEN 'Ipswich Town'
    WHEN 'Leicester' THEN 'Leicester City'
    WHEN 'Newcastle' THEN 'Newcastle Utd'
    WHEN 'Forest' THEN 'Nott''ham Forest'
    ELSE "Club"
END;

