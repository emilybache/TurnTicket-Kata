import pytest

from turn_ticket import TicketDispenser, TurnTicket

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
    assert ticket1 == TurnTicket(0)
    assert ticket2 == TurnTicket(1)
    assert ticket3 == TurnTicket(2)