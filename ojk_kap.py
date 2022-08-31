from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import csv

data = pd.read_csv('d:/ojk/list_nama_ulang.csv')

x = '000000'
# z = 'BPK-901-000001' #neraca
z = 'BPK-901-000003' #kap
b = []
ulang = []

for name in data['Nama BPR_x']:
  names = {
      'nama': name.replace(" ", "+")
  }
  b.append(names)

# for c in range(len(b)):
for c in range(2,len(b)):    
  print('Download count :', c,' of', len(b))
  print('Number of ulang :', len(ulang))
  y = b[c]['nama']
  url_neraca = f'https://cfs.ojk.go.id/cfs/ReportViewerForm.aspx?BankCodeNumber={x}&BankCode={y}&Month=6&Year=2022&FinancialReportPeriodTypeCode=R&FinancialReportTypeCode={z}' 
  print(url_neraca)
  driver = webdriver.Chrome(ChromeDriverManager().install())
  try:
    driver.get(url_neraca)
    time.sleep(3)
    driver.find_element(by=By.XPATH, value='//*[@id="CFSReportViewer_ctl05_ctl05_ctl00_ctl00"]/table/tbody/tr/td/input').click()
    time.sleep(12)
    driver.find_element(by=By.XPATH, value='.//*[@id="CFSReportViewer_ctl05_ctl04_ctl00_ButtonImg"]').click()
    time.sleep(3)
    driver.find_element(by=By.XPATH, value='//*[@id="CFSReportViewer_ctl05_ctl04_ctl00_Menu"]/div[1]/a').click()
    time.sleep(12)
  except:
    bpr = {
        'nama':url_neraca
    }
    ulang.append(bpr)
    continue

df1 = pd.DataFrame(ulang)
df1.to_csv('d:/ojk/bpr_ulang_kap_4.csv')          