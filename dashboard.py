# import streamlit as st
# import pandas as pd

# from app import monitor_queues
# from app import monitor_channels
# from app import alerts

# alerts.clear()

# healthy, warning, critical, queues_data = monitor_queues()

# running, retrying, stopped, channels_data = monitor_channels()


# st.title("MQ Monitoring Dashboard")

# st.write("Welcome to MQ Dashboard")


# # Queue Summary

# st.header("Queue Summary")

# # st.metric("Healthy Queues", healthy)

# # st.metric("Warning Queues", warning)

# # st.metric("Critical Queues", critical)

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.metric("Healthy", healthy)

# with col2:
#     st.metric("Warning", warning)

# with col3:
#     st.metric("Critical", critical)

# # Queue Details

# st.subheader("Queue Details")

# queue_df = pd.DataFrame(
#     queues_data,
#     columns=["Queue", "Depth", "Status"]
# )

# st.table(queue_df)


# # Channel Summary

# st.header("Channel Summary")

# st.metric("Running Channels", running)

# st.metric("Retrying Channels", retrying)

# st.metric("Stopped Channels", stopped)


# # Channel Details

# st.subheader("Channel Details")

# channel_df = pd.DataFrame(
#     channels_data,
#     columns=["Channel", "Status"]
# )

# st.table(channel_df)


# # Alerts

# st.header("Alerts")

# for alert in alerts:

#     if "Critical" in alert or "STOPPED" in alert:
#         st.error(alert)

#     else:
#         st.warning(alert)


# st.metric("Total Alerts", len(alerts))

import streamlit as st
import pandas as pd


from app import monitor_queues, monitor_channels, alerts
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=30000, key="mq_refresh")
from datetime import datetime

st.write(
    "Last Updated:",
    datetime.now().strftime("%d-%m-%Y %H:%M:%S")
)
alerts.clear()

st.title("MQ Monitoring Dashboard")
st.write("Welcome to MQ Dashboard")

# Queue Data
healthy, warning, critical, queues_data = monitor_queues()

# Channel Data
running, retrying, stopped, channels_data = monitor_channels()

# Queue Summary
st.header("Queue Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Healthy", healthy)

with col2:
    st.metric("Warning", warning)

with col3:
    st.metric("Critical", critical)

total_queues = healthy + warning + critical

health_percent = round((healthy / total_queues) * 100, 2)

st.metric("Queue Health %", f"{health_percent}%")

# Queue Details
st.subheader("Queue Details")

queue_df = pd.DataFrame(
    queues_data,
    columns=["Queue", "Depth", "Status"]
)


st.dataframe(
    queue_df,
    hide_index=True,
    use_container_width=True
)

st.subheader("Queue Depth Chart")
st.bar_chart(queue_df.set_index("Queue")["Depth"])

# Channel Summary
st.header("Channel Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Running", running)

with col2:
    st.metric("Retrying", retrying)

with col3:
    st.metric("Stopped", stopped)

# Channel Details
st.subheader("Channel Details")

channel_df = pd.DataFrame(
    channels_data,
    columns=["Channel", "Status"]
)

st.dataframe(
    channel_df,
    hide_index=True,
    use_container_width=True
)

# Alerts
st.header("Alerts")

for alert in alerts:
    if "Critical" in alert or "STOPPED" in alert:
        st.error(alert)
    elif "warning" in alert or "RETRYING" in alert:
        st.warning(alert)
    else:
        st.info(alert)

st.metric("Total Alerts", len(alerts))

with open("mq_dashboard.txt", "r") as file:
    st.download_button(
        label="Download Report",
        data=file,
        file_name="mq_dashboard.txt",
        mime="text/plain"
    )