"""Database functions"""
from sqlalchemy import create_engine, Engine, text

def get_connection_url(params_dict: dict) -> str:
    """
    builds connection url from config dict
    :param params: dictionary with config
    """
    # create connection url
    host = params_dict["host"]
    port = params_dict["port"]
    dbname = params_dict["dbname"]
    user = params_dict["user"]
    password = params_dict["password"]
    connection_url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
    
    return connection_url

def get_all_tables_in_schema(engine: Engine, schema: str) -> tuple:
    """
    Query all tables in given schema
    """
    query = f"SELECT table_name from information_schema.tables WHERE table_schema = '{schema}' AND table_name NOT IN ('geography_columns', 'geometry_columns', 'spatial_ref_sys')"
    with engine.connect() as con:
        result = con.execute(text(query))

    return result

def get_all_schemata(engine: Engine) -> tuple:
    """
    Query all tables in given schema
    """
    query = "SELECT schema_name from information_schema.schemata WHERE schema_name NOT IN ('pg_catalog', 'information_schema','public')"
    with engine.connect() as con:
        result = con.execute(text(query))

    return result
