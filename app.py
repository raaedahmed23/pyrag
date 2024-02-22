import os
from pyrag import PyRAG
from dotenv import load_dotenv


load_dotenv()

connection_url = os.environ.get('DB_CONNECTION_URL') or ''

pyrag = PyRAG(connection_url, )

# pyrag.db.connection
# pyrag.db.cursor
# pyrag.db.create_table('table_name', [('column_name', 'type')])
# pyrag.db.drop_table('table_name')
# pyrag.db.insert_values('table', [{'column': 'value'}])
# pyrag.semantic_search('table_name', 'prompt')
# pyrag.create_embeddings('Some text here')

chat = pyrag.create_chat(
    knowledge_sources=[['bc_canada_cities_csv']],
    system_role='You are a helpful assistant',
    store_history=True,
)
