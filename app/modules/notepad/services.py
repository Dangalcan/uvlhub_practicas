from app.modules.notepad.repositories import NotepadRepository
from core.services.BaseService import BaseService


class NotepadService(BaseService):
    def __init__(self):
        super().__init__(NotepadRepository())

    def get_all_by_user(self, user_id):
        return self.repository.get_all_by_user(user_id)

    def get_notepad_by_id(self, notepad_id):
        return self.repository.get_notepad_by_id(notepad_id)
