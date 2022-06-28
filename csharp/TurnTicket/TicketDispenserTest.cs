using System;
using System.Collections.Generic;
using System.Text;
using Xunit;

namespace Turns
{
    public class TicketDispenserTest
    {
        [Fact]
        public void GetTurnTicket()
        {
            var dispenser = new TicketDispenser(new TurnNumberSequence());
            var ticket = dispenser.GetTurnTicket();
            Assert.Equal(0, ticket.TurnNumber);
        }        
        
        [Fact]
        public void GetTurnTicketWithSingletonDispenser()
        {
            var dispenser = new TicketDispenser();
            var ticket = dispenser.GetTurnTicket();
            // weak assertion - just check it's positive
            Assert.True(ticket.TurnNumber >= 0);
        }

        [Fact]
        public void WithTwoDispensers()
        {
            var sequence = new TurnNumberSequence();
            var dispenser1 = new TicketDispenser(sequence);
            var dispenser2 = new TicketDispenser(sequence);
            var ticket1 = dispenser1.GetTurnTicket();
            var ticket2 = dispenser2.GetTurnTicket();
            var ticket3 = dispenser1.GetTurnTicket();
            Assert.Equal(0, ticket1.TurnNumber);
            Assert.Equal(1, ticket2.TurnNumber);
            Assert.Equal(2, ticket3.TurnNumber);
        }
    }
}
