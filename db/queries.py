import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / 'db.sqlite')
    cursor = db.cursor()


def create_tables():
    cursor.execute(
        '''
        DROP TABLE IF EXISTS products
        '''
    )
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price DESIMAL,
            image TEXT   
        )
        '''
    )
    db.commit()


def populate_tables():
    cursor.execute(
        '''
        INSERT INTO products (name, price, image) VALUES 
        ('Тайота Супра МК-4 белый', 20000, 'image/wallpaperbetter.com_3840x2160.jpg'),
        ('Тайота Супра МК-4 черный', 23000, 'image/wallpaperbetter.com_3840x2160.jpg')
        ('Тайота Супра МК-4 красный', 19000, 'image.supra_red.jpg')
        '''

    )
    db.commit()


def get_products():
    cursor.execute(
        '''
        SELECT * FROM products
        '''
    )
    return cursor.fetchall()


if __name__ == '__main__':
    init_db()
    create_tables()
    populate_tables()
    get_products()
    pprint(get_products())
