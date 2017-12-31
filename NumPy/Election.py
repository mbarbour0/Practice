import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

survey_array = np.array(survey_responses)

total_ceballos = np.sum(survey_array == 'Ceballos')
survey_count = np.sum(survey_array != '')
percentage_ceballos = np.mean(survey_array == 'Ceballos')

possible_surveys = np.random.binomial(70, 0.54, size = 10000)/70.0
large_surveys = np.random.binomial(7000, 0.54, size = 10000)/7000.0

plt.hist(possible_surveys, bins = 20, range = (0,1), histtype='step')
plt.hist(large_surveys, bins = 20, range = (0,1), histtype='step')
plt.show()

ceballos_loss_surveys = np.mean(possible_surveys < 0.5)

ceballos_loss_new = np.mean(large_surveys < 0.50)

print ceballos_loss_new