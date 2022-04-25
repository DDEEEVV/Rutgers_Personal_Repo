-- Create a new table
BEGIN;


CREATE TABLE IF NOT EXISTS public.banks
(
    bank_id integer[],
    bank_name character varying(50),
    bank_routing_number bigint,
    PRIMARY KEY (bank_id)
);
END;

-- Query all fields from the table
SELECT * FROM banks;
