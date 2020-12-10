import pandas as pd
from pprint import pprint
import os
import datetime

from json_structure import data

json_data = {
  "expand": "schema,names",
  "issues": [
    {
      "fields": {
        "issuetype": {
          "avatarId": 10300,
          "description": "",
          "id": "10005",
          "name": "New Feature",
          "subtask": "False"
        },
        "status": {
          "description": "A resolution has been taken, and it is awaiting verification by reporter. From here issues are either reopened, or are closed.",
          "id": "5",
          "name": "Resolved",
          "statusCategory": {
            "colorName": "green",
            "id": 3,
            "key": "done",
            "name": "Done"
          }
        },
        "summary": "Recovered data collection Defraglar $MFT problem"
      },
      "id": "11861",
      "key": "CAE-160"
    },
    {
        "fields": {
          "issuetype": {
            "avatarId": 10300,
            "description": "",
            "id": "10005",
            "name": "New Feature",
            "subtask": "False"
          },
          "status": {
            "description": "A resolution has been taken, and it is awaiting verification by reporter. From here issues are either reopened, or are closed.",
            "id": "5",
            "name": "Resolved",
            "statusCategory": {
              "colorName": "green",
              "id": 3,
              "key": "done",
              "name": "Done"
            }
          },
          "summary": "Recovered data collection Defraglar $MFT problem"
        },
        "id": "11861",
        "key": "CAE-160"
      }
    ],
  "maxResults": 5,
  "startAt": 0,
  "total": 160
}

##############################

pre = os.path.dirname(os.path.realpath(__file__))
file_name = 'json_structure.json'
file_name = 'pet.json'
path = os.path.join(pre, file_name)
df = pd.read_json(path)
# pprint(vars(df))
# FIELDS = ["key", "fields.summary", "fields.issuetype.name",\
#      "fields.status.name", "fields.status.statusCategory.name"]

# df_norm = pd.json_normalize(json_data['issues'])

df_norm = pd.json_normalize(data['issues'], max_level=999)
# list_local_tab = ['CAMERA.items', 'FACING.items', 'NOTE_UNSUCCESS.items']
dict_local_tab = {'CAMERA.items': None, 'FACING.items': None,
                  'NOTE_UNSUCCESS.items': None}

for i, v in dict_local_tab.items():
    df_local = df_norm[i]
    df_local = pd.json_normalize(df_local[0])
    dict_local_tab[i] = df_local

# local_items = ['CAMERA.items', ]

# df_local = df_norm['CAMERA.items']
# df_local = pd.json_normalize(df_local[0])

# df_local = df_norm['CAMERA.items']
# df_local = pd.json_normalize(df_local[0])

# for k, v in file_to_printed.items():
#     date_name = datetime.datetime.now()
#     write_file_name = f'level_{k}_{date_name}.csv'
#     write_path = os.path.join(pre, write_file_name)
#     v.to_csv(path_or_buf=write_path)

# CAMERA_items = pd.json_normalize(df_norm['CAMERA.items'], max_level=999)

date_name = datetime.datetime.now()
write_file_name = f'level_CAMERA.items_{date_name}.xlsx'
write_path = os.path.join(pre, write_file_name)
writer = pd.ExcelWriter(write_path, engine='xlsxwriter')
df_norm.to_excel(writer, sheet_name='global_table')
for k, v in dict_local_tab.items():
    v.to_excel(writer, sheet_name=k)
writer.save()
