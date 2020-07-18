from covid import Covid
from pprint import pprint
covid=Covid()
# pprint(covid.get_data())
india_cases=covid.get_status_by_country_name('india')
print('Indian Cases',end='=')
pprint(india_cases)
print('indian_confirmed=',india_cases['confirmed'])

confirmed = covid.get_total_confirmed_cases()
print('confirmed_all_over_world=',confirmed)

recovered=covid.get_total_recovered()
print('recovered_all_over_world=',recovered)

Active=covid.get_total_active_cases()
print('Active_all_over_world=',Active)

deaths=covid.get_total_deaths()
print('Deaths_all_over_world=',deaths)