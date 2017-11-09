# Sisense Analytics


Steps:

1. Create new folder "C:\sisense_analytics"
```
Note: Make sure that you create folder with the same name and syntax "sisense_analytics"
```
2. Download this "sisense_analytics_exe" repository with zip option to your Sisense server.
3. Unzip the "sisense_analytics_exe" repository to the new folder "C:\sisense_analytics".
4. If you have Sisense version 6.7 and above, make sure you create WriteUser for accessing your mongo.
[Documentation link] (https://documentation.sisense.com/accessing-sisense-application-database)
5. Go to "C:\Sisense Analytics\sisense_analytics_exe" open configuration file ("sisense_analytics_config.ini") and add WriteUser and password.

It looks like this:
```
[mongo_auth]
;ReadUser, AppUser, WriteUser
user = WriteUser 
password = sisense1234
```

In case this is your first set-up:
6. Go to "C:\sisense_analytics\sisense_analytics_exe\admin" and open "sisense_analytics.ecube"
7. Run "C:\sisense_analytics\sisense_analytics_exe\sisense_analytics.exe" as admin.
8. Now you will see all your Sisense Analytics CSV files within "C:\sisense_analytics" folder.

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


## Congratulation you set-up the sisense analytics cube !!!!!

9.You can set-up as admin schedule builds with the "C:\sisense_analytics_exe\admin\build_sisense_analytics.bat" file.
[Example link](https://support.sisense.com/hc/en-us/articles/230646488-Schedule-sequential-ElastiCube-builds-using-windows-task-scheduler)

```
Note: You can test the build by just double click your bat file.
```


10. You can monitor you last build activity with this log:

```
"C:\Sisense Analytics\sisense_analytics_last_log.txt"
```

