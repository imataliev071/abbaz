import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / 'db.sqlite')
    cursor = db.cursor()


def create_tables():
    cursor.execute('''DROP TABLE IF EXISTS all_cars''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS all_cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    descr TEXT,
    price INT,
    url TEXT,
    img TEXT
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS quest (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age TEXT,
        car_marka TEXT,
        bm TEXT,
        how_cars TEXT
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subscribe (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_user
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS 'Order' (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_user INT,
        id_products INT
    )
    ''')
    cursor.execute('''DROP TABLE IF EXISTS products''')
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price DESIMAL,
            image TEXT,
            id_marka INTEGER,
            FOREIGN KEY (id_marka) REFERENCES marka (id) 
        )
        '''
    )
    db.commit()

    cursor.execute('''DROP TABLE IF EXISTS marka''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS marka (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    ''')


def populate_tables():
    cursor.execute(''' 
        INSERT INTO marka (name) VALUES 
        ('Tayota'),
        ('Nissan'),
        ('Lexus')
    ''')
    cursor.execute(
        '''
        INSERT INTO products (name, price, image, id_marka) VALUES 
        ('Супра МК-4 белый', 20000, 'image/supra_white.jpg', 1),
        ('Супра МК-4 черный', 23000, 'image/supra_black.jpg', 1),
        ('Супра МК-4 красный', 29000, 'image/supra_red.jpg', 1),
        ('Nissan GRT 35', 30000, 'image/nissan_gtr_1.jpg', 2),
        ('Nissan GRT 34', 20000, 'image/nissan_gtr_2.jpg', 2),
        ('Lexus lx-570', 53988, 'image/lexus_570.jpg', 3 ),
        ('Lexus lx-600', 86900, 'image/lexus_600.jpg', 3 )
        '''

    )
    db.commit()


def get_products(id_n):
    cursor.execute(
        '''
        SELECT * FROM products WHERE id_marka = :id_n
        ''', {'id_n': id_n}
    )
    return cursor.fetchall()


def save_questions(data_quest):
    print(data_quest)
    cursor.execute('''
        INSERT INTO quest (name, age, car_marka, bm, how_cars) VALUES 
        (:name, :age, :car_marka, :bm, :how_cars)
    ''', data_quest)
    db.commit()


def receiving_user_id():
    cursor.execute('''
    SELECT id_user FROM subscribe
    ''')
    return cursor.fetchall()


def save_all_cars(title, descr, price, url, img):
    data = {
        'title': title,
        'descr': descr,
        'price': price,
        'url': url,
        'img': img
    }

    cursor.execute('''
    INSERT INTO all_cars (title, descr, price, url, img) VALUES
    (:title, :descr, :price, :url, :img)
    ''', data)

    db.commit()


def save_subscribe(data_subscribe):
    print(data_subscribe)
    cursor.execute('''
    INSERT INTO subscribe (id_user) VALUES 
    (:id_user)
    ''', {'id_user': data_subscribe})
    db.commit()


def get_marka():
    cursor.execute(
        '''
        SELECT * FROM marka
        '''
    )
    return cursor.fetchall()


def save_bay_cars(customer, data_bay_cars):
    print(data_bay_cars)
    cursor.execute('''
    INSERT INTO 'Order' (id_user, id_products) VALUES 
    (:id_user, :id_products)
    ''', {'id_user': customer, 'id_products': data_bay_cars})
    db.commit()


if __name__ == '__main__':
    init_db()
    create_tables()
    populate_tables()
    get_products()
    pprint(get_products())
