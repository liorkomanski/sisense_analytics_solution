# -*- coding: utf-8 -*-
'''
DESCRIPTION
   Sisense Analytics based CSV
AUTHOR
    Dan Kushner (dan.kushner@sisense.com)

'''
from __future__ import print_function
import subprocess
import os
import time
import string
import json
import re  #split library
import csv
import pymongo as mongo
import ConfigParser
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Export_collection_to_csv:

    def __init__(self, collection, headers, log):
        self.collection= collection
        self.headers = headers
        self.log=log
        self.rows= []

    def create_rows(self):
        for i, d in enumerate(self.collection, 1):
            row={}
            for h in self.headers:
                if '.' in h: # Handle Mongo collection with object inside objects types
                    query= h.split('.')
                    try:
                        row[h] = str(d[query[0]][query[1]])#.encode('utf8') if self.isaAcii(d[query[0]][query[1]]) else row[h] = d[query[0]][query[1]]
                    except:
                        row[h] = None
                        pass
                else:
                    try:
                        row[h] = str(d[h])#.encode('utf8') if self.isAscii(d[h]) else row[h] = d[h]
                    except:
                        row[h] = None
                        pass
            self.rows.append(row)
        return self.headers, self.rows


    def create_csv(self, name, headers, rows):
        Config = ConfigParser.ConfigParser()
        Config.read(r"sisense_analytics_config.ini")
        path_directory = Config.get('csv_directory_path', 'path')
        try:
            with open(os.path.join(path_directory,name+'.csv'), 'wb') as f:
                f_csv = csv.DictWriter(f, headers, extrasaction='ignore')
                f_csv.writeheader()
                f_csv.writerows(rows)
        except Exception as e:
            print('Fail- Could not run psm ' + e.message, file=log)




    def get_user_by_group(self):
        rows = [];
        for i in self.collection:
            if 'groups' in i:
                for g in i['groups']:
                    row = {}
                    row['_id'] = i['_id']
                    row['userName'] = str(i['userName'])
                    row['group_id'] = str(g)
                    rows.append(row)
        return rows



class PSM_build:

    def __init__(self, cube, mode, log):
        self.log = log
        self.cube = cube
        self.mode = mode
        self.psm = r"C:\Program Files\Sisense\Prism\Psm.exe"


    def get_cube_info(self):
        try:
            cube_info = subprocess.check_output('"' + self.psm + '" ecube info name="' + self.cube + '"', shell=True)
            print(cube_info, file=log)
        except Exception as e:
            print('Fail- Could not run psm ' + e.message, file=log)
            return

    def build_process(self):
        try:
            cube_build_process = subprocess.check_output('"' + self.psm + '" ecube build name="' + self.cube + '" ' +'"mode="'+ self.mode , shell=True)
            print(cube_build_process, file=self.log)
            # print(cube_build_process)
            if "build successfully ended" in cube_build_process:
                print ("Boom successfully ended!!!!!", file=self.log)
                return
            else:
                print("Something build_process fail", file=self.log)
        except Exception as e:
            print("Something don't work execute build process, please check that you set up sisense analytics cube and you executed the first build manually", file=self.log)



if __name__ == '__main__':
    START = time.time()
    repository = r"C:\ProgramData\Sisense\PrismWeb\Repository"
    prod = r"C:\ProgramData\Sisense\PrismWeb\DB\Prod"
    Config = ConfigParser.ConfigParser()
    Config.read(r"sisense_analytics_config.ini")
    path_directory = Config.get('csv_directory_path', 'path')
    #create_dir_for_csv(path_directory)
    mongo_ip= Config.get('mongo_location', 'ip')
    mongo_port=Config.get('mongo_location', 'port')
    get_user_by_group=Config.get('get_users_by_group', 'generate')
    log= open(os.path.join(path_directory, 'sisense_analytics_last_log.txt'), 'w+')
    if os.path.exists(repository):
        user = Config.get('mongo_auth', 'user')
        password = Config.get('mongo_auth', 'password')
        print(user, password, file=log)
        """ Connect to MongoDB """
        try:
            c = mongo.MongoClient('mongodb://' + user + ':' + password + '@'+mongo_ip+':'+mongo_port+'/')
            print ("Connected successfully", file=log)
        except Exception as e:
            print ("Could not connect to MongoDB: "+ e, file=log)
            exit()
    else:
        """ Connect to MongoDB """
        try:
            c = mongo.MongoClient(mongo_ip, int(mongo_port))
            print ("Connected successfully", file=log)
        except Exception as e :
            print ("Could not connect to MongoDB: "+ e, file=log)
            exit()



    '''------------(1) elasticube collection-----------------'''
    print('Process elasticube collection.....')
    collection_elasticube=c["prismWebDB"].elasticubes.find({})
    headers_elasticubes=['_id','server','title']
    elasticubes=Export_collection_to_csv(collection_elasticube, headers_elasticubes, log)
    rows=elasticubes.create_rows()
    elasticubes.create_csv('elasticubes', rows[0], rows[1])

    '''------------(2) users collection-----------------'''
    print('Process users collection.....')
    collection_users=c["prismWebDB"].users.find({})
    headers_users=['_id','active','created','email','userName','firstName','lastName','groups','lastLogin','lastUpdated','activeDirectory','roleId']
    users=Export_collection_to_csv(collection_users, headers_users,log)
    rows=users.create_rows()
    users.create_csv('users', rows[0], rows[1])

    if str(get_user_by_group) == 'y':
        '''--------- Create user by group CSV ------------'''
        print('Process users_by_group collection.....')
        collection_users_by_group = c["prismWebDB"].users.find({})
        user_by_group_header = ['_id', 'userName', 'group_id']
        user_by_group = Export_collection_to_csv(collection_users_by_group, user_by_group_header, log)
        users_by_group_rows = user_by_group.get_user_by_group()
        user_by_group.create_csv('users_by_group', user_by_group_header, users_by_group_rows)

    '''------------(3) groups collection-----------------'''
    print('Process groups collection.....')
    collection_groups = c["prismWebDB"].groups.find({})
    headers_groups=['_id','name','admins','everyone','created','lastUpdated','ad']
    groups = Export_collection_to_csv(collection_groups, headers_groups, log)
    rows = groups.create_rows()
    groups.create_csv('groups', rows[0], rows[1])

    '''------------(4) roles collection-----------------'''
    print('Process users roles.....')
    collection_roles = c["prismConfig"].roles.find({})
    headers_roles = ['_id', 'name']
    roles = Export_collection_to_csv(collection_roles, headers_roles, log)
    rows = roles.create_rows()
    roles.create_csv('roles', rows[0], rows[1])

    '''------------(5) dashboard collection-----------------'''
    print('Process dashboard collection.....')
    collection_dashboards = c["prismWebDB"].dashboards.find({})
    headers_dashboards=['_id','created','editing', 'instanceType','lastUpdated', 'lastUsed', 'oid', 'original','owner','title','type','source','isPublic','usageCount','datasource.id','datasource.title','datasource.database','datasource.address']
    dashboards=Export_collection_to_csv(collection_dashboards, headers_dashboards, log)
    rows = dashboards.create_rows()
    dashboards.create_csv('dashboards', rows[0], rows[1])
    # headers_filters=['_id', 'filters.jaql.dim','filters.jaql.column','filters.jaql.datatype','filters.jaql.table','filters.jaql.level']

    '''------------(6) widgets collection-----------------'''
    print('Process widget collection.....')
    collection_widgets = c["prismWebDB"].widgets.find({})
    headers_widgets = ['_id','created', 'desc', 'instanceType', 'lastUpdated', 'lastUsed', 'oid', 'title', 'type', 'subtype', 'dashboardid', 'usageCount', 'datasource.id', 'datasource.title', 'datasource.address', 'datasource.database']
    widgets = Export_collection_to_csv(collection_widgets, headers_widgets, log)
    rows = widgets.create_rows()
    widgets.create_csv('widgets', rows[0], rows[1])

    '''------------(7) trace collection-----------------'''
    print('Process trace collection.....')
    collection_trace = c["monitor"].trace.find({})
    headers_trace=['_id','message', 'timestamp', 'meta.method','meta.url', 'meta.userId', 'meta.userName', 'meta.response_time','meta.status', 'meta.type']
    trace=Export_collection_to_csv(collection_trace, headers_trace, log)
    rows = trace.create_rows()
    trace.create_csv('trace', rows[0], rows[1])

    '''------------(8) jobs collection-----------------'''
    print('Process jobs collection.....')
    collection_elasticube=c["prismWebDB"].jobs.find({"active" : True, "jobType" : "dashboardSubscription"})
    headers_jobs=['_id','active','created','dashboardId', 'lastExecution', 'lastUpdated', 'lastUsed', 'schedule', 'timezone', 'type', 'executionPerDay', 'isDataChange']
    jobs=Export_collection_to_csv(collection_elasticube, headers_jobs, log)
    rows=jobs.create_rows()
    jobs.create_csv('jobs', rows[0], rows[1])


    '''----------Execute Build ------'''
    cube = Config.get('cube', 'name')
    build_mode = Config.get('cube', 'mode')
    execute_build= Config.get('cube', 'execute_build')
    if str(execute_build) == 'y':
        print('Starting build process.....')
        run_build=PSM_build(cube, build_mode, log)
        run_build.build_process()
        run_build.get_cube_info()

    print('\n' + 'The script took: {} seconds.'.format(str(time.time() - START)), file=log)
