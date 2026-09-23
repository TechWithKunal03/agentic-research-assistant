import streamlit as st

from agents import run_research


st.set_page_config(
    page_title="Agentic Research Assistant",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 Agentic AI Research Assistant")

st.write(
    "A multi-agent AI system that plans, researches, "
    "analyzes, critiques and synthesizes research."
)


query = st.text_area(
    "Enter your research question",
    placeholder=(
        "Example: What are the advantages "
        "of RAG over fine-tuning?"
    )
)


if st.button("🔎 Start Research"):

    if not query.strip():

        st.warning(
            "Please enter a research question."
        )

    else:

        with st.spinner(
            "Agents are researching..."
        ):

            result = run_research(query)

        st.success(
            "Research completed!"
        )

        with st.expander(
            "🧠 Research Plan"
        ):
            st.write(
                result["plan"]
            )

        with st.expander(
            "🔍 Research Findings"
        ):
            st.write(
                result["research"]
            )

        with st.expander(
            "📊 Analysis"
        ):
            st.write(
                result["analysis"]
            )

        with st.expander(
            "🧐 Critic Review"
        ):
            st.write(
                result["critique"]
            )

        st.subheader(
            "📝 Final Answer"
        )

        st.write(
            result["final_answer"]
        )
