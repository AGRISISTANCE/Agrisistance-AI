
# 🌱 AGRISISTANCE

**A2SV-Agrisistance** is an AI-driven web application aimed at helping African farmers optimize land use and boost crop productivity. Utilizing advanced machine learning algorithms and data analytics, AGRISISTANCE offers actionable insights and personalized recommendations tailored to individual farming needs.


THE AI FEATURES IN AGRISISTANCE:
the web application has 3 main features that are AI generated:

# **1/Predecting the best crops to invest in based off data of the soil:**


this feature uses a machine learning trained model that predicts the best fitted crops based off 5 parameters: oxygen levels, potassium / azote / phosphorus levels, ph levels, and humidity levels
these parameters are fetched using IOT devices, or manually entered or web-scraped using an openAI API

the model is trained to fit the parameters accordingly and generate a number of best crops to invest in 

# **2/OPTIMIZIG LAND USE AND BUDGET:**

this feature uses an optimization mechanism that falls within the search algorithms category, using a combination of genetic algorithms and hill-climbing, it suggests the best price-area-crop combinations in order to maximize the profit obtained, it takes as input the list of suggested crops from the first model and the total budget to be invested as well as estimated costs of each crops, the latter is obtained using web-scraping, it outputs the expected profit off each crop as well as the total expected profit based off the current budget

# **3/Generating an accomodated business plan for the farmer:**

this feature uses a generative model that takes all the already mentioned parameters as input , and using openAI , it generates a well fitted business model containing: statistics and predictions, advice and suggestions, calculations of cost and resource management as well as profit expectations

# The following Schema represents the flow of the models and the expected output and input at each endpoint:**
