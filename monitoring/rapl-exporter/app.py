import time
import sys
from prometheus_client import start_http_server, Gauge, Counter

# Pfad im Container (wir mounten das später Read-Only)
RAPL_FILE = "/host_sys/class/powercap/intel-rapl/intel-rapl:0/energy_uj"

# Metriken
# 1. Gauge: Geht hoch und runter -> Aktueller Verbrauch in Watt
POWER_WATTS = Gauge('host_power_watts', 'Current CPU power usage in Watts')

# 2. Counter: Geht nur hoch -> Gesamter Energieverbrauch in Joule
# Das ist ESSENZIELL für deine Kostenberechnung.
ENERGY_JOULES = Counter('host_energy_joules_total', 'Total energy consumed by CPU in Joules')

def read_energy_uj():
    try:
        with open(RAPL_FILE, "r") as f:
            return int(f.read().strip())
    except Exception as e:
        # Wir printen nach stderr, damit docker logs das anzeigt
        print(f"Error reading RAPL: {e}", file=sys.stderr)
        return None

def main():
    # Startet Webserver auf Port 8000 (intern im Container)
    print("Starte RAPL Exporter auf Port 8000...", file=sys.stderr)
    start_http_server(8000)

    last_uj = read_energy_uj()
    
    while True:
        time.sleep(1.0) # 1 Sekunde Messintervall
        current_uj = read_energy_uj()
        
        if last_uj is not None and current_uj is not None:
            # Differenz berechnen
            diff_uj = current_uj - last_uj
            
            # Overflow Schutz (falls Zähler resetet, sehr selten, aber sauberer Code)
            if diff_uj < 0:
                last_uj = current_uj
                continue

            # Watt berechnen (Joule pro Sekunde)
            watts = diff_uj / 1_000_000
            
            # Metriken setzen
            POWER_WATTS.set(watts)
            # Counter erhöhen (Prometheus rechnet das später in kWh um)
            ENERGY_JOULES.inc(diff_uj / 1_000_000)
            
            last_uj = current_uj

if __name__ == '__main__':
    main()