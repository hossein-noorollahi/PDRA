# Step 2: Generating Files for SwissADME
# Input: filtered_cp_above_90.csv
# Output: 'compounds.csv' and 'molecules_for_adme.txt'

df = pd.read_csv('filtered_cp_above_90.csv')
filtered_df = df[df['Score'] > 90]

# Extracting drug names list
drug_names = filtered_df['Name'].tolist()

def get_cid(name):
    """Fetch PubChem CID for the given compound name."""
    url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}/cids/JSON'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        cids = data.get('IdentifierList', {}).get('CID', [])
        if cids:
            return cids[0]
    return None

def get_smiles(cid):
    """Fetch SMILES notation for the given CID."""
    url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/ConnectivitySMILES/JSON'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        props = data.get('PropertyTable', {}).get('Properties', [])
        if props and 'ConnectivitySMILES' in props[0]:
            return props[0]['ConnectivitySMILES']
    return None

output = []            # List to store CSV data
output_for_adme = []   # List to store SwissADME text data

for name in drug_names:
    cid = get_cid(name)
    if cid:
        smiles = get_smiles(cid)
        if smiles:
            output.append([name, cid, smiles])
            output_for_adme.append(f"{smiles} {name}")
            print(f"✅ {name}: CID={cid}, SMILES found -> {smiles}")
        else:
            print(f"❌ {name}: SMILES not found for CID {cid}")
    else:
        print(f"❌ {name}: CID not found")
    time.sleep(0.2)  # Prevent request rate limits

# Save CSV file with compounds having SMILES
with open('compounds.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Compound Name', 'CID', 'SMILES Notation'])
    writer.writerows(output)

print("\nCSV file 'compounds.csv' created successfully with compounds that have SMILES.")

# Save text file formatted for SwissADME input
with open('molecules_for_adme.txt', 'w', encoding='utf-8') as f:
    for line in output_for_adme:
        f.write(line + "\n")

print("Text file 'molecules_for_adme.txt' created successfully for SwissADME input.")