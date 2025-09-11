## Mitchell-Schaeffer Finitewave model

This is a phenomenological two-variable model capturing the essence of cardiac 
action potential dynamics using a simplified formulation. It separates inward and 
outward currents and uses a single gating variable to regulate excitability.

This model implementation can be used separately from the Finitewave, allowing for standalone simulations and testing of the model dynamics without the need for the entire framework.

### Reference
Mitchell, C. C., & Schaeffer, D. G. (2003). A two-current model for the dynamics of cardiac membrane potential. 
Bulletin of Mathematical Biology, 65, 767–793.

DOI: https://doi.org/10.1016/S0092-8240(03)00041-7

### How to use (quickstart)
```bash
python -m examples.mitchell_schaeffer_example
```

### How to test
```bash
python -m pytest -q
```

### Repository structure
```text
.
├── mitchell_schaeffer/               # equations package (ops.py)
│   ├── __init__.py
│   └── ops.py                        # fill with the model equations (pure functions)
├── implementation/                   # 0D model implementation
│   ├── __init__.py
│   └── mitchell_schaeffer_0d.py
├── example/
│   └── mitchell_schaeffer_example.py # minimal script to run a short trace
├── tests/
│   └── mitchell_schaeffer_test.py    # smoke test; extend with reproducibility checks
├── .gitignore
├── LICENSE                           # MIT
├── pyproject.toml                    # placeholders to replace
└── README.md                         # this file
```

### Variables
- `u` — Transmembrane potential (dimensionless)
- `h` — Gating variable (dimensionless)

### Parameters
Parameters and their defualt values
- `tau_close = 150.0` - Inactivation time constant (closing).
- `tau_open = 120.0`  - Recovery time constant (opening).
- `tau_out = 6.0`     - Time constant for outward current (repolarization)
- `tau_in = 0.3`      - Time constant for inward flow.
- `u_gate = 0.13`     - Threshold potential for switching gate dynamics.

