import matplotlib.pyplot as plt
import numpy as np

def check_for_symptoms (patients, symptoms, plot):
	symptoms_data = []
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
		data = [symptom, patient_with_symptom, patient_without_symptom, patient_undetermined]
		symptoms_data.append(data)
		if plot:
			plot_data = [patient_with_symptom, patient_without_symptom, patient_undetermined]
			plot_labels = ["Positive", "Negative", "Undetermined"]
			plt.pie (plot_data, labels=plot_labels)
			plt.title (symptom)
	if plot:
		plt.show()
	return symptoms_data


def compare(ppd, npd, plot, min_difference):
	normalized_ppd = []
	normalized_npd = []
	conditions = []
	positive_ppd = []
	positive_npd = []
	negative_ppd = []
	negative_npd = []
	for value in ppd:
		normalized_ppd.append([value[0], value[1]/(value[1]+value[2]), value[2]/(value[1]+value[2]), value[3]])
		conditions.append(value[0])
		positive_ppd.append(value[1]/(value[1]+value[2]))
		negative_ppd.append(value[2]/(value[1]+value[2]))
	for value in npd:
		normalized_npd.append([value[0], value[1]/(value[1]+value[2]), value[2]/(value[1]+value[2]), value[3]])
		positive_npd.append(value[1]/(value[1]+value[2]))
		negative_npd.append(value[2]/(value[1]+value[2]))
	differences = []
	for i in range (len(positive_ppd)):
		differences.append(positive_ppd[i]-positive_npd[i])

	for i in range (len(differences)):
		if (positive_ppd[i]+positive_npd[i]) > 0:
			differences[i] = differences[i]/(positive_ppd[i] + positive_npd[i])
		else:
			differences[i] = 0
		if abs(differences[i]) > min_difference/100:
			print (conditions[i] + " has a difference of " + str(differences[i]))

	if plot:
		fig,ax = plt.subplots(2)
		x = np.arange(len(conditions))
		plt.title("Relation between Covid and non covid symptomatology")
		ax[0].set_title("COVID Results")
		ax[0].bar(x, positive_ppd, width=0.35)
		ax[0].bar(x+0.35, negative_ppd, width=0.35)
		ax[0].set_ylim([0,1])
		ax[1].set_title("NON-COVID Results")
		ax[1].bar(x, positive_npd, width=0.35)
		ax[1].bar(x+0.35, negative_npd, width=0.35)
		ax[1].set_ylim([0,1])

		plt.setp(ax[1], xticks=x, xticklabels=conditions)
		plt.setp(ax[1].get_xticklabels(), rotation=90)
		plt.setp(ax[0], xticks=x, xticklabels=conditions)

		for a in fig.get_axes():
			a.label_outer()
#		fig.tight_layout()

		fig2,ax2 = plt.subplots()
		x = np.arange(len(differences))
		plt.title("Difference between COVID and non-COVID symptoms")
		plt.stem (x, differences, use_line_collection=True)
		plt.xticks(np.arange(len(differences)), conditions, rotation=90)
#		fig2.tight_layout()
		plt.show()


def check_for_multiple_symptoms (patients, symptoms_raw, plot):
	symptoms = symptoms_raw.split(',')
	symptoms_values = []
	result = [0, 0, 0]
	for symptom in symptoms:
		symptoms_values.append(int(symptoms_general[1][symptoms_general[0].index(symptom)]))
	for patient in patients:
		has_symptoms = True
		is_undetermined = False
		for i in symptoms_values:
			if patient.split(',')[i] == symptoms_general[3][symptoms_general[0].index(symptoms[symptoms_values.index(i)])]:
				has_symptoms = False
			elif not patient.split(',')[i] == symptoms_general[2][symptoms_general[0].index(symptoms[symptoms_values.index(i)])] and not patient.split(',')[i] == symptoms_general[3][symptoms_general[0].index(symptoms[symptoms_values.index(i)])]:
				is_undetermined = True
		if has_symptoms and not is_undetermined:
			result[0] += 1
		elif not has_symptoms and not is_undetermined:
			result[1] += 1
		else:
			result[2] += 1
	if plot:
		plt.title ("Presence of " + symptoms_raw)
		plt_labels = ["Presence", "Absence", "Undetermined"]
		plt.pie(result, labels=plt_labels)
		plt.show()


f = open ("./Files/COPEDICATClinicSympt_DATA_2020-12-17_1642.csv", 'r')

data = []
for line in f:
	data.append(line)

patients_COVID_Positive = []
patients_COVID_Negative = []

for value in data:
	if value.split(',')[31] == '1' and (value.split(',')[117] == '1' or value.split(',')[122] == '1'):
		patients_COVID_Positive.append(value)
	elif value.split(',')[31] == '1' and (value.split(',')[117] == '2' and value.split(',')[122] == '2'):
		patients_COVID_Negative.append(value)

symptoms_general = [["Fever", "Cough", "Dysphonia", "Dyspnea", "Tachypnea", "Alterated Respiratory Auscultation",
		     "Odynophagia", "Nasal Congestion", "Fatigue", "Headache", "Conjuntivitis", "Retro-ocular Pain",
		     "Gastrointestinal Symptoms", "Skin Signs", "Lymphadenopathy", "Hepatomegaly", "Splenomegaly",
		     "Hemorrhagies", "Irritability", "Neurologic Manifestations", "Shock", "Taste Alteration",
		     "Smell Alteration"],
		    ["33", "38", "42", "44", "46", "48", "52", "54", "56", "58", "60", "62", "64", "69", "74", "76",
		     "78", "80", "82", "84", "91", "93", "95"],
		    ['1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
		     '1', '1', '1', '1'],
		    ['2', '2', '2', '2', '2', '1', '2', '2', '2', '2', '2', '2', '0', '0', '2', '2', '2', '2', '2',
		     '0', '0', '0', '0']]

#check_for_symptoms(patients_COVID_Positive, "Cough", True)
positive_patients_data = check_for_symptoms(patients_COVID_Positive, "Fever,Cough,Dysphonia,Dyspnea,Tachypnea,Alterated Respiratory Auscultation,Odynophagia,Nasal Congestion,Fatigue,Headache,Conjuntivitis,Retro-ocular Pain,Gastrointestinal Symptoms,Skin Signs,Lymphadenopathy,Hepatomegaly,Splenomegaly,Hemorrhagies,Irritability,Neurologic Manifestations,Shock,Taste Alteration,Smell Alteration", False)
negative_patients_data = check_for_symptoms(patients_COVID_Negative, "Fever,Cough,Dysphonia,Dyspnea,Tachypnea,Alterated Respiratory Auscultation,Odynophagia,Nasal Congestion,Fatigue,Headache,Conjuntivitis,Retro-ocular Pain,Gastrointestinal Symptoms,Skin Signs,Lymphadenopathy,Hepatomegaly,Splenomegaly,Hemorrhagies,Irritability,Neurologic Manifestations,Shock,Taste Alteration,Smell Alteration", False)
compare (positive_patients_data, negative_patients_data, True, 1)
mult_positive_patients_data = check_for_multiple_symptoms (patients_COVID_Positive, "Fever,Cough", False)
mult_negative_patients_data = check_for_multiple_symptoms (patients_COVID_Negative, "Fever,Cough", False)
