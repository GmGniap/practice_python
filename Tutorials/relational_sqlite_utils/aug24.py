from sqlite_utils import Database

def create_tableA():
    ## recreate=True for replacing existing file
    db = Database("chickens.db", recreate=True)
    db["tableA"].insert_all([
        {
            "name" : "92 Ron",
            "station_id": 1,
            "region" : 2,
            "Price": 1200,
        },
        {
            "name" : "95 Ron",
            "station_id": 2,
            "region": 1,
            "Price": 1250,
        }    
    ])

    for row in db["tableA"].rows:
        print(row)
        
    db["tableA"].insert(
        {
            "name": "Disel",
            "station_id": 1,
            "region": 2,
            "Price": 1000,
        }
    )
    print("-----x-----")
    print(db.tables)

def create_tableB():
    db = Database("chickens.db")
    db["tableB"].insert_all([
        {
            "station_id": 1,
            "station_name": "Yangon Sanchaung",
            "Status": "Active",
        },
        {
            "station_id": 2,
            "station_name": "Central Sagaing",
            "Status": "Active",
        },
        {
            "station_id": 3,
            "station_name": "Mandalay 35 Street",
            "Status": "Active",
        }
    ])

def create_tableC():
    db = Database("chickens.db")
    db["tableC"].insert_all([
        {
            "region_id":1,
            "region_name": "Yangon",
            "MIMU_Pcode": "MMR0013"
        },
        {
            "region_id":2,
            "region_name": "Sagaing",
            "MIMU_Pcode": "MMR0008",
        },
        {
            "region_id":3,
            "region_name": "Mandalay",
            "MIMU_Pcode": "MMR0007",
        }
    ])
    print(db.tables)

def create_relation():
    db = Database("chickens.db")
    db["tableA"].add_foreign_key("station_id","tableB","station_id")
    db["tableA"].add_foreign_key("region","tableC","region_id")
    print("Done making relation!")

def create_new_table():
    db = Database("chickens.db")
    db.execute("CREATE TABLE new_table AS select a.name,a.station_id, \
                a.region, \
                a.Price, \
                b.station_name, \
                c.region_name from tableA as a \
                INNER JOIN tableB as b ON a.station_id = b.station_id \
                INNER JOIN tableC as c ON a.region = c.region_id \
                order by a.rowid")
    print(db.tables)
    
if __name__ == '__main__':
    ## Creating Tables
    # create_tableA()
    # create_tableB()
    # create_tableC()
    
    ## Create Primary keys
    
    ## Create Foreign keys & make relations
    # create_relation()
    
    ## Show custom sql table that used JOIN
    create_new_table()
    