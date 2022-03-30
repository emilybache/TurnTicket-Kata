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


_ticket_provider = next_turn_number()


class TicketDispenser:
    def next_turn_ticket(self):
        next_turn_number = _ticket_provider.__next__()
        ticket = TurnTicket(next_turn_number)
        return ticket
