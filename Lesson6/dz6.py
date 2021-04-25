if __name__ == '__main__':

    import sqlite3

    conn_db = sqlite3.connect('lesson6_db.sqlite3')
    cur_db = conn_db.cursor()

    # создание вспомогательных таблиц
    cur_db.executescript("""
        CREATE TABLE IF NOT EXISTS categories (
            category_name VARCHAR(100) NOT NULL,
            category_description TEXT NOT NULL,
            PRIMARY KEY (category_name)
        );
        CREATE TABLE IF NOT EXISTS units (
            unit VARCHAR(2) NOT NULL,
            PRIMARY KEY (unit)
        );
        CREATE TABLE IF NOT EXISTS positions (
            position VARCHAR(100) NOT NULL,
            PRIMARY KEY (position)
        );
    """)

    # Создание основных таблиц
    cur_db.executescript("""
        CREATE TABLE IF NOT EXISTS goods (
            good_id BIGINT UNIQUE NOT NULL,
            good_name VARCHAR(255) NOT NULL,
            good_unit VARCHAR(2),
            good_cat VARCHAR(100),
            PRIMARY KEY (good_id),
            FOREIGN KEY (good_unit) REFERENCES units(unit) ON UPDATE CASCADE ON DELETE SET NULL,
            FOREIGN KEY (good_cat) REFERENCES categories(category_name) ON UPDATE CASCADE ON DELETE SET NULL
        );
        CREATE TABLE IF NOT EXISTS employees (
            employee_id BIGINT UNIQUE NOT NULL,
            employee_fio VARCHAR(255) NOT NULL,
            employee_position VARCHAR(100),
            PRIMARY KEY (employee_id),
            FOREIGN KEY (employee_position) REFERENCES positions(position) ON UPDATE CASCADE ON DELETE SET NULL
        );
        CREATE TABLE IF NOT EXISTS vendors (
            vendor_id BIGINT UNIQUE NOT NULL,
            vendor_name VARCHAR(255) NOT NULL,
            vendor_ownerchipform VARCHAR(50),
            vendor_address TEXT,
            vendor_phone BIGINT NOT NULL,
            vendor_email VARCHAR(100),
            PRIMARY KEY (vendor_id)
        );
    """)

    conn_db.commit()
    conn_db.close()
