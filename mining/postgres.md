# Reading
[select](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-select/)
[distinct](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-select-distinct/)
[column-alias](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-column-alias/)

[where and operator in where](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-where/)
[in & not in](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-in/)
[between](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-between/)
[Like & Ilike](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-like/)
[isnull](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-is-null/)	

[subquery](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-subquery/)
[exists](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-exists/)
[any](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-any/)
[all](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-all/)

[order-by](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-order-by/)
[limit & offset](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-limit/)
[fetch](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-fetch/)

[join](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-joins/)
[table-alias](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-alias/)
[inner join](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-inner-join/)
[self-join](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-self-join/)
[cross-join](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-cross-join/)
[natural-join](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-natural-join/)

[group-by](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-group-by/)
[having](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-having/)
[grouping-set](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-grouping-sets/)

[union](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-union/)
[intersect](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-intersect/)
[except](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-except/)


[]()



# NOT Reading
[concat](https://www.postgresqltutorial.com/postgresql-concat-function/)
[lenth](https://www.postgresqltutorial.com/postgresql-length-function/)
[left-join](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-left-join/)
[right-join](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-right-join/)
[full-join](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-full-outer-join/)
[rollup](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-rollup/)
[cube](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-cube/)

ROUND(AVG(length), 2) avg_length
extract

customer INNER JOIN payment USING(customer_id)
customer INNER JOIN payment p ON p.customer_id = c.customer_id

SELECT select_list
FROM table_name
LIMIT row_count OFFSET row_to_skip;

limit 5 offset 3
offset 3 rows fetch first 5 rows only

Summary
Use the ORDER BY clause in the SELECT statement to sort rows.
Use the ASC option to sort rows in ascending order and DESC option to sort rows in descending order. The ORDER BY clause uses the ASC option by default.
Use NULLS FIRST and NULLS LAST options to explicitly specify the order of NULL with other non-null values.

SELECT
	select_list
FROM
	table_name
ORDER BY
	sort_expression1 [ASC | DESC],
	sort_expressionN [ASC | DESC];
	
The LENGTH() function accepts a string and returns the length of that string.


1. from
1. where
1. group by
1. having
1. select
1. distinct
1. order by
1. limit

