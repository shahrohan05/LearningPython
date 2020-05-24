from dog import Dog


class Poodle(Dog):
    fur_color = "multi"

    def __init__(self, name, highlight_feature):
        Dog.__init__(self, name)
        self.highlight_feature = highlight_feature
        self.add_trick("Super-Fast Tail Chasing")

    def __call__(self, *args, **kwargs):
        Dog.__call__(self)
        print("POODLE Fur Color: %s, Highlight Feature : %s" % (self.fur_color, self.highlight_feature))


if __name__ == "__main__":
    Poodle("Zinty", "Alert and Intelligent")()

