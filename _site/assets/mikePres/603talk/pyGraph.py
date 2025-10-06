import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as pe

fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

# Colors
colors = {
    "blue": "#1f77b4",
    "orange": "#ff7f0e",
    "green": "#2ca02c",
    "purple": "#9467bd",
}


# Box drawing function
def draw_box(x, y, w, h, text, color):
    box = patches.FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02",
        linewidth=2,
        edgecolor=color,
        facecolor=color + "20",
        path_effects=[pe.withStroke(linewidth=3, foreground="white")],
    )
    ax.add_patch(box)
    ax.text(
        x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=11, wrap=True
    )


# Arrows
def draw_arrow(x1, y1, x2, y2):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(facecolor="black", arrowstyle="->"),
    )


# Step 1: Start in Current Configuration
draw_box(
    1,
    8.2,
    8,
    1,
    r"Start in Current Config: Define $\mathbf{T}, \mathbf{L}, \dot{\psi}$ and $\mathbf{L} = \mathbf{L}^e + \mathbf{L}^p$",
    colors["blue"],
)

# Step 2: Pull back to reference config
draw_box(
    1,
    6.5,
    8,
    1.2,
    r"Pull back to Ref Config: Define $\tilde{\mathbf{T}}$, $\bar{\mathbf{B}}$, $s$, and write Eq (28)",
    colors["orange"],
)
draw_arrow(5, 8.2, 5, 7.7)

# Step 3: Simplify using assumptions
draw_box(
    1,
    4.7,
    8,
    1.4,
    r"Simplify with (a1)–(a6): Isotropy, Incompressibility, Small Stretch"
    + "\n"
    + r"Derive $\mathbf{D}^p, \mathbf{W}^p, \dot{s}, \dot{\bar{\mathbf{B}}}$",
    colors["green"],
)
draw_arrow(5, 6.5, 5, 6.1)

# Step 4: Return to current configuration
draw_box(
    1,
    2.8,
    8,
    1.4,
    r"Return to Current Config: Use $\mathbf{R}^{eT} \tilde{\mathbf{T}} \mathbf{R}^e \approx \mathbf{T}$"
    + "\n"
    + r"Write final form: Eqs. 77–86 with Jaumann derivatives",
    colors["purple"],
)
draw_arrow(5, 4.7, 5, 4.3)

# Final Output
draw_box(
    2.5,
    1,
    5,
    1,
    r"Final Model: $\dot{\mathbf{T}}, \mathbf{D}^p, \dot{s}, \dot{\bar{\mathbf{B}}}$ for FEA Implementation",
    colors["blue"],
)
draw_arrow(5, 2.8, 5, 2.4)

plt.tight_layout()
# plt.savefig("./myFig.png")
plt.savefig("/home/mi/603/603talk/anandFlow.png")
