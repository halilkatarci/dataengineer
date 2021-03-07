# Data Engineer Masterclass

This github repository describes the necessary steps to download the imdb dataset and transfer it to the previously prepared tables in mysql. Please create the tables using the commands in `create_tables.sql`.  

### Clone Steps

0. Clone this repo

`git clone https://github.com/mertyyanikk/dataengineer`

1. Enter `dataengineer` directory

### Dependency Steps

3. First and biggest dependency python 3.7 or higher.

4. After Python setup is complete, run requirements.txt.

`pip install -r requirements.txt`

### Deployment steps
5. Create `imdb_dataset` directory and get in.

`mkdir imdb_dataset && cd imdb_dataset`

6. Download imdb dataset. If you have any problem with `wget`, you can download manually with the following link. Please make sure that your dataset is in the `imdb_dataset` directory. (https://datasets.imdbws.com/)

`wget -r -nH -R "index.html*" --cut-dirs=1 https://datasets.imdbws.com/`

7. Go back to the dataengineer folder.

`cd ..`

8. Fill in <...> and run the command once to integrate the imdb dataset into mysql.

`HOST=<user-ip> USER=<mysql-username> PASSWORD=<mysql-password> DATABASE=<database-name> python imdb_to_mysql.py`

* `HOST` IP address where mysql is installed 
* `USER` Mysql user name
* `PASSWORD` Mysql password
* `DATABASE` Database name which you want to import data
