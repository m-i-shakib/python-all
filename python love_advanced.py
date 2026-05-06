import math
import random
import pygame

# -------------------- Config --------------------
W, H = 1000, 700
FPS = 60
CENTER = (W // 2, H // 2 - 20)

BG = (6, 6, 10)
TEXT_COLOR = (245, 245, 255)

# Particles
SPAWN_PER_FRAME = 14
MAX_PARTICLES = 2200
TRAIL_ALPHA = 25  # lower = longer trails

# Heart
BASE_SCALE = 18.5
PULSE_SPEED = 0.055

# -------------------- Heart curve --------------------
def heart_point(t: float):
    # Classic parametric heart (x, y)
    x = 16 * (math.sin(t) ** 3)
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
    return x, y

def heart_derivative(t: float):
    # Numerical derivative (simple & stable)
    dt = 1e-3
    x1, y1 = heart_point(t - dt)
    x2, y2 = heart_point(t + dt)
    return (x2 - x1) / (2*dt), (y2 - y1) / (2*dt)

def clamp(v, a, b):
    return a if v < a else b if v > b else v

# -------------------- Particle --------------------
class Particle:
    __slots__ = ("x","y","vx","vy","life","max_life","size","hue_shift","spin")

    def __init__(self, x, y, vx, vy, life, size, hue_shift=0.0):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.life = life
        self.max_life = life
        self.size = size
        self.hue_shift = hue_shift
        self.spin = random.uniform(-1.2, 1.2)

    def update(self):
        # Slight drag + gentle gravity-like pull to center (gives elegant motion)
        drag = 0.985
        self.vx *= drag
        self.vy *= drag

        cx, cy = CENTER
        dx = (cx - self.x) * 0.0008
        dy = (cy - self.y) * 0.0008
        self.vx += dx
        self.vy += dy

        self.x += self.vx
        self.y += self.vy

        self.life -= 1
        return self.life > 0

def color_from_energy(e, hue_shift=0.0):
    # e in [0..1], maps to pink/red neon-ish
    # We'll fake hue shift by mixing channels
    r = int(255 * clamp(0.65 + 0.35 * e, 0, 1))
    g = int(255 * clamp(0.08 + 0.22 * e, 0, 1))
    b = int(255 * clamp(0.12 + 0.35 * (1 - e), 0, 1))

    # subtle hue shift
    b = int(clamp(b + 80 * hue_shift, 0, 255))
    return (r, g, b)

def draw_glow_circle(surf, x, y, radius, col, alpha):
    # Multi-layer circle for glow (additive blend surface)
    for k in (3.5, 2.2, 1.4, 1.0):
        rr = int(radius * k)
        aa = int(alpha / (k * 1.2))
        pygame.draw.circle(surf, (*col, aa), (int(x), int(y)), rr)

# -------------------- Main --------------------
def main():
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Advanced Love Animation ❤️ (Particles + Glow + Trails)")
    clock = pygame.time.Clock()

    # Surfaces
    trail = pygame.Surface((W, H), pygame.SRCALPHA)  # persistent trails
    glow = pygame.Surface((W, H), pygame.SRCALPHA)   # additive glow pass

    font_big = pygame.font.SysFont("Segoe UI", 56, bold=True)
    font_small = pygame.font.SysFont("Segoe UI", 22)

    particles = []
    t = 0.0
    phase = 0.0
    text_phase = 0.0

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fade trails slowly (creates motion blur/trails)
        trail.fill((0, 0, 0, TRAIL_ALPHA), special_flags=pygame.BLEND_RGBA_SUB)
        glow.fill((0, 0, 0, 0))

        # Heartbeat pulse
        phase += PULSE_SPEED
        beat = 0.65 + 0.35 * (0.5 + 0.5 * math.sin(phase))  # 0.65..1.0
        # add a sharper "kick" occasionally
        kick = 1.0 + 0.12 * math.exp(-((math.sin(phase)) * 2.2) ** 2)
        scale = BASE_SCALE * (0.92 + 0.22 * beat) * kick

        # Spawn particles along the heart curve
        for _ in range(SPAWN_PER_FRAME):
            a = random.random() * math.tau
            hx, hy = heart_point(a)
            dx, dy = heart_derivative(a)

            # Normalize tangent
            mag = math.hypot(dx, dy) + 1e-9
            tx, ty = dx / mag, dy / mag

            # Screen position
            x = CENTER[0] + hx * scale
            y = CENTER[1] - hy * scale

            # velocity: mostly outward normal-ish + a bit along tangent
            # approximate normal by rotating tangent
            nx, ny = -ty, tx

            speed = random.uniform(0.6, 2.8) * (0.8 + 0.7 * beat)
            spread = random.uniform(-0.7, 0.7)
            vx = (nx + tx * spread) * speed
            vy = (ny + ty * spread) * speed

            life = random.randint(70, 140)
            size = random.uniform(1.2, 3.2) * (0.9 + 0.6 * beat)
            hue_shift = random.uniform(-0.2, 0.25)

            particles.append(Particle(x, y, vx, vy, life, size, hue_shift))

        # Limit particles
        if len(particles) > MAX_PARTICLES:
            particles = particles[-MAX_PARTICLES:]

        # Update + draw particles
        alive = []
        for p in particles:
            if p.update():
                alive.append(p)

                energy = p.life / p.max_life  # 1..0
                col = color_from_energy(energy, p.hue_shift)

                # Glow pass (additive)
                alpha = int(180 * (energy ** 0.7))
                draw_glow_circle(glow, p.x, p.y, int(p.size * 2.2), col, alpha)

                # Core dot on trail (normal alpha blend)
                core_alpha = int(200 * (energy ** 0.9))
                pygame.draw.circle(trail, (*col, core_alpha), (int(p.x), int(p.y)), int(p.size))

        particles = alive

        # Compose
        screen.fill(BG)
        screen.blit(trail, (0, 0))
        screen.blit(glow, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

        # Draw subtle heart outline as neon curve
        outline = []
        steps = 180
        for i in range(steps + 1):
            a = (i / steps) * math.tau
            hx, hy = heart_point(a)
            outline.append((CENTER[0] + hx * scale, CENTER[1] - hy * scale))

        # outline glow-ish lines (multiple strokes)
        for w in (6, 3, 1):
            alpha = 40 if w == 6 else 70 if w == 3 else 160
            pygame.draw.aalines(trail, (255, 80, 120, alpha), True, outline)

        # Floating text with fade
        text_phase += 0.03
        bob = math.sin(text_phase) * 6
        fade = int(180 + 75 * (0.5 + 0.5 * math.sin(text_phase * 0.7)))

        msg = "I LOVE YOU ❤️"
        surf = font_big.render(msg, True, TEXT_COLOR)
        surf.set_alpha(fade)
        rect = surf.get_rect(center=(W // 2, int(H * 0.83 + bob)))
        screen.blit(surf, rect)

        hint = font_small.render("Close window to exit  |  Made with Python + Pygame", True, (170, 170, 190))
        hint.set_alpha(180)
        screen.blit(hint, (20, H - 34))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
