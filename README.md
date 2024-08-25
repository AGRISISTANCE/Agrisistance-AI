# 🌱 AGRISISTANCE

**A2SV-Agrisistance** is an AI-driven web application designed to assist African farmers in optimizing land use and maximizing crop productivity. By employing advanced machine learning algorithms and data analytics, AGRISISTANCE delivers actionable insights and personalized recommendations tailored to each farming scenario.

## **Features**

### **1. Predicting the Best Crops to Invest In**

This feature uses a machine learning model to identify the most suitable crops based on soil parameters. Key factors include:
- **Oxygen Levels**
- **Potassium, Nitrogen, and Phosphorus Levels**
- **pH Levels**
- **Humidity Levels**

These parameters can be gathered from IoT devices, manually entered, or web-scraped using OpenAI APIs. The model processes this data to recommend the best crops for investment.

### **2. Optimizing Land Use and Budget**

The optimization feature utilizes genetic algorithms and hill-climbing techniques to determine the ideal crop-to-price-to-area combinations. Inputs include:
- Crop recommendations from the prediction model
- Total budget
- Estimated costs for each crop

The output includes the optimal distribution of crops to maximize profit, considering the total budget and available land area.

### **3. Generating a Tailored Business Plan**

Using generative models and OpenAI, this feature creates a comprehensive business plan, including:
- **Statistical Analysis and Predictions**
- **Strategic Advice and Suggestions**
- **Cost and Resource Management Calculations**
- **Profit Expectations**

This plan provides farmers with actionable strategies for effective resource management and financial planning.

## **API Endpoints**

### **/predict**

- **Method:** `POST`
- **Description:** Receives soil parameters and budget information to predict the best crops to plant.
- **Input:**
  ```json
  {
    "ph": 6.5,
    "temperature": 25,
    "rainfall": 200,
    "humidity": 80,
    "nitrogen": 40,
    "phosphorus": 20,
    "potassium": 15,
    "o2": 21,
    "budget": 1000,
    "area": 500
  }

- **Output:** List of recommended crops, cost, revenue, and profit projections.

### **/chat**
- **Method:**  ```POST```
- **Description:** Provides a conversational interface to answer questions and assist with inquiries, such as recommendations on crops based on various conditions.
- **Input:**
```json
{
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "user",
      "content": "What are the best crops to plant in sandy soil?"
    }
  ],
  "max_token": 150,
  "temperature": 0.7,
  "response_format": "text/plain",
  "user_id": "12345"
}
```

- **Headers:**
```
- Content-Type: application/json
- api_token: <your_api_token_here>
```

- Output: Response containing recommendations or information based on the user's query.



## **Getting Started**

### **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/Agrisistance-AI.git 
   ```

2. Navigate to the project directory:
    ```bash
    cd Agrisistance-AI
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### **Running the Application**
1. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

2. Access the application at:
    ```bash
    http://127.0.0.1:8000
    ```

## Configuration
Ensure you have a .env file in the root directory with the necessary environment variables, including API tokens and configuration settings.
    ```bash
    API_TOKEN=YOUR_API_TOKEN
    ```