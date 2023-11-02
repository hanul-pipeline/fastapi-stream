import configparser
import mysql.connector
import os

current_dir = os.path.dirname(os.path.abspath(__file__))


# read config
def get_config(group, req_var):
    config_dir = os.path.join(current_dir, '../config/config.ini')

    config = configparser.ConfigParser()
    config.read(config_dir)
    result = config.get(group, req_var)
    
    return result


# db connection
def db_conn(charset=True):
    host = get_config('MySQL', 'host')
    user = get_config('MySQL', 'user')
    password = get_config('MySQL', 'passwd')
    database = get_config('MySQL', 'database')
    port = get_config('MySQL', 'port')
    
    if charset:
        conn = mysql.connector.connect(host=host,
                                       user=user,
                                       password=password,
                                       database=database,
                                       port=port)
    else:
        conn = mysql.connector.connect(host=host,
                                       user=user,
                                       password=password,
                                       database=database,
                                       port=port,
                                       charset='utf8mb4')
        
    return conn


# confirmed
def flatten_dict(dictionary, parent_key='', sep='_'):
    items = {}
    
    for k, v in dictionary.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v

    return items


# confirmed
def return_rows(items):
    item_list = []

    measurement = items["measurement"]
    rest = items
    del rest["measurement"]

    for index in measurement:
        item = {**rest, **index}
        item_list.append(item)

    return item_list

