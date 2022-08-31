import os

folderPath = r'd:\ojk\labul kap juni 2022\r'
fileNumber = 859

for filename in os.listdir(folderPath):
    os.rename(folderPath + '\\' + filename, folderPath + '\\' + "labul_kap_bpr_" + str(fileNumber) + '.xlsx')
    fileNumber += 1