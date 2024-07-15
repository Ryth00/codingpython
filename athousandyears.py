import time
from threading import Thread, Lock
import sys

lock = Lock()


def animate_text(text, delay=0.15):  # Menyesuaikan penundaan antar karakter menjadi 0.15 detik
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
        ("Heart beats fast", 0.15),
        ("Colors and promises", 0.15),
        ("How to be brave", 0.15),
        ("How can I love when I'm afraid to fall?", 0.14),
        ("But watching you stand alone", 0.15),
        ("All of my doubt suddenly goes away somehow", 0.14),
        ("One step closer", 0.15),
        ("I have died every day waiting for you", 0.14),
        ("Darling, don't be afraid, I have loved you", 0.14),
        ("For a thousand years", 0.15),
        ("I'll love you for a thousand more", 0.15),
    ]
    delays = [0.5, 3.5, 7.0, 11.0, 15.0, 19.5, 23.5, 27.5, 31.5, 35.5, 39.5]

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
