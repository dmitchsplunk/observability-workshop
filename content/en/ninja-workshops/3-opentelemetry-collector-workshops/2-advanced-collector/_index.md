---
title: Advanced Collector Configuration
description: Practice setting up the OpenTelemetry Collector configuration from scratch and go though several advanced configuration scenarios's.
weight: 2
archetype: chapter
authors: ["Robert Castley,", "Charity Anderson,", "Pieter Hagen", "&", "Geoff Higginbottom"]
time: 90 minutes
---

The goal of this workshop is to help you become comfortable creating and modifying OpenTelemetry Collector configuration files. You’ll start with a minimal `agent.yaml` file and gradually configure several common advanced scenarios.

The workshop also explores how to configure the OpenTelemetry Collector to store telemetry data locally instead of transmitting it to a third-party vendor backend. Furthermore, this approach significantly enhances the debugging and troubleshooting process and is useful for testing and development environments where you don’t want to send data to a production system.

To get the most out of this workshop, you should have a basic understanding of the OpenTelemetry Collector and its configuration file format. Additionally, proficiency in editing YAML files is required. The entire workshop is designed to run locally.

### Workshop Overview

During this workshop, we will cover the following topics:

- **Setting up the agent locally**: Add metadata, and introduce the debug and file exporters.
- **Configuring a gateway**: Route traffic from the agent to the gateway.
- **Configuring the Filelog receiver**: Collect log data from various log files.
- **Enhancing agent resilience**: Basic configurations for fault tolerance.
- **Configuring processors**:
  - Filter out noise by dropping specific spans (e.g., health checks).
  - Remove unnecessary tags, and handle sensitive data.
  - Transform data using OTTL in the pipeline before exporting.
- **Configuring Connectors**: Route data to different endpoints based on the values received.

By the end of this workshop, you'll be familiar with configuring the OpenTelemetry Collector for a variety of real-world use cases.

---

### Prerequisites

- For this workshop, using a good YAML editor will be hugely beneficial. We recommend downloading [**Visual Studio Code**](https://code.visualstudio.com/download) or use the [**online version**](https://vscode.dev/).
- **Create a directory** on your machine for the workshop (e.g., `advanced-otel`). We will refer to this directory as `[WORKSHOP]` in the instructions.
- **Download the OpenTelemetry Collector and Load Generator** for your platform and place it in the `[WORKSHOP]` directory:

{{% notice note %}}
Having access to [**jq**](https://jqlang.org/download/) is recommended. This lightweight command-line tool helps process and format JSON data, making it easier to inspect traces, metrics, and logs from the OpenTelemetry Collector.
{{% /notice %}}

| Platform                         | OpenTelemetry Collector | Load Generator |
|----------------------------------|-------------------------|----------------|
|  Apple Mac (Apple Silicon)   | **[otelcol_darwin_arm64](https://github.com/signalfx/splunk-otel-collector/releases/download/v0.117.0/otelcol_darwin_arm64)** | [**loadgen_darwin_arm64**](https://github.com/splunk/observability-workshop/raw/refs/heads/main/workshop/ninja/advanced-otel/loadgen/build/loadgen-darwin-arm64) |
|  Apple Mac (Intel)           | **[otelcol_darwin_amd64](https://github.com/signalfx/splunk-otel-collector/releases/download/v0.117.0/otelcol_darwin_amd64)** | [**loadgen_darwin_amd64**](https://github.com/splunk/observability-workshop/raw/refs/heads/main/workshop/ninja/advanced-otel/loadgen/build/loadgen-darwin-amd64)|
|  Windows AMD/64              | **[otelcol_windows_amd64.exe](https://github.com/signalfx/splunk-otel-collector/releases/download/v0.117.0/otelcol_windows_amd64.exe)** | [**loadgen_windows_amd64.exe**](https://github.com/splunk/observability-workshop/raw/refs/heads/main/workshop/ninja/advanced-otel/loadgen/build/loadgen-windows-amd64.exe) |
|  Linux (AMD/64)              |**[otelcol_linux_amd64](https://github.com/signalfx/splunk-otel-collector/releases/download/v0.117.0/otelcol_linux_amd64)** | [**loadgen_linux_amd64**](https://github.com/splunk/observability-workshop/raw/refs/heads/main/workshop/ninja/advanced-otel/loadgen/build/loadgen-linux-amd64)|
|  Linux (ARM/64)              |**[otelcol_linux_arm64](https://github.com/signalfx/splunk-otel-collector/releases/download/v0.117.0/otelcol_linux_arm64)** | [**loadgen_linux_arm64**](https://github.com/splunk/observability-workshop/raw/refs/heads/main/workshop/ninja/advanced-otel/loadgen/build/loadgen-linux-arm64)|

{{% notice title="Exercise" style="green" icon="running" %}}

Once downloaded, rename the collector binary to `otelcol` (`otelcol.exe` on Windows) and the load generator binary to `loadgen` (`loadgen.exe` on Windows). On Mac and Linux, update the file permissions to make them executable:

```bash
chmod +x otelcol loadgen && \
./otelcol -v && \
./loadgen --help
```

{{% tabs %}}
{{% tab title="Initial Linux/Mac Directory Structure" %}}

```text
[WORKSHOP]
├── otelcol      # OpenTelemetry Collector binary
└── loadgen      # Load Generator binary
```

{{% /tab %}}
{{% tab title="Initial Windows Directory Structure" %}}

```text
[WORKSHOP]
├── loadgen.exe  # Load Generator binary
└── otelcol.exe  # OpenTelemetry Collector binary
```

{{% /tab %}}
{{% /tabs %}}

{{% /notice %}}

{{% notice style="warning" title="macOS Users" icon="desktop" %}}
Before running the binaries on macOS, you need to remove the quarantine attribute that macOS applies to downloaded files. This step ensures they can execute without restrictions.

Run the following command in your terminal:

```bash
xattr -dr com.apple.quarantine otelcol && \
xattr -dr com.apple.quarantine loadgen
```

{{% /notice %}}
