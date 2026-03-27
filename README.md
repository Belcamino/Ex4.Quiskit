# Ex4.quiskit
Il codice Python seguente mostra come utilizzare la libreria qiskit  per creare uno stato di Bell, un esempio fondamentale di entanglement quantistico tra due qubit. 
Preliminarmente con i comandi seguenti si installano le librerie necessarie:
pip install qiskit-aer
pip install qiskit
Uno stato di Bell, come abbiamo visto in Qubit, può essere uno dei quattro stati massimamente entangled: qui creeremo lo stato 1/√2(|00⟩+|11⟩). Per farlo basterà creare un circuito quantistico con due qubit e due bit classici; applicando la porta di Hadamard (H) al primo qubit, questo è messo in uno stato di sovrapposizione 1/√2(|0⟩+|1⟩). Poi applichiamo una porta CNOT con il qubit 0 come controllo e il qubit 1 come target: se il qubit 0 è |0>, il qubit 1 rimane |0>, mentre se il qubit 0 è |1>, il qubit 1 diventa |1>; in questo modo i due qubit risultano entangled. 
Il sistema composto dalle due porte crea, quindi lo stato di Bell richiesto. Poi eseguiamo la misura di entrambi i qubit, mappiamo i risultati sui bit classici e ci aspettiamo di vedere solo i risultati '00' e '11', ciascuno con circa il 50% di probabilità, ed è esattamente quel che succede nella simulazione.
