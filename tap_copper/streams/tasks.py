import singer

from tap_copper.streams.base import BaseStream

LOGGER = singer.get_logger()


class TasksStream(BaseStream):
    API_METHOD = "POST"
    TABLE = "tasks"
    KEY_PROPERTIES = ["id"]

    @property
    def path(self):
        return "/tasks/search"

    def custom_body(self):
        return {"minimum_modified_date": self.get_start_date()}
