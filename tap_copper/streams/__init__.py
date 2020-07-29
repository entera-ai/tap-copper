from tap_copper.streams.activities import ActivitiesStream
from tap_copper.streams.companies import CompaniesStream
from tap_copper.streams.contact_types import ContactTypesStream
from tap_copper.streams.custom_fields import CustomFieldsStream
from tap_copper.streams.customer_sources import CustomerSourcesStream
from tap_copper.streams.leads import LeadsStream
from tap_copper.streams.opportunities import OpportunitiesStream
from tap_copper.streams.people import PeopleStream
from tap_copper.streams.projects import ProjectsStream
from tap_copper.streams.tasks import TasksStream
from tap_copper.streams.users import UsersStream

AVAILABLE_STREAMS = [
    UsersStream,
    PeopleStream,
    LeadsStream,
    CompaniesStream,
    OpportunitiesStream,
    ProjectsStream,
    TasksStream,
    ActivitiesStream,
    CustomFieldsStream,
    CustomerSourcesStream,
    ContactTypesStream
]

__all__ = [
    "UsersStream",
    "PeopleStream",
    "LeadsStream",
    "CompaniesStream",
    "OpportunitiesStream",
    "ProjectsStream",
    "TasksStream",
    "ActivitiesStream",
    "CustomFieldsStream",
    "CustomerSourcesStream",
    "ContactTypesStream"
]
