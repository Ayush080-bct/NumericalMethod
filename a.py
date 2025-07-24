import subprocess

def check_signal_strength():
    cmd = "netsh wlan show interfaces"
    output = subprocess.check_output(cmd, shell=True).decode()

    for line in output.split("\n"):
        if "Signal" in line:
            strength = int(line.split(":")[1].strip().replace("%", ""))
            print(f"Signal Strength: {strength}%")

            # Rough estimate of quality
            if strength > 80:
                print("Excellent signal 🔥")
            elif strength > 60:
                print("Good signal 😊")
            elif strength > 40:
                print("Fair signal 😐")
            else:
                print("Poor signal 😞")
            break

check_signal_strength()
