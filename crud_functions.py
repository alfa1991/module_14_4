import sqlite3

def initiate_db():
    """Создает таблицу Products, если она еще не создана."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_all_products():
    """Возвращает все записи из таблицы Products."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products

def insert_sample_data():
    """Заполняет таблицу Products примерными данными."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Проверяем, есть ли уже данные в таблице
    cursor.execute('SELECT COUNT(*) FROM Products')
    count = cursor.fetchone()[0]

    if count == 0:
        sample_products = [
            ('CodliverOil', 'Кодливерное масло, полезно для здоровья.', 500),
            ('PapayaLeaf', 'Листья папайи, хороши для пищеварения.', 300),
            ('VitaminCOriginal', 'Оригинальный витамин C, укрепляет иммунитет.', 400),
            ('CranberryExtract', 'Экстракт клюквы, полезен для мочевыводящих путей.', 350),
            ('Ginseng', 'Женьшень, повышает жизненную силу.', 600),
            ('SeleniumAdvanced', 'Улучшенный селен, поддерживает здоровье.', 450),
        ]
        cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', sample_products)
        conn.commit()
    conn.close()
