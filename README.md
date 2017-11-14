# Sisense Analytics


Steps:

1. Create new folder "C:\sisense_analytics"
```
Note: Make sure that you create folder with the same name and syntax "sisense_analytics"
```

2. Download this "sisense_analytics_exe" repository with zip option to your Sisense server.

![image](https://user-images.githubusercontent.com/7319365/32697769-bd4213dc-c7a0-11e7-8c78-a0a2b24bdddb.png)

3. Unzip the "sisense_analytics_exe" repository to the new folder "C:\sisense_analytics".

![image](https://user-images.githubusercontent.com/7319365/32697719-86d809ce-c79f-11e7-803d-c6dd7bacb259.png)

4. If you have Sisense version 6.7 and above, make sure you create WriteUser for accessing your mongo.

[Documentation link](https://documentation.sisense.com/accessing-sisense-application-database)

5. Go to "C:\sisense_analytics\sisense_analytics_solution-master" open configuration file ("sisense_analytics_config.ini") and add WriteUser and password.

It looks like this:

![image](https://user-images.githubusercontent.com/7319365/32697741-fc52c752-c79f-11e7-8580-98094a47e9f4.png)


### In case this is your first set-up:

6. Go to "C:\sisense_analytics\sisense_analytics_solution-master\admin" and open "sisense_analytics.ecube"

7. Run "C:\sisense_analytics\sisense_analytics_solution-master\sisense_analytics.exe" as admin.

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

9. Run full build to ""C:\sisense_analytics\sisense_analytics_solution-master\admin\sisense_analytics.ecube".

### Congratulation you set-up the sisense analytics cube !!!!!

10. Import ""C:\sisense_analytics\sisense_analytics_solution-master\admin\sisense_analytics.dash" to your sisense web.

[Import dash file guide](https://documentation.sisense.com/exporting-importing-dashboards)

11.You can set-up as admin schedule builds with the "C:\sisense_analytics\sisense_analytics_solution-master\admin\build_sisense_analytics.bat" file.

[Example link](https://support.sisense.com/hc/en-us/articles/230646488-Schedule-sequential-ElastiCube-builds-using-windows-task-scheduler)

```
Note: You can test the build by just double click your bat file.
```

12. You can monitor you last build activity with this log:

```
"C:\Sisense Analytics\sisense_analytics_last_log.txt"
```



