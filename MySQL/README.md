# MySQL

> The goal is to learn MySQL by developing a comprehensive database solution for an educational institution named **VPK University**. This application should efficiently manage key academic components, including:
>
> - **Students, Courses and Assets Management**

## Database administration

This was categorized using the following roles:

- **admin**: 
  - Has high-level access to the entire MySQL account, serving as an alternative to **root**.
- **architect**:
  - Has high-level access only to the **vpk_university** database.
  - Manages tables.
- **analyst**:
  - Has read-only access to the **vpk_university** database.
  - Only Accesses data.
- **app**:
  - Similar to **architect**, but this role is intended for applications like microservices, not physical users.

## Tables

- **students**: Contains information about students.
  - **id**: Six-digit unique primary key with auto-increment.
  - **name**: Name of the student.
  - **password**: Student's password.
  - **course_id**: Foreign key linked to the **courses** table.

- **courses**: Contains information about courses.
  - **id**: Unique string identifier.
  - **name**: Name of the course.

- **address**: Contains the address of students.
  - **id**: Shared primary key, which is the primary key of the **students** table. Since the address is unique, it's better to have a shared primary key.
  - **area**: Area of the address.
  - **pin_code**: PIN code of the address.

- **assets**: Contains asset details of students like laptop, keyboard, mouse etc.
  - **id**: Unique auto increment id
  - **name**: Asset name
  - **category**: Asset category like laptop or mouse
  - **student_id**: Foreign key linked to the **students** table.

## Steps

### 1. Start MySQL as ROOT

```shell
mysql -h localhost -P 3306 -u root -p // Enter password in prompt
```

### 2. Create admin role and assign to user and login to mysql as admin

- In the below example, admin role created using ROOT account.
- SQL can be logged in as multiple user, the default user is ROOT.
- But Database administrator, should not use ROOT as credentials.
- Using ROOT credentials, create ADMIN role, then create users, and then assign ADMIN role to them.

```sql
-- Create admin role and grant access to whole
CREATE ROLE 'admin'@'%';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%';
GRANT CREATE USER, CREATE ROLE, GRANT OPTION ON *.* TO 'admin'@'%'; -- Above grant is not enough for creating role and user
FLUSH PRIVILEGES;

-- Admin
CREATE USER 'imViki23'@'%' IDENTIFIED BY 'password123';
GRANT 'admin'@'%' TO 'imViki23'@'%';
SET DEFAULT ROLE 'admin'@'%' TO 'imViki23'@'%';
FLUSH PRIVILEGES;
```

### 3. Start MySQL as imViki23 (admin)

```batch
mysql -h localhost -P 3306 -u imViki23 -p // Enter password in prompt
```

### 4. Admin creates database

```sql
CREATE DATABASE vpk_university;

-- Switch between databases
USE vpk_university;
```

### 5. Admin creates supporting roles

- With this admin role create further roles and users.

```sql

-- Architect
CREATE ROLE 'architect';
GRANT ALL PRIVILEGES ON vpk_university.* TO 'architect'@'%';

-- App
CREATE ROLE 'app';
GRANT ALL PRIVILEGES ON vpk_university.* TO 'app'@'%';

-- Analyst
CREATE ROLE 'analyst';
GRANT SELECT ON vpk_university.* TO 'analyst'@'%'; -- Only READ access to analyst so GRANT SELECT ON

FLUSH PRIVILEGES;
```

### 6. Admin creates users and assign roles

```sql

-- Karikalan is an architect, only he is person who has special access to university database
CREATE USER 'karikalan' @'%' IDENTIFIED BY 'password123';
GRANT 'architect' @'%' TO 'karikalan' @'%';
SET DEFAULT ROLE 'architect' @'%' TO 'karikalan' @'%';

-- karuvaki is just an analyst, he can just view database content because he has analyst role
CREATE USER 'karuvaki' @'%' IDENTIFIED BY 'password123';
GRANT 'analyst' @'%' TO 'karuvaki' @'%';
SET DEFAULT ROLE 'analyst' @'%' TO 'karuvaki' @'%';

-- vpk_app needs app role, because app is not a physical user
CREATE USER 'vpk_app' @'%' IDENTIFIED BY 'password123';
GRANT 'app' @'%' TO 'vpk_app' @'%';
SET DEFAULT ROLE 'app' @'%' TO 'vpk_app' @'%';

FLUSH PRIVILEGES;
```

### 7. Start MySQL as karikalan (architect)

Stop using even **admin** role going forward. **architect** should design tables.

```batch
mysql -h localhost -P 3306 -u karikalan -p // Enter password in prompt
```

### 8. Architect creates tables

```sql

USE vpk_university;

CREATE TABLE courses (
    id VARCHAR(100) PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    password VARCHAR(100) NOT NULL,
    name VARCHAR(50) NOT NULL,
    course_id VARCHAR(100) NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(id)
) AUTO_INCREMENT = 100000;

CREATE TABLE address (
    id INT AUTO_INCREMENT PRIMARY KEY,
    area VARCHAR(50) NOT NULL,
    pin_code VARCHAR(6) NOT NULL,
    FOREIGN KEY (id) REFERENCES students(id)
);

CREATE TABLE assets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    category VARCHAR(10) NOT NULL,
    student_id INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- Below are alter command examples

-- Add column with foreign key support
-- ALTER TABLE employees
-- ADD COLUMN role_id INT,
-- ADD FOREIGN KEY (role_id) REFERENCES roles(id);

-- Modify column, here not null is added
-- ALTER TABLE employees
-- MODIFY COLUMN role_id INT NOT NULL;

-- Drop foreign key constraint
-- ALTER TABLE employees DROP FOREIGN KEY employees_ibfk_1;

-- Drop column
-- ALTER TABLE employees DROP COLUMN role_id;
```

### 9. Microservice inserts data through web or mobile app (OR) Architect inserts data manually

```sql
INSERT INTO courses (id, name) VALUES ('ECE', 'Electronics and Communication Engineering');
INSERT INTO courses (id, name) VALUES ('MECH', 'Mechanical Engineering');
INSERT INTO courses (id, name) VALUES ('CSE', 'Computer Science Engineering');

-- $2a$10$3N2ZjQ7AFhIyJWLYcIq4O.A9B4LqCsPfv9YA/RvSCxTxkfaGm2 decodes to Ramesh
INSERT INTO students (password, name, course_id) VALUES ('$2a$10$3N2ZjQ7AFhIyJWLYcIq4O.A9B4LqCsPfv9YA/RvSCxTxkfaGm2', 'Ramesh', 'ECE');
SET @student_id = LAST_INSERT_ID(); -- Shared primary key, so use student table primary key in address table
INSERT INTO address (id, area, pin_code) VALUES (@student_id, 'Thanjai', '234566');
INSERT INTO assets(name, category, student_id) VALUES ('HP Pavilion 15', 'LAPTOP', @student_id);
INSERT INTO assets(name, category, student_id) VALUES ('HP Pavilion Keyboard 1', 'KEYBOARD', @student_id);

-- $2a$10$Fh8zInGfx5QJL5dPlOk0heLsr.xQYmRyQ7wYRmsxDyLI0Ass1assC decodes to Suresh
INSERT INTO students (password, name, course_id) VALUES ('$2a$10$Fh8zInGfx5QJL5dPlOk0heLsr.xQYmRyQ7wYRmsxDyLI0Ass1assC', 'Suresh', 'MECH');
SET @student_id = LAST_INSERT_ID(); -- Shared primary key, so use student table primary key in address table
INSERT INTO address (id, area, pin_code) VALUES (@student_id, 'Theni', '453567');
INSERT INTO assets(name, category, student_id) VALUES ('Dell Mouse 13', 'MOUSE', @student_id);
```

### 10. Try it out

- Login in as **karuvaki** and try inserting data into tables, you will get access denied error for karuvaki, because she has only **analyst** role which has only READ access to tables.

## FAQ's

Refer [FAQ's](FAQ.md#faq)