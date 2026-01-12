# Docker Projects

This directory contains Docker configurations for various services running on the server.

## Projects

### 1. System & Power Monitoring (`/monitoring`)

This project sets up a full monitoring stack to track system performance and power consumption.

**Key Components:**
- **Prometheus**: Collects and stores metrics.
- **Grafana**: Visualizes the data (Dashboards).
- **Node Exporter**: Exports standard Linux metrics (CPU, RAM, Disk I/O).
- **RAPL Exporter**: A custom Python application that reads Intel RAPL sensors to track detailed CPU power usage (Watts & Joules).

#### Used Ports

| Service | Host Port | Internal Port | Description |
|---------|-----------|---------------|-------------|
| **Grafana** | `3000` | `3000` | Dashboard Interface (Default Login: admin/admin) |
| **Prometheus** | `9090` | `9090` | Metics Database & Query UI |
| **RAPL Exporter** | - | `8000` | Internal metrics endpoint for power usage |
| **Node Exporter** | - | `9100`* | Internal metrics endpoint for system stats |

*> Note: Node Exporter uses the default port 9100 but is configured safely without host port mapping in compose.*

---

### 2. Minecraft Server (`/opt/minecraft`)

*Note: The configuration for the Minecraft project is located in `/opt/minecraft` and was not accessible for automatic scanning.*

Typically, Minecraft servers use the following ports:
- **Game Port**: `25565` (TCP/UDP)
- **RCON**: `25575` (TCP) - *Remote Console*
- **Geyser (Bedrock)**: `19132` (UDP) - *Bedrock Edition Proxy*
- **BlueMap**: `8100` (TCP) - *Web Map*
- **Plan**: `8804` (TCP) - *Player Analytics Webchart*
