from datetime import datetime


# Get current date in a readable format
def get_current_date():
    return datetime.now().strftime("%B %d, %Y")


query_writer_instructions = """Your goal is to generate complex and diverse web search queries. These queries are used for an advanced automated web research tool that can analyze complex results, track links, and synthesize information.

Instructions:
- Always prioritize using a single search query, only add another query if the original question requires multiple aspects or elements and one query is not sufficient.
- Each query should focus on a specific aspect of the original question.
- Do not generate more than {number_queries} queries.
- Queries should be diverse; if the topic is broad, generate more than 1 query.
- Do not generate multiple similar queries; 1 is sufficient.
- Queries should ensure collecting the latest information. The current date is {current_date}.

Format:
- Format your response as a JSON object with these two exact keys:
   - "rationale": A brief explanation of why these queries are relevant
   - "query": A list of search queries

Example:

Topic: Which grew more last year - Apple's stock revenue growth or the number of people buying iPhones
```json
{{
    "rationale": "To accurately answer this comparative growth question, we need specific data points for Apple's stock performance and iPhone sales metrics. These queries target the precise financial information needed: company revenue trends, product-specific unit sales data, and stock price movements for the same fiscal period for direct comparison.",
    "query": ["Apple fiscal year 2024 total revenue growth", "iPhone fiscal year 2024 unit sales growth", "Apple fiscal year 2024 stock price growth"],
}}
```

Context: {research_topic}"""


web_searcher_instructions = """Conduct targeted Google searches to collect the latest, credible information about "{research_topic}" and synthesize it into verifiable textual content.

Instructions:
- Queries should ensure collecting the latest information. The current date is {current_date}.
- Conduct multiple, diverse searches to collect comprehensive information.
- Integrate key findings while carefully tracking the source of each specific piece of information.
- Output should be a well-structured summary or report based on search findings.
- Only include information found in search results; do not fabricate any information.

Research Topic:
{research_topic}
"""

reflection_instructions = """You are a professional research assistant analyzing a summary about "{research_topic}".

Instructions:
- Identify knowledge gaps or areas that need deeper exploration, and generate follow-up queries (one or more).
- If the provided summary is sufficient to answer the user's question, do not generate follow-up queries.
- If there are knowledge gaps, generate follow-up queries that help expand understanding.
- Focus on technical details, implementation specifics, or emerging trends that are not sufficiently covered.

Requirements:
- Ensure follow-up queries are self-contained and include necessary context for web search.

Output Format:
- Format your response as a JSON object with these exact keys:
   - "is_sufficient": true or false
   - "knowledge_gap": Description of what information is missing or needs clarification
   - "follow_up_queries": Write a specific question to address this gap

Example:
```json
{{
    "is_sufficient": true, // or false
    "knowledge_gap": "The summary lacks information on performance metrics and benchmarks", // Empty string if is_sufficient is true
    "follow_up_queries": ["What are the typical performance benchmarks and metrics used to evaluate [specific technology]?"] // Empty array if is_sufficient is true
}}
```

Carefully reflect on the summary to identify knowledge gaps and generate follow-up queries. Then, generate your output following this JSON format:

Summary:
{summaries}
"""

answer_instructions = """Based on the provided summary, generate a high-quality answer to the user's question in English.

Instructions:
- The current date is {current_date}.
- You are the last step in a multi-step research process; do not mention that you are the last step.
- You have access to all information collected from previous steps.
- You have access to the user's question.
- Based on the provided summary and user question, generate a high-quality answer in English.
- Properly include the sources you use from the summary in your answer, using markdown format (e.g., [apnews](https://vertexaisearch.cloud.google.com/id/1-0)). This is required.
- Please answer all content in English, including analysis, conclusions, and explanations.

User Context:
- {research_topic}

Summary:
{summaries}"""
