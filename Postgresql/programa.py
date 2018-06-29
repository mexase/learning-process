import os
import psycopg2
from datetime import date, datetime


class Database:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=aracnobook user=pgadmin password=123")
        self.cur = self.conn.cursor()

    def consultar_tabela(self):
        nome_name = ((input_correto('Nome', str, mensagem='Digite o valor para consulta: ', obrigatorio=True))+'%')
        self.cur.execute("SELECT id, name FROM books_book WHERE name ILIKE %s order by id", (nome_name ,))
        prt = self.cur.fetchall()
        print(prt)

    def insert(self, nome_tabela, dict_campos):
        campos = ', '.join(dict_campos.keys())
        values = ', '.join(['%s']*len(dict_campos.keys()))
        sql = f'INSERT INTO {nome_tabela}({campos}) VALUES ({values}) RETURNING id'
        self.cur.execute(sql, tuple(dict_campos.values()))
        returnid = self.cur.fetchone()[0]
        self.conn.commit()
        print('Entrada', dict_campos.get('name'), 'salva no ID', returnid, '\n')

    def atualizar_tabela(self):
        dado_antigo = input_correto('Nome antigo', str, mensagem='Digite o'
                                    ' valor antigo: ', obrigatorio=True)
        dado_novo = input_correto('Nome novo', str, mensagem='Digite o'
                                  ' valor novo: ', obrigatorio=True)
        self.cur.execute("UPDATE books_book SET name=%s WHERE name=%s", (dado_novo, dado_antigo))
        self.conn.commit()

    def excluir_linha_da_tabela(self):
        deleta_nome = input_correto('Deleta Valor', str, mensagem='Digite o nome do livro para deleção: ', obrigatorio=True)
        self.cur.execute("DELETE FROM books_book where name = %s", (deleta_nome, ))
        self.conn.commit()


db = Database()


def input_correto(nome_campo, tipo_de_dado, mensagem='',
                  obrigatorio=False, max_length=0, is_store=False):
    if mensagem == '':
        mensagem = f'Entre com o valor para "{nome_campo}": '
    while True:
        try:
            if tipo_de_dado == datetime:
                valor_input = str(input(mensagem))
            if tipo_de_dado == date:
                valor_input = str(input(mensagem))
            else:
                valor_input = tipo_de_dado(input(mensagem))
            if not valor_input and obrigatorio is True:
                print('É necessário passar um valor')
            if tipo_de_dado == str and max_length > 0 and len(
               valor_input) != max_length:
                print(f'Este campo precisa de {max_length} caracteres')
                continue
            if tipo_de_dado == int and is_store is True and valor_input > 7 and obrigatorio is True:
                print(f'Este campo só aceita números entre 1 e 7\n')
                continue
            if tipo_de_dado == datetime:
                valor_input = datetime.strptime(valor_input, PADRAO_DATA)
            if tipo_de_dado == date:
                valor_input = date.stptime(valor_input, PADRAO_DATA)
            if valor_input and obrigatorio is True:
                return valor_input
                break
        except ValueError:
            print('Erro de valor')


def coleta_de_dados_do_livro():
    dicionario = dict(
        name=input_correto('name', str, obrigatorio=True),
        url=input_correto('url', str, obrigatorio=True),
        last_updated='now()',
        image_url=input_correto('image_url', str, obrigatorio=True),
        author=input_correto('author', str, obrigatorio=True),
        publisher=input_correto('publisher', str, obrigatorio=True),
        language=input_correto('idioma', str, obrigatorio=True),
        description=input_correto('Descrição', str, obrigatorio=True),
        currency=input_correto('moeda', str, obrigatorio=True, max_length=3),
        pricing=input_correto('Preço', float, obrigatorio=True),
        rating=input_correto('Rating', float, obrigatorio=True),
        isbn10=input_correto('ISBN10', str, obrigatorio=True),
        isbn13=input_correto('ISBN13', str, obrigatorio=True),
        deduplication_status='0',
        asin='',
        sku='',
        barcode=input_correto('Código de barras', str, obrigatorio=True),
        reviews=input_correto('Reviews', int, obrigatorio=True),
        store_id=input_correto(
                'store_id',
                int,
                mensagem=('Digite o número correspondente à loja: \n1 - '
                          'BookDepository \n'
                          '2 - Casa del libro \n3 - Cia dos livros\n4'
                          ' - Cultura ''\n5 - GoodReads \n6 - Saraiva \n7'
                          ' - Skoob: \n'), obrigatorio=True, is_store=True)
    )
    return dicionario


PADRAO_DATA = '%d/%m/%Y'

if __name__ == '__main__':
    while True:
        while True:
            try:
                escolha = int(input('Digite o número da opção desejada: \n 1 -'
                                    ' Consultar, 2 - Inserir, 3 - Atualizar '
                                    '4 - Excluir: 5 - Sair: '))
                break
            except ValueError:
                print('Valor incorreto')
                os.system('clear')

        if escolha == 1:
            os.system('clear')
            db.consultar_tabela()

        elif escolha == 2:
            os.system('clear')
            db.insert('books_book', coleta_de_dados_do_livro())

        elif escolha == 3:
            os.system('clear')
            db.atualizar_tabela()

        elif escolha == 4:
            os.system('clear')
            db.excluir_linha_da_tabela()

        elif escolha == 5:
            os.system('clear')
            break
        else:
            print('Escolha incorreta')
