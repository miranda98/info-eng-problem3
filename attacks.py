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

def calculate_entropy(data):
    _, counts = np.unique(data, return_counts=True)
    probabilities = counts / len(data)
    return -np.sum(probabilities * np.log2(probabilities))

def LFSR_dynamic_entropy_attack(cipher, c, window_size):
    N = len(cipher)
    m = len(c)
    
    # Inicialización
    best_seed = None
    best_entropy_difference = float('inf')
    
    for possible_seed in range(2**m):
        # Generar la salida del LFSR con la semilla actual
        state = np.array([int(bit) for bit in format(possible_seed, f'0{m}b')])
        LFSR_output = np.zeros(N)
        
        for i in range(N):
            next_bit = np.mod(np.sum(c*state), 2)
            LFSR_output[i] = state[m-1]
            state = np.concatenate((np.array([next_bit]), state[0:m-1]))
        
        # Calcular la entropía dinámica
        dynamic_entropies = []
        for i in range(0, N, window_size):
            current_window = LFSR_output[i:i+window_size]
            dynamic_entropies.append(calculate_entropy(current_window))
        
        # Calcular la diferencia total de entropía
        entropy_difference = np.sum(np.abs(np.diff(dynamic_entropies)))
        
        # Actualizar si la diferencia es menor
        if entropy_difference < best_entropy_difference:
            best_entropy_difference = entropy_difference
            best_seed = possible_seed
    
    return best_seed

def freq_attack(cipher):
    """
    Analyse the frequency distribution of the ciphertext or intermediate values
    Look for biases or patterns that may be related to the key
    In LFSR, certain seeeds might produce patterns that are distinguishable in the ciphertext
    """
    # Calcular la frecuencia de cada bit en la secuencia cifrada
    bit_frequencies = np.bincount(cipher)

    # Encontrar el bit más frecuente (suponiendo que es la clave)
    most_frequent_bit = np.argmax(bit_frequencies)

    return most_frequent_bit

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

def short_cycle_attack(cipher, max_cycle_length):
    N = len(cipher)

    # Buscar repeticiones de ciclos cortos en la secuencia cifrada
    for cycle_length in range(1, max_cycle_length + 1):
        is_short_cycle = True
        for i in range(N - cycle_length):
            if cipher[i] != cipher[i + cycle_length]:
                is_short_cycle = False
                break
        if is_short_cycle:
            return cycle_length

    return None