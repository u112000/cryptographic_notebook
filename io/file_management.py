#! python3

from ..config import config

class FileManagement:
    def __init__(self):
        try:
            self.config = json.load(open(config, 'rt', encoding='utf-8'))
            self.notebook_db_path = self.config['notebook_db']
            self.keys_db_path = self.config['keys_db']
        except (FileNotFoundError, KeyError) as err:
            sys.exit(f'{err}')
        
    def return_notebook_dbpath(self):
        return self.notebook_db_path

    def return_keys_dbpath(self):
        return self.keys_db_path
