""" 
CONSTANTE = 'Variaveis' que não vão mudar muitas condições no mesmo if (ruim)
    < -  Contafem de complexidade(ruim)
"""

velocidade = 61 #velocidade atual do carro
local_carro = 100 #local em que o carro esta na estrada

RADAR_1 = 60 #velocidade maxima do radar 1 
LOCAL_1 = 100 # local onde esta o radar 1
RADAR_RANGE = 1 # A distancia onde o radar paga 

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('velocidade do carro passou o limite permitido')
    
if carro_passou_radar_1:
    print('Carro passou no radar 1')
    
if carro_multado_radar1:
    print('Veiculo foi multado!')
