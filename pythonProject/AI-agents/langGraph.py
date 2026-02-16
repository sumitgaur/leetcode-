from typing import TypedDict, Literal

from langgraph.graph import StateGraph, END


# -----------------------------
# 1. Define shared state
# -----------------------------
class JobState(TypedDict):
    text: str
    category: Literal["short", "long"]
    result: str


# -----------------------------
# 2. Define agents (nodes)
# -----------------------------

def classifier_agent(state: JobState) -> JobState:
    """Classifies input based on length"""
    if len(state["text"]) < 20:
        state["category"] = "short"
    else:
        state["category"] = "long"
    return state
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

def llm_classifier(state: JobState) -> JobState:
    prompt = f"Classify text as short or long:\n{state['text']}"
    response = llm.invoke(prompt).content.lower()

    state["category"] = "short" if "short" in response else "long"
    return state


def short_text_agent(state: JobState) -> JobState:
    state["result"] = f"SHORT text detected: {state['text']}"
    return state


def long_text_agent(state: JobState) -> JobState:
    state["result"] = f"LONG text detected: {state['text']}"
    return state


# -----------------------------
# 3. Build LangGraph
# -----------------------------
graph = StateGraph(JobState)

# Register nodes
graph.add_node("classifier", classifier_agent)
graph.add_node("short_agent", short_text_agent)
graph.add_node("long_agent", long_text_agent)

# Entry point
graph.set_entry_point("classifier")

# Conditional routing
graph.add_conditional_edges(
    "classifier",
    lambda state: state["category"],
    {
        "short": "short_agent",
        "long": "long_agent",
    },
)

# End nodes
graph.add_edge("short_agent", END)
graph.add_edge("long_agent", END)

# Compile graph
app = graph.compile()


# -----------------------------
# 4. Execute graph
# -----------------------------
if __name__ == "__main__":
    input_state = {
        "text": "LangGraph is an agent orchestration framework",
    }

    output = app.invoke(input_state)
    print(app.get_graph().draw_mermaid())
    print(output)
