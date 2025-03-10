import requests
import time
import curses
from threading import Thread

TOKEN = "ENTER_BEARER_TOKEN_HERE" #U NEED AT LEAST 100 GOLD TO PERFORM THIS
URL = "https://core.api-wolvesville.com/players/self"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}
DELAY = 0.2  # Change this Delay to your Desire (0.2 is fine)
WORDLIST_FILE = "wordlist.txt"

checked_count = 0
valid_count = 0
failed_count = 0
valid_usernames = []
running = True

def load_wordlist():
    try:
        with open(WORDLIST_FILE, "r", encoding="utf-8") as f:
            usernames = [line.strip() for line in f if line.strip()]
        return usernames
    except FileNotFoundError:
        print(f"❌ Cant find '{WORDLIST_FILE}'.")
        exit()

def check_username(username):
    global checked_count, valid_count, failed_count, valid_usernames

    payload = {"username": username, "gender": "FEMALE"}
    response = requests.put(URL, json=payload, headers=HEADERS)

    checked_count += 1
    if response.status_code == 200:
        valid_count += 1
        valid_usernames.append(username)
    else:
        failed_count += 1

def display_screen(stdscr):
    global checked_count, valid_count, failed_count, valid_usernames, running

   
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(1000)

    
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    while running:
        stdscr.clear()

        
        stdscr.addstr(0, 0, "========================", curses.color_pair(3) | curses.A_BOLD)
        stdscr.addstr(1, 0, f" CHECKED: {checked_count}", curses.A_BOLD)
        stdscr.addstr(2, 0, f" VALID:   {valid_count}", curses.color_pair(1) | curses.A_BOLD)
        stdscr.addstr(3, 0, f" FAILED:  {failed_count}", curses.color_pair(2))
        stdscr.addstr(4, 0, "========================", curses.color_pair(3) | curses.A_BOLD)

        
        y = 6
        for username in valid_usernames[-20:]:
            stdscr.addstr(y, 0, f"[SUCCESS] - {username}", curses.color_pair(1))
            y += 1

        stdscr.refresh()
        time.sleep(1)


def main():
    global checked_count, valid_count, failed_count, running

   
    usernames = load_wordlist()

    
    display_thread = Thread(target=curses.wrapper, args=(display_screen,))
    display_thread.start()

    
    for username in usernames:
        check_username(username)
        time.sleep(DELAY)

    
    running = False
    display_thread.join()

if __name__ == "__main__":
    main()
