# YouTube Transcript Question-Answering Using LangChain

This project enables users to query a YouTube video transcript and receive detailed, context-aware responses using LangChain. By leveraging OpenAI's embeddings and large language models, it creates a vector database from a video's transcript and retrieves relevant information for queries.

## Project Overview

The goal of this project is to:
1. **Load YouTube Transcripts**: Extract transcript data from a YouTube video.
2. **Create a Vector Database**: Process the transcript into smaller chunks and store it in a FAISS-based vector database.
3. **Answer Questions**: Use a language model to provide detailed, accurate answers to user queries based on the transcript.

## Features

- **YouTube Loader**: Automatically fetches the transcript of a YouTube video using its URL.
- **Vector Database**: Stores and retrieves relevant transcript sections using FAISS.
- **Query Processing**: Answers questions using only factual information from the transcript.
- **Error Handling**: Returns "I don't know" if insufficient information is available in the transcript.

## Dependencies

- `langchain_community`
- `langchain`
- `langchain_openai`
- `faiss`
- `dotenv`
- `OpenAI API`

