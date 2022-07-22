-- -- Creation of policy table based on CasbinRule model
-- CREATE TABLE IF NOT EXISTS CasbinRule (
--   id SERIAL PRIMARY KEY,
--   ptype varchar(2) NOT NULL,
--   v0 INT NOT NULL,
--   v1 varchar(25) NOT NULL,
--   v2 varchar(25) NOT NULL,
--   v3 varchar(25),
--   v4 varchar(25),
--   v5 varchar(25)
-- );

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS casbin_rule_id_seq;

-- Table Definition
CREATE TABLE casbin_rule (
    id int4 NOT NULL DEFAULT nextval('casbin_rule_id_seq'::regclass),
    ptype VARCHAR(255),
    v0 VARCHAR(255),
    v1 VARCHAR(255),
    v2 varchar(255),
    v3 VARCHAR(255),
    v4 VARCHAR(255),
    v5 VARCHAR(255),
    PRIMARY KEY (id)
);

-- Fill Policies table
INSERT INTO casbin_rule(ptype, v0, v1, v2) values('p', '2', 'users', 'read');
INSERT INTO casbin_rule(ptype, v0, v1, v2) values('p', '2', 'visualizations', 'read');
--INSERT INTO policy(ptype, v0, v1 , v2) values('p', '2', 'reports', 'write');