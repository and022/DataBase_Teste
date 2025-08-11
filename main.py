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

# Crud da classe Usúario 
# Adicionando um usuario novo
Change_Put_Usuario = Usuario(nome="Andre Neri Batista",email="andry033@gmail,com",senha="03697//",status="ativo")
session.add(Change_Put_Usuario)
session.commit()

#fazendo a leitura dos dados R =  read
print("id", Change_Put_Usuario.id)
print("nome", Change_Put_Usuario.nome)
print("email", Change_Put_Usuario.email)
print("senha", Change_Put_Usuario.senha)
print("status", Change_Put_Usuario.status)

#Crud da classe Produto
Change_put_produto = Produto(nome= "Guarda- roupa", qtde=150, dono=Change_Put_Usuario.id)
session.add(Change_put_produto)
session.commit

#fazendo a leitura dos dados R =  read
print("nome", Change_put_produto.nome)
print("qtde", Change_put_produto.qtde)
print("dono", Change_put_produto.dono)



#fazendo update "U colocando um novo usuario"

Change_Put_Usuario.nome_produto = "Julio freitas"
session.add(Change_Put_Usuario)
session.commit()

print("novo nome:" ,Change_Put_Usuario.nome_produto)

# D - delete  deletando um Produto ou Usuario (nesse caso estou deletando um produto)

session.delete(Change_put_produto)
session.commit()