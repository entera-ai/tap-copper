import singer

from tap_copper.streams.base import BaseStream

LOGGER = singer.get_logger()


class ActivitiesStream(BaseStream):
    API_METHOD = "POST"
    TABLE = "activities"
    KEY_PROPERTIES = ["id"]

    @property
    def path(self):
        return "/activities/search"

    def fetch_activity_types(self):
        url = "https://api.prosperworks.com/developer_api/v1/activity_types"
        method = "GET"
        response = self.client.make_request(url, method)

        activity_types = []
        for _type in response:
            for record in response[_type]:
                activity_types.append(record)

        return activity_types

    def custom_body(self):
        return {
            "full_result": True, 
            "minimum_activity_date": self.get_start_date(),
            "activity_types": self.fetch_activity_types()
        }
