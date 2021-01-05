times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico', 'São Paulo', 'Internacional',
         'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético', 'Fluminense',
         'Botafogo', 'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')

print('='*15)
print(f'Cinco primeiros colocados: {times[:5]}')
print('='*15)
print(f'Quatro últimos colocados: {times[16:]}')
print('='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('='*15)
#for cont in range(0, len(times)):
#    if times[cont] == 'Chapecoense':
#        print(f'Posição da Chapecoense: {cont+1}º')
print(f'A Chapecoense está na {times.index("Chapecoense")+1}º posição!')
