#%%
###PRINT O MES DE ACORDO COM O NUMERO INPUTADO
month = input()


#%%
months_dict = { 
'1': 'January',
'2': 'February',
'3': 'March',
'4': 'April',
'5': 'May',
'6': 'June',
'7': 'July',
'8': 'August',
'9': 'September',
'10': 'October',
'11': 'November',
'12': 'December',
}

#%%
for i in months_dict:
    if month == i:
        print(months_dict[i])
# %%
