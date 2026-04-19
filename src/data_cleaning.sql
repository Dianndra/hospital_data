-- DATA CLEANING

SELECT *
FROM setadata.dbo.prod_hospital_data;

SELECT *
INTO setadata.dbo.hospital_data
FROM setadata.dbo.prod_hospital_data;
---------------------------------------------------------------------------------------------------------------
--1 REMOVE NULL ROWS
DELETE
FROM setadata.dbo.hospital_data
WHERE facility_uid IS NULL;

DELETE
FROM setadata.dbo.hospital_data
WHERE start_date IS NULL;

----------------------------------------------------------------------------------------------------------------
-- 2 DROP IRRELEVANT COLUMNS
ALTER TABLE setadata.dbo.hospital_data
DROP COLUMN state_unique_id, registration_no, website, email_address, operation_status, doctors, nurses, midwives,
			beds, operational_hours, facility_level_option;

ALTER TABLE setadata.dbo.hospital_data
DROP COLUMN facility_code;

-----------------------------------------------------------------------------------------------------------------
--3 CHANGE DATAYPES AND COLUMN NAME
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'setadata.dbo.hospital_data';

ALTER TABLE setadata.dbo.hospital_data
ALTER COLUMN start_date date;

ALTER TABLE setadata.dbo.hospital_data
ALTER COLUMN facility_uid integer;

EXEC sp_rename 'setadata.dbo.hospital_data.ooperational_days', 'operation_days', 'COLUMN';


-----------------------------------------------------------------------------------------------------------------
--4. CHANGE TO UPPER CASE
UPDATE setadata.dbo.hospital_data
SET physical_location = UPPER(physical_location);

UPDATE setadata.dbo.hospital_data
SET facility_name = UPPER(facility_name);

-------------------------------------------------------------------------------------------------------------------
--5. REMOVE LAGOS FROM PHYSICAL LOCATION COLUMN
SELECT REPLACE(physical_location, 'Lagos', ' ')
FROM setadata.dbo.hospital_data;

