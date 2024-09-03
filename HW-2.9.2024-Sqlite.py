"""
SQLITE

1. Create/Drop table:
CREATE TABLE shopping (id INTEGER PRIMARY KEY, name TEXT, amount
INTEGER);
מייצר את שמות העמודים בלי הערכים
--

DROP TABLE shopping
מוחק אותה
--------------------------------------------------------------------
2. Rename table:
ALTER table shopping RENAME to shopp
ALTER table shopp RENAME to shopping
-- alter changes the table name
------------------------------------------------------
3. Insert rows into table:
INSERT INTO shopping VALUES (1, 'Avokado', 5);
INSERT INTO shopping VALUES (2, 'Milk', 2);
INSERT INTO shopping VALUES (3, 'Bread', 3);
INSERT INTO shopping VALUES (4, 'Chocolate', 8);
INSERT INTO shopping VALUES (5, 'Bamba', 5);
INSERT INTO shopping VALUES (6, 'Orange', 10);

1	Avokado	    5
2	Milk	    2
3	Bread	    3
4	Chocolate	8
5	Bamba	    5
6	Orange	    10
---------------------------------------------------
4. Display table:
select * from shopping

1	Avokado 	5
2	Milk	    2
3	Bread	    3
4	Chocolate	8
5	Bamba	    5
6	Orange	    10
----------------------------------------------------------
5. ?
SELECT id, name FROM shopping

1	Avokado
2	Milk
3	Bread
4	Chocolate
5	Bamba
6	Orange
------------------------------------------------------------------
6. ?
SELECT * FROM shopping WHERE amount > 5
4	Chocolate	8
6	Orange	    10

SELECT * FROM shopping WHERE amount = 2
2	Milk	2

SELECT * FROM shopping WHERE name LIKE 'Bamba'
5	Bamba	5

--------------------------------------------------------------
7. ?
DELETE from shopping WHERE name like 'Orange';
1	Avokado	    5
2	Milk	    2
3	Bread	    3
4	Chocolate	8
5	Bamba	    5
------------------------------------------------------------
8. ?
UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'
1	Avokado 	5
2	Milk	    2
3	Bread	    3
4	Chocolate	8
5	Bisli   	5

UPDATE shopping SET amount=1 WHERE name LIKE 'Milk'
1	Avokado 	5
2	Milk    	1
3	Bread	    3
4	Chocolate	8
5	Bisli	    5
---------------------------------------------------
9. ?
ALTER TABLE shopping ADD COLUMN maavar
ID      Name        amount      maaver
1	    Avokado 	5
2	    Milk    	1
3	    Bread   	3
4	    Chocolate	8
5	    Bisli   	5
------------------------------------------------------------------------
10. ?
UPDATE shopping SET maavar=6 WHERE id=1;
UPDATE shopping SET maavar=3 WHERE id=2;
UPDATE shopping SET maavar=12 WHERE id=3;
UPDATE shopping SET maavar=8 WHERE id=4;
UPDATE shopping SET maavar=5 WHERE id=5;

3	Bread	    3	12
4	Chocolate	8	8
1	Avokado 	5	6
5	Bisli	    5	5
2	Milk	    1	3
--------------------------------------------------------------------------
11. ?
SELECT * FROM shopping WHERE amount > 1 AND maavar > 5
1	Avokado 	5	6
3	Bread	    3	12
4	Chocolate	8	8

SELECT * FROM shopping WHERE maavar BETWEEN 3 AND 5
2	Milk	1	3
5	Bisli	5	5
------------------------------------------------------------------
12. ?
SELECT * FROM shopping ORDER BY maavar
2	Milk	    1	3
5	Bisli	    5	5
1	Avokado 	5	6
4	Chocolate	8	8
3	Bread	    3	12
# The ORDER BY command sorts the result set in ascending order by default.

SELECT * FROM shopping ORDER BY maavar DESC
3	Bread	    3	12
4	Chocolate	8	8
1	Avokado	    5	6
5	Bisli	    5	5
2	Milk	    1	3
# DESC: To sort the records in descending order

----------------------------------------------------------------
13. ?
CREATE TABLE books (id INTEGER PRIMARY KEY, name TEXT);
INSERT INTO books VALUES (1, 'SQL PROGRAMMING');
INSERT INTO books VALUES (2, 'CSHARP PROGRAMMING');
# Table: Books
ID  name
1	SQL PROGRAMMING
2	CSHARP PROGRAMMING

DELETE FROM books;
-------------------------------------------------------------
14. ?
SELECT COUNT(*)from shopping
5

SELECT MAX(amount) from shopping
8

SELECT AVG(amount) from shopping
4.4

SELECT MIN(amount) from shopping
1
-------------------------------------------------------------
15. ?
INSERT INTO shopping VALUES (6, 'Onions', 3, 6);
3	Bread   	3	12
4	Chocolate	8	8
1	Avokado 	5	6
6	Onions  	3	6
5	Bisli   	5	5
2	Milk    	1	3

INSERT INTO shopping VALUES (7, 'Orio', 1, 8);
3	Bread	    3	12
4	Chocolate	8	8
7	Orio	    1	8
1	Avokado	    5	6
6	Onions	    3	6
5	Bisli	    5	5
2	Milk	    1	3

Select maavar, COUNT(*)FROM shopping GROUP BY maavar
maavar  count
3	    1
5	    1
6	    2
8	    2
12	    1

# SELECT maavar, COUNT(*): This part of the query selects two things:
# maavar: This is the column you're interested in.
# It could be something like a product ID, category, or any other identifier in your shopping table.
# COUNT(*): This counts the number of rows for each unique value in the maavar column.
# FROM shopping: This specifies the table you're querying from, which in this case is shopping.
# GROUP BY maavar: This groups the rows in the shopping table by each unique value in the maavar column.
# The COUNT(*) function then counts the number of rows in each group.

----------------------------------------------------------------
16. ?
SELECT id AS "SECRET", name, amount, maavar FROM shopping

secret  name        amount  maavar
1	    Avokado 	5	    6
2	    Milk	    1   	3
3	    Bread	    3	    12
4	    Chocolate	8	    8
5	    Bisli   	5	    5
6	    Onions	    3	    6
7	    Orio	    1	    8
-----------------------------------------------------------------------
17. ?
Select maavar, COUNT(*)FROM shopping GROUP BY maavar HAVING COUNT(*)>1
maavar  count
6   	2
8	    2
-------------------------------------------------------------------------

18. ?
CREATE TABLE prices (id INTEGER PRIMARY KEY, price INTEGER);
INSERT INTO prices VALUES (1, 3);
INSERT INTO prices VALUES (2, 7);
INSERT INTO prices VALUES (3, 12);
INSERT INTO prices VALUES (4, 5);
INSERT INTO prices VALUES (5, 3);
INSERT INTO prices VALUES (6, 2);
INSERT INTO prices VALUES (7, 10);

ID  price
1	3
2	7
3	12
4	5
5	3
6	2
7	10

SELECT s.id, s.name, s.amount, s.maavar, p.price FROM shopping s JOIN
prices p ON s.id=p.id

ID  name        amount      maavar      price
1	Avokado	    5	         6	        3
2	Milk	    1	         3	        7
3	Bread	    3	         12	        12
4	Chocolate	8	         8      	5
5	Bisli	    5            5	        3
6	Onions	    3	         6	        2
7	Orio	    1	         8	        10

שאילתה זו שולפת נתונים מהטבלאות shopping ו-prices כך
שהנתונים ישולבו ביניהן בהתבסס על התאמה של הערכים בעמודה id.
התוצאה תהיה סט של שורות המכיל את העמודות id, name, amount,
ו-maavar מהטבלה shopping, וגם את העמודה price מהטבלה prices,
וכל זה רק עבור השורות שבהן יש התאמה בין הערכים של id בשתי הטבלאות.

--------------------------------------------------------------------------

19. ? SECRET מה מחושב בתוך

SELECT s.id, s.name, s.amount, s.maavar, p.price, s.amount * p.price AS
"SECRET" FROM shopping s JOIN prices p ON s.id=p.id
ID      name            amount      maavar      price       secret
1	    Avokado	        5	        6       	3       	15
2	    Milk	        1	        3	        7       	7
3	    Bread	        3	        12	        12      	36
4	    Chocolate   	8       	8	        5       	40
5	    Bisli       	5	        5	        3       	15
6	    Onions      	3	        6	        2       	6
7	    Orio	        1	        8	        10	        10

בחר s.id, s.name, s.amount, s.maavar, p.price,
ו (s.amount * p.price בתור "secret") מטבלת shopping עם הכינוי s,
והצטרף לטבלת prices עם הכינוי p באמצעות s.id=p.id.

בתוך SECRET, מחושב הערך של כמות (s.amount) הפריטים שנרכשו כפול במחיר היחידה (p.price).
התוצאה היא המחיר הכולל עבור אותה כמות של הפריט,
כלומר כמה כסף צריך לשלם עבור הכמות המסוימת של המוצר הזה.
--------------------------------------------------------------------------------------------------

20. ?
SELECT s.id, s.name, s.amount, s.maavar, p.price FROM shopping s JOIN
prices p ON s.id=p.id WHERE p.price = (SELECT MAX(price) FROM prices)

ID      name            amount      maavar      price
3	    Bread	        3	        12	        12
---------------------------------------------------------------------------------------------

( 2 ( פתור:
Students
BIRTH (INTEGER)
CITY (TEXT)
NAME (TEXT)
ID (INTEGER)PRIMARY KEY
1974
TEL AVIV
SHALOM
1
1980
RAANANA
YURI
2
1994
RISHON
ANAT
3
1990
REHOVOT
DANA
4
1987
JERUSALEM
OMER
5
GRADE

ID      Birth       Name        City
1	    1974    	SHALOM  	TEL AVIV
2	    1980	    YURI	    RAANANA
3	    1994	    ANAT    	RISHON
4	    1990	    OMER    	REHOVOT
5	    1987	    GRADE   	JERUSALEM
------------------------------------------
- כתוב את השאילתות ליצירת הטבלאות )ללא האיכלוס(
SELECT ID, NAME, BIRTH FROM Students
=>
1	SHALOM	1974
2	YURI	1980
3	ANAT	1994
4	OMER	1990
5	GRADE	1987
___________________________________________________________________

- כתוב שאילתא אשר מדפיסה את כל התלמידים ולכל תלמיד את הציון שהוא קיבל
1.
ALTER TABLE Students ADD COLUMN score
result:
ID      Birth       Name        City        Score
1	    1974	    SHALOM	    TEL AVIV
2   	1980	    YURI	    RAANANA
3	    1994	    ANAT    	RISHON
4	    1990	    OMER    	REHOVOT
5	    1987	    GRADE   	JERUSALEM

2.
UPDATE Students SET score = 80 WHERE id=1;
UPDATE Students SET score = 87 WHERE id=2;
UPDATE Students SET score = 92 WHERE id=3;
UPDATE Students SET score = 100 WHERE id=4;
UPDATE Students SET score = 77 WHERE id=5;

Result:
ID      Birth       Name        City        Score
1	    1974    	SHALOM  	TEL AVIV	80
2	    1980    	YURI    	RAANANA 	87
3	    1994    	ANAT    	RISHON  	92
4   	1990	    OMER    	REHOVOT	    100
5	    1987	    GRADE   	JERUSALEM	77
___________________________________________________________________
- כתוב שאילתא אשר מחשבת את הממוצע הכיתתי

SELECT AVG(score) from Students
=> 87.2
___________________________________________________________________
- כתוב שאילתא להוספת עמודה EXCELLENT . כעת שים YES כאשר הציון גבוה מ- 90 אחרת שים NO

ALTER TABLE Students ADD COLUMN EXCELLENT

UPDATE Students
SET EXCELLENT = 'YES'
WHERE score > 90;

UPDATE Students
SET EXCELLENT = 'NO'
WHERE score < 90;

ID      Birth       Name        City        Score       EXCELLENT
1	    1974	    SHALOM	    TEL AVIV	80	        NO
2	    1980    	YURI    	RAANANA	    87	        NO
3	    1994    	ANAT	    RISHON	    92	        YES
4   	1990	    OMER    	REHOVOT	    100	        YES
5	    1987	    GRADE   	JERUSALEM	77	        NO
___________________________________________________________________

- *כתוב שאילתא אשר מדפיסה את כל התלמידים ולכל תלמיד את הציון שהוא קיבל רק עבור
התלמידים אשר קיבלו מעל הממוצע

SELECT Name, Score
FROM Students
WHERE Score > (SELECT AVG(Score) FROM Students);

Result:
ANAT	92
OMER	100
___________________________________________________________________

- * כתוב שאילתא אשר מדפיסה את התלמיד ואת ציונו עבור התלמיד אשר קיבל את הציון הגבוה
ביותר

SELECT Name, Score
FROM Students
WHERE Score = (SELECT MAX(Score) FROM Students);

Result:
OMER	100


"""