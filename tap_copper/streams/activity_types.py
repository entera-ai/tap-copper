import singer

from tap_copper.streams.base import BaseStream

LOGGER = singer.get_logger()


class ActivityTypesStream(BaseStream):
    API_METHOD = "GET"
    TABLE = "activity_types"
    KEY_PROPERTIES = ["id"]

    @property
    def path(self):
        return "/activity_types"

    def get_stream_data(self, response):
        transformed = []
        for records in response.values():
            for record in records:
                ## removes fields with missing/wrong data type
                record = self.transform_record(record)
                transformed.append(record)
        return transformed

    def sync_data(self):
        table = self.TABLE

        LOGGER.info("Syncing data for {}".format(table))
        url = self.get_url()

        response = self.client.make_request(url, self.API_METHOD)
        transformed = self.get_stream_data(response)

        with singer.metrics.record_counter(endpoint=table) as counter:
            singer.write_records(table, transformed)
            counter.increment(len(transformed))

        LOGGER.info("Synced {}".format(table))

        return self.state
