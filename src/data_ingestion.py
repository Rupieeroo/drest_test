import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine
from dataframe_from_dict import DataFrameFromDict
import json

engine = create_engine('sqlite:///:memory:')

def read_json():
    '''
        Reads the json file and returns it as a dictionary
    '''
    try:
        with open('data/data.json', 'r') as f:
            data_dict = json.loads(f.read())
        print("Successfully loaded json")
        return data_dict
    except:
        print("Something went wrong when writing to the file")


def clean_data(data=dict):
    '''
        Cleans the data to be output as a DataFrame
    '''
    with DataFrameFromDict(data) as df:
    # DataFrame built by class in dataframe_from_dict.py
        df['anonymous_id'] = df['anonymousId']
        df['af_channel'] = df['context.traits.af_channel']
        df['af_status'] = df['context.traits.af_status']
        df['device_id'] = df['context.traits.device_id']
        df['user_id'] = df['context.traits.user_id']
        df['username'] = df['context.traits.username']
        df['app_opened_at_timestamp'] = df['context.traits.app_opened_at_timestamp']
        df['app_session_id'] = df['context.traits.app_session_id']
        df['build'] = df['context.traits.build']
        df['campaign'] = df['context.traits.campaign']
        df['campaign_id'] = df['context.traits.campaign_id']
        df['email'] = df['context.traits.email']
        df['reputation'] = df['context.traits.reputation']
        df['time_units'] = df['context.traits.time_units']
        df['dollars'] = df['context.traits.dollars']
        df['install_timestamp'] = df['context.traits.install_timestamp']
        df['app_opened_at_timestamp'] = df['context.traits.app_opened_at_timestamp']
        df['game_stage_1xp_start_timestamp'] = df['context.traits.game_stage_1xp.start_timestamp']
        df['game_stage_1xp_completed_timestamp'] = df['context.traits.game_stage_1xp.completed_timestamp']
        df['game_stage_1xp_completed_in_game_time_seconds'] = df['context.traits.game_stage_1xp.completed_in_game_time_seconds']
        df['game_stage_1xp_photoshoot_challenge_start_timestamp'] = df['context.traits.game_stage_1xp_photoshoot_challenge.start_timestamp']
        df['game_stage_1xp_photoshoot_challenge_completed_timestamp'] = df['context.traits.game_stage_1xp_photoshoot_challenge.completed_timestamp']
        df['game_stage_1xp_photoshoot_challenge_completed_in_game_time_seconds'] = df['context.traits.game_stage_1xp_photoshoot_challenge.completed_in_game_time_seconds']
    return df


def dataframe_to_sql(df=object):
    '''
        outputs the dataframe to a relational database sql schema and prints the result
    '''
    try:
        output_sql = df.to_sql('ios', engine)
        print('DataFrame successfully loaded to SQL Schema')
        return output_sql
    except:
        print('DataFrame to SQL failed')
    finally:
        # Read from the relational table
        res = pd.read_sql_query('SELECT * FROM ios', engine)
        print(res)


if __name__ == "__main__":
    raw_data = read_json()
    cleaned_data = clean_data(raw_data)
    dataframe_to_sql(cleaned_data)