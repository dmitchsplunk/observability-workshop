---
title: Local Hosting with Multipass
weight: 1
description: Learn how to create a local hosting environment with Multipass - Windows/Linux/Mac(Intel)
---

Install [Multipass](https://multipass.run/) and Terraform for your operating system. On a Mac (Intel), you can also install via [Homebrew](https://brew.sh/) e.g.

```text
brew install multipass terraform jq
```

Clone workshop repository:

```bash
git clone https://github.com/splunk/observability-workshop
```

Change into Multipass directory:

```bash
cd observability-workshop/local-hosting/multipass
```

Log Observer Connect:

If you plan to use your own Splunk Observability Cloud Suite Org and or Splunk instance, you may need to create a new **Log Observer Connect** connection:
Follow the instructions found in the [documentation](https://docs.splunk.com/observability/en/logs/lo-connect-landing.html) for [Splunk Cloud](https://docs.splunk.com/observability/en/logs/scp.html#logs-scp) or [Splunk Enterprize](https://docs.splunk.com/observability/en/logs/set-up-logconnect.html).

Additional requirements for running your own **Log Observer Connect** connection are:

- Create an index called **splunk4rookies-workshop**
- Make sure the Service account user used in the **Log observer Connect** connection has access to the **splunk4rookies-workshop** index (you can remove all other indexes, as all workshop log data should go to this index).

Initialize Terraform:

{{< tabs >}}
{{% tab title="Command" %}}

```bash
terraform init -upgrade
```

{{< /tab >}}
{{< tab title="Example Output" >}}

```text
Initializing the backend...

Initializing provider plugins...
- Finding latest version of hashicorp/random...
- Finding latest version of hashicorp/local...
- Finding larstobi/multipass versions matching "~> 1.4.1"...
- Installing hashicorp/random v3.5.1...
- Installed hashicorp/random v3.5.1 (signed by HashiCorp)
- Installing hashicorp/local v2.4.0...
- Installed hashicorp/local v2.4.0 (signed by HashiCorp)
- Installing larstobi/multipass v1.4.2...
- Installed larstobi/multipass v1.4.2 (self-signed, key ID 797707331BF3549C)
```

{{< /tab >}}
{{< /tabs >}}

Create Terraform variables file. Variables are kept in file `terrform.tfvars` and a template is provided, `terraform.tfvars.template`, to copy and edit:

```bash
cp terraform.tfvars.template terraform.tfvars
```

The following Terraform variables are required:

- `swipe_id`: [SWiPE ID](https://swipe.splunk.com/) for the instance
- `splunk_index`: Splunk Index to send logs to. Defaults to `splunk4rookies-workshop`.

Instance type variables:

- `splunk_presetup`: Provide a preconfigured instance (OTel Collector and Online Boutique deployed with RUM enabled). The default is `false`.
- `splunk_diab`: Install and run Demo-in-a-Box. The default is `false`.
- `tagging_workshop`: Install and configure the Tagging Workshop. The default is `false`.
- `otel_demo` : Install and configure the OpenTelemetry Astronomy Shop Demo. This requires that `splunk_presetup` is set to `false`. The default is `false`.

Optional advanced variables:

- `wsversion`: Set this to `main` if working on the development of the workshop, otherwise this can be omitted.
- `architecture`: Set this to the correct architecture, `arm64` or `amd64`. Defaults to `arm64` which is appropriate for Apple Silicon.

Run `terraform plan` to check that all configuration is OK. Once happy run `terraform apply` to create the instance.

{{< tabs >}}
{{% tab title="Command" %}}

```bash
terraform apply
```

{{< /tab >}}
{{% tab title="Example Output" %}}

``` text
random_string.hostname: Creating...
random_string.hostname: Creation complete after 0s [id=cynu]
local_file.user_data: Creating...
local_file.user_data: Creation complete after 0s [id=46a5c50e396a1a7820c3999c131a09214db903dd]
multipass_instance.ubuntu: Creating...
multipass_instance.ubuntu: Still creating... [10s elapsed]
multipass_instance.ubuntu: Still creating... [20s elapsed]
...
multipass_instance.ubuntu: Still creating... [1m30s elapsed]
multipass_instance.ubuntu: Creation complete after 1m38s [name=cynu]
data.multipass_instance.ubuntu: Reading...
data.multipass_instance.ubuntu: Read complete after 1s [name=cynu]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.

Outputs:

instance_details = [
  {
    "image" = "Ubuntu 22.04.2 LTS"
    "image_hash" = "345fbbb6ec82 (Ubuntu 22.04 LTS)"
    "ipv4" = "192.168.205.185"
    "name" = "cynu"
    "state" = "Running"
  },
]
```

{{% /tab %}}
{{< /tabs >}}

Once the instance has been successfully created (this can take several minutes), `exec` into it using the `name` from the output above. The password for Multipass instance is `Splunk123!`.

{{< tabs >}}
{{% tab title="Command" %}}

```bash
multipass exec cynu -- su -l splunk
```

{{< /tab >}}
{{% tab title="Example Output" %}}

```text
$ multipass exec kdhl -- su -l splunk
Password:
Waiting for cloud-init status...
Your instance is ready!
```

{{% /tab %}}
{{< /tabs >}}

Validate the instance:

```bash
kubectl version --output=yaml
```

To delete the instance, first make sure you have exited from instance and then run the following command:

```bash
terraform destroy
```
