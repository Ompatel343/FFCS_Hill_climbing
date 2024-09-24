import copy
from collections import defaultdict

# Days of the week
DAYS = ['MON', 'TUE', 'WED', 'THU', 'FRI']

# Time conversion functions
def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

# Sample courses with their respective slots
COURSES = {
    'ARTIFICIAL INTELLIGENCE': ['E1+TE1'],
    'OPERATING SYSTEMS': ['B1+TB1'],
    'OPERATING SYSTEMS LAB': [
        'L1+L2', 'L7+L8', 'L13+L14', 'L19+L20', 'L25+L26'
    ],
    'AWS SOLUTIONS ARCHITECT': ['F1+TF1'],
    'COMPILER DESIGN': ['C1+TC1'],
    'COMPILER DESIGN LAB': [
        'L3+L4', 'L9+L10', 'L15+L16', 'L21+L22', 'L27+L28'
    ],
    'DATABASE SYSTEMS': ['A1+TA1'],
    'DATABASE SYSTEMS LAB': [
        'L5+L6', 'L11+L12', 'L17+L18', 'L23+L24', 'L29+L30'
    ],
    'COMPUTER NETWORKS': ['D1+TD1'],
    'COMPUTER NETWORKS LAB': [
        'L1+L2', 'L7+L8', 'L13+L14', 'L19+L20', 'L25+L26'
    ]
}

# Timing details for theory slots
THEORY_SLOTS = {
    'A1': [('MON', '08:00', '08:50'), ('WED', '09:51', '10:40')],
    'TA1': [('FRI', '10:41', '11:30')],
    'B1': [('TUE', '08:00', '08:50'), ('THU', '09:51', '10:40')],
    'TB1': [('MON', '10:41', '11:30')],
    'C1': [('WED', '08:00', '08:50'), ('FRI', '09:51', '10:40')],
    'TC1': [('TUE', '10:41', '11:30')],
    'D1': [('THU', '08:00', '08:50'), ('MON', '09:51', '10:40')],
    'TD1': [('FRI', '12:31', '13:20')],
    'E1': [('FRI', '08:00', '08:50'), ('TUE', '09:51', '10:40')],
    'TE1': [('THU', '10:41', '11:30')],
    'F1': [('MON', '08:51', '09:40'), ('WED', '09:51', '10:40')],
    'TF1': [('FRI', '11:40', '12:30')],
}

# Define lab time slots (including Monday through Friday)
LAB_SLOTS = {
    # MONDAY
    'L1': [('MON', '08:00', '08:50')],
    'L2': [('MON', '08:51', '09:40')],
    'L3': [('MON', '09:51', '10:40')],
    'L4': [('MON', '10:41', '11:30')],
    'L5': [('MON', '11:40', '12:30')],
    'L6': [('MON', '12:31', '13:20')],
    # TUESDAY
    'L7': [('TUE', '08:00', '08:50')],
    'L8': [('TUE', '08:51', '09:40')],
    'L9': [('TUE', '09:51', '10:40')],
    'L10': [('TUE', '10:41', '11:30')],
    'L11': [('TUE', '11:40', '12:30')],
    'L12': [('TUE', '12:31', '13:20')],
    # WEDNESDAY
    'L13': [('WED', '08:00', '08:50')],
    'L14': [('WED', '08:51', '09:40')],
    'L15': [('WED', '09:51', '10:40')],
    'L16': [('WED', '10:41', '11:30')],
    'L17': [('WED', '11:40', '12:30')],
    'L18': [('WED', '12:31', '13:20')],
    # THURSDAY
    'L19': [('THU', '08:00', '08:50')],
    'L20': [('THU', '08:51', '09:40')],
    'L21': [('THU', '09:51', '10:40')],
    'L22': [('THU', '10:41', '11:30')],
    'L23': [('THU', '11:40', '12:30')],
    'L24': [('THU', '12:31', '13:20')],
    # FRIDAY
    'L25': [('FRI', '08:00', '08:50')],
    'L26': [('FRI', '08:51', '09:40')],
    'L27': [('FRI', '09:51', '10:40')],
    'L28': [('FRI', '10:41', '11:30')],
    'L29': [('FRI', '11:40', '12:30')],
    'L30': [('FRI', '12:31', '13:20')],
}

def get_slot_timings(slot):
    """Retrieve the timings for a given slot."""
    if slot in THEORY_SLOTS:
        return THEORY_SLOTS[slot]
    elif slot in LAB_SLOTS:
        return LAB_SLOTS[slot]
    else:
        return []

def is_conflict(timetable, timings):
    """Check if any of the timings conflict with the existing timetable."""
    for timing in timings:
        day, start_time, end_time = timing[0], timing[1], timing[2]
        for scheduled in timetable.get(day, []):
            # Check for overlap
            s_start = time_to_minutes(scheduled[1])
            s_end = time_to_minutes(scheduled[2])
            t_start = time_to_minutes(start_time)
            t_end = time_to_minutes(end_time)
            if not (t_end <= s_start or t_start >= s_end):
                return True
    return False

def backtrack_schedule(courses, course_list, index, timetable, course_assignments):
    """Recursive function to schedule courses without conflicts."""
    if index == len(course_list):
        return True  # All courses scheduled

    course = course_list[index]
    slot_options = courses[course]

    for slot_option in slot_options:
        slots = slot_option.split('+')
        timings_list = []
        conflict = False
        for slot in slots:
            slot_timings = get_slot_timings(slot)
            if not slot_timings:
                conflict = True
                break
            # Add all timings for the slot
            for timing in slot_timings:
                timings_list.append((timing[0], timing[1], timing[2], course))
        if conflict or is_conflict(timetable, timings_list):
            continue

        # No conflict, add timings to timetable
        for timing in timings_list:
            timetable.setdefault(timing[0], []).append(timing)
        course_assignments[course] = timings_list

        # Recurse to next course
        if backtrack_schedule(courses, course_list, index + 1, timetable, course_assignments):
            return True

        # Backtrack
        for timing in timings_list:
            timetable[timing[0]].remove(timing)
        del course_assignments[course]

    return False  # No valid slot found

def generate_initial_timetable():
    """Generates an initial timetable using backtracking."""
    timetable = {}
    course_assignments = {}
    course_list = list(COURSES.keys())

    success = backtrack_schedule(COURSES, course_list, 0, timetable, course_assignments)
    if success:
        return timetable
    else:
        return None

def calculate_gaps(timetable):
    """Calculates the total number of 10-minute gaps in the timetable."""
    total_gaps = 0
    for day in DAYS:
        day_slots = []
        for timing in timetable.get(day, []):
            start = time_to_minutes(timing[1])
            end = time_to_minutes(timing[2])
            day_slots.append((start, end))
        if not day_slots:
            continue
        day_slots.sort()
        # Merge overlapping slots
        merged_slots = [day_slots[0]]
        for current in day_slots[1:]:
            last = merged_slots[-1]
            if current[0] <= last[1]:
                merged_slots[-1] = (last[0], max(last[1], current[1]))
            else:
                merged_slots.append(current)
        # Calculate gaps
        for i in range(len(merged_slots) - 1):
            gap = merged_slots[i + 1][0] - merged_slots[i][1]
            total_gaps += gap // 10
    return total_gaps

def hill_climbing():
    """Performs hill climbing to minimize gaps in the timetable."""
    timetable = generate_initial_timetable()
    if timetable is None:
        print("Failed to generate an initial timetable without conflicts.")
        return None

    current_gaps = calculate_gaps(timetable)
    iterations = 0

    while True:
        iterations += 1
        neighbors = get_neighbors(timetable)
        if not neighbors:
            break

        neighbor_gaps = []
        for neighbor in neighbors:
            gaps = calculate_gaps(neighbor)
            neighbor_gaps.append((gaps, neighbor))

        # Find the neighbor with the least gaps
        neighbor_gaps.sort(key=lambda x: x[0])
        best_gap, best_timetable = neighbor_gaps[0]

        if best_gap < current_gaps:
            timetable = best_timetable
            current_gaps = best_gap
            print(f"Iteration {iterations}: Found better timetable with {current_gaps} gaps.")
        else:
            break

    print(f"Final timetable has {current_gaps} gaps after {iterations} iterations.")
    return timetable

def get_neighbors(timetable):
    """Generates neighboring timetables by swapping lab slot options."""
    neighbors = []
    for course in COURSES:
        if 'LAB' in course:
            current_slots = [timing for timing in timetable.values() for timing in timing if timing[3] == course]
            current_option = None
            for option in COURSES[course]:
                slots = option.split('+')
                slot_timings = []
                for slot in slots:
                    slot_timings.extend(get_slot_timings(slot))
                if all(any(t[1] == timing[1] and t[0] == timing[0] for t in current_slots) for timing in slot_timings):
                    current_option = option
                    break

            other_options = [opt for opt in COURSES[course] if opt != current_option]
            for option in other_options:
                new_timetable = copy.deepcopy(timetable)
                # Remove current lab timings
                for day in DAYS:
                    new_timetable[day] = [t for t in new_timetable.get(day, []) if t[3] != course]
                # Try assigning new lab slot
                slots = option.split('+')
                course_timings = []
                conflict = False
                for slot in slots:
                    slot_timings = get_slot_timings(slot)
                    if not slot_timings:
                        conflict = True
                        break
                    # Check for conflicts
                    if is_conflict(new_timetable, [(t[0], t[1], t[2], course) for t in slot_timings]):
                        conflict = True
                        break
                    course_timings.extend([(t[0], t[1], t[2], course) for t in slot_timings])
                if conflict:
                    continue
                # No conflict, add to timetable
                for timing in course_timings:
                    new_timetable.setdefault(timing[0], []).append(timing)
                neighbors.append(new_timetable)
    return neighbors

def print_timetable(timetable):
    """Prints the timetable in a readable format."""
    for day in DAYS:
        print(f"\n{day}:")
        day_schedule = timetable.get(day, [])
        if not day_schedule:
            print("  No classes scheduled.")
            continue
        # Sort the day's schedule
        day_schedule.sort(key=lambda x: time_to_minutes(x[1]))
        for entry in day_schedule:
            print(f"  {entry[1]} - {entry[2]}: {entry[3]}")

if __name__ == "__main__":
    final_timetable = hill_climbing()
    if final_timetable:
        print_timetable(final_timetable)
