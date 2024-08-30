# hearApp

This is a dockerized Python application that uses the requests library to extract data related to commits and issues. This data is then loaded into a SQLite database, upon which dbt is used for simple data transformations, such as aggregating the number of commits and issues by month and by user. 

Please ensure you have Docker installed as it is needed for running the application. 

Instructions for Running this Application: 

1. Begin by Git Cloning the Repository.
2. Run the following commands in your terminal from within the hearApp directory:

   docker build -t hear_app .
   
   docker run hear_app

Running these two commands should provide you with an output ensuring that the Docker Image has been built and that the application has run. The running of the application should reveal that the data loading scripts ran properly, providing the number of data points that were entered into their corresponding tables, as well as the output logs for dbt debug and dbt run, plus a list of tables found under 'main' and main_dbt'. 

The following Architecture Diagram is an example of how this simple dockerized application could be expanded into a more sophisticated end-to-end data processing pipeline. 

   <img width="842" alt="architectureDiagram" src="https://github.com/user-attachments/assets/07966b20-206b-4709-874b-4d1224077e49">

The simple solution leverages the same technologies present in my application, with the addition of AWS S3 buckets for the storage of the extracted data. The benefits of this simple solution are simplicity and ease of use, as SQLite is a serverless database stored within a local file system, making it highly portable. SQLite  maintains ACID compliance ensuring that all transactions are processed in a reliable manner. Additionally, SQLite interacts easily with dbt for data transformations, allowing you to run an entire ETL workflow with minimal resource consumption, perfect for running projects locally. The transformed data stored within SQLite can then be pushed to downstream BI Applications, such as Tableau or PowerBI, for the creation of data visualization dashboards. 

While this simple solution is quite robust in capabilities, it doesn't exactly offer a highly scalable approach. Given that the incoming data is being published to an event broker, we can expect larger data volumes and faster data velocities, especially for real-time data. AWS S3 can still serve as a data lake for raw data, while MongoDB and PostgreSQL are good options for storing data with high-write workloads. PostgreSQL offers the advantages of a typical relational database, such as a strict schema structure, ACID Compliance, and relational datastores, making it perfect for transactional data coming in through the event broker. On the otherhand, MongoDB offers us a more flexible data storage schema that can be scaled horizontally across various servers, perfect for unstructured or semi-structured data, such as the raw data concerning issues and commits coming from the API. Using Snowflake for subsequent data layers is ideal for large-scale cloud-native data processing, as well as complex analytics. Snowflake offers the automated scaling of storage and compute resources independently, allowing you to scale your resources up or down based on workflow demands, without manual intervention. It also offers the ability to handle concurrent workloads, via its multi-cluster architecture, without impacting query performance. This type of scaling can prove to be more challenging with traditional databases. Additionally, the combination of dbt and Snowflake serves as a powerful method for building out a robust and informative data mart, perfect for downstream analytics. Snowflake offers a live and direct connection to tools such as Tableau and PowerBI, ensuring data visualizations serve only the latest data. 










