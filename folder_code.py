import os
import pandas as pd

make_data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'Country': ['USA', 'UK', 'Australia', 'Germany'],
    'Score': [90, 85, 88, 92],
    'Gender': ['Male', 'Female', 'Male', 'Female']
}


df = pd.DataFrame(make_data)

new_data = {'Name':'Hridoy','Age':23,'Country':'bd','Score':99,'Gender':'Male'}
df.loc[len(df.index)] = new_data

new_data1 = {'Name':'Khan','Age':25,'Country':'india','Score':98,'Gender':'Male'}
df.loc[len(df.index)] = new_data1

new_data2 = {'Name':'borsha','Age':23,'Country':'savar','Score':100,'Gender':'female'}
df.loc[len(df.index)] = new_data2

folder_name = 'data'

os.makedirs(folder_name,exist_ok=True)

file_name = os.path.join(folder_name,'dumy_data.csv')

df.to_csv(file_name,index=False)

print(f'folder and file create successfull on {file_name}')  # folder and file create successfull on data\dumy_data.csv