from typing import List, Optional

from fastapi import Request


class CreatePersonForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.name: Optional[str] = None
        self.email: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.name = form.get("full_name")
        self.email = form.get("email")

    async def is_valid(self):
        return True
        # if not self.username or not (self.username.__contains__("@")):
        #     self.errors.append("Email is required")
        # if not self.password or not len(self.password) >= 4:
        #     self.errors.append("A valid password is required")
        # if not self.errors:
        #     return True
        # return False
