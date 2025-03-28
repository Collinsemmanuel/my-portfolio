import streamlit as st

def main():
    st.set_page_config(page_title="Emmanuel Kibet | AI Engineer", page_icon=":computer:")

    # Sidebar Navigation
    page = st.sidebar.radio("Navigate", 
        ["About", "Experience", "Projects", "Skills", "Contact"])

    # Shared styling
    st.markdown("""
    <style>
    .main-title {
        font-size: 3em;
        color: #2C3E50;
        text-align: center;
    }
    .subtitle {
        font-size: 1.5em;
        color: #34495E;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    if page == "About":
        st.markdown("<h1 class='main-title'>Emmanuel Kibet</h1>", unsafe_allow_html=True)
        st.markdown("<h2 class='subtitle'>AI Engineer | Software Developer | Project Manager</h2>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("## About Me")
            st.write("""
            Passionate AI Engineer with expertise in developing intelligent systems 
            for healthcare and business optimization. Committed to leveraging 
            technology to solve real-world challenges and drive innovation.
            """)
        
        with col2:
            st.write("## Contact Info")
            st.write("""
            📍 Kabarak, Kenya
            📞 +254 728 770 399
            ✉️ emmanuelkibet42018@gmail.com
            """)

    elif page == "Experience":
        st.header("Professional Experience")
        
        # Lish AI Labs
        st.subheader("AI Engineer - Lish AI Labs")
        st.write("July 2023 - Present")
        st.markdown("""
        - Developed AI-driven automation systems for healthcare
        - Built NLP-powered chatbots using Python
        - Designed backend systems for data processing
        """)

        # Tum AI Insights
        st.subheader("Founder - Tum AI Insights and Integrations")
        st.write("January 2024 - Present")
        st.markdown("""
        - Spearheaded AI automation for B2B communication
        - Designed agentic software for scheduling and analytics
        - Managed full project lifecycle
        """)

    elif page == "Projects":
        st.header("Featured Projects")
        
        # MediFlow AI
        st.subheader("MediFlow AI")
        st.write("Healthcare Workflow Automation")
        st.markdown("""
        - Revolutionized healthcare operations with AI tools
        - Technologies: LangChain, Flowise, WhatsApp API, PostgreSQL
        """)

        # SmartHealthMonitor
        st.subheader("SmartHealthMonitor Prototype")
        st.write("Health Monitoring System")
        st.markdown("""
        - Designed health monitoring tool for elderly and chronic patients
        - Integrated IoT and Python for real-time tracking
        """)

    elif page == "Skills":
        st.header("Technical Skills")
        skills = {
            "AI & Machine Learning": ["LLMs", "NLP", "Chatbots"],
            "Software Development": ["Python", "Flask", "FastAPI", "REST APIs"],
            "Data Science": ["Data Cleaning", "Visualization", "Machine Learning Models"],
            "Tools": ["LangChain", "Flowise", "PostgreSQL", "WhatsApp API"]
        }

        for category, skill_list in skills.items():
            st.subheader(category)
            st.write(", ".join(skill_list))

    elif page == "Contact":
        st.header("Get in Touch")
        
        with st.form(key='contact_form'):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")
            submit_button = st.form_submit_button(label='Send')
            
            if submit_button:
                st.success("Message sent successfully! Emmanuel will get back to you soon.")

if __name__ == "__main__":
    main()