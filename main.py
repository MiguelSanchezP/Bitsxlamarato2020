import matplotlib.pyplot as plt

def check_for_symptoms (patients, symptoms):
	for symptom in symptoms.split(','):
		patient_with_symptom = 0
		patient_without_symptom = 0
		patient_undetermined = 0
		for patient in patients:
			if patient.split(',')[int(symptoms_general[1][symptoms_general[0].index(symptom)])] == symptoms_general[2][symptoms_general[0].index(symptom)]:
				patient_with_symptom += 1
			elif patient.split(',')[int(symptoms_general[1][symptoms_general[0].index(symptom)])] == symptoms_general[3][symptoms_general[0].index(symptom)]:
				patient_without_symptom += 1
			else:
				patient_undetermined += 1
		plot_data = [patient_with_symptom, patient_without_symptom, patient_undetermined]
		plot_labels = ["Positive", "Negative", "Undetermined"]
		plt.pie (plot_data, labels=plot_labels)
		plt.title (symptom)
	plt.show()


f = open ("./Files/COPEDICATClinicSympt_DATA_2020-12-17_1642.csv", 'r')

data = []
for line in f:
	data.append(line)

patients_COVID_Positive = []

for value in data:
	if value.split(',')[122] == '1' or value.split(',')[127] == '1':
		patients_COVID_Positive.append(value)


symptoms_general = [["Fever", "Cough", "Dysphonia", "Dyspnea", "Tachypnea", "Alterated Respiratory Auscultation",
		     "Odynophagia", "Nasal Congestion", "Fatigue", "Headache", "Conjuntivitis", "Retro-ocular Pain",
		     "Gastrointestinal Symptoms", "Skin Signs", "Lymphadenopathy", "Hepatomegaly", "Splenomegaly",
		     "Hemorragies", "Irritability", "Neurologic Manifestations", "Shock", "Taste Alteration",
		     "Smell Alteration"],
		    ["38", "43", "47", "49", "51", "53", "57", "59", "61", "63", "65", "67", "69", "74", "79", "81",
		     "83", "85", "87", "89", "96", "98", "100"],
		    ['1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
		     '1', '1', '1', '1'],
		    ['2', '2', '2', '2', '2', '1', '2', '2', '2', '2', '2', '2', '0', '0', '2', '2', '2', '2', '2',
		     '0', '0', '0', '0']]

check_for_symptoms(patients_COVID_Positive, "Fever")
