using WMPLib;

class Program
{
    static readonly object lockObj = new object();

    static void AnimateText(string text, double delay)
    {
        lock (lockObj)
        {
            foreach (char c in text)
            {
                Console.Write(c);
                Thread.Sleep((int)(delay * 1000));
            }
            Console.WriteLine();
        }
    }

    static async Task SingLyric(string lyric, double delay, double speed)
    {
        await Task.Delay((int)(delay * 1000));
        AnimateText(lyric, speed);
    }
    public static async Task Title()
    {
        Console.Write("\u001b[38;2;194;120;115m");
        var title = new List<Tuple<string, double>>
        {
            new Tuple<string, double>("I Like You The Most", 0.06),
            new Tuple<string, double>("By Shad", 0.08),            
        };

        var textDelay = new List<double> { 1, 2 };
        var task = new List<Task>();
        for (int j = 0; j < title.Count; j++)
        {
            var lyric = title[j].Item1;
            var speed = title[j].Item2;
            var delay = textDelay[j];
            task.Add(SingLyric(lyric, delay, speed));
        }        
        await First();        
        await Task.WhenAll(task);        
    }
    public static async Task First()
    {        
        await Task.Delay(3500);
        Console.WriteLine();
        Console.Write("\u001b[0m");
        var lyrics = new List<Tuple<string, double>>
        {
            new Tuple<string, double>("Cause you're the one that I like", 0.06),
            new Tuple<string, double>("I can't deny", 0.08),
            new Tuple<string, double>("Every night you're on my mind", 0.07),
            new Tuple<string, double>("So if I call you tonight", 0.08),
            new Tuple<string, double>("Will you pick up and give me your time?", 0.08),
            new Tuple<string, double>("Miss you every night", 0.08),
            new Tuple<string, double>("Miss you all the time", 0.07),
            new Tuple<string, double>("No, I don't even know", 0.07),
            new Tuple<string, double>("Where to start", 0.05)
        };        
        var delays = new List<double> { 0.3, 3, 4.5, 6.0, 8.5, 13, 14.5, 17, 17.6 };

        var tasks = new List<Task>();
        for (int j = 0; j < lyrics.Count; j++)
        {
            var lyric = lyrics[j].Item1;
            var speed = lyrics[j].Item2;
            var delay = delays[j];
            tasks.Add(SingLyric(lyric, delay, speed));
        }      

        await Task.WhenAll(tasks);
        await Second();
    }
    public static async Task Second()
    {
        var lyrics2 = new List<Tuple<string, double>>
        {
            new Tuple<string, double>("Cause you're the one that I like", 0.06),
            new Tuple<string, double>("I can't deny", 0.08),
            new Tuple<string, double>("Everything I feel inside", 0.08),
            new Tuple<string, double>("Will you tell me I'm the one", 0.08),
            new Tuple<string, double>("The one inside of your heart??", 0.08),
            new Tuple<string, double>("Used to brush aside", 0.08),
            new Tuple<string, double>("Now I can't deny", 0.07),
            new Tuple<string, double>("That, baby, you're my special one", 0.07),
            new Tuple<string, double>("'Cause you're the one that I like", 0.07)
        };

        var delays2 = new List<double> { 0.5, 2.8, 4.5, 6.0, 8.5, 13, 14.5, 17, 19 };

        Console.WriteLine("\n");
        var tasks2 = new List<Task>();
        for (int j = 0; j < lyrics2.Count; j++)
        {
            var lyric = lyrics2[j].Item1;
            var speed = lyrics2[j].Item2;
            var delay = delays2[j];
            tasks2.Add(SingLyric(lyric, delay, speed));
        }

        await Task.WhenAll(tasks2);
        Thread.Sleep(1500);
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.WriteLine(@"
Tiktok: kiryo_1364
Github: kiryo36x");
        
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine("\nHappy Valentines Day!");
        Console.ResetColor();        
    }

    static async Task Main(string[] args)
    {                        
        WindowsMediaPlayer player = new WindowsMediaPlayer();
        player.URL = @"C:\Users\blood\source\repos\Love you the most\Love you the most\I Like You The Most.mp3"; //change the path by copying the full path of the mp3 from your solution explorer
        player.controls.play();        
        await Title();
        Console.ReadLine();
    }
}