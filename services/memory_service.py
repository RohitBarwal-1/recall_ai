from collections import deque
from uuid import uuid4
from typing import Dict, List


class ShortTermMemory:
    def __init__(self, max_message: int = 10):
        self.max_messages = max_message
        self.sessions: Dict[str, deque] = {}


    def create_session(self) -> str:
        session_id = str(uuid4())

        self.sessions[session_id] = deque(
            maxlen=self.max_messages
        )

        return session_id
    

    def add_message(self, session_id: str, role: str, content: str ) -> None:
        if session_id not in self.sessions:
            raise ValueError("Invalid session_id")

        self.sessions[session_id].append({
            "role": role,
            "content": content
        })


    def get_history(self, session_id: str) -> List[dict]:
        if session_id not in self.sessions:
            raise ValueError("Invalid session_id")

        return list(self.sessions[session_id])


    def clear_session(self, session_id: str) -> None:
        if session_id in self.sessions:
            self.sessions[session_id].clear()
