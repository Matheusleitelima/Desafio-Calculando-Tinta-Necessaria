
# 🖌️ Desafio com Funções: Calculando Tinta Necessária

## 📄 Descrição

Este programa calcula a quantidade de tinta necessária para pintar uma parede. Ele solicita informações do usuário sobre o rendimento da tinta, a altura e a largura da parede, e calcula quantas latas de tinta serão necessárias.

## 🔹 Entradas

O usuário deve informar:  
- **Rendimento da tinta:** m² por litro  
- **Altura da parede:** em metros  
- **Largura da parede:** em metros  

## 🔹 Processamento

1. **Calcular a área da parede:**  
   ```text
   Área = Altura × Largura
   ```

2. **Determinar a quantidade de tinta necessária (em litros):**  
   ```text
   Litros_necessarios = Área / Rendimento
   ```

3. **Arredondar a quantidade para cima:**  
   Uma lata de tinta completa é necessária, mesmo que só uma fração seja usada.

## 🔹 Saída

O programa exibirá a mensagem:  
```text
Você necessita de X latas de tinta
```
onde `X` é o número de latas calculadas.

## 🔹 Exemplo de Teste

- **Rendimento da tinta:** 5 m² por litro  
- **Altura da parede:** 3 metros  
- **Largura da parede:** 4 metros  

**Cálculo:**
1. Área = 3 × 4 = 12 m²  
2. Litros necessários = 12 / 5 = 2,4  
3. Latas necessárias = 3 (arredondando para cima)  

**Saída esperada:**  
```text
Você necessita de 3 latas de tinta
```

## 🔹 Observações

- Recomenda-se criar uma **função** que receba os parâmetros e retorne a quantidade de latas.  
- Essa abordagem facilita reutilização do código e futuras alterações, como incluir múltiplas paredes ou diferentes rendimentos.
