from pypdf import PdfReader, PdfWriter
import os

inputDir = os.path.join(os.getcwd(),'Input')
outputDir = os.path.join(os.getcwd(),'Output')

def mergeInputs():
	pyMerger = PdfWriter()
	if len(os.listdir(inputDir)) < 2:
		print("Não há arquivos de entrada o suficiente\n")
		return
	print("Os arquivos",end=" ")
	for file in os.listdir(inputDir):
		print(f"[{file}]",end=" ")
		if file.endswith('.pdf'):
			pyMerger.append(os.path.join(inputDir,file))
	pyMerger.write(os.path.join(outputDir,'Combination.pdf'))
	print("Foram unidos em [Combination.pdf]\n")
	
def separateInputs():
	if len(os.listdir(inputDir)) < 1:
		print("Não há arquivos de entrada o suficiente\n")
		return
	for file in os.listdir(inputDir):
		print(f"Lendo agora: {file}")
		inputPdf = PdfReader(os.path.join(inputDir,file))
		res = input(f"Você vai dividir em quantidades diferentes de paginas? (Y/N) ")
		divs = []
  
		if(res == 'Y' or res == 'y'):
			tot = 0; it = 1
			while(tot < len(inputPdf.pages)):
				res = input(f"Quantas páginas para o {it}° arquivo? ")
				divs += [min(int(res),len(inputPdf.pages) - tot)]
				tot += min(int(res),len(inputPdf.pages) - tot)
				it += 1
		else:
			res = input(f"No máximo, quantas páginas cada arquivo? ")
			divs = [int(res)]*(len(inputPdf.pages)//int(res))
			if len(inputPdf.pages)%int(res) > 0:
				divs += [len(inputPdf.pages)%int(res)]
   
		t = 0; id = 1
		for num in divs:
			outputPdf = PdfWriter()
			for i in range(t,t+num):
				outputPdf.add_page(inputPdf.pages[i])
			outputPdf.write(os.path.join(outputDir,f"{file[:-4]}_File{id}_{num}pages.pdf"))
			t += num
			id += 1
		print()

def rotateInputs():
	if len(os.listdir(inputDir)) < 1:
		print("Não há arquivos de entrada o suficiente\n")
		return
	for file in os.listdir(inputDir):
		print(f"Lendo agora: {file}")
		inputPdf = PdfReader(os.path.join(inputDir,file))
		outputPdf = PdfWriter()
		outputPdf.append(inputPdf)
  
		pageNum = 1
		while pageNum != 0:
			pageNum = int(input("Digite o número da página do PDF para rotacionar (0 -> Sair): "))
			if pageNum > 0 and pageNum <= len(inputPdf.pages):
				deg = int(input(f"Em quantos graus girar a página {pageNum} em sentido horário? "))
				deg = (deg-(deg%90))%360
				outputPdf.pages[pageNum-1].rotate(deg)
		outputPdf.write(os.path.join(outputDir,'Rotation.pdf'))
		print(f'Arquivo [{file}] rotacionado e armazenado em [Rotation.pdf]\n')

def eraseInputs():
	if len(os.listdir(inputDir)) < 1:
		print("Não há arquivos de entrada o suficiente\n")
		return
	for file in os.listdir(inputDir):
		print(f"Lendo agora: {file}")
		inputPdf = PdfReader(os.path.join(inputDir,file))
		outputPdf = PdfWriter()
		postOutputPdf = PdfWriter()
  
		pageNum = 1; pages = []
		while pageNum != 0:
			pageNum = int(input("Digite o número da página do PDF para apagar (0 -> Sair): "))
			if pageNum > 0 and pageNum <= len(inputPdf.pages):
				pages.append(pageNum-1)
		pages.append(-1)
    
		pages = sorted(pages,reverse=True); ind = 0
		for i in reversed(range(len(inputPdf.pages))):
			if i == pages[ind]:
				ind += 1
			else:
				outputPdf.add_page(inputPdf.pages[i])
		for i in reversed(range(len(outputPdf.pages))):
			postOutputPdf.add_page(outputPdf.pages[i])
 
		postOutputPdf.write(os.path.join(outputDir,'Deletion.pdf'))
		print(f'Arquivo [{file}] alterado e armazenado em [Deletion.pdf]\n')
 
print(); exec = 1
while exec != 0:
	exec = int(input("Escolha sua ação:\n 1 -> Juntar PDFs\n 2 -> Separar PDFs\n 3 -> Rotacionar Páginas\n 4 -> Apagar Páginas\n 0 -> Sair\n\n"))
	print()
	if exec == 1:
		mergeInputs()
	elif exec == 2:
		separateInputs()
	elif exec == 3:
		rotateInputs()
	elif exec == 4:
		eraseInputs()