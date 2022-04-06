# Works Single View

## Describe briefly the matching and reconciling method chosen.

 1- Reading from the csv file as a Dictionary with the DictReader method from the csv library.
 2- Converting data into appropiate type with some string methods such as 'split()'.
 3- Grouping works' data into tuples (selected for it's efficiency) and appending them into a list of cleaned data.
 3- From a set of the cleaned data list, to ensure not creating same object twice, created the objects to be saved into the PostgreSQL DB with the object manager method get_or_create, again, to ensure data does not duplicates in the DB. 


## 2. We constantly receive metadata from our providers, how would you automatize the process?

Unless there is a heavy reason to handle it from the backend, i would automate this process adding an app to the django project with a UI for the providers to upload data to the system instead of sending the csv file.

If need be, i would host the project on Heroku, select the storage for the file to be saved at and set a scheduled script to be run with a defined frequency as an add-on on Heroku. 

https://devcenter.heroku.com/articles/advanced-scheduler

## Intructions on how to execute.

Exceute the code as a regular django command with 'import_data' and appending the file's name as an argument:

```
python manage.py import_data works_metadata.csv
```


# Works Single View API

## 1. Imagine that the Single View has 20 million musical works, do you think your solution would have a similar response time?

The query to the DB is the most time cosuming task for the whole operation, if for every request it needs to query the DB, filter all unwanted rows to just get 1 record, no it wouldn't

## 2. If not, what would you do to improve it?

I would modify the view function to cache the data, so next time the same record is requested it can be served from the cached and not from the DB. 

I would also pair with the DBA for query optimization ideas such as index creation. 

## Intructions on how to execute.

Query the API by just entering the url followed by the ISWC code

```
http://127.0.0.1:8000/<iswc>
```



