from . import models
from django.contrib.auth.models import Group
import uuid

class AccountService:
    @staticmethod
    def generate_session_state(client: str) -> str:
        session_id = str(uuid.uuid4())
        models.SessionLog(session_id=session_id, client_id=client).save()
        return session_id