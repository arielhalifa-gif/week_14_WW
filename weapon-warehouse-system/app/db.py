import mysql.connector


class DbConnector:
    @staticmethod
    def create_connection():
        config = {'user': 'user',
                  'password': 'password',
                  'host': '127.0.0.1',
                  'database': 'weapon_warehouse',
                  'raise_on_warnings': True}
        connection = mysql.connector.connect(**config)
        return connection

    @staticmethod
    def create_db():
        conn = DbConnector.create_connection()
        cursor = conn.cursor()
        query = "CREATE DB IF NOT EXISTS weapon_warehouse"
        cursor.execute(query)
        conn.commit()
        cursor.close()
        return "dataBase created"
    
    @staticmethod
    def create_table():
        conn = DbConnector.create_connection()
        cursor = conn.cursor()
        query = """ CREATE TABLE IF NOT EXISTS 'weapons_list' (
                            `ID` int PRIMARY_KEY AUTO_INCREMENT,
                            `weapon_id` varchar(50),
                            `weapon_name` varchar(50),
                            `weapon_type` varchar(50),
                            `range_km` int,
                            `weight_kg` float,
                            `manufacturer` varchar(50),
                            `origin_country` varchar(50),
                            `storage_location` varchar(100),
                            `year_estimated` int,
                            `risk_level` varchar(50))"""
        cursor.execute(query)
        conn.commit()
        cursor.close()
        return "table created"
    

    @staticmethod
    def insert_data(clean_df):
        conn = DbConnector.create_connection()
        cursor = conn.cursor()
        query = """INSERT INTO weapons_list(weapon_name, weapon_type, range_km, weight_kg, manufacturer,
                        origin_country, storage_location, year_estimated, risk_level)
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        for row in clean_df:
            cursor.execute(query, (row["weapon_name"],
                                   row["weapon_type"],
                                   row["range_km"],
                                   row["weight_kg"],
                                   row["manufacturer"],
                                   row["origin_country"],
                                   row["storage_location"],
                                   row["year_estimated"],
                                   row["risk_level"],),)
        conn.commit()
        cursor.close()
