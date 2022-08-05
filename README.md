# PDF

PDFの解析方法をいろいろ試しています。

# 使用ライブラリ

* PyPDF2：MetadataやAnnotationなどを解析するのに適している。テキストは日本語に対応していないので出力結果は文字化けする。
https://pypdf2.readthedocs.io/en/latest/index.html

* pdfminer：テキストは日本語に対応している。すべてのObjectをParseしてくれるらしい。\
https://pdfminersix.readthedocs.io/en/latest/index.html\
テキスト分析についてはこちらの説明が参考になります。https://pdfminersix.readthedocs.io/en/latest/topic/converting_pdf_to_text.html

# 使用方法

url内にPDFへのパスを入力してください。\
パスはURLでもよいですし、ローカルにあるPDFファイルへのパスでも使用できます。
実行するとテキストオブジェクトがprint出力されます。
PDFにテキスト関係エレメントがあるかどうかは「ExtractText.existTextElement」で判定できます。テキストPDFか画像PDFの判定ができるはず…。