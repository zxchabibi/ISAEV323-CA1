colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255)
}

r1, g1, b1 = colors["red"]
r2, g2, b2 = colors["blue"]
mixed_color = ((r1 + r2) // 2, (g1 + g2) // 2, (b1 + b2) // 2)
print(f"Смесь red и blue: {mixed_color}")

r, g, b = colors["green"]
inverted_color = (255 - r, 255 - g, 255 - b)
print(f"Инвертированный green: {inverted_color}")
    