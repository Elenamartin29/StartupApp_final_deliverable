import streamlit as st

def display():
    st.title("📘 Startup Lifecycle")

    st.markdown("""
    Startups go through different **growth phases**, each with their own challenges, focus, and funding needs.
    Below you'll find a guide to understand each phase, what usually happens, and what investors look for.
    """)

    st.subheader("💡 1. Ideation")
    st.markdown("""
    - The team identifies a problem and imagines a solution.
    - No product yet, just brainstorming and early research.
    - ✍️ *Goal:* Validate that the problem is real and worth solving.

    #### 🧠 Real example: **Airbnb (2007)**
    > Chesky and Gebbia rented air mattresses in their apartment to visitors during a conference. Just an idea, not a business yet.
    """)

    st.subheader("🧪 2. Validation")
    st.markdown("""
    - The startup builds an MVP (Minimum Viable Product).
    - Starts talking to real users, maybe launching landing pages or prototypes.
    - ✍️ *Goal:* Find early adopters and gather feedback.

    #### 🧠 Real example: **Dropbox (2008)**
    > Dropbox made a video demo before coding the product to test interest. It worked — they got thousands of signups overnight.
    """)

    st.subheader("🚀 3. Early Stage")
    st.markdown("""
    - The product is live, first users or revenue start coming in.
    - Team grows. Might raise a **Pre-Seed** or **Seed** funding round.
    - ✍️ *Goal:* Prove traction and scalability.

    #### 🧠 Real example: **Instagram (2010)**
    > Instagram launched with filters and simplicity. Within weeks, they had millions of users and investors lining up.
    """)

    st.subheader("📈 4. Growth")
    st.markdown("""
    - The business model works. Now it's time to scale.
    - Investment often comes from **Series A** and **Series B** rounds.
    - ✍️ *Goal:* Dominate a market or expand into new ones.

    #### 🧠 Real example: **Uber (2011–2014)**
    > Uber expanded rapidly city by city, raising hundreds of millions in Series A, B, C rounds to fuel global domination.
    """)

    st.subheader("🏁 5. Exit or Maturity")
    st.markdown("""
    - Options include IPO, acquisition, or sustainable operations.
    - ✍️ *Goal:* Return value to investors and secure long-term stability.

    #### 🧠 Real example: **Spotify (2018)**
    > Spotify went public through a direct listing. By then, it was a mature, global company with strong revenue and growth.
    """)

    st.markdown("---")
    st.subheader("💸 What do funding rounds mean?")
    
    st.markdown("""
    | 💼 **Funding Round** | **Stage Focus**                   | **Growth Focus**                                | **Amount**     |
    |----------------------|----------------------------------|--------------------------------------------------|----------------|
    | Pre-Seed             | Proof of concept / MVP           | Hiring                                           | $10K to $1M     |
    | Series A             | Revenue Growth                   | Dev, Ops, Marketing                              | ~$10M          |
    | Series B             | Expansion                        | Hiring, Buying, Scaling                          | $15M to $25M    |
    | Series C             | International / Acquisitions     | Mergers, global markets                          | ~$50M          |
    """)
    st.image("startup-funding-stages.png", caption="Types of Funding Rounds for Startups", use_container_width=True)

    st.info("Funding is a signal, but not a guarantee. What matters is product, team, timing… and a bit of luck.")
