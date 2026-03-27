!pip install qiskit-aer
!pip install qiskit

# Importiamo le librerie necessarie da Qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# 1. Creiamo un circuito quantistico con 2 qubit e 2 bit classici
# I qubit sono i sistemi quantistici su cui operiamo.
# I bit classici sono usati per memorizzare i risultati delle misurazioni.
qc = QuantumCircuit(2, 2)

# 2. Applichiamo una porta Hadamard (H) al primo qubit (qubit 0).
# La porta H crea una sovrapposizione: se il qubit era |0>, ora è in uno stato di uguale probabilità di essere |0> o |1>.
qc.h(0)

# 3. Applichiamo una porta CNOT (CX) con il qubit 0 come controllo e il qubit 1 come target.
# La porta CNOT flip il target qubit se il controllo è |1>. Insieme alla porta H, questo crea entanglement.
# Se il qubit 0 è |0>, il qubit 1 rimane |0>. Se il qubit 0 è |1>, il qubit 1 diventa |1>.
# Questo crea lo stato di Bell: (1/sqrt(2)) * (|00> + |11>)
qc.cx(0, 1)

# 4. Misuriamo entrambi i qubit e li mappiamo sui rispettivi bit classici.
# Misuriamo il qubit 0 e il suo risultato va nel bit classico 0.
# Misuriamo il qubit 1 e il suo risultato va nel bit classico 1.
qc.measure([0, 1], [0, 1])

# Visualizziamo il circuito per capire le operazioni che stiamo eseguendo
print("Visualizzazione del Circuito Quantistico:")
print(qc.draw(output='text'))

# 5. Scegliamo un simulatore locale (AerSimulator è un simulatore ad alte prestazioni di Qiskit)
simulator = AerSimulator()

# Compiliamo il circuito per il simulatore scelto. Questo ottimizza il circuito per l'hardware target.
compiled_circuit = transpile(qc, simulator)

# Eseguiamo il circuito sul simulatore per un certo numero di 'shots' (ripetizioni).
# Un numero elevato di shots ci dà una stima più precisa delle probabilità.
job = simulator.run(compiled_circuit, shots=1024)

# Otteniamo i risultati del lavoro di simulazione
result = job.result()

# Otteniamo i conteggi delle misurazioni (quante volte è stato misurato ogni stato)
counts = result.get_counts(qc)

# 6. Visualizziamo i risultati come un istogramma
print("Risultati delle misurazioni (counts):")
print(counts)

# Plotting dell'istogramma dei risultati
fig = plot_histogram(counts)
display(fig)
