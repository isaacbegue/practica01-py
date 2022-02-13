import pandas as pd

excelData = pd.read_excel('E:\Documentos\ebc-python\practica01-py\sample-xls-file-for-testing.xls')
dataFrame = pd.DataFrame(excelData)
print(dataFrame)