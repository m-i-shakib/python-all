import math, random, os
import pygame
import wave, struct

# ===================== SETTINGS =====================
NAME_LEFT  = "Yeamin"
NAME_RIGHT = "Beeva"

W, H = 1100, 720
FPS = 60

# Bright neon palette
BG_TOP  = (6, 6, 20)
BG_BOT  = (44, 10, 70)
LEFT_COL  = (255, 40, 160)   # neon pink
RIGHT_COL = (255, 190, 40)   # neon orange
TEXT_COL  = (255, 255, 255)

STAR_COUNT = 150

JOIN_TIME = 3.0
HOLD_TIME = 2.6
LOOP = True

# Heart rendering (small surface for performance)
HEART_SIZE = 640   # smaller = faster
HEART_CENTER = (W//2, H//2 - 25)

# Music
MUSIC_VOLUME = 0.65
MUSIC_FILE = "love_loop.wav"

# ===================== HELPERS =====================
def clamp(v, a, b):
    return a if v < a else b if v > b else v

def lerp(a, b, t):
    return a + (b - a) * t

def smoothstep(t):
    t = clamp(t, 0.0, 1.0)
    return t * t * (3 - 2 * t)

def ease_out_elastic(t):
    t = clamp(t, 0.0, 1.0)
    c4 = (2 * math.pi) / 3
    if t == 0: return 0
    if t == 1: return 1
    return pow(2, -10 * t) * math.sin((t * 10 - 0.75) * c4) + 1

def draw_gradient_bg(surf):
    for y in range(H):
        k = y / (H - 1)
        r = int(lerp(BG_TOP[0], BG_BOT[0], k))
        g = int(lerp(BG_TOP[1], BG_BOT[1], k))
        b = int(lerp(BG_TOP[2], BG_BOT[2], k))
        pygame.draw.line(surf, (r, g, b), (0, y), (W, y))

def draw_vignette(surf):
    vg = pygame.Surface((W, H), pygame.SRCALPHA)
    for i in range(16):
        a = int(10 + i * 10)
        pygame.draw.rect(vg, (0, 0, 0, a), (i*16, i*10, W - i*32, H - i*20), border_radius=30)
    surf.blit(vg, (0, 0))

def draw_glow_circle(surf, x, y, r, col, alpha):
    for k in (3.5, 2.6, 1.9, 1.3, 1.0):
        rr = max(1, int(r * k))
        aa = max(0, int(alpha / (k * 1.15)))
        pygame.draw.circle(surf, (*col, aa), (int(x), int(y)), rr)

# ===================== AUDIO (SAFE) =====================
def generate_love_wav(filename="love_loop.wav", seconds=24, sample_rate=44100):
    if os.path.exists(filename):
        return filename

    def sine(freq, t):
        return math.sin(2 * math.pi * freq * t)

    chords = [
        (220.00, 261.63, 329.63),
        (174.61, 220.00, 261.63),
        (130.81, 196.00, 261.63),
        (196.00, 246.94, 293.66),
    ]
    melody = [329.63, 293.66, 261.63, 293.66, 329.63, 392.00, 349.23, 329.63]
    step = 0.5

    wf = wave.open(filename, "w")
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)

    total = int(seconds * sample_rate)
    for n in range(total):
        t = n / sample_rate
        c1, c2, c3 = chords[int(t // 3) % len(chords)]
        pad = 0.33*sine(c1,t) + 0.23*sine(c2,t) + 0.19*sine(c3,t)

        m = melody[int((t/step)) % len(melody)]
        mel = 0.17*sine(m,t) + 0.05*sine(m*2,t)

        pulse = 0.70 + 0.30*(0.5 + 0.5*math.sin(2*math.pi*1.05*t))
        x = math.tanh((pad+mel)*pulse * 1.25)

        fade = 1.0
        if t < 0.5: fade = t/0.5
        if t > seconds - 1.0: fade = max(0.0, (seconds-t)/1.0)
        x *= fade

        s = int(clamp(x, -1, 1) * 32767)
        wf.writeframes(struct.pack("<h", s))

    wf.close()
    return filename

def try_music_safe(filename, volume):
    # music fail হলেও program চলবে
    try:
        if not os.path.exists(filename):
            return False
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
        print("Music: ON ->", filename)
        return True
    except Exception as e:
        print("Music: OFF (error) ->", e)
        return False

# ===================== HEART (OPTIMIZED SMALL SURF) =====================
def heart_point(t):
    x = 16 * (math.sin(t) ** 3)
    y = 13*math.cos(t) - 5*math.cos(2*t) - 2*math.cos(3*t) - math.cos(4*t)
    return x, y

def make_heart_points_local(size):
    # map heart into [0..size] surface
    cx = cy = size // 2
    # x range about -16..16 => width 32; y range about -17..13 => height 30-ish
    s = size / 36.0
    pts = []
    steps = 260
    for i in range(steps):
        a = (i / steps) * math.tau
        hx, hy = heart_point(a)
        pts.append((cx + hx * s, cy - hy * s))
    return pts

def split_half_local(pts, cx, left=True):
    half = []
    for x, y in pts:
        if left and x <= cx: half.append((x, y))
        if (not left) and x >= cx: half.append((x, y))
    return half

def prebuild_hearts(size):
    pts = make_heart_points_local(size)
    cx = size // 2

    left_pts = split_half_local(pts, cx, left=True)
    right_pts = split_half_local(pts, cx, left=False)

    left = pygame.Surface((size, size), pygame.SRCALPHA)
    right = pygame.Surface((size, size), pygame.SRCALPHA)
    mask = pygame.Surface((size, size), pygame.SRCALPHA)

    if len(left_pts) >= 3:
        pygame.draw.polygon(left, (*LEFT_COL, 255), left_pts)
        pygame.draw.aalines(left, (255,255,255,160), False, left_pts)

    if len(right_pts) >= 3:
        pygame.draw.polygon(right, (*RIGHT_COL, 255), right_pts)
        pygame.draw.aalines(right, (255,255,255,160), False, right_pts)

    pygame.draw.polygon(mask, (255,255,255,255), pts)
    return left, right, mask

def draw_inner_gradient_fullheart(screen, center, size, mask, t, scale=1.0):
    # build fill then clip by mask
    fill = pygame.Surface((size, size), pygame.SRCALPHA)
    cx = cy = size // 2

    for i in range(12):
        k = i / 11
        r = int(lerp(LEFT_COL[0], RIGHT_COL[0], k))
        g = int(lerp(LEFT_COL[1], RIGHT_COL[1], k))
        b = int(lerp(LEFT_COL[2], RIGHT_COL[2], k))
        pulse = 0.5 + 0.5*math.sin(t*2.3 + i*0.7)
        a = int(40 + 30*pulse)
        rad = int((size*0.33) - i*12)
        draw_glow_circle(fill, cx, cy+8, max(10, rad), (r,g,b), a*8)

    fill.blit(mask, (0,0), special_flags=pygame.BLEND_RGBA_MULT)

    if scale != 1.0:
        fill = pygame.transform.smoothscale(fill, (int(size*scale), int(size*scale)))

    x = center[0] - fill.get_width()//2
    y = center[1] - fill.get_height()//2
    screen.blit(fill, (x, y))

# ===================== STARS =====================
class Star:
    __slots__=("x","y","tw","a","r")
    def __init__(self):
        self.x = random.uniform(0, W)
        self.y = random.uniform(0, H)
        self.tw = random.uniform(0.7, 2.6)
        self.a = random.randint(60, 180)
        self.r = random.choice([1,1,2])
    def update(self, t):
        self.a = int(70 + 120*(0.5 + 0.5*math.sin(t*self.tw + self.x*0.01)))

# ===================== SPARKS =====================
class Spark:
    __slots__=("x","y","vx","vy","life","mx","col","sz")
    def __init__(self, x, y, vx, vy, life, col, sz):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.life = self.mx = life
        self.col = col
        self.sz = sz
    def update(self):
        self.vy += 0.05
        self.vx *= 0.99
        self.vy *= 0.99
        self.x += self.vx
        self.y += self.vy
        self.life -= 1
        return self.life > 0

def spawn_sparks(lst, x, y, strength=1.0):
    n = int(75 * strength)
    for _ in range(n):
        ang = random.random() * math.tau
        spd = random.uniform(2.0, 9.0) * strength
        vx = math.cos(ang) * spd
        vy = math.sin(ang) * spd
        life = random.randint(30, 65)
        sz = random.uniform(1.2, 3.2)
        col = random.choice([(255,40,160), (255,190,40), (255,255,255), (120,210,255)])
        lst.append(Spark(x, y, vx, vy, life, col, sz))

# ===================== TEXT =====================
def draw_text_center(surf, text, pos, font, col, alpha=255):
    x, y = pos
    for dx, dy, a in [(3,3,130), (-3,-3,130), (2,-2,95), (-2,2,95)]:
        g = font.render(text, True, (255, 80, 190))
        g.set_alpha(a)
        surf.blit(g, g.get_rect(center=(x+dx, y+dy)))

    t = font.render(text, True, col)
    t.set_alpha(alpha)
    surf.blit(t, t.get_rect(center=(x, y)))

# ===================== MAIN =====================
def main():
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("WOW Half-Heart Join ❤️ (Stable)")
    clock = pygame.time.Clock()

    base = pygame.Surface((W, H))
    fx = pygame.Surface((W, H), pygame.SRCALPHA)
    glow = pygame.Surface((W, H), pygame.SRCALPHA)

    font_name = pygame.font.SysFont("Segoe UI", 34, bold=True)
    font_big  = pygame.font.SysFont("Segoe UI", 46, bold=True)
    font_hint = pygame.font.SysFont("Segoe UI", 18)

    # build heart assets once (FAST)
    left_base, right_base, full_mask = prebuild_hearts(HEART_SIZE)

    # build music file then play (safe)
    generate_love_wav(MUSIC_FILE, seconds=24)
    music_on = try_music_safe(MUSIC_FILE, MUSIC_VOLUME)

    stars = [Star() for _ in range(STAR_COUNT)]
    sparks = []

    start = pygame.time.get_ticks()
    last_join_state = False

    running = True
    while running:
        clock.tick(FPS)
        now = (pygame.time.get_ticks() - start) / 1000.0

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        total_cycle = JOIN_TIME + HOLD_TIME
        tcycle = (now % total_cycle) if LOOP else min(now, total_cycle)

        pj = clamp(tcycle / JOIN_TIME, 0.0, 1.0)
        ps = smoothstep(pj)
        joined = (tcycle >= JOIN_TIME)

        # join event
        if joined and not last_join_state:
            spawn_sparks(sparks, HEART_CENTER[0], HEART_CENTER[1], strength=1.35)
        last_join_state = joined

        # draw bg
        draw_gradient_bg(base)
        fx.fill((0,0,0,0))
        glow.fill((0,0,0,0))

        for s in stars:
            s.update(now)
            pygame.draw.circle(fx, (245, 250, 255, s.a), (int(s.x), int(s.y)), s.r)

        # pulse after join
        pulse = 1.0 + (0.05 * math.sin(now * 3.0) if joined else 0.0)
        scale = 1.0 * pulse

        # movement outside -> center
        left_start_x  = W * 0.10
        right_start_x = W * 0.90
        end_left_x    = HEART_CENTER[0] - 110
        end_right_x   = HEART_CENTER[0] + 110

        lx = lerp(left_start_x, end_left_x, ps)
        rx = lerp(right_start_x, end_right_x, ps)

        floaty = math.sin(now * 1.25) * 7

        # rotate while coming in (small rotation = stable)
        rot_strength = (1.0 - ps)
        rot_left = rot_strength * 18
        rot_right = -rot_strength * 18

        # transform halves (from small surface)
        left_img = pygame.transform.rotozoom(left_base, rot_left, scale)
        right_img = pygame.transform.rotozoom(right_base, rot_right, scale)

        # positions
        screen.blit(base, (0,0))
        screen.blit(fx, (0,0))

        # glow ramp
        galpha = int(260 * (pj ** 1.25))
        draw_glow_circle(glow, HEART_CENTER[0], HEART_CENTER[1], int(95 + 85*pj), (255, 80, 190), galpha)
        draw_glow_circle(glow, HEART_CENTER[0], HEART_CENTER[1], int(60 + 55*pj), (255, 220, 70), int(galpha*0.75))

        # blit halves centered
        screen.blit(left_img, (lx - left_img.get_width()//2, HEART_CENTER[1] - left_img.get_height()//2 + floaty))
        screen.blit(right_img, (rx - right_img.get_width()//2, HEART_CENTER[1] - right_img.get_height()//2 + floaty))

        # inner gradient after join (clip by mask)
        if joined:
            # scale mask too (same scale)
            mask_scaled = pygame.transform.smoothscale(full_mask, (int(HEART_SIZE*scale), int(HEART_SIZE*scale)))
            draw_inner_gradient_fullheart(screen, HEART_CENTER, HEART_SIZE, mask_scaled, now, scale=scale)

        # sparks
        alive = []
        for sp in sparks:
            if sp.update():
                alive.append(sp)
                e = sp.life / sp.mx
                draw_glow_circle(glow, sp.x, sp.y, int(sp.sz*2.6), sp.col, int(170*(e**0.85)))
                pygame.draw.circle(screen, (*sp.col, int(235*(e**0.9))), (int(sp.x), int(sp.y)), max(1, int(sp.sz)))
        sparks = alive

        # bloom pass
        small = pygame.transform.smoothscale(glow, (W//3, H//3))
        big = pygame.transform.smoothscale(small, (W, H))
        screen.blit(big, (0,0), special_flags=pygame.BLEND_RGBA_ADD)

        # text
        name_y = HEART_CENTER[1] + 55 + floaty
        draw_text_center(screen, NAME_LEFT,  (lx, name_y), font_name, TEXT_COL, 255)
        draw_text_center(screen, NAME_RIGHT, (rx, name_y), font_name, TEXT_COL, 255)

        if joined:
            msg = f"{NAME_LEFT} ❤️ {NAME_RIGHT}"
            draw_text_center(screen, msg, (W//2, int(H*0.18)), font_big, TEXT_COL, 255)

        draw_vignette(screen)

        hint = ("Music: ON" if music_on else "Music: OFF") + "   |   Close window to exit"
        hs = font_hint.render(hint, True, (210,210,230))
        hs.set_alpha(235)
        screen.blit(hs, (22, H-34))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Double-click করলে window বন্ধ হয়ে যায়—এইটা থাকলে error দেখা যাবে
        print("ERROR:", e)
        input("Press Enter to close...")
