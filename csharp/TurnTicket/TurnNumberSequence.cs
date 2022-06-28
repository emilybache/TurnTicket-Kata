namespace Turns;

public class TurnNumberSequence
{
    private static TurnNumberSequence _instance;
    private int _turnNumber = 0;

    public int GetNextTurnNumber()
    {
        return _turnNumber++;
    }
    
    public static TurnNumberSequence GetInstance()
    {
        if (_instance == null)
        {
            _instance = new TurnNumberSequence();
        }
        return _instance;
    }
}