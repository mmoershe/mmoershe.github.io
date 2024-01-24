[1. select mit from, where, order by](#1)  
[2. Erweiterungen mit group by, having](#2)  
[3. Erweiterungen mit den verschiedenen join-Arten](#3)  
[4. Erweiterungen mit union](#4)  
[5. Erweiterungen mit berechneten Spalten, Aliasnamen](#5)  
[6. Views, Funktionen](#6)  
[7. case, like](#7)  
[8. Datentypen](#8)  
[9. Umgang mit null-Werten](#9)  
[10. Das CRUD-Prinzip](#10)  
[11. ER-Modelle](#11)  
[12. Erstellen von Tabellen](#12)  
[13. Constraints und die jeweilige Wirkung,](#13)  
[14. Wozu dient ein Index](#14)  
[15. Transaktionen](#15)  
[16. Der ETL-Prozess](#16)  
[17. REST / UNORGANISED](#17)  

# KLAUSUR 

*Folgende Stichworte sollten Sie verstanden haben und anwenden können:*

<a name="1"></a> 

## select mit from, where, order by

### distinct 
Unique Values im Select
```
select distinct MonthOfYear as uninquemonths from Datumswerte D
    order by MonthOfYear
```

### top 

```
select top(1) Date, WeekOfYear from Datumswerte 
     order by WeekOfYear DESC
```

### order by 
**asc** ist default value, other is **desc**

<a name="2"></a>

## Erweiterungen mit group by, having

### Important Aggregate Functions
- count
- sum
- avg
  - vorher in float umwandeln (mit cast() oder convert())!
- min
- max
- stdev (statistical standard deviation)
- *many more* 

### group by 

```
select Year, MonthOfYear, avg(DayOfMonth) as Average_DayOfMonth from Datumswerte 
     group by Year, MonthOfYear 
     order by Year, MonthOfYear
```

 When you use more than one column in the GROUP BY clause, it groups the results based on the unique combinations of those columns. In your query, it means that each unique combination of "Year" and "MonthOfYear" will be treated as a group, and the AVG(DayOfMonth) will be calculated for each group separately.

### having 

**having** wird nur in Verbindung mit group by benutzt. Damit kann man eine weitere Kondition setzen und Daten aussortieren.  
Der Unterschied zu **where** liegt darin, dass **having** diese Konditionen NACH der Aggregation anwendet.  
Natürlich mit logischer Verknüpfung möglich.  

<a name="3"></a>

## Erweiterungen mit den verschiedenen join-Arten

### INNER JOIN [default]

only returns rows where both tables match the conditiony

### LEFT JOIN 

returns ALL row from the left (first) table and all matching from the right(second) one.  
No matches -> null values for the right table 

### RIGHT JOIN 

vice versa 

### FULL JOIN

also "full outer join" in Pandas.  
Combined LEFT and RIGHT JOIN  
every row from both tables will appear!

### CROSS JOIN 

combined every row from the first table with every row from the second table  
utter chaos 

<a name="4"></a>

## Erweiterungen mit union

<a name="5"></a>

## Erweiterungen mit berechneten Spalten, Aliasnamen

<a name="6"></a>

## Views, Funktionen

### VIEW 

Erstellung virtueller Tabellen um Datenzugriff zu steuern.  
Beispielsweise um bestimmte Columns aus Sicherheitsgründen zu verbergen, unnötige komplexe Daten zu abstrahieren und erleichtern, etc...   

```
CREATE VIEW sales_summary AS
SELECT product_id, SUM(quantity * price) AS total_sales
FROM sales
GROUP BY product_id;
```
> Von nun an kann *sales_summary* als eigener table benutzt werden.  

### Functions

#### concat(*string1 + string2 + string_n*) 

concatenates two or more values into a string.  
works with all datatypes and variables  
```
select concat(Titel, 'asf') from Vorlesungen V 
     join Professoren P 
          on V.gelesenVon = P.PersNr
     where Name like concat('%', @ProfessorName, '%')
```

#### left(*string, n: int*) / right(*string, n: int*)

returns the first n characters from the left (or right) side of a string. If n is higher than len(string), the entire string is returned. Negative values for n throws an error. 

```
select left('I adore Python', 5)
--> 'I ado'
select right('I adore Python', 5)
--> 'ython'
```

#### len(x)

#### convert(), try_convert() or cast() 

minor differences I don't care about. *cast()* is the simpler and more basic function.  

##### convert(*datatype, expression*)

```
convert(int, '1')
```

##### try_convert(*datatype, experssion*)  
>if conversion fails, it returns ***null*** instead of throwing an error. MSSQL exlusive.  

```
try_convert(int, '1')
```

##### cast(*expression* **as** *datatype*)
```
cast('1' as int)
```

#### choose(*index, val1, val2, ..., valn*)

```
select choose(DayOfWeek, 'Monday', 'Tuesday', 'Wednesday', 'Thursady', 'Friday', 'Saturday', 'Sunday') as 'DayOfWeek', 
     count(*) from Datumswerte
          group by DayOfWeek
```

<a name="7"></a>

## case, like

### case expression

- ELSE is optional 

```
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    WHEN conditionN THEN resultN
    ELSE result
END
```

```
select case 
     when DayOfWeek = 1 then 'Monday'
     when DayOfWeek = 2 then 'Tuesday'
     when DayOfWeek = 3 then 'Wednesday'
     when DayOfWeek = 4 then 'Thursday'
     when DayOfWeek = 5 then 'Friday'
     when DayOfWeek = 6 then 'Saturday'
     else 'Sunday' end as 'DayOfTheWeek', 
     count(*) from Datumswerte 
          group by DayOfWeek
```

### like operator 

- The percent sign % represents zero, one, or multiple characters
- The underscore sign _ represents one, single character

```
select * from elden_ring_weapons
     where name like 'Malenia%'
```


<a name="8"></a>

## Datentypen

### STRINGS

> N = Unicode

#### char(n) / nchar(n)
Fixed-length character string with the length *n*. Missing characters are padded with spaces.  

#### varchar(n)
kleiner, schneller, sparsamer, deutsch Sonderzeichen such as aöü  
nvarchar, doppelt so schnell für andere Sonderzeichen und Akzente, für Namen sinnvoll  
es gibt auch varchar(max)  hat kein Maximum, welches natürlicherweise bei ~4096 liegt.   
> PLZ einfach immer als varchar(5) in Deutschland, smallint ist zu klein, int ist ungünstig weil im Osten PLZen mit 0 anfangen! (Außerdem müssen wir nicht mit diesen rechnen)  
### INT
int  
smallint  
### float 
float
### MORE PARTICULAR DATATYPES

#### MONEY
#### DATE  

<a name="9"></a>

## Umgang mit null-Werten

"is not null" anstatt von "=null" 
```
select distinct P.Name from Professoren P 
     left join Vorlesungen V 
          on V.gelesenVon = P.PersNr
     where Titel is null
```

<a name="10"></a>

## Das CRUD-Prinzip

### CREATE
#### insert
> column names are not required if all values are passed. 
```
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...) 
```
#### (create)
```
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
)
```

### READ
#### select
```
SELECT column1, column2, ...
FROM table_name
```
### UPDATE
#### update
```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition
```
#### (alter)
> Modify entire table / database structure
```
ALTER TABLE TableName
ADD NewColumn datatype
```
```
ALTER TABLE table_name
DROP COLUMN column_name
```
```
ALTER TABLE table_name
RENAME COLUMN old_name to new_name
```
### DELETE
#### delete
> deletes rows where condition is met
```
DELETE FROM table_name WHERE condition
```
#### (drop)
> deletes entire tables 
```
drop table table_name 
```
```
drop table if exists table_name
```

<a name="11"></a>

## ER-Modelle

<a name="12"></a>

## Erstellen von Tabellen

<a name="13"></a>

## Constraints und die jeweilige Wirkungen

### PRIMARY KEY

Gewährleistet die Eindeutigkeit und Unveränderlichkeit der ausgewählten Spalten in einer Tabelle. Der Primärschlüssel identifiziert eindeutig jeden Datensatz in der Tabelle.

#### IDENTITY

to automatically increment ID, so theres no need to give it with every insert()  
only one allowed per table
```
IDENTITY(*seed:int=1, increment:int=1*)
```

```
CREATE TABLE employees ( 
     employee_id PRIMARY KEY IDENTITY(1,1)
)
```

### FOREIGN KEY

Definiert eine Beziehung zwischen den Datensätzen in zwei Tabellen, indem sie sicherstellt, dass Werte in einer Spalte einer Tabelle auf Werte in einer anderen Spalte in einer anderen Tabelle verweisen. Dies wird als referenzielle Integrität bezeichnet.

```
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
```

#### CASCADE

```
-- Erstellen der Haupttabelle (orders)
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(50)
);

-- Erstellen der referenzierenden Tabelle (order_items) mit FOREIGN KEY und CASCADE
CREATE TABLE order_items (
    item_id INT PRIMARY KEY,
    order_id INT,
    item_name VARCHAR(50),
    CONSTRAINT fk_order FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

> CONSTRAINT keyword ist hier nur, um diesem constraint einen Namen zu geben

```
CREATE TABLE referencing_table (
    -- ...
    referencing_column1 data_type,
    referencing_column2 data_type,
    -- ...
    FOREIGN KEY (referencing_column1, referencing_column2, ...)
        REFERENCES referenced_table (referenced_column1, referenced_column2, ...)
        ON DELETE referential_action
        ON UPDATE referential_action
);
```

### UNIQUE

ensures values are unique. Also allows (one) NULL value.  

```
CREATE TABLE students (
    student_id INT UNIQUE,
    student_name VARCHAR(50)
)
```

### CHECK 

Eigene Bedingungen von Spalten definieren.  

```
CREATE TABLE employees (
    employee_id INT PRIMARY KEY identity(1,1),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hire_date DATE,
    salary money CHECK (salary >= 0)    
)
```

### DEFAULT

sets default value  

```
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date DATE DEFAULT GETDATE()
)
```



<a name="14"></a>

## Wozu dient ein Index

Ein Index wird in der Regel nicht explizit benutzt. Er beschleunigt lediglich das Arbeiten in der Datenbank.  
Ein richtiger Index ist extrem wichtig beim Beschleunigen einer Datenbank  
beim Kreiieren wird automatisch auf ID Primärschlüssel ein Index gelegt.  
Ohne Index muss man immer einen Tablescan machen num mit einem where einen Datensatz zu finden.  
Indizen werden besonders schnell, wenn man einen unique Index erstellt.
Mehr Speicherplatz benötigt.  

```
create unique index ixtextsp3 on test 
```





<a name="15"></a>

## Transaktionen

<a name="16"></a>

## Der ETL-Prozess

---
---

<a name="167"></a>

# UNORGANISED

SQL ist mengenbasiert (?)  
mengenbasierter Ansatz, MENGENLEHRE (??)  
Seit 1992 ging die Sprache in viele Richtungen, in Details leider unterschiedlich :( [SQL Dialekte (tf?)]  
Wir gehen auf die Version von Microsoft  
Variabilität eines Kommandos ist extrem hoch  
Man unterscheidet zwischen relationalen (SQL) Datenbanken und NoSQL (not only SQL)  

# SQL Basics 

## Statements 

### Variables 
```
declare @given_number INT
set @given_number = 2137

select count(*) anzahl_Vorlesungen_von_bestimmter_Personalnr from Professoren P 
     join Vorlesungen V 
          on P.PersNr = V.gelesenVon
     where PersNr = @given_number
```

### case when then end

```
CASE
   WHEN condition1 THEN result1
   WHEN condition2 THEN result2
   ...
   ELSE else_result
END
```

```
select case 
     when DayOfWeek = 1 then 'Monday'
     when DayOfWeek = 2 then 'Tuesday'
     when DayOfWeek = 3 then 'Wednesday'
     when DayOfWeek = 4 then 'Thursday'
     when DayOfWeek = 5 then 'Friday'
     when DayOfWeek = 6 then 'Saturday'
     else 'Sunday' end as 'DayOfTheWeek', 
     count(*) from Datumswerte 
          group by DayOfWeek
```

## Functions

### concat(*string1 + string2 + string_n*) 

concatenates two or more values into a string.  
works with all datatypes and variables  
```
select concat(Titel, 'asf') from Vorlesungen V 
     join Professoren P 
          on V.gelesenVon = P.PersNr
     where Name like concat('%', @ProfessorName, '%')
```

### left(*string, n: int*) / right(*string, n: int*)

returns the first n characters from the left (or right) side of a string. If n is higher than len(string), the entire string is returned. Negative values for n throws an error. 

```
select left('I adore Python', 5)
--> 'I ado'
select right('I adore Python', 5)
--> 'ython'
```

### len(x)

### convert(), try_convert() or cast() 

minor differences I don't care about. *cast()* is the simpler and more basic function.  

#### convert(*datatype, expression*)

```
convert(int, '1')
```

#### try_convert(*datatype, experssion*)  
>if conversion fails, it returns ***null*** instead of throwing an error. MSSQL exlusive.  

```
try_convert(int, '1')
```

#### cast(*expression* **as** *datatype*)
```
cast('1' as int)
```

### choose(*index, val1, val2, ..., valn*)

```
select choose(DayOfWeek, 'Monday', 'Tuesday', 'Wednesday', 'Thursady', 'Friday', 'Saturday', 'Sunday') as 'DayOfWeek', 
     count(*) from Datumswerte
          group by DayOfWeek
```


# Basics 

SQL ist formatfrei  
Bei MS SQL ist das Semicolon nicht erforderlich (außer bei common tables expressions (with))  
NICHT case sensitive! select == SELECT  
AUCH NICHT IN STRINGS????  
Ist bei Datenbanken standard. crazy fucking horny shit  
(COLLATION)   

Umlaute werden interpretiert, beispielsweise ß ist ss  

between schließt Ränder mit ein 
between 50 and 59 INKLUSIVE 50 und 59  

trim() wie strip()  
subselect  

SQL interpretiert strings nach lexikanischer Sortierung  ("c4">"c3")  

<> ist ungleich  

letzte Stelle eines Integers % 10  

Tabellennamen fangen mit Buchstaben an und haben einen sinnvollen Namen  
Name einer Spalte ist ein Attribut  
Datensätze = Zeilen 
Elemente haben keine Reihenfolge, bzw. die Reihenfolge ist unerheblich  
Wenn es auf Reihenfolge ankommt, muss man diese extern anfordern.  
Relationale Abfragen sollten die gesamte Tabellenstruktur berücksichtigen um eine Frage zu beantworten.  
SQL ist immer eine Beigabe zu anderen Programmiersprachen (PYTHONNNNN :snake_emoji:)  
Maßgabe war: mit einem englischen Satz Datenbank befragen (ist aber nicht mehr ganz so lollo)  
join nicht wie in Python, sondern es "joined" zwei Tabellen.    
mit Python Script auf SQL Datenbank zugreifen?  
SQL Queries sind unumkehrbar  

Bei einem binären Operator wird der kleinere von beiden Datentypen verwendet
Beispiel:  
332/100 --> 3

**'' statt ""!**  

"gruppiert nach" heißt nicht direkt dass group by verwendet werden soll  

arrays: ()  

"is not null" anstatt von "=null"  

## Gesamtkonstrukt 

Ein Datenbankserver muss laufen, damit er die Datenbank benutzen kann. Datenbankserver ist eine Software Komponente welche lokal läuft und hat eine Verbindung zu einer Datenbank. An diesen Datenbankserver werden auch die Commands gescchickt und wir bekommen einen Ergebnistext zurück (Recordset).  
Um diese Anfrage erst stellen zu können, braucht man eine weitere Softwarekomponente (Management Studio oder Azure Data Studio oder VSCode)

Dreiwertige Logik 

Null ist auch zu sich selbst verschieden.  
# Kommandos 

use 

count, zählt nur Anzahl, für Anzahl individueller Werte count(distinct "Spalte") benutzen  

alias  
sql abbeitet nicht von oben nach unten ab, "P" kann hier benutzt werden bevor dieser Alias "definiert" wird.   
```
select P.Name, V.Titel 
    from Professoren P
        join Vorlesungen V
            on P.PersNr = V.gelesenVon
```

---

Distinct zusatz an Menge dransetzen, um Dubletten zu entfernen  
distinct value1, value2  
heißt, dass die Kombination von value1, value2 distinct sein muss!  
Selationen Kalkül   

like 
eine art Filterbedingung ig?  
Trunkierungsoperatoren
like ist kein RegEx äquivalent  
Platzhalter %, steht für 0-n Zeichen, im RegEx: .*?  
Platzhaler _, steht für genau ein Zeichen, im RegEx: .  
Platzhalter [a-c] ein Zeichen mit a, b, c und [^e-g] ohne die Zeichen e, f, g  

GO unterteilt das Script in logische Sinneinheiten, welche einzlend ausgeführt werden. Wenn ein Error auftaucht, springt er zum nächsten GO.  

group by 
asc ist default value, desc nicht  
mehrere Sortierkriterien  
group by Rang desc, Name asc  

top()
wählt eine gewisse menge an Zeilen zurück  
"with ties"  um bei Dopplungen alle zu bekommen.  

as or = für Bennenung  von Ausgabespalten  

**Namen der Tabellen anzeigen:**  
select * from sys.tables

iif()  
inline function  
erstes teil ist eine Bedingung  
zweites wenn true  
drittes wenn false   
geht auch verschachtelt  
toll für Einzelvergleiche  

case when (bedingung) then (wenn True) else (wenn False) end as (name)  
(gibt es irgendwie auch mit enumerate)  
lässt sich natürlich auch verschachteln  
else ist optional  



Select  
Select * from Tablename  
EIGENTLICH ist das eine Kürzung von dem hier:   
select * from dbo.Tablename  

**Aggregatfunktionen** == Werte sind durch Zählen oder anderen Mathematischen Funktionen, anstelle dass man einfach eine Menge zurückgibt. 

stringaggregate 
try_convert 
case when then 
first day of a wekk is nicht immer Montag!!!!!!!!!  

## constraints  

primary key (MatrNr, VorlNr)  
kann auch bedeuten, dass die KOMBINATION unique ist. Hier könnte zum Beispiel jeweils eins von beiden Null sein  
Null-Werte sind auch eindeutige Werte. Null müsste man explizit ausschließen mit beispielsweise 
```
MatrNr int not null, 
VorlNr int not null
```

Einschränkungen für Werte beim Erstellen von Tabellen 
```
create table test (
  ID int primary key, -- Die IDs sind garantiert unterschiedlich
  -- uniqueidentifier kann bei verteilten Systemen verwendet werden. 
  Sp2 varchar(10) null, 
  Sp3 varchar(10) not null, -- Hier muss immer ein Wer stehen 
)
```

Was ist ein Index?????  
Ein Index wird in der Regel nicht explizit benutzt. Er beschleunigt lediglich das Arbeiten in der Datenbank.  
Ein richtiger Index ist extrem wichtig beim Beschleunigen einer Datenbank  
beim Kreiieren wird automatisch auf ID Primärschlüssel ein Index gelegt.  
Ohne Index muss man immer einen Tablescan machen num mit einem where einen Datensatz zu finden.  
Indizen werden besonders schnell, wenn man einen unique Index erstellt.  
```
create unique index ixtextsp3 on test 
```

Fremdschlüssel ist mit einem Primärschlüssel verknüpft, er kann aber nicht NUR an einem primärschlüssel verbunden sein, sondern auch an eine Spalte, welche einen Unique Constraint hat.  
Vorteil:  
- Möglichkeit dass aus Referenz "Kaskaden" entstehen können, welche beim Löschen oder Updaten verwendet werden.  

Mit Kaskade wird zum Beispiel, wenn man den Carnap löscht, auch die referenzierten Datensätze aus anderen Tabellen mit gelöscht.  [on delete cascade]  
mit on update delete werden Änderungen an Datensätzen auch an referenzierte Datensätze in anderen Tabellen übernommen   

Lösch anomalie, wenn keine Fremdschlüsselverbindung, mithilfe des Löschens schaffen 

## CRUD 

- Create
  - insert
  - (create)
- Read
  - select
- Update 
  - update
  - (alter)
    - gesamte Tabelle
- Delete 
  - delete
  - (drop)
    - gesamte Tabelle

## create

### Datentypen
varchar, kleiner, schneller, sparsamer, deutsch Sonderzeichen such as aöü  
nvarchar, doppelt so schnell für andere Sonderzeichen und Akzente, für Namen sinnvoll  
es gibt auch varchar(max)  hat kein Maximum, welches natürlicherweise bei ~4096 liegt.  
eingebauter "Date" Datentyp  
smallint  
PLZ als varchar(5) in Deutschland, smallint ist zu klein, int ist ungünstig weil im Osten PLZen mit 0 anfangen! (Außerdem müssen wir nicht mit diesen rechnen)  
money  

Wichtige Aspekte beim Modellieren von Datenbanken:  
Beziehungen zwischen Entitäten mit Primary Key  
Datentypen  

Implizite Typenkonvertierung wenn zwei verschiedene Datentypen aufeinandertreffen, beispielsweise wenn man einen varchar durch hundert teilt 

# Entitäten und Datebankstrukturierung  

beispiel vornamen csv mit Jahr Vorname Anzahl Geschlecht Position  [Position ist wegen zweiter Vorname und so]  
was ist eine Entität?  
Klasse eines konkreten Objektes, Beschreibung von gleichartigen Objekten  
Ist Maria W der gleiche Name wie Maria M??  
Das Jahr ist eine gute Entität  
Anzahl ist eine schlecht Entität, die Anzahl muss zu was anderem dazugehören!  
Geschlecht könnte eine eigene Entität sein.  
Position ist eine schlechte Entität, es sagt nichts +ber den Namen aus.  
drei Tabellen: 
*Name* mit Vorname und Geschlecht (+ID)  
*vergeben* mit Position und Anzahl  
*Jahr* mit Jahr  
Regel: Jede Entität wird zu einer Tabelle und jede mzum-Beziehung wird zu einer Tabelle.  
1:n / n:1  

# ER Modell 
Grundsätzliches Ziel der Normalisierung der Daten, um Redundanzen zu entfernen.  

## ETL Prozess 
Extract, Transform, Load (einer der Hauptaufgaben von Data Scientists)  
Redundanz entfernen 

# SQL Transaktion 

zum "ausprobieren"  
man kann einen bestimmten Code in SQL zu einer Transaction machen und diese dann wieder collbacken 

```
begin transaction 
commit 
begin transaction 
  select * from Studenten 
  delete * from Studenten 
  ...
rollback 
```

LOCKS verstehen lollo  
deadlock = zwei systeme warten auf sich gegenseitig, lösung: eins wir geopfert  

INDEX = sortierte teilsichten auf Daten, sortiert in Bäumen

DML = Data Manipulation Language 
DDL = Data Definition Language

