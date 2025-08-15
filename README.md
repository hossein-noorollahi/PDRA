# PDRA
Post Drug repurposing analysis utilizing ADME screening, toxicity predictions with Tox21, and QSAR modeling to evaluate absorption, distribution, metabolism, and excretion profiles, predict toxicities, and assess molecular activity. This streamlined workflow accelerates drug discovery while ensuring safety and efficacy.


Step-by-Step Explanation
Imported Libraries
	pandas: For reading and processing CSV files.
	requests: For making HTTP requests to PubChem API.
	csv: For writing CSV files.
	time: For adding delays between API requests.

Step 1: Filtering Data

- Read the input file export.csv.
- Filter rows based on the drug type (cp, kd, oe, cc) and scores above 90.
- Save the filtered data into separate CSV files:
	filtered_cp_above_90.csv for type cp.
	filtered_kd_above_90.csv for type kd.
	filtered_oe_above_90.csv for type oe.
	filtered_cc_above_90.csv for type cc.

Step 2: Fetching CID and SMILES

- Read the filtered file filtered_cp_above_90.csv.
- Extract the list of drug names.
- Use PubChem API to fetch the CID and SMILES notation for each drug:
	CID: Unique identifier for compounds in PubChem.
	SMILES: Chemical structure representation.
-Save two output files:
	compounds.csv: Includes drug name, CID, and SMILES notation.
	molecules_for_adme.txt: Contains SMILES formatted for SwissADME input.