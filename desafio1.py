#%%
##CONFERIR SE A QUANTIDADE DE CARACTERES QUE O USUARIO DIGITOU É MAIOR OU IGUAL AO PERMITIDO

T = input()
max = 'A'*140

#%%
len(max)
len(T)
#%%
if len(T) <= len(max):
    print('TWEET')
else:
    print('MUTE')
# %%
