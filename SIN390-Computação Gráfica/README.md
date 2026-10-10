# SIN390 — Computação Gráfica

> **Optativa** · 60 h (4 h teóricas + 0 h práticas por semana) · 4 créditos · Semestres: II

| | |
|---|---|
| **Pré-requisitos** | [MAP 112](../MAP112-%C3%81lgebra%20Linear) e [SIN 216](../SIN216-Programa%C3%A7%C3%A3o%20e%20Estruturas%20de%20Dados%20II) |
| **Programa analítico** | [Catálogo de Graduação UFV 2026 (PDF)](https://catalogo.ufv.br/pdf.php?campus=crp&disciplina=SIN%20390&ano=2026) |

## Ementa

Conceitos básicos. Noções de imagens. Transformações geométricas e coordenações homogêneas. Sistemas gráficos 2D. Visualização em 3D: Z-Buffer, BSP. Algoritmos de recorte e seleção. Algoritmos de rasterização. Modelos de iluminação e métodos para a geração de superfícies.

## Objetivos

Introduzir os conceitos básicos de geração de imagens por computação. Apresentar as técnicas de representação e transformações de primitivas em sistemas gráficos. Apresentar algoritmos de representação e manipulação de curvas. Introduzir sistemas de representação de cores. Apresentar algoritmos para representar cenários realistas e animações. Fazer com que o aluno seja capaz de construir um sistema de computação gráfica utilizando a linguagem OpenGL.

## Conteúdo programático

1. **Conceitos básicos** (4 h)
   - Histórico da computação gráfica
   - Dispositivos gráficos de entrada e saída
   - Fundamentos matemáticos para computação gráfica
2. **Noções de imagens** (4 h)
   - Codificação e quantização
   - Composição de imagens. 'blending'
   - Sistemas de cores e texturas
3. **Transformações geométricas e coordenações homogêneas** (8 h)
   - Coordenadas homogêneas e geometria projetiva
   - Transformação 'window-viewport'
   - Translação, escala, rotação, espelhamento e cisalhamento
   - Concatenação e inversão de transformações
4. **Sistemas gráficos 2D** (8 h)
   - Modelo de programação
   - Funcionamento de um sistema gráfico 2D
   - Controle da superfície de visualização
   - Primitivas de desenho e seus atributos
   - Sistemas de coordenadas e cerceamento ('clipping')
   - Programação com sistemas gráficos 2D
5. **Visualização em 3D: Z-Buffer, BSP** (12 h)
   - Projeções clássicas como transformações lineares
   - Modelos de câmeras
   - Visibilidade: Z-Buffer, BSP
   - Programação com sistemas gráficos 3D
6. **Algoritmos de recorte e seleção** (8 h)
   - Cohen-Sutherland e Cyrus-Beck: recorte de linhas
   - Suterland-Hodman e Liang-Barsky: recorte de polígonos
   - Seleção de linhas e polígonos
7. **Algoritmos de rasterização** (8 h)
   - Ponto médio e Bressenham: segmentos de retas e arcos de elipse
   - 'Scan-line': polígonos preenchidos: 'stipple', 'pattern' e textura
   - Textos matriciais, vetoriais e escaláveis
8. **Modelos de iluminação e métodos para a geração de superfícies** (8 h)
   - Modelos básicos de iluminação
   - 'Ray-Tracing'. Radiosidade

## Bibliografia

### Básica

- HEARN, D.; BAKER, M.P. Computer graphics: C version. New Jersey: Prentice-Hall, Upper Saddle River, 1996.
- AZEVEDO, E.; CONCI. Computação gráfica. Campus-Elsevier, 2003.
- GOMES, J.M.; VELHO, L. Computação gráfica. v. 1. Rio de Janeiro: IMPA, 1998.

### Complementar

- COHEN, M.; MANSSOUR, I.H. OpenGL: uma abordagem prática e objetiva. Novatec, 2006.
- BUSS, S.R. Computer graphics: a mathematical introduction with OpenGL. Cambridge, 2005.
- FOLEY, J.D.; VAN DAM, A.; FEINER, S.K.; HUHES, J.F.; PHILLIPS, R.L. Introduction to computer graphics. Reading, Mass.: Addison-Wesley, 1993.
- SHIRLEY, P. Fundamentals of computer graphics, A K Peter, 2005.

## Referências úteis

- [LearnOpenGL](https://learnopengl.com/) — tutorial de OpenGL moderno; em inglês
- [Scratchapixel](https://www.scratchapixel.com/) — fundamentos de renderização; em inglês
- [Ray Tracing in One Weekend](https://raytracing.github.io/) — série de livros abertos; em inglês
- [The Book of Shaders](https://thebookofshaders.com/) — shaders de fragmento passo a passo
- [Documentação do three.js](https://threejs.org/docs/) — gráficos 3D no navegador; em inglês

---

<sub>Ementa, objetivos, conteúdo e bibliografia transcritos do programa analítico oficial da UFV; referências úteis em `dados/referencias.json`. Tem material ou indicação desta disciplina? [Contribua](../README.md#como-contribuir). Gerado por `scripts/catalogo.py`; edite o script ou os dados, não este arquivo.</sub>
