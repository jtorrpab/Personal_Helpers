import pandas as pd
import os


# from datetime import datetime
# date_str = '2023-09-15 12:00:00'
# epoch_time = int(datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S').timestamp())

# print(epoch_time)


DEFAULT_PATH_OUT = r"C:\Personal_Projects\Personal_Helpers\Output\json_files\parquet_to_json"
file_path = r'C:\Users\juan.pablo.t.pabon\Downloads\informe_cartera.parquet'

columns_date = ['fecha_venc_neto', 'fecha_aplaza', 'fecha_comp', 'fecha_contab', 'fecha_stamp']

try:
    parquet_file = pd.read_parquet(file_path, engine="fastparquet")
    json_file = parquet_file.to_json(orient="records")
    #print(parquet_file.head(5))

    #Dar fomato a la fecha
    for column in columns_date:
        parquet_file[column] = (parquet_file[column] - pd.Timestamp('1970-01-01')) // pd.Timedelta(microseconds=1)
        parquet_file[column] *= 1000000
        parquet_file[column] = pd.to_datetime(parquet_file[column], unit="us")

        print(parquet_file[column])

    print("In progress")
except Exception as e:
    print(f"Error: {str(e)}")