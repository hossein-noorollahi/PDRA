# PDRA
**Post Drug Repurposing Analysis utilizing ADME screening, toxicity predictions with Tox21, and QSAR modeling to evaluate absorption, distribution, metabolism, and excretion profiles, predict toxicities, and assess molecular activity. This streamlined workflow accelerates drug discovery while ensuring safety and efficacy.**

## Step-by-Step Explanation
**This script is designed to streamline the process of filtering drug repurposing results and preparing molecular data for SwissADME analysis.**

### Imported Libraries
- **pandas:** For reading and processing CSV files.
- **requests:** For making HTTP requests to the PubChem API.
- **csv:** For writing CSV files.
- **time:** For adding delays between API requests.

### Step 1: Filtering Data
1. **Read the Input File:** Load the data from `export.csv`.
2. **Filter Rows:** Filter the rows based on the drug type (`cp`, `kd`, `oe`, `cc`) and scores above 90.
3. **Save Filtered Data:** Save the filtered data into separate CSV files:
   - `filtered_cp_above_90.csv` for drug type `cp`.
   - `filtered_kd_above_90.csv` for drug type `kd`.
   - `filtered_oe_above_90.csv` for drug type `oe`.
   - `filtered_cc_above_90.csv` for drug type `cc`.

### Step 2: Fetching CID and SMILES
1. **Read the Filtered File:** Load the filtered data from `filtered_cp_above_90.csv`.
2. **Extract Drug Names:** Create a list of drug names from the filtered data.
3. **Fetch CID and SMILES:**
   - Use the PubChem API to obtain the CID (unique identifier) for each drug name.
   - Use the CID to retrieve the SMILES (chemical structure representation) from PubChem.
4. **Save Output Files:**
   - `compounds.csv`: Contains drug name, CID, and SMILES notation.
   - `molecules_for_adme.txt`: Contains SMILES formatted for SwissADME input.

So far, the codes for Steps 1 and 2 have been implemented following the Drug Repurposing analysis, preparing the data for pharmacokinetic and toxicity evaluations of the identified candidate drugs. Additionally, the clustering of results and identification of significant drug groups using unsupervised learning methods have been addressed. 

In the upcoming phases, we will focus on QSAR evaluations using a wide range of machine learning and deep learning algorithms, along with a comparison of the results. Therefore, this is merely a preliminary stage for preparing the data for subsequent analyses.

The complete codes and explanations for the remaining steps, including the pharmacokinetic evaluation of candidate repurposed drugs and toxicity assessment based on the Tox21 dataset, will be added soon. This will also encompass clustering the results using unsupervised learning methods such as KMeans and Hierarchical Clustering. Furthermore, we will implement Quantitative Structure-Activity Relationship (QSAR) modeling using machine learning techniques like Random Forest, Logistic Regression, Support Vector Machine (SVM), and Gradient Boosting. Additionally, a comparison of the results with a Deep Neural Network approach will be included. Stay tuned for these updates!