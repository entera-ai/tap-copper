import singer

from tap_copper.streams.base import BaseStream

LOGGER = singer.get_logger()  # noqa


class PeopleStream(BaseStream):
    API_METHOD = "POST"
    TABLE = "people"
    KEY_PROPERTIES = ["id"]

    @property
    def path(self):
        return "/people/search"
