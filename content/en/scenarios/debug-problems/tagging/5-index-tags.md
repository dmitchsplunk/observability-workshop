---
title: Index Tags
linkTitle: 5. Index Tags
weight: 5
time: 5 minutes
---

## Index Tags

To use advanced features in **Splunk Observability Cloud** such as **Tag Spotlight**, we'll need to first index one or more tags.

To do this, navigate to **Settings** -> **APM MetricSets**.  Then click the **+ New MetricSet** button.  

Let's index the `credit.score.category` tag by entering the following details (**note**: since everyone in the workshop is using the same organization, the instructor will do this step on your behalf):

![Create Troubleshooting MetricSet](../images/create_troubleshooting_metric_set.png)

Click **Start Analysis** to proceed.

The tag will appear in the list of **Pending MetricSets** while analysis is performed.  

![Pending MetricSets](../images/pending_metric_set.png)

Once analysis is complete, click on the checkmark in the **Actions** column.

![MetricSet Configuraiton Applied](../images/metricset_config_applied.png)

## How to choose tags for indexing

Why did we choose to index the `credit.score.category` tag and not the others?

To understand this, let's review the primary use cases for tags:

* Filtering
* Grouping

### Filtering

With the filtering use case, we can use the **Trace Analyzer** capability of **Splunk Observability Cloud** to filter on traces that match a particular tag value.  

We saw an example of this earlier, when we filtered on traces where the credit score started with `7`.

Or if a customer calls in to complain about slow service, we could use **Trace Analyzer** to locate all traces with that particular customer number.

Tags used for filtering use cases are generally high-cardinality, meaning that there could be thousands or even hundreds of thousands of unique values.  In fact, **Splunk Observability Cloud** can handle an effectively infinite number of unique tag values!  Filtering using these tags allows us to rapidly locate the traces of interest.

Note that we aren't required to index tags to use them for filtering with **Trace Analyzer**.

### Grouping

With the grouping use case, we can use **Trace Analyzer** to group traces by a particular tag.

But we can also go beyond this and surface trends for tags that we collect using the powerful **Tag Spotlight** feature in **Splunk Observability Cloud**, which we’ll see in action shortly.

Tags used for grouping use cases should be low to medium-cardinality, with hundreds of unique values.

For custom tags to be used with **Tag Spotlight**, they first need to be indexed.

We decided to index the `credit.score.category` tag because it has a few distinct values that would be useful for grouping. In contrast, the customer number and credit score tags have hundreds or thousands of unique values, and are more valuable for filtering use cases rather than grouping.

## Troubleshooting vs. Monitoring MetricSets

You may have noticed that, to index this tag, we created something called a **Troubleshooting MetricSet**. It's named this way because a Troubleshooting MetricSet, or TMS, allows us to troubleshoot issues with this tag using features such as **Tag Spotlight**.

You may have also noticed that there's another option which we didn't choose called a **Monitoring MetricSet** (or MMS).  Monitoring MetricSets go beyond troubleshooting and allow us to use tags for alerting and dashboards.  We'll explore this concept later in the workshop.
