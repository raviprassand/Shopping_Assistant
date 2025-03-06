This Shopping Assistant, developed using the LangGraph framework, facilitates product search, recommendations, and shopping cart management in a conversational setting. The assistant integrates LangGraph’s tools for smooth and responsive interactions, allowing users to find products, manage their shopping cart, and inquire about order and purchase-related information. also, tools are interacting with database in the backend for product search, order status, delivery time retrieval etc.

Assistant Capabilities
Product Search and Recommendations:

The assistant responds to product-related inquiries, including product specifications, price, and availability from database.
A recommendation system suggests related or alternative products based on user queries, enhancing the shopping experience with personalized options.
Cart Management:

Users can add items to their shopping cart or remove them during the conversation, with the assistant prompting confirmations for each cart action.
The assistant provides live updates on the items in the cart, showing the product details and quantity.
Order and Purchase Queries:

The assistant responds to questions regarding checkout, delivery times, payment options, and order status.
For a smooth transaction experience, the assistant offers follow-up support on order status and estimated delivery.
Conversational Flow
Multi-Turn Conversations:

The assistant handles multi-turn interactions, remembering the context of user queries and follow-up questions.
It manages interruptions and seamlessly resumes the conversation, ensuring a natural user experience.
Structured Response Flow:

The response flow includes:
Human Message: Initial query from the user.
AI Message: AI’s response based on the query.
Tool Message: Specific tool action, if applicable (e.g., adding an item to the cart).
Testing and Validation
Scenario Testing:

The assistant was tested across various shopping scenarios to validate accuracy and reliability in conversation flow, including:
Complex queries involving multiple products.
Out-of-stock scenarios.
Invalid or ambiguous queries.
Edge Case Handling:

Documented common edge cases (e.g., items out of stock, unclear queries), ensuring the assistant gracefully manages these situations without disrupting the conversation.
Dataset Information
Dataset Source:
The dataset was sourced from Kaggle, and pre-processing steps were applied to prepare it for use, including:
Removing rows with null values.
Modifying product title length for better readability, as the dataset initially only included descriptions.
The data is stored in an PostreSQL database.
Functionalities in assistant_tools.py:
Key functionalities include:
search_products: Searches products based on user queries.
add_to_cart: Adds selected items to the cart.
remove_from_cart: Removes items from the cart.
view_cart: Displays items in the cart.
checkout: Processes the checkout.
get_payment_options, get_order_status, get_delivery_time: Provides payment options, order status, and delivery information.
Output Screenshots
Screenshots documenting the assistant's interactions and key functionalities are stored in the "Output Screenshot" folder for reference.

Steps to Run
Environment Setup
Create a .env file in the project root directory with the following content:

DB_HOST = <Your_Database_Host>
DB_PORT = <Your_Database_Port>
DB_DATABASE = <Your_Database_Name>
DB_USER = <Your_Database_Username>
DB_PASSWORD = <Your_Database_Password>
GROQ_API_KEY = <Your_Groq_API_Key>

Install PostgreSQL:

Ensure PostgreSQL is installed on your system.
For installation, visit the PostgreSQL official site.
Database Setup:

Make sure you have the following information ready:
Database Host: DB_HOST
Database Port: DB_PORT
Database Name: DB_DATABASE
Username: DB_USER
Password: DB_PASSWORD
Log in to PostgreSQL: Open a terminal and connect to PostgreSQL as the desired user. For example:

psql -U <username>
Replace <username> with your PostgreSQL username.

Create a New Database: Create the database where you will restore the backup:

CREATE DATABASE <database_name>;
Replace <database_name> with the desired database name.

Exit PostgreSQL: Type \q to exit the PostgreSQL shell:

\q
Restore the Backup: Use the psql command-line tool to restore the backup from the backup.sql file:

psql -U <username> -d <database_name> -f backup.sql
Replace:

<username>: Your PostgreSQL username.
<database_name>: The name of the database created in step 2.
backup.sql: Path to the provided SQL backup file.
Install Dependencies:

Run the following command to install all dependencies:
pip install -r requirements.txt
(The requirements.txt file includes all necessary packages, including langchain, langchain-groq, langgraph, python-dotenv, and groq.)
Run the Assistant:

Start the assistant by executing:
python main.py
Interact with the Assistant:

Enter shopping-related queries to initiate conversations with the assistant.
Example query: "Hi, I am looking for a gaming monitor" will prompt the assistant to display available mugs.
Cart Management:
Select a product type, and then ask the assistant to add it to the cart.
The assistant provides real-time cart updates, allowing users to view, modify, or remove items from the cart as needed.
Checkout and Order Support:
Proceed with checkout options, including reviewing cart items, modifying quantities, and finalizing the purchase.
The assistant also responds to order-related questions, including delivery status, payment methods, and estimated arrival times.
