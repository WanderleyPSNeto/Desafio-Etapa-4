# Importa as bibliotecas necessárias
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

# Cria uma instância do Flask
app = Flask(__name__)

# Configura o banco de dados
engine = create_engine('sqlite:///characters.db')

# Define a base de dados
Base = declarative_base()

# Cria a tabela de personagens
class Personagem(Base):
    __tablename__ = 'personagens'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(Text, nullable=False)
    link_imagem = Column(String(255), nullable=False)
    programa = Column(String(255), nullable=False)
    animador = Column(String(255), nullable=False)

# Cria os personagens iniciais
Personagem.metadata.create_all(engine)

personagem1 = Personagem(
    nome='Mickey Mouse',
    descricao='Um rato antropomórfico que é o personagem principal da franquia Mickey Mouse, que é uma das propriedades de mídia mais valiosas do mundo.',
    link_imagem='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Mickey_Mouse_at_Disneyland.jpg/1200px-Mickey_Mouse_at_Disneyland.jpg',
    programa='Disneylândia',
    animador='Walt Disney'
)

personagem2 = Personagem(
    nome='Donald Duck',
    descricao='Um pato antropomórfico que é o deuteragonista da franquia Mickey Mouse.',
    link_imagem='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Donald_Duck_-_Mickey_Mouse_Club_House.png/1200px-Donald_Duck_-_Mickey_Mouse_Club_House.png',
    programa='Mickey Mouse Club House',
    animador='Walt Disney'
)

personagem3 = Personagem(
    nome='Minnie Mouse',
    descricao='Uma ratinha antropomórfica que é a namorada de Mickey Mouse.',
    link_imagem='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Minnie_Mouse_-_2013.jpg/1200px-Minnie_Mouse_-_2013.jpg',
    programa='Disneylândia',
    animador='Walt Disney'
)

engine.execute(Personagem.__table__.insert(), [personagem1.__dict__, personagem2.__dict__, personagem3.__dict__])

# Função para criar um novo personagem
def criar_personagem():

    # Obtém as informações do personagem do request
    nome = request.json['nome']
    descricao = request.json['descricao']
    link_imagem = request.json['link_imagem']
    programa = request.json['programa']
    animador = request.json['animador']

    # Cria um novo personagem com as informações obtidas
    personagem = Personagem(
        nome=nome,
        descricao=descricao,
        link_imagem=link_imagem,
        programa=programa,
        animador=animador
    )

    # Insere o novo personagem no banco de dados
    engine.execute(Personagem.__table__.insert(), personagem.__dict__)

    # Retorna uma resposta com o status 201 (Created)
    return jsonify({'status': 201})

# Função para recuperar todos os personagens
def recuperar_personagens():

    # Obtém todos os personagens do banco de dados
    personagens = engine.execute(Personagem.__table__.select())

    # Retorna uma lista de personagens
    return jsonify({'personagens': [personagem.__dict__ for personagem in personagens]})

# Fun
