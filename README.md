# Multi Cloud Serverless Function
In this assignment, an HTTP serverless function was deployed in Google Cloud and Microsoft Azure to classify a laboratory value: serum creatinine.

Each function accepts an input which is the creatinine level (mg/dL) and returns the output as either normal or abnormal, based on established clinical thresholds.

The rule implemented was:

- Normal: creatinine between 0.59 and 1.04 mg/dL (adult women)

- Abnormal: creatinine < 0.59 mg/dL or > 1.04 mg/dL

Citation:
Mayo Clinic. Creatinine test. https://www.mayoclinic.org/tests-procedures/creatinine-test/about/pac-20384646
# Recording 
<https://www.loom.com/share/0bcde8b5c3de45a589f74b3b34e66c73>

# Google Cloud Platform
1. Created a Cloud Run service using inline Python source.
   - Region: us-east4
2. Defined the function entry point as creatinine_class.
3.  Allowed unauthenticated HTTP access.
4. Request Based for Billing; Minimium instances set to 1; Ingress: allow all traffic
5.  Create and deploy function.
6.  Get Function URL from GCP console to test Python requests
Endpoint:
<https://creatinine-classifier-354962182496.us-east4.run.app/?creatinine=0.8>
<img width="700" height="700" alt="Screenshot 2025-12-10 000325" src="https://github.com/user-attachments/assets/bd9ff1f5-ba61-42fd-90fa-da4aca0531e5" />

Testing:

<img width="700" height="700" alt="Screenshot 2025-12-10 101913" src="https://github.com/user-attachments/assets/b455c354-60bf-46b4-b649-68c99b902639" />

# Azure
1. Created an Azure Function App using Python with an HTTP trigger. (Automatically chooses Linux once python is selected)
2. Deployed the function in the East US region.
3. Added an HTTP-triggered function named creatinine_class with Function-level authentication.
4. Add code and save & deploy your function
5. Retrieved the function key and tested the endpoint using Python requests.

Endpoint:
<https://creatinine-classifier-hta5e2ebdkbbbga8.eastus-01.azurewebsites.net/api/creatinine_class>

Testing:
<img width="700" height="700" alt="image" src="https://github.com/user-attachments/assets/b76da27c-585d-45eb-8268-93b1c3401397" />

# Comparsions 
During this project, the main differences between the cloud platforms were how routing and access are handled. Azure Functions required the correct function route and a function key in order for requests to work, and missing either one initially resulted in 404 errors. Google Cloud Run was easier to access publicly but required specifying the correct function entry point during deployment. Both platforms also showed brief delays when the service had not been used recently, which is normal behavior for serverless applications.


