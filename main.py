from sqlalchemy import create_engine, Column, String, Integer, Boolean 
from sqlalchemy.orm import sessionmaker , declarative_base


database = create_engine("sqlite:///mydatabase.db")

Session = sessionmaker(bind=database)
session = Session()

#criando as tabelas  nesse caso vou criar uma simples cadastro de usuarios e produtos
#Para isso vou usar Classes init e o Self (padrao do python)

# Criando a classe usuario 

Base_dados = declarative_base()

    # Criando a classe usuario 
class  Usuario (Base_dados):

    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key = True)
    nome_produto = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("status", Boolean)

    def __init__ (self, nome, email, senha, status=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.status = status


# Criando a classe produtos
class Produto(Base_dados):
    __tablename__ = "produto"

    id = Column("id", Integer, primary_key = True)
    nome_do_produto = Column("nome",String)
    qtde = Column("qtde", Integer)
    # IMPORTANDO O foreingKey
    from sqlalchemy import ForeignKey
    dono = Column("dono", ForeignKey("usuarios.id"))

    def __init__ (self, nome, qtde, dono):
        self.nome = nome
        self.qtde = qtde
        self.dono = dono
    

Base_dados.metadata.create_all(bind=database)

#criando as tabelas  nesse caso vou criar uma simples cadastro de usuarios e produtos
#Para isso vou usar Classes init e o Self (padrao do python)

# Criando a classe usuario 

     # 17:48



