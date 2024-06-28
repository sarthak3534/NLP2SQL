import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_sql_query_chain
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain


os.environ["GOOGLE_API_KEY"] = ""
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = ""

def gemini():
    return ChatGoogleGenerativeAI(model="gemini-pro")

def connect_db():
    return SQLDatabase.from_uri("sqlite:///STUDENTS.db")

llm = gemini()
db = connect_db()


db_chain = SQLDatabaseChain.from_llm(llm,db, verbose=True)
qns1 = db_chain.invoke("How many students which  section is B .note that don't include and prefix like ''' or sufix of any thing . only give me query")
