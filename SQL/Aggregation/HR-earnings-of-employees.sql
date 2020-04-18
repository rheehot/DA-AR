SELECT MAX(SALARY * MONTHS), COUNT(SALARY * MONTHS)
FROM EMPLOYEE
WHERE (SALARY * MONTHS) = (SELECT SALARY * MONTHS FROM EMPLOYEE ORDER BY SALARY * MONTHS DESC LIMIT 1)