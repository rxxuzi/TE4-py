class Printer:
    def print_document(self, document):
        print(f"Printing document: {document}")

class Scanner:
    def scan_document(self):
        print("Scanning a document")

class MultiFunctionDevice(Printer, Scanner):
    def copy_document(self):
        print("Copying a document")
        self.scan_document()
        self.print_document("Copied document")

# マルチ機能デバイスのインスタンスを作成
mfd = MultiFunctionDevice()

# 継承されたメソッドを呼び出す
mfd.print_document("My Document")  # Printerから継承
mfd.scan_document()                # Scannerから継承
mfd.copy_document()                # MultiFunctionDevice自体のメソッド

