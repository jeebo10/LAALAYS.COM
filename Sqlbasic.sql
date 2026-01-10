/*galinta xog cusub table-ka*/
INSERT INTO
    students (studentId, studentName, studentPhone)
VALUES
    (1, 'mahad cali', + 252634295072);

/*soo aqrinta xog cusub. */
SELECT
    *
FROM
    students;

/* wax ka badalidda xogta table-ka */
UPDATE students
SET
    studentName = 'axmed cali'
where
    studentId = 1
    /* ka tirtirinta table-ka*/
DELETE FROM students
WHERE
    studentId = 2;