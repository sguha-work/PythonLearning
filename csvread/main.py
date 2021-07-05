import numpy as np

def ifExist(list, dataToSearch):
    numpyList = np.array(list)
    x = numpyList.where(dataToSearch)
    return len(x[0])

def main(fileName):
    subjectNumberList = ['027','028','029','030','037','039','041', '042','043','044','048','052','054','055','064','066','083','105','265','283','301','302']
    subjectNameList = ['027-HISTORY','028-POLITICAL SCIENCE', '029-GEOGRAPHY', '030-ECONOMICS', '037-PSYCOLOGY', '039-SOCIOLOGY', '041-MATHEMATICS','042-PHYSICS', '043-CHEMISTRY', '044-BIOLOGY', '048-PHYSICAL EDUCATION', '052-APP-COMMARCIAL ART', '054-BUSINESS STUDIES', '055-ACCOUNTANCY','064-HOME SCIENCE', '066-ENTREPRENEURSHIP', '083-COMPUTER SCIENCE (NEW)', '105-BENGALI', '265-INFORMATICS PRAC.(OLD)', '283-COMPUTER SCIENCE (OLD)', '301-ENGLISH CORE', '302- HINDI CORE']
    index = 0
    for subjectNumber in subjectNumberList:
        mainCSVFile = open(fileName, 'r')
        linesFromMainFile = mainCSVFile.readlines()
        outputFileName = 'output/'+subjectNameList[index]+'.csv'
        outputFile = open(outputFileName, 'w')
        linesToWrite = ['S.NO.,ROLL NO.,NAME,SUB1,TH MARKS,30% COMP\n']
        count = 0
        for individualLine in linesFromMainFile:
            splitedLine = individualLine.split(',')
            serialNumber = splitedLine[0]
            rollNo = splitedLine[1]
            name = splitedLine[2]
            if splitedLine[3] == subjectNumber:
                count = count+1
                line = serialNumber+','+str(rollNo)+','+name+','+splitedLine[3]+','+splitedLine[4]+','+splitedLine[5]+'\n'
                linesToWrite.append(line)
            if splitedLine[6] == subjectNumber:
                count = count + 1
                line = serialNumber + ',' + str(rollNo) + ',' + name + ',' + splitedLine[6] + ',' + splitedLine[7] + ',' + \
                       splitedLine[8] + '\n'
                linesToWrite.append(line)
            if splitedLine[9] == subjectNumber:
                count = count + 1
                line = serialNumber + ',' + str(rollNo) + ',' + name + ',' + splitedLine[9] + ',' + splitedLine[10] + ',' + \
                       splitedLine[11] + '\n'
                linesToWrite.append(line)
            if splitedLine[12] == subjectNumber:
                count = count + 1
                line = serialNumber + ',' + str(rollNo) + ',' + name + ',' + splitedLine[12] + ',' + splitedLine[13] + ',' + \
                       splitedLine[14] + '\n'
                linesToWrite.append(line)
            if splitedLine[15] == subjectNumber:
                count = count + 1
                line = serialNumber + ',' + str(rollNo) + ',' + name + ',' + splitedLine[15] + ',' + splitedLine[16] + ',' + \
                       splitedLine[17] + '\n'
                linesToWrite.append(line)
            if splitedLine[18] == subjectNumber:
                count = count + 1
                line = serialNumber + ',' + str(rollNo) + ',' + name + ',' + splitedLine[18] + ',' + splitedLine[19] + ',' + \
                       splitedLine[20] + '\n'
                linesToWrite.append(line)
        mainCSVFile.close()
        outputFile.writelines(linesToWrite)
        outputFile.close()
        index += 1

main('CLASS XI UPLOAD LIST.xlsx - Sheet1.csv')