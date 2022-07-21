-- Creation of policy table
CREATE TABLE IF NOT EXISTS policy (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL,
  object varchar(25) NOT NULL,
  action varchar(10) NOT NULL
);

-- Fill Policies table
INSERT INTO policy(user_id, object,action) values('1', '*', '*');
INSERT INTO policy(user_id, object,action) values('2', 'visualizations', 'read');
INSERT INTO policy(user_id, object,action) values('2', 'reports', 'write');