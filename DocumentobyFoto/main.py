import cv2
import pytesseract

# Configuração do caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows

def extract_text_from_image(image_path, output_txt_path):
    # Carregar a imagem
    img = cv2.imread(image_path)

    # Pré-processar a imagem (opcional, dependendo da qualidade da imagem)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Aplicar algum tipo de threshold ou filtragem, se necessário
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # Usar Tesseract para fazer OCR
    text = pytesseract.image_to_string(thresh, lang='eng')

    # Salvar o texto extraído em um arquivo .txt
    with open(output_txt_path, 'w') as file:
        file.write(text)

    print(f'Texto extraído e salvo em {output_txt_path}')

# Exemplo de uso com caminho absoluto (ajuste conforme necessário)
image_path = r'C:\IA\visao-computacional\DocumentobyFoto\c.jpg'
output_txt_path = r'C:\IA\visao-computacional\DocumentobyFoto\output3.txt'
extract_text_from_image(image_path, output_txt_path)
