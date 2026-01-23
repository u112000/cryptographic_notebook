#! python3

def create_note():
    from ...core.admin_database import DatabaseMain
    from ...cli.core_functions_display.create_note_display import create_parameters
    create_parameters_data: tuple = create_parameters()
    db = DatabaseMain()
    db.main_inserter(create_parameters_data)

