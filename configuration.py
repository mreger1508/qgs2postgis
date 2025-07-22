"""Module to load pg_service.conf"""
import os
import subprocess
import configparser as cp
from configparser import ConfigParser

def check_pg_service_conf():
    """
    check if pg_service.conf exists
    """
    pg_service_path = os.path.expanduser("~/.pg_service.conf")
    
    if not os.path.isfile(pg_service_path):
        with open(pg_service_path, "w", encoding="utf-8") as conf:
            conf.write("# PostgreSQL service definitions\n")
            conf.write("[sample_service]\n")
            conf.write("host=localhost\n")
            conf.write("port=5432\n")
            conf.write("dbname=sample_database\n")
            conf.write("user=sample_user\n")
            conf.write("password=sample_password\n")

def load_services():
    """
    read pg_service.conf and return all serivces
    """
    # path to .pg_service_conf
    pg_service_path = os.path.expanduser("~/.pg_service.conf")

    # read config
    config = cp.ConfigParser()
    config.read(pg_service_path)

    # list all services
    services = config.sections()

    return services, config

def get_connection_params(config: ConfigParser, service: str) -> dict:
    """
    read connection params from config for service
    """
    # get connection params
    params_dict = {}
    for key, value in config[service].items():
        params_dict[key] = value
    
    return params_dict

def open_filedialog():
    """
    Open .pg_service.conf directory
    """
    pg_service_path = os.path.expanduser("~/.pg_service.conf")
    subprocess.run(["open", "-R", pg_service_path])

def get_config(service: str) -> ConfigParser:
    """
    get config
    """
    # path to .pg_service_conf
    pg_service_path = os.path.expanduser("~/.pg_service.conf")

    # read config
    config = cp.ConfigParser()
    config.read(pg_service_path)

    return config
