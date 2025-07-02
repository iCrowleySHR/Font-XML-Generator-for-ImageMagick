import os
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, ElementTree
import getpass

def gerar_type_xml(caminho_saida='type.xml'):
    # Diretórios de fontes: sistema e usuário
    user = getpass.getuser()
    dirs_fontes = [
        Path("C:/Windows/Fonts"),
        Path(f"C:/Users/{user}/AppData/Local/Microsoft/Windows/Fonts")
    ]
    
    extensoes_suportadas = ('.ttf', '.otf')
    fontes_ja_adicionadas = set()

    # Elemento raiz
    typemap = Element("typemap")

    for dir_fontes in dirs_fontes:
        if not dir_fontes.exists():
            continue
        for fonte in dir_fontes.iterdir():
            if fonte.suffix.lower() in extensoes_suportadas:
                nome_fonte = fonte.stem
                caminho_fonte = fonte.resolve().as_posix()

                # Evitar duplicatas com mesmo nome
                if nome_fonte.lower() in fontes_ja_adicionadas:
                    continue
                fontes_ja_adicionadas.add(nome_fonte.lower())

                SubElement(typemap, "type", {
                    "name": nome_fonte,
                    "fullname": nome_fonte,
                    "family": nome_fonte,
                    "style": "Normal",
                    "stretch": "Normal",
                    "weight": "400",
                    "glyphs": caminho_fonte
                })

    # Salvar XML
    tree = ElementTree(typemap)
    tree.write(caminho_saida, encoding="utf-8", xml_declaration=True)
    print(f"Arquivo '{caminho_saida}' criado com sucesso com {len(fontes_ja_adicionadas)} fontes.")

# Executar
if __name__ == "__main__":
    gerar_type_xml("type.xml")
