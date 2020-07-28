import singer

from tap_copper.streams.base import BaseStream

LOGGER = singer.get_logger()  # noqa


class LeadsStream(BaseStream):
    API_METHOD = "POST"
    TABLE = "leads"
    KEY_PROPERTIES = ["id"]

    @property
    def path(self):
        return "/leads/search"

    def custom_body(self):
        return {"minimum_modified_date": self.get_start_date()}
