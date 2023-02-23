reate or replace procedure SNOWFLAKE_PYTHON_DB.PUBLIC.for_loop_over_cursor()
returns string
language javascript
as
$$
declare "SNOWFLAKE_PYTHON_DB"."PUBLIC"."OBJECT_NAME" float;
version float;
object_name varchar;
DB varchar;
c1 cursor for select max(version) version, object_name, DB, schema from sql_deployment_file group by DB, Schema, object_name

