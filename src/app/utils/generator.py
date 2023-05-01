import csv
import random
from random import randint
import time
from datetime import datetime
import os
import psycopg2

params = {
    "number_visitor": 100,
    "number_camera": 100,
    "number_shelf": 100,
    "number_product": 100,
    "number_chainStore": 100,
}


def generate_visitor():
    header = ['description', 'location', 'view', 'detection']
    with open('../tables/visitor.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        
        writer.writerow(header)
        
        for i in range(params['number_visitor']):
            id = i + 5
            description = randint(100, 999)
            location = str(randint(150, 200)) + " " + str(randint(150, 200))
            view = str(randint(0, 100)) + ";" + str(randint(0, 100)) + ";" + str(randint(0, 100)) \
                    + str(randint(0, 100)) + ";" + str(randint(0, 100)) + ";" + str(randint(0, 100))
            detection = str(randint(150, 200)) + " " + str(randint(150, 200)) + " " \
                         + str(randint(150, 200)) + " " + str(randint(150, 200))
            
            data = [description, location, view, detection]
            writer.writerow(data)


def generate_camera():
    header = ['location', 'resolution', 'view', 'type_cam']
    with open('../tables/camera.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerow(header)

        for i in range(params['number_camera']):
            id = i + 5
            location = str(randint(150, 200)) + " " + str(randint(150, 200)) + " " + str(randint(150, 200))
            resolution = str(randint(150, 1920)) + " " + str(randint(150, 1080))
            rotation = [str(randint(10, 180)) + " " for i in range(9)]
            type_cam = "SimpleCamera"
            data = [location, resolution, rotation, type_cam]
            writer.writerow(data)


def generate_shelf():
    header = ['location', 'length']
    with open('../tables/shelf.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerow(header)

        for i in range(params['number_shelf']):
            id = i + 5
            location = str(randint(150, 200)) + " " + str(randint(150, 200)) + " " + str(randint(150, 200))
            length = str(randint(150, 200))

            data = [location, length]
            writer.writerow(data)


def generate_product():
    header = ['location', 'name', 'dataEnd', 'weight', 'status', 'price']
    with open('../tables/product.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerow(header)

        for i in range(params['number_product']):
            id = i + 5
            location = str(randint(150, 200)) + " " + str(randint(150, 200)) + " " + str(randint(150, 200))
            length = str(randint(150, 200))

            name = str(i)
            d = random.randint(1, int(time.time()))
            dataEnd = datetime.fromtimestamp(d).strftime('%Y-%m-%d')
            weight = str(randint(1, 100))
            status = random.randint(0, 1)
            price = str(randint(1, 10000))

            data = [location, name, dataEnd, weight, status, price]
            writer.writerow(data)


def generate_chainStore():
    header = ['location', 'name', 'nameDir', "income", "consumption"]
    with open('../tables/chainStore.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerow(header)

        for i in range(params['number_chainStore']):
            id = i + 5
            location = str(randint(150, 200)) + " " + str(randint(150, 200)) + " " + str(randint(150, 200))
            name = str(i)
            nameDir = "Director"
            income = random.randint(1, 1000000)
            consumption = random.randint(1, 1000000)

            data = [location, name, nameDir, income, consumption]
            writer.writerow(data)



def generate_relations(table_name, n, m):
    header = ['idn', 'idm']
    
    with open(table_name, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        
        writer.writerow(header)
        
        for i in range(n):
            
            idm = randint(1, m)
            data = [i + 1, idm]
            writer.writerow(data)


def main():

    generate_visitor()
    generate_camera()
    generate_shelf()
    generate_product()
    generate_chainStore()


    # generate_relations('./tables/mental_visitor.csv', params['number_visitor'], params['number_of_diseases'] - 1)


def copy_to_database():

    conn = psycopg2.connect(database = "shop", user="postgres", password="postgres", host="localhost", port="6432")
    print("Databes opened")

    cursor = conn.cursor()

    os.system("sudo cp -rf tables/ /home/akovel/Documents/bmstu/ics7-db-cw/src/data/PGDATA/csv_tables/")
    cursor.execute(open("../scripts/copy_from_csv.sql", "r").read())

    conn.commit()
    conn.close()

    print("ALL DONE")
    
    
if __name__ == "__main__":
    main()
    copy_to_database()
