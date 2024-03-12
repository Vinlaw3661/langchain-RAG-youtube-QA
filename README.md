# LangChain-RAG
This project explores the basics of using the LangChain framework in creating Retrieval Augmented Generation (RAG) systems by leveraging Large Language Models
The 5 main concepts covered are:

1. **Models:**
   - The core machine learning models used for natural language processing tasks. These models can be pre-trained models like GPT-3 or custom models you train on your own data.

2. **Prompts:**
   - Prompts are essentially instructions or templates provided to the language model. They guide the model in understanding what kind of output is expected.

3. **Indexes:**
   - In vector databases, indexes play a crucial role in enabling fast and efficient retrieval of similar data points. Unlike traditional relational databases that use indexes on tables with rows and columns, vector databases deal with high-dimensional vectors representing data objects.
   - 
4. **Agents:**
   - Agents in LangChain serve as the glue that brings everything together. They orchestrate the NLP workflow by:
      1. Selecting the appropriate tools based on the user's query or task.
      2. Executing prompts with the LLM through the Model I/O layer.
      3. Processing the LLM's output potentially using other tools.

5. **Tools:**
   - Tools in LangChain represent external services or functionalities that can be integrated into your NLP pipeline. These tools can be used for various purposes like:
      1. Data retrieval: You can use tools to fetch data from external sources like databases or APIs.
      2. Data processing: Tools can be used for tasks like text cleaning, normalization, or tokenization.
      3. Post-processing: Some tools might be used for tasks like sentiment analysis or summarization after the LLM generates an output.

