## Contexto e Objetivo

A análise de movimento humano a partir de vídeo em tempo real é uma área crescente, especialmente no contexto de saúde e fitness. Este projeto tem como objetivo desenvolver um sistema que utilize a tecnologia MediaPipe Pose para detetar a pose de um praticante de exercício físico e, a partir disso, contar o número de agachamentos (squats) e flexões (push-ups) realizados. O sistema deverá reconhecer as poses típicas desses exercícios e incrementar contagens de forma automática, auxiliando em treinos e avaliações de desempenho.

## Cenário de Utilização Exemplo

Imagine um utilizador a realizar uma sessão de treino caseiro, posicionado em frente a uma câmara. O sistema analisa em tempo real a pose do utilizador, detetando quando ele se agacha e se levanta, ou quando realiza uma flexão completa. Ao final da sessão, o sistema apresenta o número total de agachamentos e flexões, ajudando o utilizador a acompanhar a sua evolução sem necessitar de um avaliador humano.

## Requisitos Funcionais

- **Deteção de Pose com MediaPipe Pose:**  
  - Configurar e utilizar a biblioteca MediaPipe Pose para obter landmarks corporais a partir de frames de vídeo.
  - Extrair informações da posição das articulações relevantes (por exemplo, joelhos, ancas para agachamentos; cotovelos, ombros para flexões).

- **Lógica de Contagem:**  
  - Definir critérios para considerar um agachamento como completo (ex: ângulo do joelho abaixo de um certo limiar e depois retorno à posição inicial).  
  - Definir critérios para considerar uma flexão completa (ex: ângulo do cotovelo reduzido até um certo ponto e depois retornando à extensão).  
  - Incrementar contadores de cada tipo de exercício conforme os movimentos sejam concluídos.

## Requisitos Não Funcionais

- **Desempenho em Tempo Real:**  
  O sistema deve ser capaz de processar frames de vídeo a uma taxa razoável, permitindo feedback quase imediato durante o exercício.

- **Robustez e Precisão:**  
  O sistema não precisa ser perfeito, mas deve ser suficientemente robusto para lidar com pequenas variações posturais, iluminação e ângulos de câmara.

- **Simplicidade do Código e Comentários:**  
  O código deve ser organizado, comentado e fácil de entender, dado que é um projeto para estudantes com pouca experiência prática.

## Tecnologias e Ferramentas (Recomendadas)

- **Linguagem:** Python, pela facilidade de integração com MediaPipe.
- **MediaPipe Pose:** Biblioteca principal para extração de landmarks do corpo.  
- **OpenCV (opcional):** Para leitura de frames da câmara e exibição do resultado.  
- **NumPy (opcional):** Para cálculos numéricos e manipulação de dados.

## Etapas Sugeridas para o Desenvolvimento

1. **Configuração do Ambiente:**  
   - Instalar Python e MediaPipe Pose.  
   - Verificar documentação do MediaPipe Pose: [MediaPipe Pose Documentation](https://developers.google.com/mediapipe/solutions/pose).

2. **Leitura de Vídeo e Deteção de Pose:**  
   - Capturar frames da câmara ou de um vídeo.  
   - Processar cada frame com MediaPipe Pose para obter os landmarks.

3. **Definição da Lógica de Contagem:**  
   - Analisar a posição das articulações em diferentes fases do movimento (por exemplo, medir ângulos entre articulações).  
   - Definir condições para identificar o início e o fim de um agachamento ou flexão.

4. **Incremento das Contagens e Visualização:**  
   - Manter contadores separados para agachamentos e flexões.  
   - Exibir o count no ecrã juntamente com o vídeo (opcional).

5. **Testes e Ajustes:**  
   - Testar o sistema com diferentes utilizadores, ritmos de exercício e condições de iluminação.  
   - Ajustar os critérios de deteção para melhorar a precisão.

## Entregáveis

- **Código Fonte:**  
  Organizado, comentado, incluindo um README com instruções de instalação e uso.

- **Demonstração Funcional:**  
  Vídeo ou capturas de ecrã do sistema a funcionar, mostrando a contagem de agachamentos e flexões.

## Duração e Organização

- **Tempo Total:** Cerca de 3 semanas.  
- **Tamanho dos Grupos:** 2 a 3 estudantes do 3º ano de Informática, juniores.

## Valor Educativo

Este projeto permite:  
- Aplicar técnicas de visão computacional e análise de pose humana em tempo real.  
- Desenvolver lógica algorítmica para reconhecimento de movimentos, ligando teoria (ângulos, landmarks) a aplicações práticas.  
- Aprimorar a capacidade de teste, refinamento e otimização de um sistema interativo.  
