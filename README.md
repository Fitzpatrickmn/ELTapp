# hearApp

This is a dockerized Python application that uses the requests library to extract data related to commits and issues. This data is then loaded into a SQLite database, upon which dbt is used for simple data transformations, such as aggregating the number of commits and issues by month and by user. 

Please ensure you have Docker installed, as it is needed for running the application. 

Instructions for Running this Application: 

1. Begin by Git Cloning the Repository.
2. Run the following commands in your terminal from within the hearApp directory:

   docker build -t hear_app .
   docker run hear_app

Running these two commands should provide you with an output ensuring that the Docker Image has been built and that the application has run. The running of the application should reveal that the data loading scripts ran properly, providing the number of data points that were entered into their corresponding tables, as well as the output logs for dbt debug and dbt run, plus a list of tables found under 'main' and main_dbt'. 



   <img width="842" alt="architectureDiagram" src="https://github.com/user-attachments/assets/07966b20-206b-4709-874b-4d1224077e49">

