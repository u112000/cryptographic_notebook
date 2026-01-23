#! python3


                          'create': 'Create a new note',
                          'list': 'List all notes (ID & title)',
                          'delete': 'Delete a note by ID',
                          'view_note': 'Decrypt note, view its contents and meta',
                          'sort_by_category': 'Sort through all notes by categorization',
                          'help': 'Show this help',
                          'mood_graph': 'Display mood analysis chart',
                          'exit': 'Quit program'}

def core_commands(n: str):
    if n == 'create':
        from .core_functions.create_note import create_note
        create_note()
    elif n == 'list':
        ...

