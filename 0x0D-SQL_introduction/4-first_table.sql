-- Script that creates a table called first_table in the current database in your MySQL server.
CREATE TABLE first_table(
	id INT,
	name VARCHAR(256))
FROM information_schema.tables WHERE table_schema = DATABASE()
IF NOT EXISTS first_table;
