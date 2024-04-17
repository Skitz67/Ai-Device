RESET = "\033[0m"
# ANSI escape codes for colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# ANSI escape codes for bright (bold) colors
BRIGHT_BLACK = "\033[30;1m"
BRIGHT_RED = "\033[31;1m"
BRIGHT_GREEN = "\033[32;1m"
BRIGHT_YELLOW = "\033[33;1m"
BRIGHT_BLUE = "\033[34;1m"
BRIGHT_MAGENTA = "\033[35;1m"
BRIGHT_CYAN = "\033[36;1m"
BRIGHT_WHITE = "\033[37;1m"

# ANSI escape code for background color
BACKGROUND_BLACK = "\033[40m"
BACKGROUND_RED = "\033[41m"
BACKGROUND_GREEN = "\033[42m"
BACKGROUND_YELLOW = "\033[43m"
BACKGROUND_BLUE = "\033[44m"
BACKGROUND_MAGENTA = "\033[45m"
BACKGROUND_CYAN = "\033[46m"
BACKGROUND_WHITE = "\033[47m"


import colorsys


def adjust_brightness(r, g, b, factor):
    h, l, s = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
    l = max(min(l * factor, 1.0), 0.0)
    r, g, b = [int(x * 255.0) for x in colorsys.hls_to_rgb(h, l, s)]
    return r, g, b


def print_rgb(
    text,
    r,
    g,
    b,
    brightness=1.0,
    background=None,
    bold=False,
    underline=False,
    italic=False,
):
    r, g, b = adjust_brightness(r, g, b, brightness)
    style = ""
    if bold:
        style += "\033[1m"
    if underline:
        style += "\033[4m"
    if italic:
        style += "\033[3m"
    if background is not None:
        br, bg, bb = background
        style += f"\033[48;2;{br};{bg};{bb}m"
    print(f"{style}\033[38;2;{r};{g};{b}m{text}\033[0m")


if __name__ == "__main__":
    print_rgb(
        "Hello, World!",
        255,
        0,
        0,
        brightness=1,
        background=(0, 0, 255),
        bold=True,
        underline=True,
        italic=True,
    )
