#!/usr/bin/env python3.10

# Full Derivation of Anand's Constitutive Model (Extended 30+ Slides Version)
from manim import *


class AnandFullProcedure(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(0.8)
        title = Text(
            "Anand (1985): Full Thermo-Viscoplastic Model Derivation", font_size=34
        ).to_edge(UP)
        self.play(FadeIn(title))

        slide_counter = 1

        def slide(equation, label_text, color=None):
            nonlocal slide_counter
            label = Text(f"{slide_counter}. {label_text}", font_size=26).next_to(
                equation, DOWN
            )
            self.play(Write(equation), FadeIn(label))
            if color:
                self.play(equation.animate.set_color(color))
            self.wait(2)
            slide_counter += 1

        # Slide 1: Kinematics
        slide(
            MathTex(
                r"\mathbf{F} = \mathbf{F}^e \mathbf{F}^p,\quad \det\mathbf{F}^p=1",
                font_size=34,
            ),
            "Kinematic Decomposition",
        )
        slide(
            MathTex(
                r"\mathbf{C} = \mathbf{F}^T\mathbf{F},\quad \mathbf{E} = \frac{1}{2}(\mathbf{C} - \mathbf{I})",
                font_size=34,
            ),
            "Strain and Right Cauchy-Green Tensor",
        )

        # Slide 3–5: State Variables
        slide(
            MathTex(
                r"\{\mathbf{F}^e,\,\theta,\,\mathbf{g},\,\bar{\mathbf{B}},\,s\}",
                font_size=34,
            ),
            "State Variables",
        )
        slide(
            MathTex(r"\bar{\mathbf{B}}=\text{Backstress-like Tensor}", font_size=34),
            "Backstress Interpretation",
        )
        slide(
            MathTex(r"s=\text{Isotropic Resistance Scalar}", font_size=34),
            "Flow Resistance Scalar",
        )

        # Thermodynamics: Energy, Entropy, Dissipation
        slide(
            MathTex(
                r"\dot{\phi}_r = \rho\dot{\psi} - \mathbf{T}:\dot{\mathbf{E}}^e - \eta_r\dot{\theta}",
                font_size=34,
            ),
            "Internal Power and Energy Balance",
        )
        slide(
            MathTex(r"\eta_r = -\frac{\partial \psi}{\partial \theta}", font_size=34),
            "Entropy From Free Energy",
        )
        slide(
            MathTex(
                r"\dot{\psi} = \frac{\partial \psi}{\partial \mathbf{E}^e} : \dot{\mathbf{E}}^e + \frac{\partial \psi}{\partial s} \dot{s}",
                font_size=34,
            ),
            "Free Energy Rate Expansion",
        )
        slide(
            MathTex(
                r"\Rightarrow \mathbf{T} : \mathbf{L}^p - \dot{\psi} + \eta_r \dot{\theta} \geq 0",
                font_size=34,
            ),
            "Reduced Dissipation Inequality (Eq. 28)",
        )

        # Reference Configuration Transformations
        slide(
            MathTex(
                r"\tilde{\mathbf{T}} = \mathbf{R}^T \mathbf{T} \mathbf{R}", font_size=34
            ),
            "Pull Back Stress to Reference Config",
        )
        slide(
            MathTex(
                r"\mathbf{D} = \mathbf{R}^T \dot{\mathbf{E}}^e \mathbf{R}, \quad \mathbf{L}^p = \mathbf{R}^T \mathbf{L}^p \mathbf{R}",
                font_size=34,
            ),
            "Deformation Rates to Reference",
        )

        # General Form (S4)
        slide(
            MathTex(
                r"\dot{\mathbf{E}}^e = \hat{\mathbf{K}}(\tilde{\mathbf{T}},\theta,\mathbf{B},s) + \hat{\mathbf{A}}(\theta)\dot{\theta}",
                font_size=34,
            ),
            "General Stress–Strain Form",
        )
        slide(
            MathTex(
                r"\dot{\mathbf{B}} = \hat{\mathbf{H}}(\tilde{\mathbf{T}},\theta,\mathbf{B},s)",
                font_size=34,
            ),
            "Backstress Evolution",
        )
        slide(
            MathTex(
                r"\dot{s} = \hat{s}(\tau,\bar{\tau}_b,s,\theta,\bar{p})", font_size=34
            ),
            "Resistance Evolution",
        )

        # Define Invariants
        slide(
            MathTex(
                r"\tau = \left\{\tfrac{1}{2}\operatorname{tr}(\tilde{\mathbf{T}}'^2)\right\}^{1/2},\quad \bar{p} = -\tfrac{1}{3}\operatorname{tr}(\tilde{\mathbf{T}})",
                font_size=34,
            ),
            "Stress Invariants",
        )
        slide(
            MathTex(
                r"\bar{\tau}_b = \left\{\tfrac{1}{2}\operatorname{tr}(\mathbf{B}^2)\right\}^{1/2}",
                font_size=34,
            ),
            "Backstress Invariant",
        )

        # Polynomial Simplifications (S3)
        slide(
            MathTex(
                r"\mathbf{L}^p = x_1 \tilde{\mathbf{T}}' + \eta_1(\tilde{\mathbf{T}}'\mathbf{B} - \mathbf{B}\tilde{\mathbf{T}}')",
                font_size=34,
            ),
            "Flow Rule Simplified",
        )
        slide(
            MathTex(
                r"\dot{\mathbf{B}} = \xi_1 \tilde{\mathbf{T}}' + \xi_2 \mathbf{B}",
                font_size=34,
            ),
            "Backstress Simplified",
        )
        slide(
            MathTex(
                r"\dot{s} = h_0 \left|1 - \frac{s}{s^*}\right|^a \text{sign}(1 - \frac{s}{s^*}) \dot{\varepsilon}^p",
                font_size=32,
            ),
            "Resistance Evolution Polynomial",
        )
        slide(
            MathTex(
                r"s^* = \hat{s}\left(\frac{\dot{\varepsilon}^p}{A} e^{Q/RT}\right)^n",
                font_size=34,
            ),
            "Saturation Strength",
        )

        # Return to Current Configuration
        slide(
            MathTex(
                r"\mathbf{D} = \mathbf{R}\dot{\mathbf{E}}^e\mathbf{R}^T", font_size=34
            ),
            "Push Forward to Spatial Config",
        )

        # Final Model (Eqs. 77–86)
        slide(
            MathTex(
                r"\dot{\tilde{\mathbf{T}}} = \mathbb{L}[\mathbf{D} - \mathbf{D}^p] - \mathbf{\Pi} \dot{\theta}",
                font_size=34,
            ),
            "Stress Rate Equation (Eq. 77)",
        )
        slide(
            MathTex(
                r"\mathbf{D}^p = \dot{\bar{\varepsilon}}^p\left\{ \frac{\tilde{\mathbf{T}}'}{2\bar{\tau}} \right\}",
                font_size=34,
            ),
            "Flow Direction (Eq. 83)",
        )
        slide(
            MathTex(
                r"\dot{\bar{\varepsilon}}^p = A e^{-Q/RT} \left[ \sinh\left(\frac{\xi \sigma}{s}\right)\right]^m",
                font_size=34,
            ),
            "Strain Rate (Eq. 84)",
        )
        slide(
            MathTex(
                r"\dot{s} = h(\bar{\sigma},s,\theta) \dot{\bar{\varepsilon}}^p - r(s,\theta)",
                font_size=34,
            ),
            "Final Evolution Equation (Eq. 86)",
        )

        # Final Frame Zoom
        self.wait(2)
        self.play(self.camera.frame.animate.scale(1.1))
        self.wait(2)
