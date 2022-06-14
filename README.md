# PythonFlask_WhitPosgreSQL_APIREST
REST API whit Python, Flask and PostgreSQL, using the HTTP protocol with the *GET, POST, PUT* and *DELETE* methods and the JSON format to send and receive data.

First install the necessary packages whit: pip flask flask-cors psycopg2 python-decouple python-dotenv

Import the database into PostgreSQL using the backup found in the Backup_Database folder in this project

Activate the virtual environment whit: .\venv\Scripts\activate

Modify the .env file for your database manager environment variables:

SECRET_KEY=SECRET_KEY

PGSQL_HOST=host

PGSQL_USER=user

PGSQL_PASSWORD=password

PGSQL_DB=database

Verify the correct functioning of the api through any (Api-testing) creating each of the GET, POST, PUT and DELETE methods. Passing a JSON as a parameter to the POST methods

__*POST METHOD*__

![image](https://user-images.githubusercontent.com/81335756/173490448-05dbe33d-2769-4927-8e47-31d8a7d19214.png)

![image](https://user-images.githubusercontent.com/81335756/173490531-09629556-66f1-4cea-8976-b265c402ccd1.png)

__*GET METHOD*__

![image](https://user-images.githubusercontent.com/81335756/173490945-1a3825dd-6a70-4764-834c-c00af3b102f7.png)

![image](https://user-images.githubusercontent.com/81335756/173490999-79595a28-66d3-4ede-98f0-a365f27539c2.png)

![image](https://user-images.githubusercontent.com/81335756/173491098-29613faf-d7d1-4c23-aacc-1ec9ab325b0d.png)

__*PUT METHOD*__

![image](https://user-images.githubusercontent.com/81335756/173491201-b3b65fe1-089f-4ecb-a62d-38a30e5edc10.png)

__*DELETE METHOD*__

![image](https://user-images.githubusercontent.com/81335756/173491286-632e7c39-347c-4546-a91f-00f1a797e7b9.png)


# SWAGGER

Being a local api, it will not show all its operation correctly, however, it will show part of its documented operation (find it in a TXT in the SWAGGER folder of this project).

![image](https://user-images.githubusercontent.com/81335756/173492097-b9b98e38-b219-487d-9354-286b79677da7.png)

