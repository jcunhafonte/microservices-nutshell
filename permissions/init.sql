-- Creation of policy table based on CasbinRule model
CREATE TABLE IF NOT EXISTS policy (
  id SERIAL PRIMARY KEY,
  ptype varchar(2) NOT NULL,
  v0 INT NOT NULL,
  v1 varchar(25) NOT NULL,
  v2 varchar(25) NOT NULL,
  v3 varchar(25),
  v4 varchar(25),
  v5 varchar(25)
);

-- Fill Policies table
INSERT INTO policy(ptype, v0, v1, v2) values('p', '2', 'users', 'read');
INSERT INTO policy(ptype, v0, v1, v2) values('p', '2', 'visualizations', 'read');
--INSERT INTO policy(ptype, v0, v1 , v2) values('p', '2', 'reports', 'write');