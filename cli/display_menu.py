#! python3

from rich import print

class DisplayMenu:
    def __init__(self):
        self.user_input = ''
        self.menu_cols = (
            'Core Commands',
            'Description')
        self.menu_row = {'list': 'List all notes (ID & title)',
                          'create': 'Create a new note',
                          'delete': 'Delete a note by ID',
                          'view_note': 'Decrypt note, view its contents and meta',
                          'sort_by_category': 'Sort through all notes by categorization',
                          'help': 'Show this help',
                          'mood_graph': 'Display mood analysis chart',
                          'exit': 'Quit program'}
        self.valid_input = self.menu_row.keys()

    def display_table(self):
        from rich.table import Table
        t = Table()
        for each_col in self.menu_cols:
            t.add_column(each_col)
        for key, value in self.menu_row.items():
            t.add_row(key, value)
        return t

    def get_user_input(self):
        print(self.display_table())
        user_respond = input('Menu Command: ').strip().lower()
        while user_respond not in self.valid_input:
            user_respond = input(r'"Previous input was invalid" Menu Command: ').strip().lower()
        return user_respond
        
