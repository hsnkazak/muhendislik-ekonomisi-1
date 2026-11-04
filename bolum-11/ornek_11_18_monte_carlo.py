import sys
import numpy as np

# Kullanılan sürümler
print("Python:", sys.version.split()[0])
print("NumPy:", np.__version__)

# Beş yıllık temel proje verileri
Q = np.array([168, 176, 183, 189, 194], dtype=float) * 1_000
P = np.array([950, 1000, 1050, 1103, 1158], dtype=float)

raw_material = np.array(
    [360, 378, 397, 417, 438],
    dtype=float
)

energy_use = np.array(
    [4.00, 3.90, 3.85, 3.80, 3.75],
    dtype=float
)

energy_price = np.array(
    [4.00, 4.40, 4.80, 5.20, 5.60],
    dtype=float
)

labor_hours = np.array(
    [0.300, 0.285, 0.275, 0.268, 0.262],
    dtype=float
)

hourly_wage = np.array(
    [220, 235, 251, 268, 286],
    dtype=float
)

maintenance = np.array(
    [5.0, 5.6, 6.3, 7.1, 8.0],
    dtype=float
) * 1_000_000

other_costs = np.array(
    [8.0, 8.5, 9.0, 9.5, 10.0],
    dtype=float
) * 1_000_000

delta_nis = np.array(
    [2.5, 1.8, 1.4, 1.0, -16.7],
    dtype=float
) * 1_000_000

after_tax_salvage = np.array(
    [0, 0, 0, 0, 11.25],
    dtype=float
) * 1_000_000

initial_investment = 200_000_000
initial_nis = 10_000_000
tax_rate = 0.25
discount_rate = 0.18

discount_factor = (
    1 + discount_rate
) ** np.arange(1, 6)

# Şok sırası:
# Q, P, hammadde, enerji fiyatı, bakım, sabit yatırım
std = np.array(
    [0.10, 0.07, 0.10, 0.15, 0.12, 0.08]
)

def simulate(rho_qp, n_sim=100_000, seed=42):

    corr = np.eye(6)

    corr[0, 1] = corr[1, 0] = rho_qp
    corr[1, 2] = corr[2, 1] = 0.50
    corr[2, 3] = corr[3, 2] = 0.40
    corr[0, 4] = corr[4, 0] = 0.30

    cov = np.outer(std, std) * corr

    rng = np.random.default_rng(seed)

    shocks = rng.multivariate_normal(
        mean=np.zeros(6),
        cov=cov,
        size=n_sim
    )

    Q_sim = Q[None, :] * (
        1 + shocks[:, 0, None]
    )

    P_sim = P[None, :] * (
        1 + shocks[:, 1, None]
    )

    raw_sim = raw_material[None, :] * (
        1 + shocks[:, 2, None]
    )

    energy_price_sim = energy_price[None, :] * (
        1 + shocks[:, 3, None]
    )

    maintenance_sim = maintenance[None, :] * (
        1 + shocks[:, 4, None]
    )

    investment_sim = initial_investment * (
        1 + shocks[:, 5]
    )

    depreciation = investment_sim / 5

    revenue = Q_sim * P_sim

    operating_cost = (
        Q_sim * raw_sim
        + Q_sim
        * energy_use[None, :]
        * energy_price_sim
        + Q_sim
        * labor_hours[None, :]
        * hourly_wage[None, :]
        + maintenance_sim
        + other_costs[None, :]
    )

    fna = (
        revenue
        - operating_cost
        - depreciation[:, None]
    ) * (1 - tax_rate) + depreciation[:, None]

    nna = (
        fna
        - delta_nis[None, :]
        + after_tax_salvage[None, :]
    )

    npv = (
        -investment_sim
        - initial_nis
        + np.sum(
            nna / discount_factor[None, :],
            axis=1
        )
    )

    return npv / 1_000_000


def report(npv):
    print(
        "Ortalama NBD:",
        round(np.mean(npv), 2)
    )
    print(
        "Medyan NBD:",
        round(np.median(npv), 2)
    )
    print(
        "%5 yüzdelik:",
        round(np.quantile(npv, 0.05), 2)
    )
    print(
        "%95 yüzdelik:",
        round(np.quantile(npv, 0.95), 2)
    )
    print(
        "P(NBD > 0):",
        round(100 * np.mean(npv > 0), 1),
        "%"
    )


# Temel simülasyon
npv_base = simulate(rho_qp=-0.40)
report(npv_base)

# Karşılaştırma:
# satış fiyatı ile miktar korelasyonu sıfır
npv_zero_corr = simulate(rho_qp=0.00)
report(npv_zero_corr)
