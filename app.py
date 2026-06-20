import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="UK Relocation",
    page_icon="🇬🇧",
    layout="wide"
)

# CSS
st.markdown("""
<style>

/* GENEL */
.stApp{
    background:
    radial-gradient(circle at top,#35115e 0%,#12091f 40%,#05070d 100%);
     
}

 h1,h2,h3,h4,h5,h6,p,label,span{
    color:#ffffff !important;
}

 h1{
    color:#ff4fd8 !important;
    text-shadow:
    0 0 15px #ff4fd8,
    0 0 35px #ff4fd8;
}

/* SIDEBAR */
section[data-testid="stSidebar"]{
    background:#0b0b14;
    border-right:1px solid rgba(255,79,216,.3);
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* CARDA */
div[data-testid="metric-container"]{
    background:rgba(255,255,255,.04);
    border:1px solid rgba(255,79,216,.35);
    border-radius:20px;
    padding:18px;
    box-shadow:
    0 0 20px rgba(255,79,216,.2);
}

div[data-testid="metric-container"]:hover{
    transform:translateY(-4px);
    transition:.3s;
}

/* INPUT */
.stNumberInput input{
    background:#1b1035 !important;
    color:white !important;
    border:2px solid #ff4fd8 !important;
    border-radius:12px !important;
}

/* SELECTBOX */
div[data-baseweb="select"]{
    background:#1b1035 !important;
    border:2px solid #ff4fd8 !important;
    border-radius:15px !important;
}

div[data-baseweb="select"] span{
    color:white !important;
    font-weight:bold !important;
}

/* MENU */
ul[role="listbox"]{
    background:#1b1035 !important;
}

li[role="option"]{
    background:#1b1035 !important;
    color:white !important;
}

li[role="option"]:hover{
    background:#ff4fd8 !important;
    color:white !important;
}

[data-testid="stDataFrame"]{
    border-radius:20px;
    overflow:hidden;
}

[data-testid="stDataFrame"] *{
    color:black !important;
}

/* BUTTON */
.stButton button{
    background:linear-gradient(
    135deg,
    #ff4fd8,
    #8b5cf6
    );
    color:white;
    border:none;
    border-radius:15px;
    font-weight:bold;
}

.stButton button:hover{
    box-shadow:
    0 0 20px #ff4fd8;
}

/* SUCCESS */
.stSuccess{
    background:#00c48c !important;
    color:white !important;
    border-radius:15px;
}

/* SCROLL */
::-webkit-scrollbar{
    width:10px;
}

::-webkit-scrollbar-thumb{
    background:#ff4fd8;
    border-radius:10px;
}
section[data-testid="stSidebar"]{
    width:260px !important;
}
</style>
""", unsafe_allow_html=True)

# DATA
data = [
["London",1600,250,120,130,2100,95,90],
["Manchester",900,220,100,110,1330,88,85],
["Birmingham",850,220,95,105,1270,85,82],
["Liverpool",800,210,90,100,1200,82,80],
["Leeds",850,220,95,105,1270,84,81],
["Sheffield",780,200,85,95,1160,80,82],
["Bristol",1100,230,100,120,1550,87,88],
["Nottingham",820,210,90,100,1220,81,80],
["Leicester",800,205,90,95,1190,79,79],
["Newcastle",760,195,85,90,1130,81,84],
["Southampton",950,220,95,110,1375,83,85],
["Brighton",1200,230,100,120,1650,84,89],
["Reading",1150,230,100,120,1600,88,86],
["Oxford",1300,240,110,130,1780,90,92],
["Cambridge",1350,240,110,130,1830,92,93],
["Derby",780,200,85,95,1160,78,79],
["Coventry",820,205,90,100,1215,80,80],
["Hull",720,190,80,90,1080,74,76],
["York",950,220,95,110,1375,85,91],
["Stoke-on-Trent",730,190,80,90,1090,75,75],
["Blackpool",700,185,80,85,1050,70,74],
["Preston",760,195,85,90,1130,76,78],
["Bolton",740,190,80,90,1100,75,77],
["Warrington",850,210,90,100,1250,81,80],
["Chester",950,220,95,110,1375,84,89],
["Luton",950,220,95,110,1375,80,75],
["Milton Keynes",1100,230,100,120,1550,86,84],
["Peterborough",800,200,85,95,1180,77,78],
["Norwich",900,215,90,100,1305,82,87],
["Ipswich",820,200,85,95,1200,76,80],
["Plymouth",850,210,90,100,1250,78,85],
["Exeter",950,220,95,110,1375,84,90],
["Portsmouth",900,215,90,100,1305,80,83],
["Swindon",850,210,90,100,1250,79,79],
["Gloucester",820,205,90,95,1210,77,80],
["Cheltenham",950,220,95,110,1375,83,88],
["Bath",1100,230,100,120,1550,85,92],
["Lancaster",800,200,85,95,1180,78,88],
["Carlisle",750,190,80,90,1110,74,81],
["Durham",820,205,90,95,1210,83,90],
["Edinburgh",1200,230,100,120,1650,92,94],
["Glasgow",900,215,90,100,1305,86,88],
["Aberdeen",950,220,95,105,1370,84,84],
["Dundee",780,195,85,90,1150,78,82],
["Inverness",850,210,90,100,1250,76,91],
["Stirling",850,210,90,100,1250,80,90],
["Perth",820,205,90,95,1210,77,88],
["Cardiff",900,215,90,100,1305,84,86],
["Swansea",780,195,85,90,1150,76,84],
["Newport",800,200,85,95,1180,75,80],
["Wrexham",760,190,80,90,1120,74,79],
["Bangor",730,185,80,85,1080,72,86],
["Belfast",850,210,90,100,1250,82,84],
["Derry",760,190,80,90,1120,74,82],
["Lisburn",800,200,85,95,1180,75,82],
["Bangor NI",780,195,85,90,1150,74,83],
["Wakefield",780,195,85,90,1150,76,78],
["Huddersfield",760,190,80,90,1120,75,77],
["Bradford",740,190,80,90,1100,74,75],
["Doncaster",730,185,80,85,1080,73,76],
["Rotherham",720,185,80,85,1070,72,75],
["Barnsley",710,180,80,85,1055,72,75],
["Middlesbrough",720,185,80,85,1070,73,76],
["Sunderland",740,190,80,90,1100,75,78],
["Telford",760,190,80,90,1120,75,77],
["Wolverhampton",780,195,85,90,1150,77,78],
["Walsall",760,190,80,90,1120,74,76],
["Dudley",750,190,80,90,1110,74,76],
["Solihull",900,215,90,100,1305,82,84],
["Slough",1050,225,100,115,1490,84,80],
["Watford",1100,230,100,120,1550,85,82],
["Crawley",950,220,95,110,1375,80,82],
["Maidstone",900,215,90,100,1305,79,83],
["Canterbury",950,220,95,110,1375,84,90],
["Dover",800,200,85,95,1180,75,80],
["Bournemouth",1000,225,95,110,1430,83,89],
["Poole",980,220,95,110,1405,82,88],
["Torquay",820,205,90,95,1210,76,87],
["Blackburn",720,185,80,85,1070,72,75],
["Burnley",700,180,80,85,1045,71,74],
["Oldham",730,185,80,85,1080,72,75],
["Rochdale",730,185,80,85,1080,72,75],
["Stockport",850,210,90,100,1250,81,83],
["Wigan",740,190,80,90,1100,74,76],
["Salford",900,215,90,100,1305,84,84],
["Southend-on-Sea",900,215,90,100,1305,79,86],
["Chelmsford",980,220,95,110,1405,84,86],
["Colchester",880,210,90,100,1280,80,84],
["Lincoln",800,200,85,95,1180,78,85],
["Grimsby",700,180,80,85,1045,70,72],
["Scunthorpe",720,185,80,85,1070,71,73],
["Worcester",850,210,90,100,1250,80,86],
["Hereford",820,205,90,95,1210,78,88],
["Shrewsbury",840,205,90,95,1230,79,88],
["Harrogate",950,220,95,110,1375,85,91],
["Scarborough",780,195,85,90,1150,76,86]
]

df = pd.DataFrame(
    data,
    columns=[
        "City",
        "Rent",
        "Food",
        "Transport",
        "Utilities",
        "Monthly Cost",
        "Job Score",
        "Quality Of Life"
    ]
)

# SIDEBAR
st.sidebar.title("🇬🇧 UK Relocation")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Cost Calculator",
        "Compare Cities",
        "AI Advisor",
        "🏆 City Rankings"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 👨‍💻 Developer

**Ebubekir Basal**

🌐 [BasalSoft](https://www.basalsoft.com)

🔗 [LinkedIn Profile](https://www.linkedin.com/in/ebubekirbasal/)

💻 [GitHub Portfolio](https://github.com/29basal)

📧 Open To Work

---
Built with ❤️ using Python & Streamlit
""")
# DASHBOARD
if menu == "Dashboard":

    st.markdown("""
    <div style="
    padding:25px;
    border-radius:20px;
    background:linear-gradient(135deg,#7b2ff7,#ff4fd8);
    text-align:center;
    margin-bottom:20px;
    ">
    <h1 style="color:white;">
    🇬🇧 UK Relocation Intelligence
    </h1>
    <p style="color:white;">
    AI Powered City Analysis & Relocation Planner
    </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🏙 Cities", len(df))
    c2.metric("💰 Avg Cost", f"£{int(df['Monthly Cost'].mean())}")
    c3.metric("💼 Avg Job Score", int(df["Job Score"].mean()))
    c4.metric("😊 Avg Life Score", int(df["Quality Of Life"].mean()))

    st.divider()

    left, right = st.columns(2)

    with left:

        top_cost = df.sort_values(
            "Monthly Cost",
            ascending=False
        ).head(10)

        fig = px.bar(
            top_cost,
            x="City",
            y="Monthly Cost",
            color="Monthly Cost",
            title="💰 Top 10 Most Expensive Cities"
        )

        fig.update_layout(
            template="plotly_dark",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        fig2 = px.scatter(
            df,
            x="Job Score",
            y="Quality Of Life",
            size="Monthly Cost",
            hover_name="City",
            title="💼 Job Market vs Quality Of Life"
        )

        fig2.update_layout(
            template="plotly_dark",
            height=450
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.divider()

    st.subheader("🏆 Top 10 Cities By Job Score")

    top_jobs = df.sort_values(
        "Job Score",
        ascending=False
    ).head(10)

    st.dataframe(
        top_jobs[
            [
                "City",
                "Monthly Cost",
                "Job Score",
                "Quality Of Life"
            ]
        ],
        use_container_width=True
    )

    st.divider()

    st.subheader("💰 Top 10 Most Affordable Cities")

    cheap = df.sort_values(
        "Monthly Cost"
    ).head(10)

    st.dataframe(
        cheap[
            [
                "City",
                "Monthly Cost",
                "Job Score",
                "Quality Of Life"
            ]
        ],
        use_container_width=True
    )
    st.markdown("""
    <div style="
    text-align:center;
    padding:25px;
    border-radius:20px;
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,79,216,0.3);
    margin-top:20px;
    ">

    <h2 style="color:#ff4fd8;">
    👨‍💻 Developed By Ebubekir Basal
    </h2>

    <p>
    UK Relocation Intelligence Platform
    </p>

    <p>
    Built With Python, Streamlit, Pandas & Plotly
    </p>

    <p>
    🔗 LinkedIn:
    <a href="https://www.linkedin.com/in/ebubekirbasal/"
    target="_blank"
    style="color:#4fd1ff;">
    linkedin.com/in/ebubekirbasal
    </a>
    </p>

    <p>
    💻 GitHub:
    <a href="https://github.com/29basal"
    target="_blank"
    style="color:#4fd1ff;">
    github.com/29basal
    </a>
    </p>

    </div>
    """, unsafe_allow_html=True)
 
# COST CALCULATOR
elif menu == "Cost Calculator":

    st.title("💰 Cost Calculator")

    city = st.selectbox(
        "Select City",
        df["City"]
    )

    budget = st.number_input(
        "Budget (£)",
        value=7000
    )

    cost = int(
        df[df["City"] == city]["Monthly Cost"]
        .values[0]
    )

    months = round(
        budget / cost,
        1
    )
    selected_city = df[
    df["City"] == city
    ].iloc[0]

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🏠 Rent",
        f"£{selected_city['Rent']}"
    )

    c2.metric(
        "🍔 Food",
        f"£{selected_city['Food']}"
    )

    c3.metric(
        "🚌 Transport",
        f"£{selected_city['Transport']}"
    )

    c4.metric(
        "⚡ Utilities",
        f"£{selected_city['Utilities']}"
    )

    st.divider()

    c5, c6, c7 = st.columns(3)

    c5.metric(
        "💰 Total Cost",
        f"£{selected_city['Monthly Cost']}"
    )

    c6.metric(
        "💼 Job Score",
        selected_city["Job Score"]
    )

    c7.metric(
        "😊 Quality Of Life",
        selected_city["Quality Of Life"]
    )

    st.success(
        f"You can stay in {city} for approximately {months} months."
    )

# COMPARE
elif menu == "Compare Cities":

    st.title("📊 Compare Cities")

    city1 = st.selectbox(
        "City 1",
        df["City"]
    )

    city2 = st.selectbox(
        "City 2",
        df["City"],
        index=1
    )

    compare = df[
        df["City"].isin([city1,city2])
    ]

    st.dataframe(
    compare[
        [
            "City",
            "Monthly Cost",
            "Job Score",
            "Quality Of Life"
        ]
    ],
    use_container_width=True
    )

    fig = px.bar(
        compare,
        x="City",
        y=["Job Score","Quality Of Life"],
        barmode="group",
        title="City Comparison"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
# AI
elif menu == "AI Advisor":

    st.title("🤖 AI Advisor")

    budget = st.number_input(
        "Budget (£)",
        value=7000
    )

    affordable = df[
        (budget / df["Monthly Cost"]) >= 5
    ]

    if len(affordable) > 0:

        best = affordable.sort_values(
            "Job Score",
            ascending=False
        ).iloc[0]

        st.markdown(f"""
            <div style="
            background:#111827;
            padding:25px;
            border-radius:20px;
            color:white;
            ">
            <h2>🤖 AI Recommendation</h2>

            <h3>{best['City']}</h3>

            <p>Monthly Cost: £{best['Monthly Cost']}</p>
            <p>Job Score: {best['Job Score']}</p>
            <p>Quality Of Life: {best['Quality Of Life']}</p>

            </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        st.markdown(
            """
            <center>
            🚀 Developed by Ebubekir Basal
            </center>
            """,
            unsafe_allow_html=True
        )


elif menu == "🏆 City Rankings":

    st.title("🏆 UK City Rankings")

    tab1, tab2, tab3 = st.tabs([
        "💼 Jobs",
        "😊 Quality Of Life",
        "💰 Affordable"
    ])

    with tab1:

        st.subheader("Best Cities For Jobs")

        jobs = df.sort_values(
            "Job Score",
            ascending=False
        ).head(10)

        st.dataframe(
            jobs[
                [
                    "City",
                    "Job Score",
                    "Monthly Cost"
                ]
            ],
            use_container_width=True
        )

    with tab2:

        st.subheader("Best Quality Of Life")

        quality = df.sort_values(
            "Quality Of Life",
            ascending=False
        ).head(10)

        st.dataframe(
            quality[
                [
                    "City",
                    "Quality Of Life",
                    "Monthly Cost"
                ]
            ],
            use_container_width=True
        )

    with tab3:

        st.subheader("Most Affordable Cities")

        affordable = df.sort_values(
            "Monthly Cost"
        ).head(10)

        st.dataframe(
            affordable[
                [
                    "City",
                    "Monthly Cost",
                    "Job Score"
                ]
            ],
            use_container_width=True
        )