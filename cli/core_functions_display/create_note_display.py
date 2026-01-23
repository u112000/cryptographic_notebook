#! python3

def create_parameters():
    from uuid import uuid4
    from datetime import datetime
    note_id = str(uuid4())
    note_title = input('Note Title > ')
    note_content = input('Note Contents > ')
    note_attachment = path_isexist(input('Path to zipped attachment or enter nothing to continue> '))
    create_date = datetime.now().strftime('%Y-%m-%d')
    last_update_date = create_date
    return (
        note_id,
        note_title,
        note_content,
        note_attachment,
        create_date,
        last_update_date)

def path_isexist(n):
    n = n.strip()
    import os
    return f"{n if os.path.isfile(n) else 'no attachments.'}"

        
