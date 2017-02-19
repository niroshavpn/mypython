
import pandas as pd
import numpy as np
import datetime
data = pd.read_csv("/Users/suresh/Documents/test.csv")
data['Grade'] = np.where(data['Marks']>=70, 'First_Class', 'Second_Class')
lavanya =data[data['Name']=='lavanya']
print(lavanya.head())

data.to_csv('/Users/suresh/Documents/out.csv')
#data['Grade']=data[data.Marks>70]
#data['Grade']= data.Grade.apply(lambda x: x in data['Marks'] and data['Grade']=='A' if (x>70) else data['Grade']=='B')
#print(data)





