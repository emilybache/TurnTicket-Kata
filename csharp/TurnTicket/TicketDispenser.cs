namespace Turns;

public class TicketDispenser
{
    private TurnNumberSequence numbers;

    public TicketDispenser() : this (TurnNumberSequence.GetInstance())
    {
    }

    public TicketDispenser(TurnNumberSequence numberSequence)
    {
        numbers = numberSequence;
    }

    public TurnTicket GetTurnTicket()
    {
        int newTurnNumber = numbers.GetNextTurnNumber();
        TurnTicket newTurnTicket = new TurnTicket(newTurnNumber);

        return newTurnTicket;
    }
}