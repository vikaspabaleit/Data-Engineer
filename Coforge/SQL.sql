1. How would you find duplicate records in a table and delete only the duplicates while keeping one copy?

  WITH dup_data AS (
  select col1, col2, col3, email_id, id,
  ROW_NUMBER() OVER(partition by email_id order by id ) as row_num 
  from employee
  )
  select col1, col2, col3, email_id, id from dup_data where row_num = 1
  
2. A table has a start_date and end_date column. How would you calculate the total number of overlapping days across all rows?

