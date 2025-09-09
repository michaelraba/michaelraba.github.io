#!/usr/bin/env python3.10

from manim import *


class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, world!")
        self.play(Write(text))
        self.wait(1)
