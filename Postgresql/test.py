import psycopg2

def consulta():
    conn = psycopg2.connect("dbname=aracnobook user=pgadmin password=123")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books_book limit 20;")
    prt = cur.fetchall()
    return prt



def inserir_tabela_em_books_book():
    conn = psycopg2.connect("dbname=aracnobook user=pgadmin password=123")
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO books_book (url, name, author, rating, isbn10, isbn13, asin, barcode, sku, publisher, pricing, currency,
     description, last_updated, store_id, language, image_url, reviews, deduplication_status)
    VALUES ('http:\\teste', 'Se Houver amanhã', 'Sheldon', '0', '00', '00', 'Teste', '20189182', '112100', 'I dont know,', 
    '95.00', 'USD', 'A test of python', '2018-05-29T14:46:09.837Z', '6', 'Enslish', 'http:\\test', '0', '2')
    """)
    conn.commit()

def atualizar_tabela_em_book_books():
    conn =psycopg2.connect("dbname=aracnobook user=pgadmin password=123")
    curr = conn.cursor()
    curr.execute("""
    UPDATE books_book set name = 'Spider-Man' where name = 'SPIDER-MAN'
        """)
    conn.commit()



#
def excluir_linha_da_tabela():
    conn = psycopg2.connect("dbname=aracnobook user=pgadmin password=123")
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM books_book where id = 26323
        """)
    conn.commit()

#inserir_tabela_em_books_book()
#atualizar_tabela_em_book_books()
print('Excluindo linha...')
excluir_linha_da_tabela()
