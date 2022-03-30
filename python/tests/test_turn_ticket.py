import pytest

from turn_ticket import TicketDispenser


def test_get_turn_ticket():
    dispenser = TicketDispenser()
    ticket = dispenser.next_turn_ticket()
    # TODO: Assert something
