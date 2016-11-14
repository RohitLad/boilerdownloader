# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import glob, re, unicodedata, os




def makeMOS(errfile):       
    #mosfilename = fil[:-5] + '.mos'
    mosfilename=''
    temp=[]
    stringset = [B299740.company,B299740.model,str(int(float(B299740.Pnom)))]
    for string in stringset:       
        temp = ''.join(e for e in string if e.isalnum())
        mosfilename = mosfilename + temp+'_'
    mosfilename = mosfilename[:-1]+'kW'
    mosfilename = strip_accents(mosfilename)    
    print mosfilename
    
    
    if not os.path.exists('mos/'+mosfilename+'.mo'):
        datafile1 = open('mos/'+mosfilename+'.mo','w+')
        datafile = open('mos/singletext.mo','a+')
        
        try:
            datafile.write('record '+mosfilename+'\n')
            datafile.write('   extends Zugabe.Zugabe_DB.CondensingBoiler.CondensingBoilerdatadef(\n\n\n')
            datafile.write('    ///file: '+fil+'\n\n')
            datafile.write('    PCSI='+B299740.PCSI+' "Ratio gross (high) heating value / net (low) heating value defined according to the fuel ",\n\n')
            datafile.write('    Tnom= 273.15+' + B299740.Tnom + '  "Nominal temperature (K)",\n\n')
            datafile.write('    PLRnom= '+ B299740.PLRnom + '  "Nominal Loading Rate (%)",\n\n')
            datafile.write('    Pnom= '+B299740.Pnom+ '*1000 "Nominal power (W)",\n\n')
            datafile.write('    etaNom='+B299740.etaNom+'*1000 "Nominal net heating value efficiency (W)",\n\n')
            datafile.write('    TInt=273.15+' +B299740.TInt+ ' "Intermediate temperature (K)",\n\n')
            datafile.write('    PLRInt=' +B299740.PLRInt+ ' "Intermediate loading rate (%)",\n\n')
            datafile.write('    PInt=' + B299740.PInt+'*1000 "Intermediate power(W)",\n\n')
            datafile.write('    etaInt=' + B299740.etaInt+' "Intermediate net heating value efficiency (%)",\n\n')
            datafile.write('    PertesT30K ='+B299740.PertesT30K+' "Stop losses (W)",\n\n')
            datafile.write('    V_flow=' +B299740.V_flow+ '/3600 "Volume of water in the boiler (m3/s)",\n\n')
            datafile.write('    Veau(displayUnit="l") =' +B299740.Veau+ ' "Volume d\'eau contenue dans la chaudiere (litre)",\n\n')
            datafile.write('    mSec = '+ B299740.mSec+' "Dry weight (kg)",\n\n')
            datafile.write('    Paux = '+B299740.Paux+' "Electrical power of auxiliary on nominal power (out circulation pump) (W)",\n\n')
            datafile.write('    Pveille = '+B299740.Pveille+' "Standby power (out circulation pump) (W)",\n\n')
            datafile.write('    Pcirculateur = '+B299740.Pcirculateur+' "Water circulation pump electrical power (W)");\n\n')
            datafile.write('end '+mosfilename+';\n\n\n')
            
            datafile1.write('record '+mosfilename+'\n')
            datafile1.write('   extends Zugabe.Zugabe_DB.CondensingBoiler.CondensingBoilerdatadef(\n\n\n')
            datafile1.write('    ///file: '+fil+'\n\n')
            datafile1.write('    PCSI='+B299740.PCSI+' "Ratio gross (high) heating value / net (low) heating value defined according to the fuel ",\n\n')
            datafile1.write('    Tnom= 273.15+' + B299740.Tnom + '  "Nominal temperature (K)",\n\n')
            datafile1.write('    PLRnom= '+ B299740.PLRnom + '  "Nominal Loading Rate (%)",\n\n')
            datafile1.write('    Pnom= '+B299740.Pnom+ '*1000 "Nominal power (W)",\n\n')
            datafile1.write('    etaNom='+B299740.etaNom+'*1000 "Nominal net heating value efficiency (W)",\n\n')
            datafile1.write('    TInt=273.15+' +B299740.TInt+ ' "Intermediate temperature (K)",\n\n')
            datafile1.write('    PLRInt=' +B299740.PLRInt+ ' "Intermediate loading rate (%)",\n\n')
            datafile1.write('    PInt=' + B299740.PInt+'*1000 "Intermediate power(W)",\n\n')
            datafile1.write('    etaInt=' + B299740.etaInt+' "Intermediate net heating value efficiency (%)",\n\n')
            datafile1.write('    PertesT30K ='+B299740.PertesT30K+' "Stop losses (W)",\n\n')
            datafile1.write('    V_flow=' +B299740.V_flow+ '/3600 "Volume of water in the boiler (m3/s)",\n\n')
            datafile1.write('    Veau(displayUnit="l") =' +B299740.Veau+ ' "Volume d\'eau contenue dans la chaudiere (litre)",\n\n')
            datafile1.write('    mSec = '+ B299740.mSec+' "Dry weight (kg)",\n\n')
            datafile1.write('    Paux = '+B299740.Paux+' "Electrical power of auxiliary on nominal power (out circulation pump) (W)",\n\n')
            datafile1.write('    Pveille = '+B299740.Pveille+' "Standby power (out circulation pump) (W)",\n\n')
            datafile1.write('    Pcirculateur = '+B299740.Pcirculateur+' "Water circulation pump electrical power (W)");\n\n')
            datafile1.write('end '+mosfilename+';\n\n\n')
                    
        except:
            print "check error in file: "+ mosfilename
            
            errfile.write(fil[:-5]+', \n')
        
            datafile.close()
            datafile1.close()
            
class Boiler(object):
        
    def __init__(self, BoilerType,Fuel,Pnom,etaNom,PInt,etaInt,PertesT30K,Tnom,Paux,Pveille,Pcirculateur,mSec,Veau,V_flow,PLRInt,TInt,PLRnom,company,model):
        self.BoilerType = BoilerType
        self.Fuel = Fuel
        self.Pnom = Pnom
        self.etaNom = etaNom
        self.PInt = PInt
        self.etaInt = etaInt
        self.PertesT30K = PertesT30K
        self.Tnom = Tnom
        self.V_flow = V_flow
        self.Paux = Paux
        self.Pveille = Pveille
        self.Veau = Veau
        self.PLRInt = str(30)
        self.Pcirculateur = Pcirculateur
        self.mSec = mSec       
        self.PLRnom = str(100)
        self.PCSI = str(1.11)
        self.TInt = str(33)
        self.company = company
        self.model = model
            
def floatchk(sth):
    try:
        float(sth)
        return True
    except:
        return False
        

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)if unicodedata.category(c) != 'Mn')
        
#######SEARCH FOR FILES#######

files = glob.glob("*.html")
errfile = open('mos/errorfile.txt','w+')
######## LOOP OVER FILES#####
for fil in files:

    ######### CHECK FOR STUFF########
    soup = BeautifulSoup(open(fil),"html.parser") 
    try:
        check = soup.find_all('div', {'class':"grid-item col-md-12 metaclass-tab-18", 'data-metaclassid':"18"})
        check1 = check[0].find_all('td',{'':''})
        check2 = soup.find_all('table', {'class':"table table-condensed", 'data-setid':"224"})
        check3 = check2[0].find_all('td',{'':''})
        check4 = soup.find_all('section', {'class':"col-xs-12", 'id':"base-infos"})

    except:
        print 'No '+fil+' \n\n '
        continue
    
    ####INIT VARIABLE########
    B299740 = Boiler('NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA')

    
    #aa = soup.body.find_all(text = re.compile('Puissance utile'))
    #print aa[0].findNext()
    try:
        B299740.BoilerType = check[0].find_all(text = re.compile('selon'))[0].findNext().get_text()
        B299740.Fuel = check[0].find_all(text = re.compile('Type de combustible'))[0].findNext().get_text()
        B299740.Pnom = check[0].find_all(text = re.compile('Puissance utile nominale: Pn_gen'))[0].findNext().get_text()[:-3]
        if not floatchk(B299740.Pnom):
            continue
        B299740.etaInt = check[0].find_all(text = re.compile('diaire: Rpint'))[0].findNext().get_text()[:-2]
        if not floatchk(B299740.etaInt):
            continue
        B299740.PInt = check[0].find_all(text = re.compile('diaire: Pint'))[0].findNext().get_text()[:-3]
        if not floatchk(B299740.PInt):
            continue
        B299740.etaNom = check[0].find_all(text = re.compile('la puissance nominale: RPn'))[0].findNext().get_text()[:-2]
        if not floatchk(B299740.etaNom):
            continue
        B299740.PertesT30K = check[0].find_all(text = re.compile('delta T30K QP030'))[0].findNext().get_text()[:-2]
        if not floatchk(B299740.PertesT30K):
            continue
        B299740.Tnom = check[0].find_all(text = re.compile('moyenne de fonctionnement: T fonct_max'))[0].findNext().get_text()[:-3]
        if not floatchk(B299740.Tnom):
            continue
        B299740.Paux = check[0].find_all(text = re.compile('la puissance nominale Pn_gen'))[0].findNext().get_text()[:-2]
        if not floatchk(B299740.Paux):
            continue
        B299740.Pveille = check[0].find_all(text = re.compile('Qveille Puissance des auxiliaires en veille'))[0].findNext().get_text()[:-2]
        if not floatchk(B299740.Pveille):
            continue
        B299740.Veau = check[0].find_all(text = re.compile('Contenance totale en eau Chaudi'))[0].findNext().get_text()[:-2]
        if not floatchk(B299740.Veau) or  float(B299740.Veau) == 0.0:
            continue
        B299740.V_flow = check[0].find_all(text = re.compile('bit nominal d'))[0].findNext().get_text()[:-4]
        if not floatchk(B299740.V_flow) or  float(B299740.V_flow) == 0.0:
            continue
        B299740.Pcirculateur = check[0].find_all(text = re.compile('moyenne du circulateur'))[0].findNext().get_text()[:-2]
        if not floatchk(B299740.Pcirculateur):
            continue        
        B299740.mSec = check3[0].find_all(text = re.compile('Poids Brut'))[0].findNext().get_text()[:-3]
        if not floatchk(B299740.mSec) or  float(B299740.mSec) == 0.0:
            continue
        B299740.company = check4[0].find_all(text = re.compile('Marque commerciale'))[0].findNext().get_text()
        B299740.model = check4[0].find_all(text = re.compile('Gamme:'))[0].findNext().get_text()   
        makeMOS(errfile)
    except:
        print 'No MAN!!   '+fil+'\n\n'

    
    

errfile.close()
        

        
