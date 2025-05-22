# Conversões e dados iniciais
tempo_min = 42 + 42 / 60  # tempo total em minutos
tempo_horas = tempo_min / 60  # tempo total em horas
distancia_km = 10
km_por_milha = 1.61
distancia_milhas = distancia_km / km_por_milha  # converter km para milhas

# Cálculo do passo médio (tempo por milha)
passo_medio_min = tempo_min / distancia_milhas
minutos_passo = int(passo_medio_min)
segundos_passo = int((passo_medio_min - minutos_passo) * 60)

# Cálculo da velocidade média em milhas por hora
velocidade_media_mph = distancia_milhas / tempo_horas

# Exibição dos resultados
print(f"Passo médio: {minutos_passo} minutos e {segundos_passo} segundos por milha")
print(f"Velocidade média: {velocidade_media_mph:.2f} milhas por hora")