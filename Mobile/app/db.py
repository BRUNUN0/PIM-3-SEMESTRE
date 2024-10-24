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

# Inserindo alguns dados de exemplo (caso a tabela esteja vazia)
cursor.execute('SELECT COUNT(*) FROM producao')
if cursor.fetchone()[0] == 0:
    cursor.executemany('''
        INSERT INTO producao (nome_planta, imagem) VALUES (?, ?)
    ''', [
        ('Alface', 'app/assets/timao.png'),
        ('Tomate', 'app/assets/timao.png'),
        ('Cenoura', 'app/assets/timao.png'),
        ('Cebolinha', 'app/assets/cebolinha.png')
    ])

# Salvando as mudanças e fechando a conexão
conn.commit()
conn.close()
