# hearApp

Instructions for Running this Application: 

1. Begin by Git Cloning the Repository.
2. Run the following commands in your terminal:

   docker build -t hear_app .
   docker run hear_app

Running these two commands should provide you with an output ensuring that the Docker Image has been built and that the application has run. The running of the application should reveal that the three scripts ran properly, providing the number of data points that were entered into their corresponding tables, as well as the output logs for dbt debug and dbt run, plus a list of tables found under 'main' and main_dbt'. 

   
