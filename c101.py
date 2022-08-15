import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def Upload_File(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')

        dbx.files_upload(f.read(),file_to)

def main():
    access_token="sl.BMAUus5nVjrurpK1I3wPnbCfcYnI7QoS-kXUQtA9gg9pDv7-EyPyqRT1tiNJyazw4XqRJHV-xvyja3moiZcd2PNeOFtSBs44Fj5EJcxsxjcMx-6cRLXWX_X9bgiclp8_EDIguuCl3uY2"

    transferData=TransferData(access_token)

    file_form=input("Enter path of file to be transferd")
    file_to=input("Enter the path of file Dropbox")

    transferData.Upload_File(file_form,file_to)

    print("File has been moved.")

main()



