
-- CREATE SEQUENCE itemnum_seq START 0000001;
-- drop table test;
-- CREATE TABLE test(
    -- itemnum int PRIMARY KEY, 
    -- nut_key int,
    -- code text,
    -- name text
-- );

-- ALTER TABLE test ALTER itemnum SET DEFAULT NEXTVAL('itemnum_seq');

-- INSERT INTO test (nut_key, code, name) VALUES
    -- (3, '1200G-2', 'part')
    -- ;
-- alter table test add constraint code_unique unique (code);


-- CREATE TABLE nuttest(
    -- nutnum int PRIMARY KEY, 
    -- cal text,
    -- name text
-- );
-- CREATE SEQUENCE nutnum_seq START 0000001;
-- ALTER TABLE nuttest ALTER nutnum SET DEFAULT NEXTVAL('nutnum_seq');

INSERT INTO nuttest (cal, name) VALUES
    (100, 'scanner')
    ;
