# PdfHax
Projeto python para fazer alterações básicas com PDFs

## Funções Existentes
### Unir PDFs
- Input: File1.pdf, File2.pdf, ..., FileN.pdf
- Output: Combination.pdf
- Pega os inputs em ordem lexicográfica e une suas páginas em um arquivo só com todas as páginas

### Separar PDFs
- Input: File1.pdf
- Output: File1_part1.pdf, File1_part2.pdf, ..., File1_partN.pdf
- Pega o input e, de acordo com o desejado pelo usuário, separa o PDF em vários outros PDFs

### Rotacionar Páginas
- Input: File1.pdf
- Output: Rotation.pdf
- Pega o input e, de acordo com o desejado pelo usuário, rotaciona as páginas do PDF individualmente e retorna esse PDF resultante

### Apagar Páginas
- Input: File1.pdf
- Output: Deletion.pdf
- Pega o input e apaga as páginas do PDF escolhidas pelo usuário e retorna esse PDF resultante
