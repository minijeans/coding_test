-- 코드를 입력하세요
-- AND OR의 우선순위 때문에 OR쪽에 괄호...!
SELECT ANIMAL_ID
     , NAME
  FROM ANIMAL_INS
 WHERE (NAME LIKE '%EL%' OR NAME LIKE '%el%' OR NAME LIKE '%eL%' OR NAME LIKE '%El%')
   AND ANIMAL_TYPE = 'Dog'
 ORDER BY NAME;