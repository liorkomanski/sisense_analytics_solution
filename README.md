# Sisense Analytics


### Setting Up guide:

#### 1. Create new folder "C:\sisense_analytics"
```
Note: Make sure that you create folder with the same name and syntax "sisense_analytics"
```

#### 2. Download this "sisense_analytics_exe" repository with zip option to your Sisense server.

![image](https://user-images.githubusercontent.com/7319365/32697769-bd4213dc-c7a0-11e7-8c78-a0a2b24bdddb.png)

#### 3. Unzip the "sisense_analytics_exe" repository to the new folder "C:\sisense_analytics".

![image](https://user-images.githubusercontent.com/7319365/32697719-86d809ce-c79f-11e7-803d-c6dd7bacb259.png)

#### 4. If you have Sisense version 6.7 and above, make sure you create WriteUser for accessing your mongo.

* Open the Sisense Web Application and go to the "Admin" screen.
* Click on the "REST API" tab.
* Click on the blue "REST API Reference" link.
* Expend "admin" section.
* Expend "POST admin/app_database/change_database_user_password" section.
* Set-up new  mongoDB "WriteUser" credentials with the following body:
```
{
  "userName": "WriteUser",
  "password": "sisense1234"
}
```

* Click "RUN" and make sure you receive 200 response massage.

The POST screen will look like this.

![image](https://user-images.githubusercontent.com/7319365/34046233-0829819a-e1b5-11e7-8b06-9500bfbd94e5.png)

[Documentation link](https://documentation.sisense.com/accessing-sisense-application-database)


#### 5. Go to "C:\sisense_analytics\sisense_analytics_solution-master" open configuration file ("sisense_analytics_config.ini") and add WriteUser and password.

It looks like this:

![image](https://user-images.githubusercontent.com/7319365/32697741-fc52c752-c79f-11e7-8580-98094a47e9f4.png)

```
Note: In case your Sisense mongo located on a different server and port, 
you can modify it in the config file under "mongo_location" section.

[mongo_location]
ip=localhost
port=27018

```

#### 6. Go to "C:\sisense_analytics\sisense_analytics_solution-master\admin" and open "sisense_analytics.ecube"

#### 7. Run "C:\sisense_analytics\sisense_analytics_solution-master\sisense_analytics.exe" as admin.

#### 8. Now you will see all your Sisense Analytics CSV files within "C:\sisense_analytics" folder.

```
"C:\sisense_analytics\dashboards.csv"
"C:\sisense_analytics\elasticubes.csv"
"C:\sisense_analytics\groups.csv"
"C:\sisense_analytics\jobs.csv"
"C:\sisense_analytics\roles.csv"
"C:\sisense_analytics\trace.csv"
"C:\sisense_analytics\users.csv"
"C:\sisense_analytics\widgets.csv"
```

#### 9. Run full build to ""C:\sisense_analytics\sisense_analytics_solution-master\admin\sisense_analytics.ecube".

## Congratulation you set-up the sisense analytics cube !!!!!

#### 10. Import dashboard files to your Sisense web. 

* Go to "C:\sisense_analytics\sisense_analytics_solution-master\admin"
* Import dashboard files (1Overview.dash, 2UsersActivity.dash, 3Dashboard.dash) to your Sisense web.
* [Import dash file guide](https://documentation.sisense.com/exporting-importing-dashboards)


#### 11. You can set-up as Admin schedule builds with the "C:\sisense_analytics\sisense_analytics_solution-master\admin\build_sisense_analytics.bat" file.

```
Notes: 
* Using regular schedule builds won't load new data to the elasticubes. Executing batch file required.
* You can test the build by just double click your batch file.
```

[Example link](https://support.sisense.com/hc/en-us/articles/230646488-Schedule-sequential-ElastiCube-builds-using-windows-task-scheduler)


#### 12. You can monitor you last build activity with this log:

```
"C:\Sisense Analytics\sisense_analytics_last_log.txt"
```



