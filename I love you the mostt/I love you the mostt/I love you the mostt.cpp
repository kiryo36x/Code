#include <iostream>   // allows us to use cout, cin (console input/output)
#include <thread>     // allows us to create threads (run things at the same time)
#include <vector>     // dynamic array (like list)
#include <chrono>     // time functions (seconds, milliseconds)
#include <mutex>      // used to protect shared resources in multithreading
#include <windows.h>  // gives access to Windows functions (for playing music)

#pragma comment(lib, "winmm.lib") // links Windows Multimedia library (needed for music)

using namespace std;

// global mutex object
// used so multiple threads don't print text at the same time
mutex lockObj;

// This function prints text letter by letter (typing effect)
void AnimateText(string text, double delay)
{
    // lock_guard automatically locks the mutex
    // this prevents multiple threads from printing together
    lock_guard<mutex> guard(lockObj);

    // loop through each character in the string
    for (char c : text)
    {
        cout << c << flush; // print character immediately
        // pause before printing the next character
        this_thread::sleep_for(chrono::milliseconds((int)(delay * 1000)));
    }

    cout << endl; // move to next line after finishing the text
}

// This function waits first, then prints the lyric
// delay = when lyric appears
// speed = typing speed
void SingLyric(string lyric, double delay, double speed)
{
    // wait before showing the lyric
    this_thread::sleep_for(chrono::milliseconds((int)(delay * 1000)));

    // print the lyric with animation
    AnimateText(lyric, speed);
}

//This function plays the MP3 music using Windows API
void PlayMusic()
{
    // location of the MP3 file in your PC
    wstring path = L"C:\\Users\\blood\\Downloads\\I Like You The Most.mp3";

    // command to open the mp3 file
    wstring cmdOpen = L"open \"" + path + L"\" type mpegvideo alias mp3";

    // send command to Windows Media Control Interface (MCI)
    mciSendString(cmdOpen.c_str(), NULL, 0, NULL);

    // command to start playing
    mciSendString(L"play mp3", NULL, 0, NULL);
}

//SECOND PART OF THE SONG
void Second()
{
    // each pair = lyric + typing speed
    vector<pair<string, double>> lyrics = {
        {"Cause you're the one that I like", 0.06},
        {"I can't deny", 0.08},
        {"Everything I feel inside", 0.08},
        {"Will you tell me I'm the one", 0.08},
        {"The one inside of your heart??", 0.08},
        {"Used to brush aside", 0.08},
        {"Now I can't deny", 0.07},
        {"That, baby, you're my special one", 0.07},
        {"'Cause you're the one that I like", 0.07}
    };

    // when each lyric should appear (seconds)
    vector<double> delays = { 0.5,2.8,4.5,6.0,8.5,13,14.5,17,19 };

    vector<thread> threads;

    // create threads so lyrics appear based on time
    for (int i = 0;i < lyrics.size();i++)
        threads.emplace_back(SingLyric, lyrics[i].first, delays[i], lyrics[i].second);

    // wait until all threads finish
    for (auto& t : threads) t.join();

    // small delay before ending message
    this_thread::sleep_for(chrono::milliseconds(1500));

    cout << "\nTiktok: kiryo17.4x\nGithub: kiryo36x\n";
    cout << "\nHappy Valentines Day!\n";
}

//FIRST PART OF THE SONG
void First()
{
    vector<pair<string, double>> lyrics = {
        {"Cause you're the one that I like", 0.06},
        {"I can't deny", 0.08},
        {"Every night you're on my mind", 0.07},
        {"So if I call you tonight", 0.08},
        {"Will you pick up and give me your time?", 0.08},
        {"Miss you every night", 0.08},
        {"Miss you all the time", 0.07},
        {"No, I don't even know", 0.07},
        {"Where to start\n\n", 0.05}
    };

    vector<double> delays = { 0.3,3,4.5,6.0,8.5,13,14.5,17,17.6 };

    vector<thread> threads;

    // start threads for lyrics
    for (int i = 0;i < lyrics.size();i++)
        threads.emplace_back(SingLyric, lyrics[i].first, delays[i], lyrics[i].second);

    for (auto& t : threads) t.join();

    // after first verse, go to second verse
    Second();
}

//SONG TITLE INTRO
void Title()
{
    vector<pair<string, double>> title = {
        {"I Like You The Most",0.10},
        {"By Shad\n",0.10}
    };

    vector<double> delays = { 1,2 };

    vector<thread> threads;

    // show title using threads
    for (int i = 0; i < title.size(); i++)
        threads.emplace_back(SingLyric, title[i].first, delays[i], title[i].second);

    for (auto& t : threads) t.join();

    // wait before starting lyrics
    this_thread::sleep_for(chrono::milliseconds(3500));

    First();
}

//PROGRAM STARTS HERE
int main()
{
    PlayMusic(); // start playing the MP3

    // wait 1.2 seconds before showing title
    this_thread::sleep_for(chrono::milliseconds(1200));

    Title(); // start the lyric animation

    cin.get(); // prevent program from closing immediately
    return 0;
}
