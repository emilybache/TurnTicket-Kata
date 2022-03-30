import pytest

from turn_ticket import TicketDispenser, TurnTicket


class StubSequence:
    def __init__(self, sequence):
        self.sequence = sequence
        self.current = -1

    def next_turn_number(self):
        self.current += 1
        return self.sequence[self.current]

def stub_dispenser(sequence):
    current = 0
    yield sequence[current]
    current += 1

def test_get_turn_ticket():
    dispenser = TicketDispenser(ticket_provider=stub_dispenser([1,2]))
    ticket = dispenser.next_turn_ticket()
    assert ticket.turnNumber == 1


def test_get_turn_ticket_with_two_dispensers():
    provider = iter([1,2])
    dispenser1 = TicketDispenser(ticket_provider=provider)
    dispenser2 = TicketDispenser(ticket_provider=provider)
    ticket1 = dispenser1.next_turn_ticket()
    ticket2 = dispenser2.next_turn_ticket()
    assert ticket1.turnNumber == 1
    assert ticket2.turnNumber == 2


def test_dispenser():
    dispenser = TicketDispenser()
    ticket = dispenser.next_turn_ticket()
    assert ticket == TurnTicket(0)


def test_two_dispensers():
    dispenser1 = TicketDispenser()
    dispenser2 = TicketDispenser()
    ticket1 = dispenser1.next_turn_ticket()
    ticket2 = dispenser2.next_turn_ticket()
    ticket3 = dispenser1.next_turn_ticket()

    # TODO: make this work
    #assert ticket1 == TurnTicket(0)
    #assert ticket2 == TurnTicket(1)
    #assert ticket3 == TurnTicket(2)