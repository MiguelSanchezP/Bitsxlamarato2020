f = open ("./Files/COPEDICATClinicSympt_DATA_2020-12-17_1642.csv", 'r')

data = []
for line in f:
	data.append(line)

#covid and other illnesses:

COVID_vrs = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[131] == '1':
		COVID_vrs.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[131] == '1':
		COVID_vrs.append(value)

COVID_adeno = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[132] == '1':
		COVID_adeno.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[132] == '1':
		COVID_adeno.append(value)

COVID_fluA&B = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[133] == '1':
		COVID_fluA&B.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[133] == '1':
		COVID_fluA&B.append(value)
    elif value.split(',')[122] == '1' and value.split(',')[134] == '1':
		COVID_fluA&B.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[134] == '1':
		COVID_fluA&B.append(value)

#covid and other more generically:

COVID_resp_vir = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[142] == '1':
		COVID_resp_vir.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[142] == '1':
		COVID_resp_vir.append(value)

COVID_bacteria = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[145] == '1':
		COVID_bacteria.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[145] == '1':
		COVID_bacteria.append(value)

COVID_inflam_diseases = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[161] == '1':
		COVID_inflam_diseases.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[161] == '1':
		COVID_inflam_diseases.append(value)

COVID_&_vaccines = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[167] == '1':
		COVID_&_vaccines.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[167] == '1':
		COVID_&_vaccines.append(value)

#covid and pathologies:

COVID_comorbidities = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[148] == '1':
		COVID_comorbidities.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[148] == '1':
		COVID_comorbidities.append(value)

#covid and more specific conditions:

COVID_cardiopathy = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[149] == '1':
		COVID_cardiopathy.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[149] == '1':
		COVID_cardiopathy.append(value)

COVID_hypertension = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[150] == '1':
		COVID_hypertension.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[150] == '1':
		COVID_hypertension.append(value)

COVID_pulm_disease = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[151] == '1':
		COVID_pulm_disease.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[151] == '1':
		COVID_pulm_disease.append(value)

COVID_asthma = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[152] == '1':
		COVID_asthma.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[152] == '1':
		COVID_asthma.append(value)

COVID_nephrology = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[153] == '1':
		COVID_nephrology.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[153] == '1':
		COVID_nephrology.append(value)

COVID_hepB = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[154] == '1':
		COVID_hepB.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[154] == '1':
		COVID_hepB.append(value)

COVID_epilepsy = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[155] == '1':
		COVID_epilepsy.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[155] == '1':
		COVID_epilepsy.append(value)

COVID_diabetes = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[156] == '1':
		COVID_diabetes.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[156] == '1':
		COVID_diabetes.append(value)

COVID_tuberculosis = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[157] == '1':
		COVID_tuberculosis.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[157] == '1':
		COVID_tuberculosis.append(value)

COVID_immunodeficiency = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[158] == '1':
		COVID_immunodeficiency.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[158] == '1':
		COVID_immunodeficiency.append(value)

COVID_neoplasia = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[159] == '1':
		COVID_neoplasia.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[159] == '1':
		COVID_neoplasia.append(value)

COVID_kawasaki = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[160] == '1':
		COVID_kawasaki.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[160] == '1':
		COVID_kawasaki.append(value)

COVID_hiv = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[162] == '1':
		COVID_hiv.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[162] == '1':
		COVID_hiv.append(value)

COVID_obesity = []
for value in data:
    if value.split(',')[122] == '1' and value.split(',')[163] == '1':
		COVID_obesity.append(value)
    elif value.split(',')[127] == '1' and value.split(',')[163] == '1':
		COVID_obesity.append(value)
