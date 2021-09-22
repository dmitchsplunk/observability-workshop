# Lab Overview

- **Splunk Synthetic Monitoring** formally [Rigor](https://rigor.com/) is a powerful monitoring service that monitors the availability of any website, mobile app, API, or system on the Internet with Uptime Checks and sends real-time alerts.

- This Lab walks your through using Chrome Selenium IDE extension to create a synthetic transaction against a Splunk demo instance and creating a Splunk Synthetic Monitoring Real Browser Check (RBC). In addition you get to learn other Splunk Synthetic Monitoring checks like REST API checks and Uptime Checks.

## Prerequisites

Login with your username and password to [https://monitoring.rigor.com](https://monitoring.rigor.com) & [https://optimization.rigor.com](https://optimization.rigor.com) and make sure you are assigned to your own account for example: **O11y Workshop**.

Edit your Splunk Synthetic Monitoring account personal information and adjust your timezone and email notifications. Splunk Synthetic Monitoring will start sending you notifications, you can turn them off at the monitoring level.

![placeholder](../images/synthetics/image5.png)

Add the [Selenium IDE](https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd?hl=en-US) extension to your **Chrome** Browser. Click on the extension and you should see the following screen:

![placeholder](../images/synthetics/image17.png)

## Using Selenium IDE

Record a web transaction using Selenium IDE to check on [http://splunk.o11ystore.com](http://splunk.o11ystore.com), name the project "**[YOUR_INITIALS] - O11y Store**"

!!! question "What is Selenium IDE?"
    - Selenium IDE is an open source record and playback test automation for the web.
    - Selenium is a portable framework for testing web applications.
    - Selenium provides a playback tool for authoring functional tests without the need to learn a test scripting language (Selenium IDE).
    - It also provides a test domain-specific language (Selenese) to write tests in a number of popular programming languages, including C#, Groovy, Java, Perl, PHP, Python, Ruby and Scala.
    - The tests can then run against most modern web browsers.
    - Selenium runs on Windows, Linux, and macOS.
    - It is open-source software released under the Apache License 2.0.

![placeholder](../images/synthetics/image29.png)

Enter [http://splunk.o11ystore.com](http://splunk.o11ystore.com) as your base URL.

![placeholder](../images/synthetics/image11.png)

Click **Start Recording**, a new window should open up with splunk.o11ystore.com - click **Vintage Camera Lens**, click **Add To Cart**, and then click **Place Order**

Close the window and then stop the recording by navigating back to Selenium IDE and name the test: "**[YOUR_INITIALS] - Checkout Flow (Desktop)**"

![placeholder](../images/synthetics/image10.png)

Your Selenium IDE Project will look something like this:

![placeholder](../images/synthetics/image19.png)

Test your recording by pressing on the play button, make sure your recording successfully completes the transaction:

![Run](../images/synthetics/image26.png)

Save your Selenium IDE Project to your Downloads folder as `Workshop.side`

![Save](../images/synthetics/image30.png)

![Save SIDE Project](../images/synthetics/save-side-project.png)

## Create Real Browser Check

Login to Splunk Synthetic Monitoring using [https://monitoring.rigor.com](https://monitoring.rigor.com). Click on **REAL BROWSER** and click **+New**{: .label-button .sfx-ui-button-blue}.

![placeholder](../images/synthetics/image3.png)

Click on "**From File**" and select your recording then click on Import

![placeholder](../images/synthetics/image1.png)

Set the **Frequency** to **5 Minutes**

![placeholder](../images/synthetics/image15.png)

Click on Steps and make the following adjustments to your recording provide a friendly name to Steps 1, 2 & 3.

![placeholder](../images/synthetics/image6.png)

Next, click **+ Add Step**, this new step will add some validation to the test. This is to ensure the checkout completed successfully. Enter **Confirm Order** for the **Name** and change the **Action** to **Wait for text present**. Enter **Your order is complete!** for the **Value**. You will now have a **Start Url** and 4 steps in your test configuration.

![placeholder](../images/synthetics/image2.png)

!!! info "Tip"
    As you are creating the steps think about how to go about using the "[Business Transaction](https://help.rigor.com/hc/en-us/articles/360049442854-How-Do-I-Use-Business-Transactions)" feature in Splunk Synthetic Monitoring which is very powerful. *"Business Transactions are a combined group of contiguous steps in a Real Browser script that are to be measured as a whole. These transactions logically group similar parts of a flow together, so that users can view the performance of multiple steps and page(s) grouped under one Business Transaction."*

Click on **Advanced** and make sure the **Viewport Size** is set to **Default desktop: 1366 x 768**

![Viewport Size](../images/synthetics/viewport-size.png)

Click on "**Test**" to test your recording. Once the test has successfully completed make sure to click on "**AFTER**" in Step 4 to validate the monitor was able to get to the order complete screen.

![placeholder](../images/synthetics/image22.png)

Click on **Create**{: .label-button .sfx-ui-button-blue} to save your Real Browser Monitor. After 5-10 minutes validate your monitor is working i.e. producing successful checks e.g.

![placeholder](../images/synthetics/image27.png)

!!! info "Tip"
    You can force to run your monitor now using **Run Now**

    ![placeholder](../images/synthetics/image8.png)

Change your view to **Segment by location** and observe the difference. You can turn off/on locations by clicking on them.

!!! question "Question?"
    Which Location has the poorest **Response Time**?

![placeholder](../images/synthetics/image9.png)

Click on one of the successful circles to drilldown into that Run:

![placeholder](../images/synthetics/image33.png)

Take a moment to explore the metrics with the **CONFIGURE METRICS/HIDE METRICS** dropdown.

![placeholder](../images/synthetics/image14.png)

Click **Page 2** in the dropdown, and scroll down to view the **Filmstrip** and the **Waterfall Chart.**

![placeholder](../images/synthetics/image16.png)

![Filmstrip](../images/synthetics/filmstrip.png)

![Waterfall](../images/synthetics/waterfall.png)

Click on **Click Here to Analyze with Optimization** which will prompt you to login to your Splunk Synthetic Monitoring Optimization Account. If you **don't have this option**, navigate to this [page](https://optimization.rigor.com/s/2373818/?sh=3AF8C48AADD6D3E5F5DAA8B4B7BB7F45).

![placeholder](../images/synthetics/image31.png)

Click the "**Best Practices Score**" tab. Scroll down, and review all the findings

![placeholder](../images/synthetics/image23.png)

![Best Practices](../images/synthetics/best-practices.png)

Spend some time to review the findings. Click into any line item

## Create Mobile RBC

Copy the RBC you created above:

![Copy Check](../images/synthetics/copy-check.png)

Rename it, for example: **RWC - Checkout Flow (Tablet)**

![Copy Check](../images/synthetics/rename-check.png)

Under the **Advanced** tab, update the following three settings and create your new mobile RBC.

![placeholder](../images/synthetics/image18.png)

Test & Validate the new monitor

!!! info "Tip"
    As you are creating the steps try using the "[Business Transaction](https://help.rigor.com/hc/en-us/articles/360049442854-How-Do-I-Use-Business-Transactions)" feature in Splunk Synthetic Monitoring. *"Business Transactions are a combined group of contiguous steps in a Real Browser script that are to be measured as a whole. These transactions logically group similar parts of a flow together, so that users can view the performance of multiple steps and page(s) grouped under one Business Transaction."*

## Resources

- [Getting Started With Selenium IDE](https://help.rigor.com/hc/en-us/articles/115004652007?flash_digest=b1ef7d1a07b68d5279ee5fef8adb87fb878cf010)

- [Splunk Synthetic Monitoring Scripting Guide](http://www2.rigor.com/scripting-guide)

- [How Can I Fix A Broken Script?](https://help.rigor.com/hc/en-us/articles/115004443988-How-Can-I-Fix-A-Broken-Script)

- [Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) (Document Object Model (DOM)

- [Selenium IDE](https://www.selenium.dev/selenium-ide/)