import sys
from scapy.all import sniff, Ether, IP, TCP, UDP, ICMP, ARP

# --- Конфигурация анализатора ---
NUM_PACKETS_TO_CAPTURE = 20  # Количество пакетов для захвата
# Сетевой интерфейс для захвата. Оставьте None, чтобы Scapy выбрал по умолчанию.
# Примеры: "eth0", "wlan0" (Linux), "Ethernet", "Wi-Fi" (Windows)
CAPTURE_INTERFACE = None
# --------------------------------

# Словарь для хранения статистики по протоколам
protocol_counts = {
    "TCP": 0,
    "UDP": 0,
    "ICMP": 0,
    "ARP": 0,
    "Other IP": 0,
    "Non-IP/ARP": 0,
    "Total Captured": 0
}

# Карта IP-протоколов для более читаемого вывода
IP_PROTO_MAP = {
    1: "ICMP",
    6: "TCP",
    17: "UDP",
    47: "GRE",
    50: "ESP",
    51: "AH",
    89: "OSPF",
    132: "SCTP"
}

def analyze_packet(packet):
    """
    Функция-обработчик для каждого захваченного пакета.
    Разбирает пакет и выводит ключевую информацию.
    """
    protocol_counts["Total Captured"] += 1
    packet_num = protocol_counts["Total Captured"]

    print(f"n--- Пакет {packet_num} (Длина: {len(packet)} байт) ---")

    # Уровень Ethernet (Layer 2)
    if packet.haslayer(Ether):
        eth_layer = packet[Ether]
        print(f"  Ethernet: {eth_layer.src} -> {eth_layer.dst} (Тип: 0x{eth_layer.type:04x})")
    else:
        print("  Ethernet: (нет информации)")

    # Уровень IP (Layer 3)
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        ip_proto_name = IP_PROTO_MAP.get(ip_layer.proto, f"Неизвестный ({ip_layer.proto})")
        print(f"  IP: {ip_layer.src} -> {ip_layer.dst} (TTL={ip_layer.ttl}, Протокол: {ip_proto_name})")

        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            print(f"    TCP: {tcp_layer.sport} -> {tcp_layer.dport} (Флаги: {tcp_layer.flags})")
            protocol_counts["TCP"] += 1
        elif packet.haslayer(UDP):
            udp_layer = packet[UDP]
            print(f"    UDP: {udp_layer.sport} -> {udp_layer.dport} (Длина: {udp_layer.len})")
            protocol_counts["UDP"] += 1
        elif packet.haslayer(ICMP):
            icmp_layer = packet[ICMP]
            print(f"    ICMP: Тип={icmp_layer.type}, Код={icmp_layer.code}")
            protocol_counts["ICMP"] += 1
        else:
            print(f"    Протокол IP L4: {ip_proto_name} (без подробного разбора)")
            protocol_counts["Other IP"] += 1
    # Уровень ARP (Layer 3)
    elif packet.haslayer(ARP):
        arp_layer = packet[ARP]
        op_code = "Запрос" if arp_layer.op == 1 else ("Ответ" if arp_layer.op == 2 else f"Неизвестно ({arp_layer.op})")
        print(f"  ARP: {arp_layer.psrc} ({arp_layer.hwsrc}) {op_code} {arp_layer.pdst} ({arp_layer.hwdst})")
        protocol_counts["ARP"] += 1
    else:
        print("  Протокол L3: Неизвестный (без подробного разбора)")
        protocol_counts["Non-IP/ARP"] += 1

def main():
    """
    Основная функция для запуска захвата пакетов и вывода статистики.
    """
    print("=" * 60)
    print("  Простой анализатор сетевых пакетов (Scapy)")
    print("=" * 60)
    print(f"Начало захвата {NUM_PACKETS_TO_CAPTURE} пакетов...")
    print(f"Используемый интерфейс: {CAPTURE_INTERFACE if CAPTURE_INTERFACE else 'по умолчанию Scapy'}")
    print("n[!] Для захвата пакетов требуются права администратора/суперпользователя.")

    try:
        sniff(count=NUM_PACKETS_TO_CAPTURE, prn=analyze_packet, iface=CAPTURE_INTERFACE, store=0)
    except PermissionError:
        print("n[ОШИБКА]: Отказано в доступе. Запустите скрипт с правами администратора.")
        sys.exit(1)
    except Exception as e:
        print(f"n[ОШИБКА]: Произошла неожиданная ошибка: {e}")
        sys.exit(1)

    print("n" + "=" * 60)
    print("  Анализ завершен. Краткая статистика:")
    print("=" * 60)
    for proto, count in protocol_counts.items():
        print(f"  {proto:<15}: {count}")
    print("=" * 60)

if __name__ == "__main__":
    main()
