import sqlite3

# Conectando ao banco de dados SQLite (ou criando, caso não exista)
conn = sqlite3.connect('PIXFARM.db')

# Criando um cursor para executar comandos SQL
cursor = conn.cursor()

# Criando a tabela 'producao'
# A estrutura será parecida com a que você usaria no SQL Server.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS producao (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_planta TEXT NOT NULL,
        imagem TEXT NOT NULL
    )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS detalhes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_inicio DATE
        )
    ''')

# Inserindo alguns dados de exemplo (caso a tabela esteja vazia)
cursor.execute('SELECT COUNT(*) FROM producao')
if cursor.fetchone()[0] == 0:
    cursor.executemany('''
        INSERT INTO producao (nome_planta, imagem) VALUES (?, ?)
    ''', [
        ('Alface', 'https://raw.githubusercontent.com/BRUNUN0/PIM-3-SEMESTRE/refs/heads/4-SEMESTRE/Mobile/app/assets/timao.png'),
        ('Tomate', 'https://raw.githubusercontent.com/BRUNUN0/PIM-3-SEMESTRE/refs/heads/4-SEMESTRE/Mobile/app/assets/timao.png'),
        ('Cenoura', 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/4/4c/Carrot_JE2_BE1.png/revision/latest?cb=20191229163404'),
        ('Cebolinha', 'https://github.com/BRUNUN0/PIM-3-SEMESTRE/blob/4-SEMESTRE/Mobile/app/assets/cebolinha.png?raw=true')
    ])

# Salvando as mudanças e fechando a conexão
conn.commit()
conn.close()
