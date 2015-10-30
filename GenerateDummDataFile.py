"""
This File regroup
python function for
data test generation
"""
import random
import itertools

def DummDataGeneration(nbOfPatient, dataType):
		
	LymphocyteBConcentration = ["No","Low","Normal","High"]
	LymphocyteTConcentration = ["No","Low","Normal","High"]
	NeutrophilsConcentration = ["No","Low","Normal","High"]
	BlastocyteConcentration = ["No","Low","Normal","High"]
	PhenotypeClassification = ["Sain", "PR", "Sclerodermie", "Unknown"]
	
	dataType = str(dataType)
	nbOfPatient = int(nbOfPatient) + 1
	for x in xrange(1,nbOfPatient):

		if dataType == "qual":
			LBC = LymphocyteBConcentration[random.randint(0,3)]
			LTC = LymphocyteTConcentration[random.randint(0,3)]
			NC = NeutrophilsConcentration[random.randint(0,3)]
			BC = BlastocyteConcentration[random.randint(0,3)]
			PC = PhenotypeClassification[random.randint(0,3)]
		else:
			LBC = random.randint(0,3)
			LTC = random.randint(0,3)
			NC = random.randint(0,3)
			BC = random.randint(0,3)
			PC = PhenotypeClassification[random.randint(0,3)]

		patientName = str(x) + "_VIRTUAL_DATA.dat"
		dataFile = open(patientName, "w")
		dataFile.write("LBC,"+str(LBC)+"\n")		
		dataFile.write("LTC,"+str(LTC)+"\n")
		dataFile.write("NC,"+str(NC)+"\n")
		dataFile.write("BC,"+str(BC)+"\n")
		dataFile.write("PC,"+str(PC)+"\n")
		dataFile.close()
			

def ConvertToBool(dataFilename):

	"""
	-> Read dataFilename
	-> Convert qualitative data into boolean (c.f tablea boolean)
	-> Write boolean data in a .bool file
	
	tableau bool:
	LBC-NO LBC-low LBC-Normal LBC-High LTC-NO LTC-low LTC-Normal LTC-High ... PC-Unknown	
	"""

	dataFilename = str(dataFilename)
	dataFileInArray = dataFilename.split(".")
	if len(dataFileInArray) > 0:

		dataAttributeToValue= {}
		dataAttributeToValue["LBC"] = "UNDEF"		
		dataAttributeToValue["LTC"] = "UNDEF" 
		dataAttributeToValue["NC"] = "UNDEF" 
		dataAttributeToValue["BC"] = "UNDEF" 
		dataAttributeToValue["PC"] = "UNDEF" 

		dataFile = open(dataFilename, "r")
		dataBoolFilename = str(dataFileInArray[0]) + ".bool"
		dataBoolFile = open(dataBoolFilename, "w")
		for line in dataFile:
			lineInArray = line.split(",")
			valueFromLine = lineInArray[1].split("\n")
			if lineInArray[0] == "LBC":
				dataAttributeToValue["LBC"] = valueFromLine[0]
			elif lineInArray[0] == "LTC":
				dataAttributeToValue["LTC"] = valueFromLine[0]
			elif lineInArray[0] == "NC":
				dataAttributeToValue["NC"] = valueFromLine[0]
			elif lineInArray[0] == "BC":
				dataAttributeToValue["BC"] = valueFromLine[0]
			elif lineInArray[0] == "PC":
				dataAttributeToValue["PC"] = valueFromLine[0]

		
		if dataAttributeToValue["LBC"] == "No":
			ValueOfLBC = "1 0 0 0 "
		elif dataAttributeToValue["LBC"] == "Low":
			ValueOfLBC = "0 1 0 0 "
		elif dataAttributeToValue["LBC"] == "Normal":
			ValueOfLBC = "0 0 1 0 "
		elif dataAttributeToValue["LBC"] == "High":
			ValueOfLBC = "0 0 0 1 "
		else:
			ValueOfLBC = "Undef "

		if dataAttributeToValue["LTC"] == "No":
			ValueOfLTC = "1 0 0 0 "
		elif dataAttributeToValue["LTC"] == "Low":
			ValueOfLTC = "0 1 0 0 "
		elif dataAttributeToValue["LTC"] == "Normal":
			ValueOfLTC = "0 0 1 0 "
		elif dataAttributeToValue["LTC"] == "High":
			ValueOfLTC = "0 0 0 1 "
		else:
			ValueOfLTC = "Undef "

		if dataAttributeToValue["NC"] == "No":
			ValueOfNC = "1 0 0 0 "
		elif dataAttributeToValue["NC"] == "Low":
			ValueOfNC = "0 1 0 0 "
		elif dataAttributeToValue["NC"] == "Normal":
			ValueOfNC = "0 0 1 0 "
		elif dataAttributeToValue["NC"] == "High":
			ValueOfNC = "0 0 0 1 "
		else:
			ValueOfNC = "Undef "
		
		if dataAttributeToValue["BC"] == "No":
			ValueOfBC = "1 0 0 0 "
		elif dataAttributeToValue["BC"] == "Low":
			ValueOfBC = "0 1 0 0 "
		elif dataAttributeToValue["BC"] == "Normal":
			ValueOfBC = "0 0 1 0 "
		elif dataAttributeToValue["BC"] == "High":
			ValueOfBC = "0 0 0 1 "
		else:
			ValueOfBC = "Undef "

		if dataAttributeToValue["PC"] == "Sain":
			ValueOfPC = "1 0 0 0"
		elif dataAttributeToValue["PC"] == "PR":
			ValueOfPC = "0 1 0 0"
		elif dataAttributeToValue["PC"] == "Sclerodermie":
			ValueOfPC = "0 0 1 0"
		elif dataAttributeToValue["PC"] == "Unknown":
			ValueOfPC = "0 0 0 1"
		else:
			ValueOfPC = "Undef "

		dataBoolFile.write(str(ValueOfLBC)+str(ValueOfLTC)+str(ValueOfNC)+str(ValueOfBC)+str(ValueOfPC)+"\n")

		dataBoolFile.close()
		dataFile.close()

	else:
		print "Error, can't parse filename\n"

		

def ConcatFiles(liste, outpout):

	"""
	-> Take a string of filenames separate with coma
	-> Take the name of the output file
	-> Concat the list of file in the input file
	"""

	filenames = liste.split(",")
	with open(str(outpout), 'w') as outfile:
    		for fname in filenames:
        		with open(fname) as infile:
            			for line in infile:
                			outfile.write(line)





def TranspoBoolFiles(filename):

	"""
	-> Take string filename as argument (must be .bool)
	-> Transposed data stored in input file
	-> write results in filename_transposed.bool file
	"""
	
	filename = str(filename)
	filenameInArray = filename.split(".")
	if filenameInArray[1] == "bool":
		inputFile = open(filename, "r")
		arrayOfLine = []
		arrayOfData = []
		for line in inputFile:
			lineWithoutBackN = line.split("\n")
			lineInArray = lineWithoutBackN[0].split(" ")
			for data in lineInArray:
				arrayOfData.append(data)				
			arrayOfLine.append(arrayOfData)
	
		inputFile.close()	
		dataTransposed = [list(x) for x in zip(*arrayOfLine)]
		outputfilename = str(filenameInArray[0]) + "_transposed.bool"
		outputFile = open(outputfilename, "w")
		for lines in dataTransposed:
			numberOfCol = len(lines)
			currentCol = 1
			for data in lines:
				outputFile.write(data)
				if currentCol < numberOfCol:
					outputFile.write(",")
				currentCol+=1
			outputFile.write("\n")

		outputFile.close()
	else:
		print "file format isn't bool\n"





def ExtractAssociationRules_save(cohorteFilename, minsup):
	
	minsup = int(minsup)
	cohorteFilename = str(cohorteFilename)
	cohorte = open(cohorteFilename, "r")
	cohorte.close()
	

	CardinalToEnsemble = {}
	CardinalToEnsemble[1] =["LBC-No","LBC-Low","LBC-Normal","LBC-High",
				"LTC-No","LTC-Low","LTC-Normal","LTC-High",
				"NC-No","NC-Low","NC-Normal","NC-High",
				"BC-No","BC-Low","BC-Normal","BC-High",
				"PC-Sain","PC-PR","PC-Sclerodermie","PC-Unknown"]
	


	CardinalToAssociatedFact = {}
	CardinalToAssociatedFact[1] = []
	CardinalToEnsembleToSupport = {}
	CardinalToEnsembleToSupport[1] =[{"LBC-No":0},{"LBC-Low":0},{"LBC-Normal":0},{"LBC-High":0},
					{"LTC-No":0},{"LTC-Low":0},{"LTC-Normal":0},{"LTC-High":0},
					{"NC-No":0},{"NC-Low":0},{"NC-Normal":0},{"NC-High":0},
					{"BC-No":0},{"BC-Low":0},{"BC-Normal":0},{"BC-High":0},
					{"PC-Sain":0},{"PC-PR":0},{"PC-Sclerodermie":0},{"PC-Unknown":0}]



	K = 1
	while(CardinalToEnsemble[K] != 0):
		"""
		for untransposed data
		i.e 1 patient = 1 line
		"""
		cohorte = open(cohorteFilename, "r")
		for patient in cohorte:
			patientWithoutBackN = patient.split("\n")
			patientInArray = patientWithoutBackN[0].split(" ")
			for indice in xrange(len(patientInArray)):
				if patientInArray[indice] == "1":
					attribut = CardinalToEnsembleToSupport[K][indice].keys()[0]
					CardinalToEnsembleToSupport[K][indice][attribut]+=1
					
		cohorte.close()
				
		for indice in xrange(len(CardinalToEnsembleToSupport[K])):
			attribut = CardinalToEnsembleToSupport[K][indice].keys()[0]
			if CardinalToEnsembleToSupport[K][indice][attribut] > minsup:
				CardinalToAssociatedFact[K].append(attribut) 		


		if K < len(CardinalToEnsemble.keys()):
			K+=1
		else:
			break
	
		
	"""
	To Do : Implement Fucking Apriori Generation
	"""	

	#print CardinalToEnsembleToSupport[1]
	print CardinalToAssociatedFact[1]





def ExtractEnsemble(cohorteFilename, minsup, mode):

	"""
	-> cohorte Filename is a file, .bool format, currently for untransposed data,
	i.e 1 patient = 1 line
	-> minsup is an int
	-> mode is a string, if equal "DEBUG" print TRACE in function, else : do nothing special
	-> return a list of associated observations

	[TODO]
	-> for transposed data
	"""


	minsup = int(minsup)
	cohorteFilename = str(cohorteFilename)
	cohorte = open(cohorteFilename, "r")
	cohorte.close()
	mode = str(mode)

	FinalAssociatedFact = []
	CardinalToEnsemble = {}
	listOfVariables = ["LBC-No","LBC-Low","LBC-Normal","LBC-High",
			   "LTC-No","LTC-Low","LTC-Normal","LTC-High",
			   "NC-No","NC-Low","NC-Normal","NC-High",
			   "BC-No","BC-Low","BC-Normal","BC-High",
			   "PC-Sain","PC-PR","PC-Sclerodermie","PC-Unknown"]

	CardinalToEnsemble[1] =[["LBC-No"],["LBC-Low"],["LBC-Normal"],["LBC-High"],
				["LTC-No"],["LTC-Low"],["LTC-Normal"],["LTC-High"],
				["NC-No"],["NC-Low"],["NC-Normal"],["NC-High"],
				["BC-No"],["BC-Low"],["BC-Normal"],["BC-High"],
				["PC-Sain"],["PC-PR"],["PC-Sclerodermie"],["PC-Unknown"]]


	CardinalToAssociatedFact = {}
	CardinalToEnsembleToSupport = {}
	CardinalToFrequentFact = {}


	"""
	Initialisation for K = 1
	"""
	K = 1
	CardinalToAssociatedFact[K] = []

	CardinalToEnsembleToSupport[K] =[{"LBC-No":0},{"LBC-Low":0},{"LBC-Normal":0},{"LBC-High":0},
					{"LTC-No":0},{"LTC-Low":0},{"LTC-Normal":0},{"LTC-High":0},
					{"NC-No":0},{"NC-Low":0},{"NC-Normal":0},{"NC-High":0},
					{"BC-No":0},{"BC-Low":0},{"BC-Normal":0},{"BC-High":0},
					{"PC-Sain":0},{"PC-PR":0},{"PC-Sclerodermie":0},{"PC-Unknown":0}]

	cohorte = open(cohorteFilename, "r")
	for patient in cohorte:
		patientWithoutBackN = patient.split("\n")
		patientInArray = patientWithoutBackN[0].split(" ")
		for indice in xrange(len(patientInArray)):
			if patientInArray[indice] == "1":
				attribut = CardinalToEnsembleToSupport[K][indice].keys()[0]
				CardinalToEnsembleToSupport[K][indice][attribut]+=1
	cohorte.close()


	# Test patient
	PatientToData = {}
	cohorte = open(cohorteFilename, "r")
	IdPatient =0
	for patient in cohorte:
		IdPatient+=1
		PatientToData[IdPatient] = []
		patientWithoutBackN = patient.split("\n")
		patientInArray = patientWithoutBackN[0].split(" ")
		for indice in xrange(len(patientInArray)):
			attribut = CardinalToEnsembleToSupport[1][indice].keys()[0]
			PatientToData[IdPatient].append({attribut:patientInArray[indice]})

	cohorte.close()


	while(len(CardinalToEnsemble[K]) != 0):

		"""
		for untransposed data
		i.e 1 patient = 1 line
		"""
		
		CardinalToAssociatedFact[K+1] = []
		CardinalToEnsemble[K+1] = []
		
		EnsembleToSupport = {}
		listOfEnsemble = []
		indexForEnsemble = 0

		if mode == "DEBUG":
			print "[TRACE1] => " + str(CardinalToEnsemble[K]) + "|" + str(K)

		for ensemble in CardinalToEnsemble[K]:
			listOfEnsemble.append(ensemble)
			EnsembleToSupport[indexForEnsemble] = 0
			for patient in PatientToData.keys():
				patientGotEnsemble = 1
				for element in ensemble:
					for compteur in xrange(len(listOfVariables)):
						variable = listOfVariables[compteur]
						if variable == element:
							indice = compteur
					if PatientToData[patient][indice][element] != str(1):
						patientGotEnsemble = 0
				if patientGotEnsemble == 1:
					EnsembleToSupport[indexForEnsemble] +=1			
			indexForEnsemble+=1

			if mode == "DEBUG":
				print "[TRACE2] => " + str( EnsembleToSupport) + "|" + str(K)


		for indexForEnsemble in xrange(len(listOfEnsemble)):
			if EnsembleToSupport[indexForEnsemble] >= minsup:
				if mode == "DEBUG":
					print "[TRACE3] => " + str(listOfEnsemble[indexForEnsemble]) + "|||" + str(EnsembleToSupport[indexForEnsemble]) + ">" + str(minsup) + "|" + str(K)
				CardinalToAssociatedFact[K].append(listOfEnsemble[indexForEnsemble])
				FinalAssociatedFact.append(listOfEnsemble[indexForEnsemble])

		if mode == "DEBUG":
			print "[TRACE4] => " + str(CardinalToAssociatedFact[K]) + "|" +str(K)	
	
	
		"""-------------------------
		|Apriori-Generation [START]|
		-------------------------"""
	
		ListOfCommunAssociation = []
		FlatListOfCommunAssociation = []
		for ensemble in CardinalToAssociatedFact[K]:
			tmpListOfParameter = []
			for element in ensemble:
				tmpListOfParameter.append(element)
				FlatListOfCommunAssociation.append(element)
				if mode == "DEBUG":
					print "[TRACE5] => " + str(element) + "|" +str(K)
			ListOfCommunAssociation.append(tmpListOfParameter)

		
		"""
		Applatir liste
		"""
		FlatListOfCommunAssociationWithoutDuplicates = []
		for parameter in FlatListOfCommunAssociation:
			if mode == "DEBUG":
				print "[TRACE6] => " + str(parameter) +"|" + str(FlatListOfCommunAssociationWithoutDuplicates) + "|" +str(K)
			if parameter not in FlatListOfCommunAssociationWithoutDuplicates:
				FlatListOfCommunAssociationWithoutDuplicates.append(parameter)

		"""
		Reformater liste applatie
		"""
		ListOfCommunFactsSingletons = []
		for parameter in FlatListOfCommunAssociationWithoutDuplicates:
			elementToAppend = []
			elementToAppend.append(parameter)
			ListOfCommunFactsSingletons.append(elementToAppend)
		
		if mode == "DEBUG":
			print "[TRACE7] => " + str(ListOfCommunFactsSingletons) + "|" +str(K)
			print "[TRACE8] => " + str(ListOfCommunAssociation) + "|" +str(K)
			print "[TRACE9] => " + str(FlatListOfCommunAssociationWithoutDuplicates) + "|" +str(K)		


		"""
		Generate Combination
		"""
		nextAssociatedFact = []
		TempNextAssociatedFact = []
		for p in itertools.combinations(ListOfCommunFactsSingletons,K+1):
			if mode == "DEBUG":
				print "[TRACE10] => " + str(p) + "|" + str(K)
			p = list(itertools.chain(*p))  # Pb when K >=2 : list applatie AND trop element
			#print "[TRACE5.5] => " + str(p) + "|" + str(K)
			
			"""
			Delete doublons
			"""
			attToCount = {}
			for att1 in p:
				attToCount[att1] = 0
			for att1 in p:
				for att2 in attToCount.keys():
					if att1 == att2:
						attToCount[att1]+=1
			pCanBeSave = 1
			for att1 in attToCount.keys():
				if attToCount[att1] >1:
					pCanBeSave = 0
			if pCanBeSave != 0:
				TempNextAssociatedFact.append(p)
				CardinalToEnsemble[K+1].append(p)
				if mode == "DEBUG":
					print "[TRACE11] => " + str(p) + "|" +str(K)

		
		"""-----------------------
		|Apriori-Generation [END]|
		-----------------------"""
		K+=1

	
	if mode == "DEBUG":
		print "[TRACE12] => TERMINATED"	

	return FinalAssociatedFact






def getDataTableFromBool(dataFilename):
	
	"""
	-> dataFilename is the name of data file
	-> write a new file .csv with header
	"""	

	dataFilename = str(dataFilename)
	dataFilenameInArray = dataFilename.split(".")
	header = "LBC-No,LBC-Low,LBC-Normal,LBC-High,LTC-No,LTC-Low,LTC-Normal,LTC-High,NC-No,NC-Low,NC-Normal,NC-High,BC-No,BC-Low,BC-Normal,BC-High,PC-Sain,PC-PR,PC-Sclerodermie,PC-Unknown\n"
	if dataFilenameInArray[1] == "bool":
		
		outputFilename = str(dataFilenameInArray[0])+ ".csv"				
		transformedData = open(outputFilename, "w")
		transformedData.write(header)
		dataToTransform = open(dataFilename, "r")
		for line in dataToTransform:
			lineToWrite = line.replace(" ", ",") 
			transformedData.write(lineToWrite)
		dataToTransform.close()
		transformedData.close()
	else:
		print "Can't create table of data from a non-bool file,\n-> Please check the extension of " + str(dataFilename)








def GenerateAssociationRules(EnsembleOfEnsembles, minsup, minconf):
	
	"""
	-> Generate Association Rules from list of ensemble
	-> [WORK IN PROGRESS]
	"""


	"""
	Extract support
	"""




	"""
	Generate rules
	"""
	for ensemble in EnsembleOfEnsembles:
		if len(ensemble) >= 2:
			m = 1
			tupleLen = 1
			HList = []
			while tupleLen < len(ensemble):
				for h in itertools.combinations(ensemble, tupleLen):
					h = list(h)
					HList.append(h)	
				tupleLen+=1
			while m <= len(ensemble):
				for h in HList:
					confiance = "todo"	
	
				m+=1






"""
Test Space
"""
"""
DummDataGeneration(10, "qual")
ConvertToBool("5_VIRTUAL_DATA.dat")
ConcatFiles("1_VIRTUAL_DATA.bool,2_VIRTUAL_DATA.bool,3_VIRTUAL_DATA.bool,4_VIRTUAL_DATA.bool,5_VIRTUAL_DATA.bool", "test.bool")
TranspoBoolFiles("test.bool")
"""

getDataTableFromBool("test_case3.bool")





ensemble = []
ensembleToSupport = {}
ensemble = ExtractEnsemble("test_case3.bool", 2, "normal")

print ensemble
print "-------------------------------------------------"
print ensembleToSupport

GenerateAssociationRules(ensemble, 4, 4)





"""
Stop = 0
while Stop == 0:
DummDataGeneration(10, "qual")
	ConvertToBool("1_VIRTUAL_DATA.dat")
	ConvertToBool("2_VIRTUAL_DATA.dat")
	ConvertToBool("3_VIRTUAL_DATA.dat")
	ConvertToBool("4_VIRTUAL_DATA.dat")
	ConvertToBool("5_VIRTUAL_DATA.dat")
	ConvertToBool("6_VIRTUAL_DATA.dat")
	ConvertToBool("7_VIRTUAL_DATA.dat")
	ConvertToBool("8_VIRTUAL_DATA.dat")
	ConvertToBool("9_VIRTUAL_DATA.dat")
	ConvertToBool("10_VIRTUAL_DATA.dat")
	listeOfInputFiles = "1_VIRTUAL_DATA.bool,2_VIRTUAL_DATA.bool,3_VIRTUAL_DATA.bool,4_VIRTUAL_DATA.bool,5_VIRTUAL_DATA.bool,6_VIRTUAL_DATA.bool,7_VIRTUAL_DATA.bool,8_VIRTUAL_DATA.bool,9_VIRTUAL_DATA.bool,10_VIRTUAL_DATA.bool"
	ConcatFiles(listeOfInputFiles, "test.bool")
	TranspoBoolFiles("test.bool")
	getDataTableFromBool("test.bool")
	result = ExtractAssociationRules("test.bool", 3)
	for liste in result:
		if len(liste) > 3:
			Stop = 1
			break
		else:
			print "[MINOR RESULT] => " +str(len(liste)) + "||" +str(result) + "||"


print "[RESULT] => " +str(result)

"""



"""
***************************************
		WorkSpace
***************************************
"""






"""
TestList = [["A"],["B"],["C"],["D"]]
TestList2 = ["B","C","D"]
TestList3 = [["B"],["C"],["D"]]
TestList4 = [["B","C"],["B","D"],["C","D"]]
TestList5 = [["B","D"]]
ListOfCardinal = []
nextAssociatedFact = []
TempNextAssociatedFact = []

for elt in TestList:
	ListOfCardinal.append(len(elt))
K = max(ListOfCardinal)

K = 2
"""



"""
Generate Combination
"""

"""
for p in itertools.combinations(list(itertools.chain(*TestList)),K+1):
	p = list(itertools.chain(*p))
	attToCount = {}
	for att1 in p:
		attToCount[att1] = 0
	for att1 in p:
		for att2 in attToCount.keys():
			if att1 == att2:
				attToCount[att1]+=1

	pCanBeSave = 1
	for att1 in attToCount.keys():
		if attToCount[att1] >1:
			pCanBeSave = 0
	
	if pCanBeSave != 0:
		TempNextAssociatedFact.append(p)	


"""
"""
double Check the list
"""
"""
listeOfAssociationToGo = {}
indiceForAssoDict=0	
for listeOfAssociation1 in TempNextAssociatedFact:
	if indiceForAssoDict == 0:
		nextAssociatedFact.append(listeOfAssociation1)
	indiceForAssoDict+=1
	for listeOfAssociation2 in TempNextAssociatedFact:
		ListOfMatch = set(listeOfAssociation1) & set(listeOfAssociation2)
		ListeOfMatch = list(ListOfMatch)
		if len(ListeOfMatch) == K+1:
			listeOfAssociationToGo[indiceForAssoDict] = "NoGo"
		else:
			listeOfAssociationToGo[indiceForAssoDict] = "Go"

for indiceAsso in listeOfAssociationToGo.keys():
	if listeOfAssociationToGo[indiceAsso] == "Go":
		nextAssociatedFact.append(TempNextAssociatedFact[indiceAsso-1])	


print nextAssociatedFact
"""

