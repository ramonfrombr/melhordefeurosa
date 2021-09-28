if [ ! -d "venv" ]; then
    echo --------------------
    echo Criando ambiente virtual (virtualenv)
    echo --------------------
    virtualenv venv
fi
source venv/bin/activate

pip install -r requirements.txt

export FLASK_APP=main.py
if [ ! -d "migrations" ]; then
    echo --------------------
    echo Iniciando a pasta de migrações
    echo --------------------
    export FLASK_APP=main.py; flask db init
fi
echo --------------------
echo Gerando código de migração DDL
echo --------------------
flask db migrate
echo --------------------
echo Executando o código DDL e migrando
echo --------------------
echo --------------------
echo Este é o código DDL que será executado
echo --------------------
flask db upgrade
echo --------------------
echo Generating test data
echo --------------------
python test_data.py