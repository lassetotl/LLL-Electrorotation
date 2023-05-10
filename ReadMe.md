## LagLivLab Electrorotation group

Hello :) Here we've uploaded some python scripts and data used in our electrorotation project at LagLivLab.

## File descriptions:

### BV2_WT_KO_Electrorotation_V23.ipynb

Jupyter notebook containing our analysis of our BV-2 cell type data (WT and KO variants), from experiments in 2023. See this notebook for examples of how to use the 'Rotation_Spectra()' function.

### BV2_WT_march_2023.npy

Numpy array containing 117 points of rpm data from three rotation experiments with BV2 WT cells and corresponding field frequencies the data was measured at. Import into python script like this:

*rpm_WT, freq_WT = np.load('BV2_WT_march_2023.npy', allow_pickle=True)*

### BV2_KO_abcd12_may_2023.npy

Numpy array containing 168 points of rpm data from four rotation experiments with BV2 KO abcd12 cells and corresponding field frequencies the data was measured at. Import into python script like this:

*rpm_KO, freq_KO = np.load('BV2_KO_abcd12_may_2023.npy', allow_pickle=True)*

### HeLa Rotation LLL.ipynb

Jupyter notebook containing the data and analysis of the initial HeLa rotation experiments performed by us 2022-2023. The aim of the HeLa experiments were to prove that our experimental setup gave reproducible results (https://wiki.uio.no/mn/fysikk/laglivlab/index.php/15.02.23). Slightly outdated script.

### Rotation_Spectra.py

Python script containing the function we use to approximate and visualize rotation curves from a set of data.
