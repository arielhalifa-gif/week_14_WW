import pandas as pd


class DataManipulation:

    @staticmethod
    def add_new_column(df):
        df['risk_level'] = pd.cat(df['range_km'], [0, 20, 100, 300, 10000], labels=['low', 'medium', 'high', 'extreme'])
        return df
    
    @staticmethod
    def replace_null(df):
        df_no_null = df.replace(to_replace=["NaN", "NULL"], value="Unknown", inplace=False)
        return df_no_null