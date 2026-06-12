ip_value = None
port_value = None
password_value = None
def main():
    import socket
    import pyautogui
    import io
    import os
    import time
    import pyttsx3
    import subprocess
    try:
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error as err:
        print(f"Error : {err}")
    print("Socket Created Succesfully")
    time.sleep(2)
    print("Waiting for connection...")
    server.bind((ip_value,port_value))
    server.listen(5)
    while True:
        client,addr = server.accept()
        client.settimeout(300)
        passw = client.recv(4096).decode("utf-8")
        if passw.strip() == password_value:
            print("Succesfully login")
            client.send("Succesfully Login---".encode("utf-8"))
            try:
                while True:
                    data = client.recv(4096)
                    if not data:
                        break
                    final_data = str(data.decode("utf-8"))
                    #keys-
                    if final_data.startswith("press"):
                        key = final_data.replace("press ","")
                        pyautogui.press(key)
                    #write
                    if final_data.startswith("write"):
                        write = final_data.replace("write ","")
                        pyautogui.write(write,interval=0.1)
                    #hotkey
                    if final_data.startswith("hotkey"):
                        hotkey = final_data.replace("hotkey ","").split("+")
                        pyautogui.hotkey(*hotkey)
                    if final_data.startswith("ss"):
                        img = pyautogui.screenshot()
                        buffer = io.BytesIO()
                        img.save(buffer,format="PNG")
                        client.sendall(buffer.getvalue())
                    if final_data.startswith("speak"):
                        speak = final_data.replace("speak ","")
                        pyttsx3.speak(speak)
                    if final_data.startswith("cmd"):
                        cmd = final_data.replace("cmd ","")
                        if cmd.startswith("cd"):
                            try:
                                change = cmd.replace("cd ","")
                                os.chdir(change)
                                client.send(f"Changed directory to {os.getcwd()}".encode("utf-8"))
                            except Exception as e:
                                client.send(f"cd Error : {e}".encode("utf-8"))
                        else:
                            try:
                                output_cmd = subprocess.run(cmd,shell=True,capture_output=True,text=True)
                                client.send(output_cmd.stdout.encode("utf-8"))
                            except Exception as e:
                                client.send(f"cmd Error : {e}".encode("utf-8"))
            except Exception as e:
                print("Client is disconnected")
                print(f"Error : {e}")
                client.close()
        else:
            client.send("Incorrect Password".encode("utf-8"))
            client.close()

    server.close()
    
main()