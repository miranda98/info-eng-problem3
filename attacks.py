import itertools
import numpy as np

def brute_force():
    all_possible_seeds = np.array(list(itertools.product([0, 1], repeat=16)))
    # Exclude the all-zero seed
    valid_seeds = all_possible_seeds[np.any(all_possible_seeds, axis=1)]
    return valid_seeds

    # There are 65535 seeds
    # TODO: Decrypt with each seed, and compare decrypted
    # value with encrypted value (NOT original image, but the COMPRESSED image)

def known_plaintxt(plain, cipher):
    # TODO
    """
    Use pair os known plaintext and ciphertext to derive relationships between the seed and the output
    Find patterns or biases that might be related to the key
    """
    pass

def freq_analysis(cipher):
    # TODO
    """
    Analyse the frequency distribution of the ciphertext or intermediate values
    Look for biases or patterns that may be related to the key
    In LFSR, certain seeeds might produce patterns that are distinguishable in the ciphertext
    """
    pass

def correlation_analysis():
    # TODO
    """
    Find statistical relationships between the key and the ciphertext
    """
    pass

def fault_injection():
    # TODO
    """
    Introduce faults into the system to observe changes in the encrypted output.
    Analyse the system's response to these faults to gain insights into the key or seed.
    """
    pass