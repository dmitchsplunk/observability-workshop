---
title: Tour of the Kubernetes Navigator
linkTitle: 2. Kubernetes Navigator
weight: 2
--- 

## 1. Cluster vs Workload View

The Kubernetes Navigator offers you two separate use cases to view your Kubernetes data.

* The **K8s workloads** are focusing on providing information in regards to workloads a.k.a. *your deployments*.
* The **K8s nodes** are focusing on providing insight into the performance of clusters, nodes, pods and containers.

You will initially select either view depending on your need (you can switch between the view on the fly if required). The most common one we will use in this workshop is the workload view and we will focus on that specifically.

### 1.1 Finding your K8s Cluster Name

Your first task is to identify and find your cluster. The cluster will be named as determined by the preconfigured environment variable `INSTANCE`. To confirm the cluster name enter the following command in your terminal:

``` bash
echo $INSTANCE-k3s-cluster
```

Please make a note of your cluster name as you will need this later in the workshop for filtering.

## 2. Workloads & Workload Details Pane

Go to the **Infrastructure** page in the Observability UI and select **Kubernetes**, this will offer you a set of Kubernetes services, one of them being the **Kubernetes workloads** pane. The pane will show a tiny graph giving you a bird's eye view of the load being handled across all workloads. Click on the **Kubernetes workloads** pane and you will be taken to the workload view.

Initially, you will see all the workloads for all clusters that are reported into your Observability Cloud Org. If an alert has fired for any of the workloads, it will be highlighted on the top right in the image below.

![workloads](../images/k8s-workloads-screen.png)

Now, let's find your cluster by filtering on **Cluster** in the filter toolbar.

{{% notice title="Note" style="info" %}}
You can enter a partial name into the search box, such as `emea-ws-7*`, to quickly find your Cluster.

Also, it's a very good idea to switch the default time from the default **-4h** back to the last 15 minutes (**-15m**).
{{% /notice %}}

![workloads-filter](../images/k8s-workloads-filter.png)

You will now just see data just for your own cluster.

{{% notice title="Workshop Question" style="tip" icon="question" %}}
How many workloads are running & how many namespaces are in your Cluster?
{{% /notice %}}

### 2.1 Using the Navigator Selection Chart

By default, the **Kubernetes Workloads** table filters by `# Pods Failed` grouped by `k8s.namespace.name`. Go ahead and expand the `default` namespace to see the workloads in the namespace.

![k8s-workload-selection](../images/workload-selection.png)

Now, let's change the list view to a heatmap view by selecting **Map** icon (next to the **Table** icon). Changing this option will result in the following visualization (or similar):

![k8s-Heat-map](../images/workloads-heatmap.png)

In this view, you will note that each workload is now a colored square. These squares will change color according to the **Color by** option you select. The colors give a visual indication of health and/or usage. You can check the meaning by hovering over the **legend** exclamation icon {{% icon icon="exclamation-circle" %}} bottom right of the heatmaps.

Another valuable option in this screen is **Find outliers** which provides historical analytics of your clusters based on what is selected in the **Color by** dropdown.

Now, let's select the **Network transferred (bytes)** from the **Color by** drop-down box, then click on the **Find outliers** and change the **Scope** in the dialog to **Per k8s.namespace.name** and **Deviation from Median** as below:

![k8s-Heat-map](../images/set-find-outliers.png)

The **Find Outliers** view is very useful when you need to view a selection of your workloads (or any service depending on the Navigator used) and quickly need to figure out if something has changed.

It will give you fast insight into items (workloads in our case) that are performing differently (both increased or decreased) which helps to make it easier to spot problems.

### 2.2 The Deployment Overview pane

The Deployment Overview pane gives you a quick insight into the status of your deployments. You can see at once if the pods of your deployments are Pending, Running, Succeeded, Failed or in an Unknown state.  

![k8s-workload-overview](../images/k8s-deployment-overview.png)

* *Running:* Pod is deployed and in a running state
* *Pending:* Waiting to be deployed
* *Succeeded:* Pod has been deployed and completed its job and is finished
* *Failed:* Containers in the pod have run and returned some kind of error
* *Unknown:* Kubernetes isn't reporting any of the known states. (This may be during the starting or stopping of pods, for example).

You can expand the Workload name by hovering your mouse on it, in case the name is longer than the chart allows.

To filter to a specific workload, you can click on three dots **...** next to the workload name in the **k8s.workload.name** column and choose **Filter** from the dropdown box:

![workload-add-filter](../images/workload-add-filter.png)

This will add the selected workload to your filters. It would then list a single workload in the **default** namespace:

![workload-add-filter](../images/heatmap-filter-down.png)

From the Heatmap above find the **splunk-otel-collector-k8s-cluster-receiver** in the **default** namespace and click on the square to see more information about the workload:

![workload-add-filter](../images/k8s-workload-detail.png)

{{% notice title="Workshop Question" style="tip" icon="question" %}}
What are the CPU request  & CPU limit units for the otel-collector?
{{% /notice %}}

At this point, you can drill into the information of the pods, but that is outside the scope of this workshop.

## 3. Navigator Sidebar

Later in the workshop, you will deploy an Apache server into your cluster which will display an icon in the **Navigator Sidebar**.

In navigators for Kubernetes, you can track dependent services and containers in the navigator sidebar. To get the most out of the navigator sidebar you configure the services you want to track by configuring an extra dimension called `service.name`. For this workshop, we have already configured the `extraDimensions` in the collector configuration for monitoring Apache e.g.

```yaml
extraDimensions:
  service.name: php-apache
```

The Navigator Sidebar will expand and a link to the discovered service will be added as seen in the image below:

![Pivotbar](../images/pivotbar.png)

This will allow for easy switching between Navigators. The same applies to your Apache server instance, it will have a Navigator Sidebar allowing you to quickly jump back to the Kubernetes Navigator.
