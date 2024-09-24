# Timetable Scheduler with Hill Climbing Optimization

## Overview

This project provides a timetable scheduling system for university courses, utilizing backtracking and hill climbing to generate an optimal schedule. The system takes predefined courses and their possible time slots, attempts to schedule them without conflicts, and optimizes the timetable by minimizing gaps between consecutive classes.

### Features:
1. **Backtracking Algorithm**: Tries to assign time slots for each course ensuring no conflicts arise.
2. **Hill Climbing Optimization**: After generating an initial schedule, this heuristic method is used to minimize gaps between classes.
3. **Slot Conflict Detection**: The system checks for overlapping classes to ensure a feasible timetable.
4. **Neighbor Generation**: For hill climbing, neighboring timetables are generated by swapping lab slots to explore better solutions.

## Installation

To use the code, you need Python 3.x installed.

### Clone the repository:
```bash
git clone https://github.com/yourusername/timetable-scheduler.git
cd timetable-scheduler
```

### Requirements
- No additional libraries are required, the code runs on built-in Python modules like `copy` and `collections.defaultdict`.

## How It Works

### Days of the Week:
The timetable schedules classes from **Monday to Friday** (`'MON'`, `'TUE'`, `'WED'`, `'THU'`, `'FRI'`).

### Time Slots:
The courses have both **theory** and **lab slots**, defined in `THEORY_SLOTS` and `LAB_SLOTS`, respectively. Each slot has a specific time on a given day.

### Course Information:
Courses are mapped to their available time slots in the `COURSES` dictionary. A course may have one or more available slots, and the system attempts to allocate one of them without conflict.

### Main Functions:
- **`generate_initial_timetable`**: Uses backtracking to generate a valid timetable.
- **`hill_climbing`**: Optimizes the initial timetable by reducing the number of 10-minute gaps between classes.
- **`is_conflict`**: Detects any overlapping time slots during scheduling.
- **`calculate_gaps`**: Calculates the number of 10-minute gaps in the timetable to assess optimization.
- **`get_neighbors`**: Generates neighboring timetables by swapping lab slots.
- **`print_timetable`**: Nicely formats and prints the final timetable.

## Usage

To run the scheduler, execute the following command:

```bash
python timetable_scheduler.py
```

This will generate and print the final optimized timetable after the hill climbing algorithm has minimized class gaps.

### Sample Output:
```
MON:
  08:00 - 08:50: ARTIFICIAL INTELLIGENCE
  09:51 - 10:40: OPERATING SYSTEMS
  ...
TUE:
  08:00 - 08:50: DATABASE SYSTEMS
  09:51 - 10:40: COMPILER DESIGN
  ...
```

## Code Structure

1. **`time_to_minutes(time_str)`**: Converts a time string (e.g., '08:00') to the number of minutes since midnight.
2. **`get_slot_timings(slot)`**: Retrieves the time periods associated with a given course slot.
3. **`backtrack_schedule(...)`**: The core backtracking algorithm to assign courses.
4. **`hill_climbing()`**: Improves the timetable by searching for neighboring timetables with fewer gaps.
5. **`print_timetable()`**: Prints the scheduled classes for each day of the week.

## Future Improvements

- Add more sophisticated optimization techniques such as Simulated Annealing.
- Introduce additional constraints like room availability or instructor schedules.
- Extend the system to handle more flexible time slots or weekend classes.
- Build a Userfriendly and Interactive Frontend that enhances the user experience.

