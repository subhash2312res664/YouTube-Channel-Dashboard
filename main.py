"""
🎯 PROJECT-1: YouTube Channel Analytics Dashboard

Author: Subhash Kumar Rana
Email: subhash_2312res664@iitp.ac.in

🔍 Description:
This Python project is designed to analyze and visualize YouTube channel data
in an engaging and functional way. It includes line plots, bar charts, pie charts,
and basic dataset exploration options.

🔧 Technologies Used:
- Python
- Pandas
- Matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("Welcome to the YouTube Channel Dashboard....!")

    while True:
        cmd = \
            (
                "\n🎯 Choose an Option from the Menu:\n"
                "--------------------------------------\n"
                "0. ❌ Exit / Close Program\n"
                "1. 📈 Line Plot       → Views over Time\n"
                "2. 📊 Bar Plot        → Views per Video (Top 10)\n"
                "3. 🥧 Pie Chart       → Engagement (👍 Like / 💬 Comment / 👎 Dislike)\n"
                "4. 🧾 Head(10)        → Show First 10 Rows of Dataset\n"
                "5. 📋 Describe()      → Statistical Summary of Dataset\n"
                "6. 🔍 Info()          → Dataset Info (Types, Nulls, etc.)\n"
                "7. 🧠 Project Info     → About the Project\n"
            )
        userinput = input(cmd)

        if userinput.lower() == "q" or userinput == "0":
            break
        elif userinput.lower() == "1":
            from YTDSF import LinePLot
            LinePLot()
        elif userinput.lower() == "2":
            from YTDSF import BarPlot
            BarPlot()
        elif userinput.lower() == "3":
            from YTDSF import PiPlot
            PiPlot()
        elif userinput == "4":
            from YTDSF import Head
            head = Head()
        elif userinput == "5":
            from YTDSF import Describe
            describe = Describe()
        elif userinput == "6":
            from YTDSF import Info
            info = Info()
        elif userinput == "7":
            from YTDSF import ProjectInfo
            projectinfo = ProjectInfo()
        elif userinput == "664":
            from YTDSF import AboutMe
            AboutMe()
        else:
            print("Please enter a valid option.")




