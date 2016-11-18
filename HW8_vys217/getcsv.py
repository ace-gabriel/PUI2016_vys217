import os

def getCSV():
    '''The function downloads a CSV file into the PUIDATA directory 
    Author: vys217 lifting code from 
    https://github.com/fedhere/PUI2016_fb55/blob/master/HW3_fb55/citibikes_gender.ipynb
    '''
    ### First I will check that it is not already there
    if not os.path.isfile(os.getenv("PUIDATA") + "/"+ "erm2-nwe9"):
        os.system("cp /projects/open/NYCOpenData/nycopendata/data/erm2-nwe9/1446832678/erm2-nwe9 " 
                  + os.getenv("PUIDATA"))
                    
    if not os.path.isfile(os.getenv("PUIDATA") + "/" + "erm2-nwe9"):
        print ("WARNING!!! something is wrong: the file is not there!")

    else:
        print ("file in place, you can continue")