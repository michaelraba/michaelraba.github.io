from manim import *


class AnandModelFullEvolution(Scene):
    def construct(self):
        slides = []

        # S5: Original Form (Mixed Configuration)
        s5_title = Text("Anand Model: Constitutive Evolution", font_size=36).to_edge(UP)
        s5_eqs = (
            VGroup(
                MathTex(
                    r"\mathbf{F} = \mathbf{F}^e \mathbf{F}^p, \quad \det \mathbf{F}^p = 1"
                ),
                MathTex(
                    r"\mathbf{T} \rightarrow \mathbf{Q} \mathbf{T} \mathbf{Q}^T, \quad \mathbf{B} \rightarrow \mathbf{Q} \mathbf{B} \mathbf{Q}^T"
                ),
                MathTex(r"\{ \mathbf{F}^e, \theta, \mathbf{g}, \mathbf{B}, s \}"),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.85)
            .shift(UP * 0.5)
        )
        s5_label = Text(
            "S5: Original Form (Mixed Configuration)", font_size=28
        ).next_to(s5_eqs, DOWN)
        slides.append((s5_title, s5_eqs, s5_label))

        # S4: General Form (Reference Configuration)
        s4_title = s5_title.copy()
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
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.85)
            .shift(UP * 0.5)
        )
        s4_label = Text(
            "S4: General Form (Reference Configuration)", font_size=28
        ).next_to(s4_eqs, DOWN)
        slides.append((s4_title, s4_eqs, s4_label))

        # Z4: Simplifying Assumptions
        z4_title = s5_title.copy()
        z4_scalar_defs = (
            MathTex(
                r"\tau := \left\{ \tfrac{1}{2} \operatorname{tr}(\tilde{\mathbf{T}}'^2) \right\}^{1/2}, \quad"
                r"\bar{\tau}_b := \left\{ \tfrac{1}{2} \operatorname{tr}(\mathbf{B}^2) \right\}^{1/2}, \quad"
                r"\bar{p} := -\tfrac{1}{3} \operatorname{tr}(\tilde{\mathbf{T}})"
            )
            .scale(0.55)
            .next_to(z4_title, DOWN, buff=0.4)
        )
        z4_eqs = (
            VGroup(
                MathTex(
                    r"\dot{\mathbf{E}}^e = \mathbf{K}[\tilde{\mathbf{T}}] + \mathbf{A} \dot{\theta}"
                ),
                MathTex(
                    r"\mathbf{L}^p = x_1 \tilde{\mathbf{T}}' + \eta_1 (\tilde{\mathbf{T}}' \mathbf{B} - \mathbf{B} \tilde{\mathbf{T}}')"
                ),
                MathTex(
                    r"\dot{\mathbf{B}} = \xi_1 \tilde{\mathbf{T}}' + \xi_2 \mathbf{B}"
                ),
                MathTex(
                    r"\dot{s} = \hat{s}(l), \quad l = \{ \tau, \bar{\tau}_b, s, \theta, \bar{p} \}"
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.85)
            .shift(DOWN * 0.5)
        )
        z4_label = Text("Z4: Simplifying Assumptions", font_size=28).next_to(
            z4_eqs, DOWN
        )
        slides.append((z4_title, VGroup(z4_scalar_defs, z4_eqs), z4_label))

        # S3: Simplified Model (Reference Configuration)
        s3_title = s5_title.copy()
        s3_eqs = (
            VGroup(
                MathTex(
                    r"\dot{\mathbf{E}}^e = \mathbf{K}[\tilde{\mathbf{T}}] + \mathbf{A} \dot{\theta}"
                ),
                MathTex(
                    r"\mathbf{L}^p = x_1 \tilde{\mathbf{T}}' + \eta_1(\tilde{\mathbf{T}}' \mathbf{B} - \mathbf{B} \tilde{\mathbf{T}}')"
                ),
                MathTex(
                    r"\dot{\mathbf{B}} = \xi_1 \tilde{\mathbf{T}}' + \xi_2 \mathbf{B}"
                ),
                MathTex(r"\dot{s} = s^+(l)"),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.9)
            .shift(UP * 1)
        )
        s3_label = Text(
            "S3: Simplified Model (Reference Configuration)", font_size=28
        ).next_to(s3_eqs, DOWN)
        slides.append((s3_title, s3_eqs, s3_label))

        # S2: Rotation to Current Configuration
        s2_title = s5_title.copy()
        s2_eqs = (
            VGroup(
                MathTex(
                    r"\dot{\mathbf{E}}^e = \mathbf{R}^T \mathbf{D}^e \mathbf{R}, \quad"
                    r"\tilde{\mathbf{T}} = \mathbf{R}^T \mathbf{T} \mathbf{R}, \quad"
                    r"\mathbf{L}^p = \mathbf{R}^T \mathbf{L}^p \mathbf{R}"
                )
            )
            .scale(0.7)
            .shift(UP * 0.5)
        )
        s2_label = Text("S2: Rotation to Current Configuration", font_size=28).next_to(
            s2_eqs, DOWN
        )
        slides.append((s2_title, s2_eqs, s2_label))

        # S1: Final Simplified Form (Current Configuration)
        s1_title = s5_title.copy()
        s1_eqs = (
            VGroup(
                MathTex(
                    r"\dot{\tilde{\mathbf{T}}} = \mathbb{L}[\mathbf{D} - \mathbf{D}^p] - \mathbf{\Pi} \dot{\theta}"
                ),
                MathTex(
                    r"\mathbf{D}^p = \dot{\gamma}^p \left\{ \frac{\tilde{\mathbf{T}}'}{2 \bar{\tau}} \right\}, \quad \mathbf{W}^p = 0"
                ),
                MathTex(
                    r"\dot{\gamma}^p = f(\bar{\tau}, s, \theta), \quad f(0, s, \theta) = 0"
                ),
                MathTex(
                    r"\bar{\tau} = \left\{ \tfrac{1}{2} \operatorname{tr}(\tilde{\mathbf{T}}'^2) \right\}^{1/2}"
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.85)
            .shift(UP * 0.5)
        )
        s1_note = (
            MathTex(
                r"\tilde{\mathbf{T}} = \mathbf{R}^T \mathbf{T} \mathbf{R}, \quad "
                r"\mathbf{D} = \mathbf{R}^T \dot{\mathbf{E}}^e \mathbf{R}, \quad "
                r"\mathbf{L}^p = \mathbf{R}^T \mathbf{L}^p \mathbf{R}"
            )
            .scale(0.5)
            .next_to(s1_eqs, DOWN, buff=0.3)
        )
        s1_label = Text(
            "S1: Final Simplified Form (Current Configuration)", font_size=28
        ).next_to(s1_note, DOWN)
        slides.append((s1_title, VGroup(s1_eqs, s1_note), s1_label))

        # Animate each slide in sequence
        for title, body, label in slides:
            self.play(FadeIn(title), Write(body), FadeIn(label))
            self.wait(3)
            self.play(*[FadeOut(mob) for mob in self.mobjects])
