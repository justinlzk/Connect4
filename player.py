colors = {
    "RED": "🔴",
    "ORANGE": "🟠",
    "YELLOW": "🟡",
    "GREEN": "🟢",
    "BLUE": "🔵",
    "PURPLE": "🟣",
    "BLACK": "⚫️",
    "WHITE": "⚪️",
    "BROWN": "🟤"
}


class Player:
    def __init__(self, num, name, color):
        self.num = num
        self.name = name
        self.color = color
        self.symbol = colors[self.color]

    def __str__(self):
        return f"{self.name}({self.symbol})"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            name = f"P{self.num}"
        self._name = name

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        try:
            colors[color]
        except KeyError:
            raise ValueError("Invalid color")
        else:
            self._color = color

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        self._symbol = symbol
        colors.pop(self.color)

    @classmethod
    def colors(cls):
        msg = "Available colors: \n"
        for color in colors:
            msg += f"  {color+":":10} {colors[color]}\n"
        return msg

