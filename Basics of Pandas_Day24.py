#PANDAS
import pandas as pd


# Series -- 1D
# 1. INTRINSIC INDEX VALUES:
'''Team = pd.Series(['Ruturaj Gaikwad',
                  'MS Dhoni',
                  'Sanju Samson',
                  'Shivam Dube',
                  'Devon Conway',
                  'Daryl Mitchell',
                  'Matheesha Pathirana'])

print('******************************')
print('Team Players:')
print(Team)
print('******************************')
print('\nType:',type(Team))'''




'''Vintage_Cars = pd.Series(['Rolls-Royce Phantom II',
                          'Hindustan Ambassador',
                          'Premier Padmini',
                          'Hindustan Contessa',
                          'Standard Herald',
                          'Jaguar Mark 2',
                          'Jaguar XK150',
                          'Willys Jeep'])

print('******************************')
print('Top Vintage Cars:')
print(Vintage_Cars)
print('******************************')
print('\nType:',type(Vintage_Cars))'''





#2. EXTRINSIC INDEX VALUES:

'''Team = pd.Series([7,31,11,25,8,88], index =[ 'MS Dhoni', 'Ruturaj Gaikwad', 'Sanju Samson', 'Shivam Dube',
                                             'Ravindra Jadeja', 'Devon Conway'])

print('******************************')
print('Team Players:')
print(Team)
print('******************************')'''




'''Score = pd.Series([75,31,58,25,18,38], index =[ 'MS Dhoni', 'Ruturaj Gaikwad', 'Sanju Samson', 'Shivam Dube',
                                             'Ravindra Jadeja', 'Devon Conway'])

print('******************************')
print('Team Score:')
print(Score)
print('******************************')'''



#3. Data Filtering:
'''Players = pd.Series(['MS Dhoni', 'Ruturaj Gaikwad',
                     'Sanju Samson', 'Shivam Dube',
                     'Ravindra Jadeja',
                     'Devon Convey','Rachin Ravindra',
                     'Daryl Mitchell','Matheesha Pathirana',
                     'Maheesh Theekshana'],
                    index =[ 'IND', 'IND', 'IND', 'IND',
                             'IND', 'NZ','NZ', 'NZ','SL',
                             'SL'])

print('******************************')
print('Team Players:')
print(Players)

print('INDIAN Players:', Players['IND'])
print('NEW ZEALAND Players:', Players['NZ'])
print('SRILANKA Players:', Players['SL'])
print('******************************')'''







#4.Series from Dictionary:
'''Players = pd.Series({'MS Dhoni':105, 'Ruturaj Gaikwad':78, 'Sanju Samson':102, 'Shivam Dube':25,
                     'Ravindra Jadeja':7, 'Convey':18,'Rachin Ravindra':0, 'Daryl Mitchell':40})

print('******************************')
print('Team Players:')
print(Players)
print('******************************')'''




























                                                       
                            

