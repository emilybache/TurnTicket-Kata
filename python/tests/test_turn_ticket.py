import pytest

from turn_ticket import TicketDispenser, TurnTicket

def test_dispenser():
    dispenser = TicketDispenser("front")
    ticket = dispenser.next_turn_ticket()
    assert ticket == TurnTicket(0, "front")


def test_two_dispensers():
    dispenser1 = TicketDispenser("front")
    dispenser2 = TicketDispenser("side")
    ticket1 = dispenser1.next_turn_ticket()
    ticket2 = dispenser2.next_turn_ticket()
    ticket3 = dispenser1.next_turn_ticket()

    # TODO: make this work
    assert ticket1 == TurnTicket(0, "front")
    assert ticket2 == TurnTicket(1, "side")
    assert ticket3 == TurnTicket(2, "front")