#! python3

from ..services.redirect_manager import core_commands
from .display_menu import DisplayMenu

class Main(DisplayMenu):
    def __init__(self):
        super().__init__()

    def redirects(self):
        input_data = self.get_user_input()
        core_commands(input_data)
        

    
    
