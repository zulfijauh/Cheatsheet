-- Create Schema
CREATE SCHEMA (if not exists) schema_name

-- Create Table
CREATE TABLE (if not exists) schema_name.table_name ( 
    column name 1, datatype(lenght), column_contraint
    column name 2, datatype(lenght), column_contraint
    ..)

-- Insert values of column per row
INSERT INTO table_name VALUES (item 1, item 2,..)
-- (insert accordingly to column's row)

DELETE FROM table_name where column x = item y

-- Update/change the value of column
UPDATE table_name 
SET column x = item y
WHERE column x = item z (replace z with y)

-- Display data
SELECT * FROM table_name 'or select by specific column by:'
SELECT column1, column2, column.. FROM table_name
-- * = all column of table

-- Edit column in table
/* To add/update table */ ALTER TABLE table_name ADD column1
/* To delete table */ ALTER TABLE table_name DROP column1

-- Delete rows/values in the table
/* specific value/condition */ DELETE FROM table_name WHERE condition
/* all rows in table */ TRUNCATE TABLE table_name

-- Delete the table
DROP TABLE table_name


-- General Function
SELECT column1, column2
FROM table_name
WHERE condition OR/AND condition
GROUP by field_name
HAVING condition
ORDER by field_name
LIMIT 'number'

-- Delete duplicate values
SELECT DISTINCT column1 FROM table_name

-- Join and merge more than 1 table
LEFT JOIN table_name alias ON main_alias.column x = joining_alias.column x
RIGHT JOIN table_name alias ON main_alias.column x = joining_alias.column x
INNER JOIN #Joining inner data and all columns side by side
FULL OUTER JOIN /*Joining outer data and all columns side by side */
UNION /* Merge rows and distinct duplicate (all columns betweet two table must have similiar data types */
UNION ALL /* Merge rows and allows all duplication (all columns betweet two table must have similiar data types */

