from enum import Enum


class TournamentStatus(Enum):
    REGISTRATIONS_OPEN = "Registrations open"
    REGISTRATIONS_CLOSED = "Registrations closed"
    COMPLETED = "Completed"
    IN_PROGRESS = "In progress"
