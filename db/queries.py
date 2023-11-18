import sqlite3
from pathlib import Path


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / 'db.sqlite')
    cursor = db.cursor()


def create_tables():
    # cursor.execute(
    #     '''
    #     DROP TABLE IF EXISTS
    #     '''
    # )
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
        ('Роббинзон Крузо', 10.00, 'link'),
        ('Ромео и Джулиетта', 9.00, 'link')
        '''

    )

def get_products():
    cursor.execute(
        '''
        SELECT * FROM products
        '''
    )
    print(cursor.fetchall())


if __name__ == '__main__':
    init_db()
    create_tables()
    populate_tables()
    get_products()
