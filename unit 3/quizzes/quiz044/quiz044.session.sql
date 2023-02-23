select count(*) from sqlite_master where type = "table";

select count(*) from INHABITANT WHERE gender="Male" and state="Friendly";

select avg(gold), villageid from INHABITANT GROUP BY villageid;

select count(*) from item where item like "A%";

select count(distinct job) from INHABITANT;

select DISTINCT item from item, INHABITANT where INHABITANT.job="Herbalist";