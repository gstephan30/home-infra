# Docker Projects

This directory contains Docker configurations for various services running on the server.

## Port Overview

| Project | Service | Host Port | Protocol | Description |
|---------|---------|-----------|----------|-------------|
| **Monitoring** | Grafana | `3000` | TCP | Dashboard Interface (Default Login: admin/admin) |
| **Monitoring** | Prometheus | `9090` | TCP | Metrics Database & Query UI |
| **Monitoring** | RAPL Exporter | - | TCP | Internal metrics endpoint (Port `8000`) |
| **Monitoring** | Node Exporter | - | TCP | Internal metrics endpoint (Port `9100`)* |
| **Minecraft** | Game Port | `25565` | TCP/UDP | Main Server Port |
| **Minecraft** | RCON | `25575` | TCP | Remote Console |
| **Minecraft** | Geyser | `19132` | UDP | Bedrock Edition Proxy |
| **Minecraft** | BlueMap | `8100` | TCP | Web Map |
| **Minecraft** | Plan | `8804` | TCP | Player Analytics Webchart |

*> Note: Node Exporter uses the default port 9100 but is configured safely without host port mapping in compose.*

## Projects

### 1. System & Power Monitoring (`/monitoring`)

This project sets up a full monitoring stack to track system performance and power consumption.

**Key Components:**
- **Prometheus**: Collects and stores metrics.
- **Grafana**: Visualizes the data (Dashboards).
- **Node Exporter**: Exports standard Linux metrics (CPU, RAM, Disk I/O).
- **RAPL Exporter**: A custom Python application that reads Intel RAPL sensors to track detailed CPU power usage (Watts & Joules).

### 2. Minecraft Server (`/opt/minecraft`)

*Note: The configuration for the Minecraft project is located in `/opt/minecraft` and was not accessible for automatic scanning.*
