import serial
import time
import telnetlib
import subprocess

HOST = "127.0.0.1"
PORT = 7356
COMMAND = "f"

def telnet_command(host, port, command):
    """Invia un comando Telnet e restituisce la risposta.

    Args:
        host (str): L'indirizzo IP del server.
        port (int): La porta del server.
        command (str): Il comando da inviare.

    Returns:
        str: La risposta del server, o una stringa vuota in caso di errore.
    """
    try:
        tn = telnetlib.Telnet(host, port)
        tn.write(command.encode('ascii') + b'\n')
        response = tn.read_some().decode('ascii').strip()
        tn.close()
        return response
    except Exception as e:
        print(f"Errore durante la connessione Telnet: {e}")
        return ""

if __name__ == "__main__":
    while True:
        # Get the frequency from the Telnet server
        freq = telnet_command(HOST, PORT, COMMAND)

        try:
            # Set up serial communication
            serialcomm = serial.Serial("/dev/ttyACM0", 9600)
            serialcomm.timeout = 1
            time.sleep(2)

            try:
                # Prepare the command to send
                h = freq + "\n"

                print(h)
                print(len(h))
                print(h.encode())
  
                # Send the command over the serial communication
                serialcomm.write(h.encode())
                time.sleep(0.5)

            except Exception as e:
                print(f"Errore durante la comunicazione seriale: {e}")
                # Uncomment if you want to call zenity in case of an error
                # subprocess.run(['zenity', '--info', '--text="Connessione telnet fallita"'])

        except Exception:
            # In case of error with the Telnet or serial connection, show a popup
            subprocess.run(['zenity', '--info', '--text="Controllare seriale Arduino"'])

serialcomm.close()
