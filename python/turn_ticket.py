from dataclasses import dataclass


@dataclass(frozen=True)
class TurnTicket:
    # which turn number you have in the queue
    turnNumber: int
    # which dispenser gave the ticket
    dispenser_name: str


_turnNumber = 0


def next_turn_number():
    global _turnNumber
    while True:
        yield _turnNumber
        _turnNumber += 1


_ticket_provider = next_turn_number()


class TicketDispenser:
    def __init__(self, name):
        self.name = name

    def next_turn_ticket(self):
        next_turn_number = _ticket_provider.__next__()
        ticket = TurnTicket(next_turn_number, self.name)
        return ticket
