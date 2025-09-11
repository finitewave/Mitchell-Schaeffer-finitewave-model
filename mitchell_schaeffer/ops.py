"""
ops.py — mathematical core of the model.

This module provides functions to compute the model equations,
as well as functions to retrieve default parameters and initial
values for the state variables.

The Mitchell-Schaeffer model is a simplified cardiac cell model
designed to capture essential features of cardiac electrophysiology
with minimal complexity. It consists of a single membrane potential
variable and a gating variable that controls the inward current.

References
- Mitchell, C. C., & Schaeffer, D. G. (2003).
    A two-current model for the dynamics of cardiac membrane
    potential. Bulletin of Mathematical Biology, 65, 767–793.
        
DOI: https://doi.org/10.1016/S0092-8240(03)00041-7
"""

__all__ = (
    "get_variables",
    "get_parameters",
    "calc_rhs",
    "calc_dh",
    "calc_J_in",
    "calc_J_out"
)


def get_variables() -> dict[str, float]:
    """
    Returns default initial values for state variables.
    """
    return {"u": 0.0, "h": 1.0}


def get_parameters() -> dict[str, float]:
    """
    Returns default parameter values for the model.
    """
    return {"tau_close": 150.0, "tau_open": 120.0, "tau_out": 6.0,  "tau_in": 0.3, "u_gate": 0.13}


def calc_rhs(J_in , J_out) -> float:
    """
    Computes the right-hand side of the model.
    """
    return J_in + J_out


def calc_dh(h, u, tau_close, tau_open, u_gate):
    """
    Updates the gating variable h for the inward current.

    The gating variable h plays the role of a generic recovery mechanism.
    - It increases toward 1 with time constant tau_open when the membrane is at rest.
    - It decreases toward 0 with time constant tau_close when the membrane is excited.

    This mimics Na⁺ channel inactivation in a simplified way.

    Parameters
    ----------
    h : float
        Current value of the gating variable.
    u : float
        Membrane potential (dimensionless, in [0,1]).
    tau_close : float
        Inactivation time constant (closing).
    tau_open : float
        Recovery time constant (opening).
    u_gate : float
        Threshold potential for switching gate dynamics.

    Returns
    -------
    float
        Updated value of h.
    """
    h = (1.0 - h) / tau_open if u < u_gate else -h / tau_close
    return h


def calc_J_in(u, h, tau_in):
    """
    Computes the inward current responsible for depolarization.

    This is a regenerative current:
    J_in = h * u² * (1 - u) / tau_in

    It activates when h is high (available) and u is sufficiently depolarized.
    The form ensures that the current grows with u but shuts off when u ~ 1.

    Parameters
    ----------
    u : float
        Membrane potential (dimensionless).
    h : float
        Gating variable controlling channel availability.
    tau_in : float
        Time constant for inward flow.

    Returns
    -------
    float
        Value of the inward current.
    """
    C = (u**2)*(1-u)
    return h*C/tau_in

def calc_J_out(u, tau_out):
    """
    Computes the outward current responsible for repolarization.

    This linear term simulates the slow repolarizing current that restores 
    the membrane potential back to rest.

    J_out = -u / tau_out

    Parameters
    ----------
    u : float
        Membrane potential.
    tau_out : float
        Time constant for outward current (repolarization).

    Returns
    -------
    float
        Value of the outward current.
    """
    return -u/tau_out
