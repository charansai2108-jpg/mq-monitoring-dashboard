# alerts=[]
# def monitor_queues():
#     with open(r"C:\Users\ADMIN\Documents\Python_WorkSpace\mq_dashborad\queues.csv", "r") as file:
#         lines=file.readlines()
#         print(lines)
#         healthy=0
#         warning=0
#         critical=0
#         queues_data=[]
#         for line in lines:
#             line = line.strip().replace('"', '')
#             queue, depth, status = line.split(",")
#             depth = int(depth)
#             print("Checking: ", queue)
#             if depth > 90:
#                 status="Critical"
#                 critical+=1
#                 # print(queue, "depth is critical")
#                 alerts.append(f"ALERT: {queue} depth {depth} is Critical")
                
#             elif depth >= 50 and depth <=90:
#                 status="Warning"
#                 warning+=1
#                 # print(queue, "Warning Alert")
#                 alerts.append(f"ALERT: {queue} depth {depth} is warning alert")
#             else:
#                 status="Healthy"
#                 healthy+=1
#                 # print(queue, "Healthy Alert")
#             queues_data.append([queue, depth, status]) 
#             if queue == "ERROR.Q" and depth > 0:
#                 alerts.append(f"ALERT: ERROR.Q contains {depth} messages")

#             if queue == "DLQ" and depth > 0:
#                 alerts.append(f"ALERT: DLQ contains {depth} messages")       
#         print("Healthy: ", healthy)
#         print("Warning: ", warning)
#         print("Critical: ", critical)
#         print(queues_data)
#     return healthy, warning, critical, queues_data

# def monitor_channels():
#     with open(r"C:\Users\ADMIN\Documents\Python_WorkSpace\mq_dashborad\channels.csv", "r") as file:
#         lines=file.readlines()
#         print(lines)
#         running=0
#         retrying=0
#         stopped=0
#         channels_data=[]
#         for line in lines:
#             line=line.strip().replace('"', '')
#             channel_name,status=line.split(",")
#             print("Checking: ", channel_name)
#             if status =="RUNNING":
#                 running+=1
#                 # print(channel_name, "Helathy")
#             elif status=="RETRYING":
#                 retrying+=1
#                 # print(channel_name, "Warning Alert")
#                 alerts.append(f"ALERT: {channel_name} is RETRYING")
#             elif status=="STOPPED":
#                 stopped+=1
#                 # print(channel_name, "Critical Alert")
#                 alerts.append(f"ALERT: {channel_name} is STOPPED")
#             channels_data.append([channel_name, status])
#         print("Running Channels : ", running)
#         print("Retrying Channels : ", retrying)
#         print("Stopped Channels : ", stopped)
#         print(channels_data)
#     return running, retrying, stopped, channels_data
# # monitor_channels()
# # monitor_queues()

# healthy, warning, critical, queues_data = monitor_queues()

# running, retrying, stopped, channels_data = monitor_channels()

# # print("\nAlerts")
# # print("------")       

# with open(r"C:\Users\ADMIN\Documents\Python_WorkSpace\mq_dashborad\mq_dashboard.txt", "w") as report:
#     report.write("===== MQ Dashboard Summary =====\n")
#     report.write("Queues\n")
#     report.write("Healthy : " + str(healthy) + "\n")
#     report.write("Warning : " + str(warning) + "\n")
#     report.write("Critical : " + str(critical) + "\n")

#     report.write("\nChannels\n")
#     report.write("Running Channels : " + str(running) + "\n")
#     report.write("Retrying Channels : " + str(retrying) + "\n")
#     report.write("Stopped Channels : " + str(stopped) + "\n")
#     report.write("\nAlerts\n")
#     report.write("------\n")
#     for alert in alerts:
#         report.write(alert + "\n")

alerts = []

def monitor_queues():
    global alerts

    healthy = 0
    warning = 0
    critical = 0
    queues_data = []

    with open(r"C:\Users\ADMIN\Documents\Python_WorkSpace\mq_dashborad\queues.csv", "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip().replace('"', '')
            queue, depth, status = line.split(",")
            depth = int(depth)

            if depth > 90:
                status = "🔴 Critical"
                critical += 1
                alerts.append(f"ALERT: {queue} depth {depth} is Critical")

            elif depth >= 50:
                status = "🟡 Warning"
                warning += 1
                alerts.append(f"ALERT: {queue} depth {depth} is warning alert")

            else:
                status = "🟢 Healthy"
                healthy += 1

            queues_data.append([queue, depth, status])

            if queue == "ERROR.Q" and depth > 0:
                alerts.append(f"ALERT: ERROR.Q contains {depth} messages")

            if queue == "DLQ" and depth > 0:
                alerts.append(f"ALERT: DLQ contains {depth} messages")

    return healthy, warning, critical, queues_data


def monitor_channels():
    channels_data = []

    running = 0
    retrying = 0
    stopped = 0

    with open(r"C:\Users\ADMIN\Documents\Python_WorkSpace\mq_dashborad\channels.csv", "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip().replace('"', '')
            channel_name, status = line.split(",")

            channels_data.append([channel_name, status])

            if status == "RUNNING":
                running += 1

            elif status == "RETRYING":
                retrying += 1
                alerts.append(f"ALERT: {channel_name} is RETRYING")

            elif status == "STOPPED":
                stopped += 1
                alerts.append(f"ALERT: {channel_name} is STOPPED")

    return running, retrying, stopped, channels_data