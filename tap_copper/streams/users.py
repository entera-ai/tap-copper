import singer

from tap_copper.streams.base import BaseStream

LOGGER = singer.get_logger()  # noqa


class UsersStream(BaseStream):
    API_METHOD = "POST"
    TABLE = "users"
    KEY_PROPERTIES = ["id"]

    @property
    def path(self):
        return "/users/search"

    def get_body(self, page_number=1, page_size=200):
        body = {"page_number": page_number, "page_size": page_size}

        return body
