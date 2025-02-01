import streamlit as st
from openai import OpenAI
from helper.helper_app import select_random_topics


# --------------------
# Variables selection
# --------------------
tests_interviews = {
                "topics": [
                    {
                    "name": "Predictive Modeling",
                    "example": "Predicting customer churn for a subscription service.",
                    "problem": "Identifying which customers are likely to stop using the service and why."
                    },
                    {
                    "name": "Recommendation Systems",
                    "example": "Suggesting products on an e-commerce platform.",
                    "problem": "Providing personalized recommendations to improve user engagement and sales."
                    },
                    {
                    "name": "Natural Language Processing (NLP)",
                    "example": "Sentiment analysis on customer reviews.",
                    "problem": "Understanding customer sentiment to improve product offerings or service quality."
                    },
                    {
                    "name": "Time Series Analysis",
                    "example": "Forecasting monthly sales for inventory planning.",
                    "problem": "Predicting demand accurately to avoid stockouts or overstocking."
                    },
                    {
                    "name": "Anomaly Detection",
                    "example": "Detecting fraudulent transactions in banking systems.",
                    "problem": "Identifying unusual patterns or behaviors that indicate fraud."
                    },
                    {
                    "name": "Image and Video Analytics",
                    "example": "Detecting defects in manufacturing products using image classification.",
                    "problem": "Automating quality control to reduce manual inspection errors."
                    },
                    {
                    "name": "Customer Segmentation",
                    "example": "Grouping customers by purchasing behavior.",
                    "problem": "Creating targeted marketing campaigns to boost conversion rates."
                    },
                    {
                    "name": "Optimization Models",
                    "example": "Optimizing delivery routes for a logistics company.",
                    "problem": "Minimizing fuel costs and delivery time."
                    },
                    {
                    "name": "A/B Testing",
                    "example": "Testing two website layouts to improve user conversion.",
                    "problem": "Determining which design leads to better engagement or sales."
                    },
                    {
                    "name": "Big Data Processing",
                    "example": "Analyzing clickstream data from millions of users on a streaming platform.",
                    "problem": "Deriving insights and recommendations from massive, unstructured datasets."
                    }
                ]
                }
topic_names = [topic["name"] for topic in tests_interviews["topics"]]


data_science_topics = [
    "Data Preprocessing", "Exploratory Data Analysis (EDA)", "Feature Engineering", "Statistical Analysis",
    "Probability Theory", "Supervised Learning", "Unsupervised Learning", "Model Evaluation Metrics",
    "Cross-Validation Techniques", "Overfitting and Underfitting", "Bias-Variance Tradeoff",
    "Ensemble Learning", "Neural Networks", "Natural Language Processing (NLP)",
    "Time Series Analysis", "Spark", "Model Deployment and Monitoring",
    "Reinforcement Learning", "Data Ethics and Privacy", "Cloud Computing for Data Science"
]
selected_themes_topics = select_random_topics(data_science_topics, num_topics=5)

# --------------------
# Sidebar
# --------------------
with st.sidebar:
    st.header("Interview selector")

    if st.toggle("API_local"):
        import helper.creden as cre
        client = OpenAI(api_key=cre.OPENAI_API_KEY)

    else:
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

    model_selection = st.sidebar.selectbox(
        "Select the model version",
        ("gpt-4o-mini", "gpt-4o")
    )

    # select the topic
    selected_topic = st.selectbox(
        "Select a topic",
        topic_names
    )
    # # If you need to get the full topic information based on the selection
    selected_topic_info = next(
        (topic for topic in tests_interviews["topics"] if topic["name"] == selected_topic),
        None
    )

    st.header("Discussion themes hint")

    number_topics = st.slider(
        "Number of topics to select",
        min_value=1,
        max_value=len(data_science_topics),
        value=5  # Default value
    )
    if st.button("Random Selection"):
        selected_themes_topics = select_random_topics(data_science_topics, num_topics= number_topics)

        # Show the selected topics
        if selected_themes_topics:
            st.write("Selected Topics:")
            for topic in selected_themes_topics:
                st.write(f"- {topic}")


# --------------------
# Prompt
# --------------------
prompt_example = f"""
When you reply, first plan how you should answer within <thinking> </thinking> XML tags. this is a space for you to write down relevant content and will be be showing to the used, for now.
once you are done with the thinking you can output the answer of the thinking <answer> </answer> XML tags. Make sure your answer is detailed and specific, also all the questions  need to be add it into the answer tag
Before ending the chat use this format <Example> </Example> in XML tags. in a JSON so we can visualize it in the message
After <thinking> </thinking> <answer> </answer> XML tags. start writing in the next line.
We are conducting a data science interview focused exclusively on data science topics. Avoid discussing unrelated subjects. Ensure
a rigorous and structured interview process with the goal of evaluating the candidate's expertise in data science. 
for each well-answered question, and maintain high expectations as a data science professional with 5 years of
experience. Look for key terminology and concepts relevant to the field.

---------------
Generated Knowledge Example Question: 
- We are working with a healthcare company to predict the likelihood of patients being readmitted within 30 days of discharge. The dataset includes patient demographics, medical history, and various other details related to their hospital stay. What steps would you take to build a model for this prediction task?
- You’ve chosen a random forest model for predicting house prices. Could you explain what might happen if the model starts overfitting the data? What steps would you take to mitigate overfitting in this case, and how would you determine if the model is truly generalizing well?

---------------

Steps to Follow:
Introduction: Begin with a brief introduction of the company. Mention that it is a consultancy that collaborates with clients from various industries and fields.
Questioning: Ask one question at a time, ensuring it pertains to data science. Move on to the next question only after receiving an answer. ask just 3 question in each interview as much
Example Problem: Incorporate this field example {selected_topic_info["example"]} and this problem {selected_topic_info["problem"]} as a case study to keep the discussion grounded, also include this topics in the questions {selected_themes_topics}.
Dataset Creation: Design a simple dataset with 5 rows and 4–8 features, including a target variable, to use as part of the problem-solving exercise. Present this dataset in a table format.
this its the example of the dataset
Question Design: Formulate one thoughtful question at a time based on the dataset or case study. If the question is unclear or unsuitable, reformulate it until it aligns with the goals of the interview.
Scoring: Assign a score from 0 to 9 for each response, where 9 represents expert-level knowledge. Evaluate based on detail, clarity, and the use of relevant data science concepts.
Conclusion: Conclude by thanking the candidate for their time and providing an overall score based on their performance.
Feedback: After completing all questions, identify areas where the interview process could be improved, providing specific points for enhancement.
Final Output: Summarize the results in a JSON format, including the overall score and interview feedback.

---------------
Interview Scoring System:
Each question is scored from 0 to 9, where 9 reflects expert-level proficiency. Evaluate the answers based on:
Clarity: Was the answer well-structured and easy to follow?
Detail: Did the candidate demonstrate depth in their understanding of data science principles?
Application of Concepts: Did the candidate incorporate relevant data science terminology and concepts (e.g., feature engineering, model selection, evaluation metrics)?
Example: "7/9" or "0/9".

---------------
<Example>
Extracted Data JSON:
  "candidate_name": "Jackeline",
  "scores": [
    "question_1": 5,
    "question_2": 6,
    "question_3": 0
  ],
  "overall_score": 11,
  "feedback": [
    "Depth of Knowledge: While you demonstrated some understanding of data science concepts, there is a need for deeper knowledge in model evaluation and data preprocessing techniques.",
    "Specificity: Providing more detailed explanations and examples would enhance your responses.",
    "Preparation: Familiarizing yourself with key evaluation metrics and their implications in classification problems would be beneficial."
</Example>

Reminder: Ensure the questions and evaluations are rigorous, leveraging your data science expertise to assess technical depth and problem-solving abilities.
When you finish all the question add a json file to download to review the questions
After printing the json just keep saying good bye in case the person wants to keep talking.
"""
context = [{'role':'system', 'content':prompt_example}]

# --------------------
# Chatbot
# --------------------
st.title("💬 Data Science Interviewer")

if "messages" not in st.session_state:
    initial_question = "We will start with the interview. Can you give me a brief introduction about yourself?"
    st.session_state["messages"] = [{"role": "assistant", "content": initial_question}]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not client:
        st.info("API is not working")
        st.stop()

    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Prepare messages for API request (including system context)
    full_conversation = context + st.session_state.messages
    response = client.chat.completions.create(model=model_selection, messages=full_conversation)

    # Get response and update session state
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
