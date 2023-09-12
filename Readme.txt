1. Clone o repositório do GitHub: git clone https://github.com/[seu-usuário-github]/characters-api

2. Abra o projeto no VS Code: code characters-api

3. Instale as dependências: pip install -r requirements.txt

4. Crie um banco de dados SQLite: sqlite3 characters.db

5. Execute os scripts de inicialização: ./init.sh

6. Inicie o servidor Flask: python app.py

O servidor Flask estará disponível em http://localhost:5000.

Para usar a API no VS Code pode usar uma extensão de cliente HTTP para testar a API no VS Code. Uma extensão popular é o Postman: https://www.postman.com/.

Como usar o Postman para testar a API:

GET http://localhost:5000/characters
POST http://localhost:5000/characters/create
Body:
{
"nome": "Mickey Mouse",
"descricao": "Um rato antropomórfico que é o personagem principal da franquia Mickey Mouse, que é uma das propriedades de mídia mais valiosas do mundo.",
"link_imagem": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Mickey_Mouse_at_Disneyland.jpg/1200px-Mickey_Mouse_at_Disneyland.jpg",
"programa": "Disneylândia",
"animador": "Walt Disney"
}

GET http://localhost:5000/characters/1
PUT http://localhost:5000/characters/1
Body:
{
"nome": "Mickey Mouse",
"descricao": "Um rato antropomórfico que é o personagem principal da franquia Mickey Mouse, que é uma das propriedades de mídia mais valiosas do mundo.",
"link_imagem": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Mickey_Mouse_at_Disneyland.jpg/1200px-Mickey_Mouse_at_Disneyland.jpg",
"programa": "Disneylândia",
"animador": "Walt Disney"
}

DELETE http://localhost:5000/characters/1