#!/usr/bin/python
import os
import dateutil.parser
import time
import datetime

print("Importing matplotlib . . .")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
print("Done importing matplotlib")

import trainees

GOAL = 200
START_DATE = "01AUG2022"

def check_section_format(section_str):
    """ Check if `section_str` has the format of a JQR section (*.*.*). """
    return section_str.count(".") == 2

def find_sig_dates(filename):
    """ Create a list of all dates when signatures were given. """
    dates = []
    with open(filename, "r") as f:
        for line in f:
            if line.count("|") == 5:
                pieces = line.split("|")
                if check_section_format(pieces[1]):
                    date_str = pieces[4].strip()
                    if date_str:
                        dates.append(date_str)
    return dates

def plot_sigs(sig_date_dict, goal):
    """ Save a matplotlib figure representing the given signatures. """
    print("Plotting signature data . . .")
    day_num_min = min(sig_date_dict.keys())
    day_num_max = max(sig_date_dict.keys())

    day_nums = [i for i in range(day_num_min - 1, day_num_max + 1)]
    cumulative_sigs = [0]

    for day_num in day_nums[1:]:
        cumulative_sigs.append(cumulative_sigs[-1]
                               + sig_date_dict.get(day_num, 0))

    fig, ax = plt.subplots()
    ax.set_ylim(0, GOAL + 10)

    # Plot the data representing cumulative signatures vs. time.
    ax.plot([datetime.date.fromordinal(day_num) for day_num in day_nums],
            cumulative_sigs)

    goal_x_nums = [day_num_min, day_num_max]
    goal_x_dates = [datetime.date.fromordinal(day_num) for day_num in goal_x_nums]
    # Plot the goal as a dashed line.
    ax.plot(goal_x_dates, [goal, goal], "r--")

    # Change the x-axis to have the actual date as the label.
    ax.xaxis.set_major_formatter(DateFormatter("%b-%d"))

    ax.set_xlabel("date")
    ax.set_ylabel("cumulative items signed off")

    # Change the aspect ratio.
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()

    x_ticks = ax.set_xticks(ax.get_xticks()[::2])
    ax.set_aspect(abs((x_max - x_min)/(y_max - y_min)) / 3)

    plt.savefig("sig-stats.png")

    print("Done plotting")

def limit_window(sig_date_dict, min_date, max_date=None):
    """ Remove entries from `sig_date_dict` whose date is outide
    the specified window.

    `max_date` defaults to the current day.
    This operates on `sig_date_dict` in place. """

    day_num_min = dateutil.parser.parse(min_date).toordinal()
    if max_date is None:
        max_date = time.asctime()
    day_num_max = dateutil.parser.parse(max_date).toordinal()

    for day in list(sig_date_dict.keys()):
        if not day_num_min <= day <= day_num_max:
            del sig_date_dict[day]

def main():
    print("Collecting signature data . . .")

    all_date_strs = []
    for path in trainees.active:
        all_date_strs.extend(find_sig_dates(path + "/README.md"))

    sig_date_dict = dict()
    for date_str in all_date_strs:
        day_num = dateutil.parser.parse(date_str).toordinal()
        if day_num == 80912:
            print(date_str)
        if day_num in sig_date_dict:
            sig_date_dict[day_num] += 1
        else:
            sig_date_dict[day_num] = 1

    limit_window(sig_date_dict, START_DATE)

    print("Done collecting data")

    plot_sigs(sig_date_dict, GOAL)

if __name__ == "__main__":
    main()
