from dataclasses import dataclass


@dataclass(frozen=True)
class TurnTicket:
    turnNumber: int


_turnNumber = -1


def next_turn_number():
    global _turnNumber
    while True:
        _turnNumber += 1
        yield _turnNumber


class TicketDispenser:
    def __init__(self, ticket_provider=None):
        self.ticket_provider = ticket_provider or next_turn_number()
    def next_turn_ticket(self):
        next_turn_number = self.ticket_provider.__next__()
        ticket = TurnTicket(next_turn_number)
        return ticket
