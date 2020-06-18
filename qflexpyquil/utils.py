# Lint as: python3
"""
Provides pyQuil utils for qFlex.
"""

import numpy as np
import pyquil
import re


def ComputeSchmidtRank(gate):

	assert isintance(gate, pyquil.quilbase.Gate)

	n_qubits = len(gate.get_qubits())

    if n_qubits == 1:
        return 1
    elif n_qubits > 2:
        raise AssertionError("Not yet implemented.")

    V, S, W = np.linalg.svd(
        np.reshape(
            np.einsum('abcd->acbd', np.reshape(pyquil.simulation.tools.lifted_gate(gate, n_qubits),
                                               [2, 2, 2, 2])), [4, 4]))

    return sum(S != 0)