#!/usr/bin/env python3.10

from manim import *


class AnandConstitutiveFlow(Scene):
    def construct(self):
        title = Text("Anand Model: Constitutive Evolution", font_size=36).to_edge(UP)

        # -------------------------------
        # Frame 1: S5 - Original Formulation (Current Config)
        # -------------------------------
        s5_eqs = (
            VGroup(
                MathTex(
                    r"\mathbf{F} = \mathbf{F}^e \mathbf{F}^p, \quad \det \mathbf{F}^p = 1"
                ),
                MathTex(
                    r"\mathbf{T} \to \mathbf{Q} \mathbf{T} \mathbf{Q}^T, \quad \mathbf{B} \to \mathbf{Q} \mathbf{B} \mathbf{Q}^T"
                ),
                MathTex(r"\{ \mathbf{F}^e, \theta, \mathbf{g}, \mathbf{B}, s \}"),
            )
            .arrange(DOWN, center=False, aligned_edge=LEFT)
            .scale(0.9)
            .shift(DOWN)
        )

        s5_label = Text(
            "S5: Original Form (Current Configuration)", font_size=28
        ).next_to(s5_eqs, DOWN)

        self.play(FadeIn(title), Write(s5_eqs), FadeIn(s5_label))
        self.wait(2)

        # -------------------------------
        # Frame 2: Rotate to Reference Config (S4)
        # -------------------------------
        s4_eqs = (
            VGroup(
                MathTex(
                    r"\dot{\phi}_r = \hat{\phi}(\tilde{\mathbf{T}}, \theta, \mathbf{B}, s)"
                ),
                MathTex(
                    r"\dot{\mathbf{E}}^e = \hat{\mathbf{E}}^e(\tilde{\mathbf{T}}, \theta, \mathbf{B}, s)"
                ),
                MathTex(
                    r"\dot{\mathbf{q}} = \hat{\mathbf{q}}(\tilde{\mathbf{T}}, \theta, \mathbf{g}, \mathbf{B}, s)"
                ),
                MathTex(
                    r"\mathbf{L}^p = \hat{\mathbf{G}}(\tilde{\mathbf{T}}, \theta, \mathbf{B}, s)"
                ),
            )
            .arrange(DOWN, center=False, aligned_edge=LEFT)
            .scale(0.9)
            .shift(DOWN)
        )

        s4_label = Text(
            "S4: General Form (Reference Configuration)", font_size=28
        ).next_to(s4_eqs, DOWN)

        self.play(FadeOut(s5_eqs), FadeOut(s5_label))
        self.play(Write(s4_eqs), FadeIn(s4_label))
        self.wait(2)

        # -------------------------------
        # Frame 3: Apply Simplifying Assumptions (Z4)
        # -------------------------------
        z_assumptions = (
            VGroup(
                MathTex(
                    r"\dot{\mathbf{E}}^e = \mathbb{K}[\tilde{\mathbf{T}}] + \mathbf{A} \dot{\theta}"
                ),
                MathTex(
                    r"\mathbf{L}^p = x_1 \tilde{\mathbf{T}}' + \eta_1 (\tilde{\mathbf{T}}' \mathbf{B} - \mathbf{B} \tilde{\mathbf{T}}')"
                ),
                MathTex(
                    r"\dot{\mathbf{B}} = \xi_1 \tilde{\mathbf{T}}' + \xi_2 \mathbf{B}"
                ),
                MathTex(r"\dot{s} = \hat{s}(l)"),
            )
            .arrange(DOWN, center=False, aligned_edge=LEFT)
            .scale(0.9)
            .shift(DOWN)
        )

        z_label = Text("Z4: Simplifying Assumptions", font_size=28).next_to(
            z_assumptions, DOWN
        )

        self.play(FadeOut(s4_eqs), FadeOut(s4_label))
        self.play(Write(z_assumptions), FadeIn(z_label))
        self.wait(2)

        # -------------------------------
        # Frame 4: Rotate back to Current Config (S2)
        # -------------------------------
        s2_eq = MathTex(
            r"\dot{\tilde{\mathbf{T}}} = \mathbb{L}[\mathbf{D} - \mathbf{D}^p] - \boldsymbol{\Pi} \dot{\theta} - \mathbf{W}^p \tilde{\mathbf{T}} + \tilde{\mathbf{T}} \mathbf{W}^p"
        ).scale(0.9)
        s2_label = Text("S2: Refined Current Configuration", font_size=28).next_to(
            s2_eq, DOWN
        )

        self.play(FadeOut(z_assumptions), FadeOut(z_label))
        self.play(Write(s2_eq), FadeIn(s2_label))
        self.wait(2)

        # -------------------------------
        # Frame 5: Final Simplified Form (S1)
        # -------------------------------
        s1_eqs = (
            VGroup(
                MathTex(
                    r"\dot{\tilde{\mathbf{T}}} = \mathbb{L}[\mathbf{D} - \mathbf{D}^p] - \Pi \dot{\theta}"
                ),
                MathTex(
                    r"\mathbf{D}^p = \dot{\gamma}^p \left\{ \frac{\tilde{\mathbf{T}}'}{2 \bar{\tau}} \right\}, \quad \mathbf{W}^p = 0"
                ),
                MathTex(
                    r"\dot{\gamma}^p = f(\bar{\tau}, s, \theta), \quad f(0, s, \theta) = 0"
                ),
                MathTex(
                    r"\bar{\tau} = \left\{ \tfrac{1}{2} \mathrm{tr}(\tilde{\mathbf{T}}'^2) \right\}^{1/2}"
                ),
            )
            .arrange(DOWN, center=False, aligned_edge=LEFT)
            .scale(0.9)
            .shift(DOWN)
        )

        s1_label = Text("S1: Final Simplified Form", font_size=28).next_to(s1_eqs, DOWN)

        self.play(FadeOut(s2_eq), FadeOut(s2_label))
        self.play(Write(s1_eqs), FadeIn(s1_label))
        self.wait(3)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
