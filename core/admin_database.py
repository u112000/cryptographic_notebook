"""
    note_id = str(uuid4())
    note_title = input('Note Title > ')
    note_content = input('Note Contents > ')
    note_attachment = path_isexist(input('Path to zipped attachment or enter nothing to continue> '))
    create_date = datetime.now().strftime('%Y-%m-%d')
    last_update_date = create_date
    """
from ..io.file_management import FileManagement
from .cryptographic_processes import CryptographyProcesses
from sqlalchemy import create_engine, MetaData, Column, Table, insert, String, LargeBinary

class DatabaseMain(FileManagement, CryptographyProcesses):
    def __init__(self):
        super().__init__()
        self.notebook_db_engine = create_engine("sqlite:///"+self.return_notebook_dbpath)
        self.keys_db_engine = create_engine("sqlite:///"+self.return_keys_dbpath)
        self.notebook_metadata = MetaData()
        self.keys_metadata = MetaData()

    def create_table(self, notebook_db_table=False, keys_db_table=False):
        if notebook_db_table:
            table_obj = Table(
                "cryptographic_notebook_db",
                self.notebook_metadata,
                Column('id', String, nullable=False),
                Column('title', String, nullable=False),
                Column('contents', LargeBinary, nullable=False),
                Column('attachment_binary', LargeBinary, nullable=False),
                Column('attachment_filename', String, nullable=False),
                Column('create_date', String, nullable=False),
                Column('last_update_date', String, nullable=False))
            self.notebook_metadata.create_all(bind=self.notebook_db_engine)
            return table_obj
        elif keys_db_table:
            table_obj = Table(
                "cryptographic_notebook_keys_db",
                self.keys_metadata,
                Column('id', String, nullable=False),
                Column('key', LargeBinary, nullable=False),
                Column('nonce', LargeBinary, nullable=False))
            self.keys_metadata.create_all(bind=self.keys_db_engine)
            return table_obj
    
    def main_inserter(self, data: tuple):
        import os
        data = list(data)
        
        note_id = data[0]
        note_title = data[1]
        note_content = self.string_encryption(data[2]) #tuple (data, key, nonce)
        note_attachment_filename = os.path.basename(data[3]) if data[3] != 'empty' else 'empty'
        note_attachment = self.file_encryption(data[3], note_content[1], note_content[2]) if data[3] != 'empty' else 'empty'
        create_date = data[4]
        last_update_date = data[5]

        self.insert_into_keys_db({
            'id': note_id,
            'key': note_content[1],
            'nonce': note_content[2]})
        
        self.insert_into_notebook_db({
            'id':note_id,
            'title':note_title,
            'contents':note_content[0],
            'attachment_binary': note_attachment,
            'attachment_filename': note_attachment_filename,
            'create_date':create_date,
            'last_update_date':last_update_date})

    def insert_into_keys_db(self, data:dict):
        table_obj = self.create_table(keys_db_table=True)
        insert_statement = insert(data)
        with self.keys_db_engine.connect() as conn:
            conn.execute(table_obj, data)
            conn.commit()
        
    def insert_into_notebook_db(self, data: dict):
        table_obj = self.create_table(notebook_db_table=True)
        insert_statement = insert(data)
        with self.notebook_db_engine.connect() as conn:
            conn.execute(table_obj, data)
            conn.commit()
        






    
