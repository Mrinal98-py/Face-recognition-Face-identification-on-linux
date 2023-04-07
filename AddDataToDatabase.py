import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("/home/buddy/PycharmProjects/faceR/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://facer-e4a8c-default-rtdb.firebaseio.com/"
})
#address realtime | data storage
#https://console.firebase.google.com/u/0/project/facer-e4a8c/database/facer-e4a8c-default-rtdb/data/~2F
#https://facer-e4a8c-default-rtdb.firebaseio.com/

ref = db.reference('faceR')

data = {
    "mr": {
            "name": "buddybok",
            "major": "coding",
            "starting_year": 2012,
            "total_attendance": 10,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
    },

    "om":
         {
             "name": "Emly Blunt",
             "major": "Economics",
             "starting_year": 2021,
             "total_attendance": 12,
             "standing": "B",
             "year": 1,
             "last_attendance_time": "2022-12-11 00:54:34"
         }

}

for key, value in data.items():
    ref.child(key).set(value)
