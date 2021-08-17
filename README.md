# Many-to-Many-Relationships-in-SQL
This application will read roster data in JSON format, parse the file, and then produce an SQLite database that contains a User, Course, and Member table and populate the tables from the data file.

Once the program has been run successfully reading the JSON data, run the following SQL command:
    
    SELECT User.name,Course.title, Member.role 
    FROM User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
    
The output should look as follows:
       
    Zakir|si422|0
    Zack|si334|0
