# Shopping Assistant

This Shopping Assistant, developed using the LangGraph framework, facilitates product search, recommendations, and shopping cart management in a conversational setting. The assistant integrates LangGraph’s tools for smooth and responsive interactions, allowing users to find products, manage their shopping cart, and inquire about order and purchase-related information. The tools interact with a backend database for product search, order status, delivery time retrieval, etc.

## Assistant Capabilities

### Product Search and Recommendations:
- Responds to product-related inquiries, including specifications, price, and availability from the database.
- A recommendation system suggests related or alternative products based on user queries, enhancing the shopping experience with personalized options.

### Cart Management:
- Users can add or remove items from their shopping cart during the conversation, with the assistant prompting confirmations for each cart action.
- Provides live updates on the items in the cart, showing product details and quantities.

### Order and Purchase Queries:
- Responds to questions regarding checkout, delivery times, payment options, and order status.
- Offers follow-up support on order status and estimated delivery.

## Conversational Flow

### Multi-Turn Conversations:
- Handles multi-turn interactions, remembering the context of user queries and follow-up questions.
- Manages interruptions and seamlessly resumes the conversation, ensuring a natural user experience.

### Structured Response Flow:
- **Human Message:** Initial query from the user.
- **AI Message:** AI’s response based on the query.
- **Tool Message:** Specific tool action, if applicable (e.g., adding an item to the cart).

## Testing and Validation

### Scenario Testing:
- The assistant was tested across various shopping scenarios to validate accuracy and reliability in conversation flow, including:
  - Complex queries involving multiple products.
  - Out-of-stock scenarios.
  - Invalid or ambiguous queries.

### Edge Case Handling:
- Documented common edge cases (e.g., items out of stock, unclear queries), ensuring the assistant gracefully manages these situations without disrupting the conversation.

## Dataset Information

### Dataset Source:
- The dataset was sourced from Kaggle and pre-processed, including:
  - Removing rows with null values.
  - Modifying product title length for better readability, as the dataset initially only included descriptions.
- The data is stored in a PostgreSQL database.

## Functionalities in `assistant_tools.py`:
Key functionalities include:
- `search_products`: Searches products based on user queries.
- `add_to_cart`: Adds selected items to the cart.
- `remove_from_cart`: Removes items from the cart.
- `view_cart`: Displays items in the cart.
- `checkout`: Processes the checkout.
- `get_payment_options`, `get_order_status`, `get_delivery_time`: Provides payment options, order status, and delivery information.

## Output Screenshots
- Screenshots documenting the assistant's interactions and key functionalities are stored in the `Output Screenshot` folder for reference.

## Steps to Run

### Environment Setup
1. Create a `.env` file in the project root directory with the following content:

```env
DB_HOST=<Your_Database_Host>
DB_PORT=<Your_Database_Port>
DB_DATABASE=<Your_Database_Name>
DB_USER=<Your_Database_Username>
DB_PASSWORD=<Your_Database_Password>
GROQ_API_KEY=<Your_Groq_API_Key>
```

### Install PostgreSQL:
- Ensure PostgreSQL is installed on your system.
- For installation, visit the [PostgreSQL official site](https://www.postgresql.org/download/).

### Database Setup:
1. Ensure you have the following information ready:
   - Database Host: `DB_HOST`
   - Database Port: `DB_PORT`
   - Database Name: `DB_DATABASE`
   - Username: `DB_USER`
   - Password: `DB_PASSWORD`

2. Log in to PostgreSQL:

```sh
psql -U <username>
```

3. Create a New Database:

```sql
CREATE DATABASE <database_name>;
```

4. Exit PostgreSQL:

```sh
\q
```

5. Restore the Backup:

```sh
psql -U <username> -d <database_name> -f backup.sql
```

### Install Dependencies:
Run the following command to install all dependencies:

```sh
pip install -r requirements.txt
```

*(The `requirements.txt` file includes all necessary packages, including `langchain`, `langchain-groq`, `langgraph`, `python-dotenv`, and `groq`.)*

### Run the Assistant:
Start the assistant by executing:

```sh
python main.py
```

### Interact with the Assistant:
- Enter shopping-related queries to initiate conversations with the assistant.
  - Example query: `"Hi, I am looking for a gaming monitor."` will prompt the assistant to display available monitors.

#### Cart Management:
- Select a product type, then ask the assistant to add it to the cart.
- The assistant provides real-time cart updates, allowing users to view, modify, or remove items from the cart as needed.

#### Checkout and Order Support:
- Proceed with checkout options, including reviewing cart items, modifying quantities, and finalizing the purchase.
- The assistant also responds to order-related questions, including delivery status, payment methods, and estimated arrival times.
