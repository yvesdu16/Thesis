import pandas as pd
import yaml
from sqlalchemy import create_engine


def parse_db() -> pd.DataFrame:
    setting = open("settings.yml")
    parsed_settings = yaml.load(setting)
    engine = create_engine(
        'mssql+pyodbc://' + parsed_settings["ServerName"] + '/' + parsed_settings["Database"] + "?" + parsed_settings[
            "Driver"])
    df = pd.read_sql_query("SELECT  * FROM data", engine)
    return df
