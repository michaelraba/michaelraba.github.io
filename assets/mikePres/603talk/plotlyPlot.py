import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Material parameters for 62Sn36Pb2Ag (Wang's Table 1)
A = 2.24e8  # 1/s
Q_R = 11200  # K
j = 13
m = 0.21
h0 = 1.62e10  # Pa
s0 = 8.47e7  # Pa
s_hat = 8.47e7  # Pa
n = 0.0277
alpha = 1.7
E = 5.2e10  # Pa

# Simulation setup
strain_rate_total = 1e-5  # 1/s
max_strain = 0.6
max_time = max_strain / strain_rate_total
t_eval = np.linspace(0, max_time, 10000)

# Temperatures
T_C_list = [-55, -25, 25, 75, 125]
T_K_list = [T_C + 273.15 for T_C in T_C_list]


# ODE system
def odes_gradual(t, y, T, strain_rate_total):
    ep_p, s = y
    eps_total = strain_rate_total * t
    sigma_trial = E * (eps_total - ep_p)
    s_safe = max(s, 1e5)
    x = j * sigma_trial / s_safe

    if abs(x) < 0.01:
        sinh_term = x
    else:
        sinh_term = np.sinh(np.clip(x, -30, 30))

    sinh_term = np.maximum(sinh_term, 1e-12)
    dep_p = A * np.exp(-Q_R / T) * np.exp((1 / m) * np.log(sinh_term))
    dep_p = max(dep_p, 1e-12)
    s_star = s_hat * (dep_p / A * np.exp(Q_R / T)) ** n

    ds = (
        h0 * np.abs(1 - s_safe / s_star) ** alpha * np.sign(1 - s_safe / s_star) * dep_p
    )

    return [dep_p, ds]


# Plotting
plt.figure(figsize=(10, 6))
for idx, (T_val, T_C) in enumerate(zip(T_K_list, T_C_list)):
    sol = solve_ivp(
        odes_gradual,
        (0, max_time),
        [0, s0],
        args=(T_val, strain_rate_total),
        t_eval=t_eval,
        method="Radau",
        rtol=1e-6,
        atol=1e-9,
    )

    ep_p_vals = sol.y[0]
    eps_total = strain_rate_total * sol.t
    sigma_vals = E * (eps_total - ep_p_vals)

    plt.plot(eps_total, sigma_vals / 1e6, label=f"{T_C}°C")  # Stress in MPa

plt.xlabel("Inelastic Strain ε (dimensionless)")
plt.ylabel("Stress σ (MPa)")
plt.title("Stress vs Inelastic Strain - 62Sn36Pb2Ag Alloy (Low Strain Rate 1e-5 1/s)")
plt.legend(title="Temperature")
plt.grid(True)
plt.tight_layout()
plt.savefig("stress_vs_strain_62Sn36Pb2Ag.png")  # Save output for Org Mode
plt.show()
