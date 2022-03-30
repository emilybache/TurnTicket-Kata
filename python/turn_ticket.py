from dataclasses import dataclass


@dataclass(frozen=True)
class TurnTicket:
    turnNumber: int


class TurnNumberSequence:
    _turnNumber = -1

    @staticmethod
    def next_turn_number():
        TurnNumberSequence._turnNumber += 1
        return TurnNumberSequence._turnNumber


class TicketDispenser:
    def next_turn_ticket(self):
        next_turn_number = TurnNumberSequence.next_turn_number()
        ticket = TurnTicket(next_turn_number)
        return ticket
