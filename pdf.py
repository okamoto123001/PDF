# urllib.requestではなく、別モジュールのrequestsを使用
import requests
from PyPDF2 import PdfReader
import io
from pdfminer.high_level import extract_text, extract_pages
from urllib.parse import urlparse
from pdfminer.layout import LTTextContainer, LTChar, LTAnno

class ExtractText:
    # TextElementをすべてprintする
    def printTextElement(self, target):
        for page_layout in extract_pages(target):
            for element in page_layout:
                # print(element)
                if isinstance(element, LTTextContainer):
                    for text_line in element:
                        print("  │─", end="")
                        print(text_line)
                        # LTTextLineがなく、LTCharやLTAnnnoがある場合もある。
                        if isinstance(text_line, LTAnno) or isinstance(text_line, LTChar):
                            self.printLTCharOrLTAnno(character)
                        else:
                            for character in text_line:
                                self.printLTCharOrLTAnno(character)

    # LTCharとLTAnnoをprintする
    def printLTCharOrLTAnno(self, character):
        if isinstance(character, LTChar):
            print("    │─", end="")
            print(character)
            print("    │─", end="")
            print(character.fontname)
            print("    │─", end="")
            print(character.size)
        else:
            print("    │─", end="")
            print(character)

    # LTTextContainerが存在するか確認    
    def existTextElement(self, target):
        for page_layout in extract_pages(target):
            for element in page_layout:
                if isinstance(element, LTTextContainer):
                    return True
        return False

url = "https://kentei.tokyo-cci.or.jp/eco/pdf/eco-gaiyou.pdf"
uparse = urlparse(url)
extractText = ExtractText()

if uparse[0] == 'http' or uparse[0] == 'https':

    # pdfのURLからレスポンスを取得
    res = requests.get(url)

    # レスポンスで得たPDFのバイトデータをFile Objectに変換
    with io.BytesIO(res.content) as f:
        # ファイルサイズ
        print(len(f.getvalue()))

        # 変換したFile ObjectをPyPDFで読み込み、Metadata取得
        reader = PdfReader(f)

        # pdfminer.sixのテキスト読み込み
        text = extract_text(f)
        print(text)

        meta = reader.metadata

        # pyPDF2のテキスト読み込み
        page = reader.pages[0]
        print(page.extract_text())

        # pdfminer extract elements
        extractText.printTextElement(f)

        # LTTextContainerがあるか確認
        print(extractText.existTextElement(f))
else:

    # 変換したFile ObjectをPyPDFで読み込み、Metadata取得
    reader = PdfReader(url)
    meta = reader.metadata
    print(meta)

    # pyPDF2のテキスト読み込み
    page = reader.pages[0]
    print(page.extract_text())

    # pdfminer.sixのテキスト読み込み
    text = extract_text(url)
    print(text)

    # pdfminer extract elements
    extractText.printTextElement(url)

    # LTTextContainerがあるか確認
    print(extractText.existTextElement(url))
