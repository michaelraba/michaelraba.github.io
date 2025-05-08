#!/usr/bin/env python3.10
# +PROPERTY: header-args:python :python /home/mi/miniconda3/envs/manim/bin/python

from manim import Scene, Square

print("✅ Manim works in fireEnv!")


from manim import *


class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, world!")
        self.play(Write(text))
        self.wait(1)
