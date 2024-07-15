import time
from threading import Thread, Lock
import sys

lock = Lock()


def animate_text(text, delay=0.5):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()


def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)


def sing_song():
    lyrics = [
        ("Cause I'll be waiting for your love", 0.08),
        ("Let's fly away together", 0.07),
        ("Let's get this dream forever", 0.06),
        ("Let's dance like we're in heaven", 0.06),
        ("Just give me your sweet love", 0.06),
        ("Let's fly away together", 0.08),
        ("Let's get this dream forever", 0.08),
        ("Let's dance like we're in heaven", 0.08),
        ("Just give me your sweet love", 0.06),
    ]
    delays = [0.9, 2.0, 3.7, 5.4, 7.1, 8.8, 10.5, 12.2, 13.9]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    sing_song()
